# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MonthBillSplitGetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.MonthBillSplitGetResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.MonthBillSplitGetResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MonthBillSplitGetResponseBodyModule(DaraModel):
    def __init__(
        self,
        bill_split_key: str = None,
        end_date: str = None,
        start_date: str = None,
        url: str = None,
    ):
        self.bill_split_key = bill_split_key
        self.end_date = end_date
        self.start_date = start_date
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_split_key is not None:
            result['bill_split_key'] = self.bill_split_key

        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.start_date is not None:
            result['start_date'] = self.start_date

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_split_key') is not None:
            self.bill_split_key = m.get('bill_split_key')

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

