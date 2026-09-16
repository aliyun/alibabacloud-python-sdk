# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListLumaCatalogsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLumaCatalogsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates a successful call. A specific error code is returned when the call fails.
        self.code = code
        # The list of data catalogs bound to the Agent. All results are returned at once without pagination.
        self.data = data
        # The message returned by the operation. The value is Operation success when the call succeeds, or a specific error description when the call fails.
        self.message = message
        # The unique identifier of the request, used for troubleshooting and ticket submission.
        self.request_id = request_id
        # Indicates whether the call was successful. A value of true indicates success.
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
            temp_model = main_models.ListLumaCatalogsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLumaCatalogsResponseBodyData(DaraModel):
    def __init__(
        self,
        catalogs: List[main_models.Catalog] = None,
        limit: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of data catalogs bound to the Agent.
        self.catalogs = catalogs
        # 本次请求实际生效的每页数量。未传 Limit 时为服务端默认值，超出上限时为收敛后的值
        self.limit = limit
        # 下一页起始Token，传入下次请求的 NextToken 可获取下一页；为空表示已无更多数据
        self.next_token = next_token
        # Agent 绑定的数据目录总数，与本页返回条数无关
        self.total_count = total_count

    def validate(self):
        if self.catalogs:
            for v1 in self.catalogs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Catalogs'] = []
        if self.catalogs is not None:
            for k1 in self.catalogs:
                result['Catalogs'].append(k1.to_map() if k1 else None)

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.catalogs = []
        if m.get('Catalogs') is not None:
            for k1 in m.get('Catalogs'):
                temp_model = main_models.Catalog()
                self.catalogs.append(temp_model.from_map(k1))

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

