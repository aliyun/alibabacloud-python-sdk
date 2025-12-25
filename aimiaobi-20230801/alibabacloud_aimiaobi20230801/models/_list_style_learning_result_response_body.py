# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListStyleLearningResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[main_models.ListStyleLearningResultResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current is not None:
            result['Current'] = self.current

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListStyleLearningResultResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListStyleLearningResultResponseBodyData(DaraModel):
    def __init__(
        self,
        aigc_result: str = None,
        id: int = None,
        rewrite_result: str = None,
        style_name: str = None,
        task_id: str = None,
    ):
        self.aigc_result = aigc_result
        self.id = id
        self.rewrite_result = rewrite_result
        self.style_name = style_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aigc_result is not None:
            result['AigcResult'] = self.aigc_result

        if self.id is not None:
            result['Id'] = self.id

        if self.rewrite_result is not None:
            result['RewriteResult'] = self.rewrite_result

        if self.style_name is not None:
            result['StyleName'] = self.style_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AigcResult') is not None:
            self.aigc_result = m.get('AigcResult')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RewriteResult') is not None:
            self.rewrite_result = m.get('RewriteResult')

        if m.get('StyleName') is not None:
            self.style_name = m.get('StyleName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

