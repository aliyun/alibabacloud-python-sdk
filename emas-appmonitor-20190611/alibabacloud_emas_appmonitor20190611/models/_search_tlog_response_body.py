# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class SearchTlogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: int = None,
        message: str = None,
        model: main_models.SearchTlogResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.SearchTlogResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchTlogResponseBodyModel(DaraModel):
    def __init__(
        self,
        data: List[Any] = None,
        page_num: int = None,
        page_size: int = None,
        took: int = None,
        total: int = None,
        trend: List[Any] = None,
    ):
        self.data = data
        self.page_num = page_num
        self.page_size = page_size
        self.took = took
        self.total = total
        self.trend = trend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.took is not None:
            result['Took'] = self.took

        if self.total is not None:
            result['Total'] = self.total

        if self.trend is not None:
            result['Trend'] = self.trend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Took') is not None:
            self.took = m.get('Took')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        return self

