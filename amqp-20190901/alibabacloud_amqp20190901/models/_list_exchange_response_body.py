# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class ListExchangeResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListExchangeResponseBodyData = None,
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
            temp_model = main_models.ListExchangeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListExchangeResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: main_models.ListExchangeResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VoList') is not None:
            temp_model = main_models.ListExchangeResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class ListExchangeResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        exchang_vo: List[main_models.ListExchangeResponseBodyDataVoListExchangVO] = None,
    ):
        self.exchang_vo = exchang_vo

    def validate(self):
        if self.exchang_vo:
            for v1 in self.exchang_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExchangVO'] = []
        if self.exchang_vo is not None:
            for k1 in self.exchang_vo:
                result['ExchangVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchang_vo = []
        if m.get('ExchangVO') is not None:
            for k1 in m.get('ExchangVO'):
                temp_model = main_models.ListExchangeResponseBodyDataVoListExchangVO()
                self.exchang_vo.append(temp_model.from_map(k1))

        return self

class ListExchangeResponseBodyDataVoListExchangVO(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        auto_delete: bool = None,
        can_delete: bool = None,
        create_time: int = None,
        exchange_type: int = None,
        internal: bool = None,
        name: str = None,
        vhost_name: str = None,
    ):
        self.attributes = attributes
        self.auto_delete = auto_delete
        self.can_delete = can_delete
        self.create_time = create_time
        self.exchange_type = exchange_type
        self.internal = internal
        self.name = name
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete

        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type

        if self.internal is not None:
            result['Internal'] = self.internal

        if self.name is not None:
            result['Name'] = self.name

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')

        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')

        if m.get('Internal') is not None:
            self.internal = m.get('Internal')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

