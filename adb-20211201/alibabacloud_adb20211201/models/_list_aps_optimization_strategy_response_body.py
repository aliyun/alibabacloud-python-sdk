# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListApsOptimizationStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListApsOptimizationStrategyResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListApsOptimizationStrategyResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListApsOptimizationStrategyResponseBodyData(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        status: str = None,
        strategy_desc: str = None,
        strategy_name: str = None,
        strategy_type: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The status of the lifecycle management policy. Valid values:
        # 
        # 1.  on: enabled.
        # 2.  off: disabled.
        self.status = status
        # The description of the lifecycle management policy.
        self.strategy_desc = strategy_desc
        # The name of the lifecycle management policy.
        self.strategy_name = strategy_name
        # The type of the lifecycle management policy. Only StrategyValue is returned.
        self.strategy_type = strategy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_desc is not None:
            result['StrategyDesc'] = self.strategy_desc

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyDesc') is not None:
            self.strategy_desc = m.get('StrategyDesc')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        return self

