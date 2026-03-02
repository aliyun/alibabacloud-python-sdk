# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetQueueConsumersResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetQueueConsumersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQueueConsumersResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        task_id: str = None,
        total_count: int = None,
        vo_list: List[main_models.GetQueueConsumersResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.task_id = task_id
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for v1 in self.vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VoList'] = []
        if self.vo_list is not None:
            for k1 in self.vo_list:
                result['VoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vo_list = []
        if m.get('VoList') is not None:
            for k1 in m.get('VoList'):
                temp_model = main_models.GetQueueConsumersResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k1))

        return self

class GetQueueConsumersResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        client_address: str = None,
        consumer_tag: str = None,
        gmt_create: int = None,
    ):
        self.client_address = client_address
        self.consumer_tag = consumer_tag
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_address is not None:
            result['ClientAddress'] = self.client_address

        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddress') is not None:
            self.client_address = m.get('ClientAddress')

        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        return self

