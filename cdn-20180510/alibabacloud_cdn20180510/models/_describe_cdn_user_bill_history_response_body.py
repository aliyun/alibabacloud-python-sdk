# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnUserBillHistoryResponseBody(DaraModel):
    def __init__(
        self,
        bill_history_data: main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryData = None,
        request_id: str = None,
    ):
        self.bill_history_data = bill_history_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.bill_history_data:
            self.bill_history_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_history_data is not None:
            result['BillHistoryData'] = self.bill_history_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillHistoryData') is not None:
            temp_model = main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryData()
            self.bill_history_data = temp_model.from_map(m.get('BillHistoryData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnUserBillHistoryResponseBodyBillHistoryData(DaraModel):
    def __init__(
        self,
        bill_history_data_item: List[main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem] = None,
    ):
        self.bill_history_data_item = bill_history_data_item

    def validate(self):
        if self.bill_history_data_item:
            for v1 in self.bill_history_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillHistoryDataItem'] = []
        if self.bill_history_data_item is not None:
            for k1 in self.bill_history_data_item:
                result['BillHistoryDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_history_data_item = []
        if m.get('BillHistoryDataItem') is not None:
            for k1 in m.get('BillHistoryDataItem'):
                temp_model = main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem()
                self.bill_history_data_item.append(temp_model.from_map(k1))

        return self

class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItem(DaraModel):
    def __init__(
        self,
        bill_time: str = None,
        bill_type: str = None,
        billing_data: main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData = None,
        dimension: str = None,
    ):
        self.bill_time = bill_time
        self.bill_type = bill_type
        self.billing_data = billing_data
        self.dimension = dimension

    def validate(self):
        if self.billing_data:
            self.billing_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_time is not None:
            result['BillTime'] = self.bill_time

        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.billing_data is not None:
            result['BillingData'] = self.billing_data.to_map()

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillTime') is not None:
            self.bill_time = m.get('BillTime')

        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('BillingData') is not None:
            temp_model = main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData()
            self.billing_data = temp_model.from_map(m.get('BillingData'))

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        return self

class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingData(DaraModel):
    def __init__(
        self,
        billing_data_item: List[main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem] = None,
    ):
        self.billing_data_item = billing_data_item

    def validate(self):
        if self.billing_data_item:
            for v1 in self.billing_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillingDataItem'] = []
        if self.billing_data_item is not None:
            for k1 in self.billing_data_item:
                result['BillingDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.billing_data_item = []
        if m.get('BillingDataItem') is not None:
            for k1 in m.get('BillingDataItem'):
                temp_model = main_models.DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem()
                self.billing_data_item.append(temp_model.from_map(k1))

        return self

class DescribeCdnUserBillHistoryResponseBodyBillHistoryDataBillHistoryDataItemBillingDataBillingDataItem(DaraModel):
    def __init__(
        self,
        bandwidth: float = None,
        cdn_region: str = None,
        charge_type: str = None,
        count: float = None,
        flow: float = None,
    ):
        self.bandwidth = bandwidth
        self.cdn_region = cdn_region
        self.charge_type = charge_type
        self.count = count
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cdn_region is not None:
            result['CdnRegion'] = self.cdn_region

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.count is not None:
            result['Count'] = self.count

        if self.flow is not None:
            result['Flow'] = self.flow

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CdnRegion') is not None:
            self.cdn_region = m.get('CdnRegion')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        return self

