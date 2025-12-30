# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class QueryBrokerDemandRecordResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryBrokerDemandRecordResponseBodyData = None,
        page_size: int = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.page_size = page_size
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        if m.get('Data') is not None:
            temp_model = main_models.QueryBrokerDemandRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryBrokerDemandRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        broker_demand_record: List[main_models.QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord] = None,
    ):
        self.broker_demand_record = broker_demand_record

    def validate(self):
        if self.broker_demand_record:
            for v1 in self.broker_demand_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BrokerDemandRecord'] = []
        if self.broker_demand_record is not None:
            for k1 in self.broker_demand_record:
                result['BrokerDemandRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.broker_demand_record = []
        if m.get('BrokerDemandRecord') is not None:
            for k1 in m.get('BrokerDemandRecord'):
                temp_model = main_models.QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord()
                self.broker_demand_record.append(temp_model.from_map(k1))

        return self

class QueryBrokerDemandRecordResponseBodyDataBrokerDemandRecord(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        create_time: int = None,
        description: str = None,
    ):
        self.biz_id = biz_id
        self.create_time = create_time
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

