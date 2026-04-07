# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListShiftSchedulesResponseBody(DaraModel):
    def __init__(
        self,
        paging: main_models.ListShiftSchedulesResponseBodyPaging = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging = paging
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paging') is not None:
            temp_model = main_models.ListShiftSchedulesResponseBodyPaging()
            self.paging = temp_model.from_map(m.get('Paging'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListShiftSchedulesResponseBodyPaging(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        shift_schedules: List[main_models.ListShiftSchedulesResponseBodyPagingShiftSchedules] = None,
        total_count: int = None,
    ):
        # The page number. Minimum value: 1. Maximum value: 100.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The shift schedules.
        self.shift_schedules = shift_schedules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.shift_schedules:
            for v1 in self.shift_schedules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ShiftSchedules'] = []
        if self.shift_schedules is not None:
            for k1 in self.shift_schedules:
                result['ShiftSchedules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.shift_schedules = []
        if m.get('ShiftSchedules') is not None:
            for k1 in m.get('ShiftSchedules'):
                temp_model = main_models.ListShiftSchedulesResponseBodyPagingShiftSchedules()
                self.shift_schedules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListShiftSchedulesResponseBodyPagingShiftSchedules(DaraModel):
    def __init__(
        self,
        shift_schedule_identifier: str = None,
        shift_schedule_name: str = None,
    ):
        # The unique identifier of the shift schedule. You can use the identifier to query the on-duty engineers in the shift schedule.
        self.shift_schedule_identifier = shift_schedule_identifier
        # The name of the shift schedule.
        self.shift_schedule_name = shift_schedule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.shift_schedule_identifier is not None:
            result['ShiftScheduleIdentifier'] = self.shift_schedule_identifier

        if self.shift_schedule_name is not None:
            result['ShiftScheduleName'] = self.shift_schedule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShiftScheduleIdentifier') is not None:
            self.shift_schedule_identifier = m.get('ShiftScheduleIdentifier')

        if m.get('ShiftScheduleName') is not None:
            self.shift_schedule_name = m.get('ShiftScheduleName')

        return self

