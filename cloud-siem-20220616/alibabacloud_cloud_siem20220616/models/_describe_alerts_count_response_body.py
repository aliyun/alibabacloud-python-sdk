# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeAlertsCountResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeAlertsCountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeAlertsCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAlertsCountResponseBodyData(DaraModel):
    def __init__(
        self,
        all: int = None,
        count_map: Dict[str, int] = None,
        high: int = None,
        low: int = None,
        medium: int = None,
        product_num: int = None,
    ):
        # The total number of alerts.
        self.all = all
        self.count_map = count_map
        # The number of high-risk alerts.
        self.high = high
        # The number of low-risk alerts.
        self.low = low
        # The number of medium-risk alerts.
        self.medium = medium
        # The number of connected services.
        self.product_num = product_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.count_map is not None:
            result['CountMap'] = self.count_map

        if self.high is not None:
            result['High'] = self.high

        if self.low is not None:
            result['Low'] = self.low

        if self.medium is not None:
            result['Medium'] = self.medium

        if self.product_num is not None:
            result['ProductNum'] = self.product_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('CountMap') is not None:
            self.count_map = m.get('CountMap')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('ProductNum') is not None:
            self.product_num = m.get('ProductNum')

        return self

