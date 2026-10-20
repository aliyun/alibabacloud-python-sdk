# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCalendarsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCalendarsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCalendarsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCalendarsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        calendars: List[main_models.ListCalendarsResponseBodyPagingInfoCalendars] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of scheduling calendars.
        self.calendars = calendars
        # The page number.
        self.page_number = page_number
        # The number of items per page.
        self.page_size = page_size
        # The total number of items.
        self.total_count = total_count

    def validate(self):
        if self.calendars:
            for v1 in self.calendars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Calendars'] = []
        if self.calendars is not None:
            for k1 in self.calendars:
                result['Calendars'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calendars = []
        if m.get('Calendars') is not None:
            for k1 in m.get('Calendars'):
                temp_model = main_models.ListCalendarsResponseBodyPagingInfoCalendars()
                self.calendars.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCalendarsResponseBodyPagingInfoCalendars(DaraModel):
    def __init__(
        self,
        all_projects: bool = None,
        description: str = None,
        end_date: str = None,
        expiration_reminder: str = None,
        fallback_policy: str = None,
        id: int = None,
        modify_time: int = None,
        name: str = None,
        overdue_policy: str = None,
        owner: str = None,
        project_ids: List[int] = None,
        schedule_policy: main_models.ListCalendarsResponseBodyPagingInfoCalendarsSchedulePolicy = None,
        start_date: str = None,
        type: str = None,
        version: int = None,
    ):
        # Indicates whether the calendar is applicable to all workspaces.
        self.all_projects = all_projects
        # The description of the scheduling calendar.
        self.description = description
        # The end date of the calendar validity period. Format: `yyyy-mm-dd`. This parameter is returned only for strongly constrained calendars.
        self.end_date = end_date
        # The expiration reminder. This parameter is returned only for strongly constrained calendars. Valid values:
        # 
        # - OneMonthBefore: One month in advance.
        # - OneWeekBefore: One week in advance.
        # - ThreeDaysBefore: Three days in advance.
        self.expiration_reminder = expiration_reminder
        # The default scheduling policy for dates that are not configured. This parameter is returned only for weakly constrained calendars. Valid values:
        # 
        # - Normal: Normal scheduling.
        # - Pause: Pause scheduling.
        # - Skip: Dry run.
        self.fallback_policy = fallback_policy
        # The ID of the scheduling calendar.
        self.id = id
        # The time when the calendar was modified. The value is a UNIX timestamp in milliseconds.
        self.modify_time = modify_time
        # The name of the scheduling calendar.
        self.name = name
        # The scheduling policy after the calendar expires. This parameter is returned only for strongly constrained calendars. Valid values:
        # 
        # - Normal: Normal scheduling.
        # - Pause: Pause scheduling.
        # - Skip: Dry run.
        self.overdue_policy = overdue_policy
        # The account ID of the owner.
        self.owner = owner
        # The list of applicable workspace IDs. An empty array is returned if AllProjects is set to true.
        self.project_ids = project_ids
        # The date scheduling policy.
        self.schedule_policy = schedule_policy
        # The start date of the calendar validity period. Format: `yyyy-mm-dd`. This parameter is returned only for strongly constrained calendars.
        self.start_date = start_date
        # The calendar type. Valid values:
        # 
        # - StrongConstraint: Strongly constrained calendar.
        # - WeakConstraint: Weakly constrained calendar.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.schedule_policy:
            self.schedule_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_projects is not None:
            result['AllProjects'] = self.all_projects

        if self.description is not None:
            result['Description'] = self.description

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expiration_reminder is not None:
            result['ExpirationReminder'] = self.expiration_reminder

        if self.fallback_policy is not None:
            result['FallbackPolicy'] = self.fallback_policy

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.overdue_policy is not None:
            result['OverduePolicy'] = self.overdue_policy

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids

        if self.schedule_policy is not None:
            result['SchedulePolicy'] = self.schedule_policy.to_map()

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllProjects') is not None:
            self.all_projects = m.get('AllProjects')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('ExpirationReminder') is not None:
            self.expiration_reminder = m.get('ExpirationReminder')

        if m.get('FallbackPolicy') is not None:
            self.fallback_policy = m.get('FallbackPolicy')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverduePolicy') is not None:
            self.overdue_policy = m.get('OverduePolicy')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('SchedulePolicy') is not None:
            temp_model = main_models.ListCalendarsResponseBodyPagingInfoCalendarsSchedulePolicy()
            self.schedule_policy = temp_model.from_map(m.get('SchedulePolicy'))

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListCalendarsResponseBodyPagingInfoCalendarsSchedulePolicy(DaraModel):
    def __init__(
        self,
        normal_dates: List[str] = None,
        skip_dates: List[str] = None,
    ):
        # The list of normal scheduling dates.
        self.normal_dates = normal_dates
        # The list of non-scheduling dates. Tasks perform dry runs on these dates.
        self.skip_dates = skip_dates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normal_dates is not None:
            result['NormalDates'] = self.normal_dates

        if self.skip_dates is not None:
            result['SkipDates'] = self.skip_dates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalDates') is not None:
            self.normal_dates = m.get('NormalDates')

        if m.get('SkipDates') is not None:
            self.skip_dates = m.get('SkipDates')

        return self

