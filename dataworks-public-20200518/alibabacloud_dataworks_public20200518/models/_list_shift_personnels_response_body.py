# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListShiftPersonnelsResponseBody(DaraModel):
    def __init__(
        self,
        paging: main_models.ListShiftPersonnelsResponseBodyPaging = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging = paging
        # The request ID. You can use the ID to troubleshoot issues.
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
            temp_model = main_models.ListShiftPersonnelsResponseBodyPaging()
            self.paging = temp_model.from_map(m.get('Paging'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListShiftPersonnelsResponseBodyPaging(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        shift_persons: List[main_models.ListShiftPersonnelsResponseBodyPagingShiftPersons] = None,
        total_count: int = None,
    ):
        # The page number. Valid values: 1 to 100. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The on-duty engineers in the shift schedule.
        self.shift_persons = shift_persons
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.shift_persons:
            for v1 in self.shift_persons:
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

        result['ShiftPersons'] = []
        if self.shift_persons is not None:
            for k1 in self.shift_persons:
                result['ShiftPersons'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.shift_persons = []
        if m.get('ShiftPersons') is not None:
            for k1 in m.get('ShiftPersons'):
                temp_model = main_models.ListShiftPersonnelsResponseBodyPagingShiftPersons()
                self.shift_persons.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListShiftPersonnelsResponseBodyPagingShiftPersons(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        shift_person_name: str = None,
        shift_person_uid: str = None,
    ):
        # The time when the on-duty engineer starts the shift.
        self.begin_time = begin_time
        # The time when the on-duty engineer ends the shift.
        self.end_time = end_time
        # The name of the on-duty engineer.
        self.shift_person_name = shift_person_name
        # The UID of the on-duty engineer.
        self.shift_person_uid = shift_person_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.shift_person_name is not None:
            result['ShiftPersonName'] = self.shift_person_name

        if self.shift_person_uid is not None:
            result['ShiftPersonUID'] = self.shift_person_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ShiftPersonName') is not None:
            self.shift_person_name = m.get('ShiftPersonName')

        if m.get('ShiftPersonUID') is not None:
            self.shift_person_uid = m.get('ShiftPersonUID')

        return self

