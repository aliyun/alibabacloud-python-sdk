# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_market20151101 import models as main_models
from darabonba.model import DaraModel

class DescribeProjectOperateLogsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeProjectOperateLogsResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeProjectOperateLogsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeProjectOperateLogsResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        operator: int = None,
        operator_name: str = None,
        operator_role: str = None,
    ):
        self.description = description
        self.gmt_create = gmt_create
        self.operator = operator
        self.operator_name = operator_name
        self.operator_role = operator_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_role is not None:
            result['OperatorRole'] = self.operator_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorRole') is not None:
            self.operator_role = m.get('OperatorRole')

        return self

