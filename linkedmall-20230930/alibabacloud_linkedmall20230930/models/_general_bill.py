# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkedmall20230930 import models as main_models
from darabonba.model import DaraModel

class GeneralBill(DaraModel):
    def __init__(
        self,
        bill_id: str = None,
        bill_period: str = None,
        download_url: List[str] = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        shop_id: str = None,
        shop_name: str = None,
        start_time: str = None,
        total_amount: main_models.Money = None,
    ):
        self.bill_id = bill_id
        self.bill_period = bill_period
        self.download_url = download_url
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.start_time = start_time
        self.total_amount = total_amount

    def validate(self):
        if self.total_amount:
            self.total_amount.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_id is not None:
            result['billId'] = self.bill_id

        if self.bill_period is not None:
            result['billPeriod'] = self.bill_period

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.shop_id is not None:
            result['shopId'] = self.shop_id

        if self.shop_name is not None:
            result['shopName'] = self.shop_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.total_amount is not None:
            result['totalAmount'] = self.total_amount.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billId') is not None:
            self.bill_id = m.get('billId')

        if m.get('billPeriod') is not None:
            self.bill_period = m.get('billPeriod')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('shopId') is not None:
            self.shop_id = m.get('shopId')

        if m.get('shopName') is not None:
            self.shop_name = m.get('shopName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('totalAmount') is not None:
            temp_model = main_models.Money()
            self.total_amount = temp_model.from_map(m.get('totalAmount'))

        return self

