# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_workorder20200801 import models as main_models
from darabonba.model import DaraModel

class ListTicketsRequest(DaraModel):
    def __init__(
        self,
        created_after_time: str = None,
        created_before_time: str = None,
        extra_condition_list: List[main_models.ListTicketsRequestExtraConditionList] = None,
        ids: str = None,
        page_size: int = None,
        page_start: int = None,
        product_code: str = None,
        ticket_status: str = None,
    ):
        self.created_after_time = created_after_time
        self.created_before_time = created_before_time
        self.extra_condition_list = extra_condition_list
        self.ids = ids
        self.page_size = page_size
        self.page_start = page_start
        self.product_code = product_code
        self.ticket_status = ticket_status

    def validate(self):
        if self.extra_condition_list:
            for v1 in self.extra_condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_after_time is not None:
            result['CreatedAfterTime'] = self.created_after_time

        if self.created_before_time is not None:
            result['CreatedBeforeTime'] = self.created_before_time

        result['ExtraConditionList'] = []
        if self.extra_condition_list is not None:
            for k1 in self.extra_condition_list:
                result['ExtraConditionList'].append(k1.to_map() if k1 else None)

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.page_start is not None:
            result['PageStart'] = self.page_start

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAfterTime') is not None:
            self.created_after_time = m.get('CreatedAfterTime')

        if m.get('CreatedBeforeTime') is not None:
            self.created_before_time = m.get('CreatedBeforeTime')

        self.extra_condition_list = []
        if m.get('ExtraConditionList') is not None:
            for k1 in m.get('ExtraConditionList'):
                temp_model = main_models.ListTicketsRequestExtraConditionList()
                self.extra_condition_list.append(temp_model.from_map(k1))

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')

        return self

class ListTicketsRequestExtraConditionList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

