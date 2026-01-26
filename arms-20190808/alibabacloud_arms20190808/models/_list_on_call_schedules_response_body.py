# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListOnCallSchedulesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.ListOnCallSchedulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The objects that were returned.
        self.page_bean = page_bean
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.ListOnCallSchedulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListOnCallSchedulesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        on_call_schedules: List[main_models.ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The information about the scheduling policy.
        self.on_call_schedules = on_call_schedules
        # The page number of the returned page.
        self.page = page
        # The number of entries returned per page.
        self.size = size
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.on_call_schedules:
            for v1 in self.on_call_schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OnCallSchedules'] = []
        if self.on_call_schedules is not None:
            for k1 in self.on_call_schedules:
                result['OnCallSchedules'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.on_call_schedules = []
        if m.get('OnCallSchedules') is not None:
            for k1 in m.get('OnCallSchedules'):
                temp_model = main_models.ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules()
                self.on_call_schedules.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListOnCallSchedulesResponseBodyPageBeanOnCallSchedules(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
    ):
        # The description of the scheduling policy.
        self.description = description
        # The ID of the scheduling policy.
        self.id = id
        # The name of the scheduling policy.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

