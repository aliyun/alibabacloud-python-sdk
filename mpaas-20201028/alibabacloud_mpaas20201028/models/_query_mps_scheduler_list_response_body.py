# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMpsSchedulerListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.QueryMpsSchedulerListResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.QueryMpsSchedulerListResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryMpsSchedulerListResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.QueryMpsSchedulerListResponseBodyResultContentData = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryMpsSchedulerListResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        return self

class QueryMpsSchedulerListResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryMpsSchedulerListResponseBodyResultContentDataList] = None,
        total_count: int = None,
    ):
        self.list = list
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryMpsSchedulerListResponseBodyResultContentDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryMpsSchedulerListResponseBodyResultContentDataList(DaraModel):
    def __init__(
        self,
        create_type: int = None,
        delivery_type: int = None,
        executed_status: str = None,
        gmt_create: int = None,
        parent_id: str = None,
        push_content: str = None,
        push_time: int = None,
        push_title: str = None,
        strategy_type: int = None,
        type: int = None,
        unique_id: str = None,
    ):
        self.create_type = create_type
        self.delivery_type = delivery_type
        self.executed_status = executed_status
        self.gmt_create = gmt_create
        self.parent_id = parent_id
        self.push_content = push_content
        self.push_time = push_time
        self.push_title = push_title
        self.strategy_type = strategy_type
        self.type = type
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.executed_status is not None:
            result['ExecutedStatus'] = self.executed_status

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.push_content is not None:
            result['PushContent'] = self.push_content

        if self.push_time is not None:
            result['PushTime'] = self.push_time

        if self.push_title is not None:
            result['PushTitle'] = self.push_title

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.type is not None:
            result['Type'] = self.type

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('ExecutedStatus') is not None:
            self.executed_status = m.get('ExecutedStatus')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PushContent') is not None:
            self.push_content = m.get('PushContent')

        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')

        if m.get('PushTitle') is not None:
            self.push_title = m.get('PushTitle')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

