# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateCalendarRequest(DaraModel):
    def __init__(
        self,
        all_projects: bool = None,
        description: str = None,
        end_date: str = None,
        expiration_reminder: str = None,
        fallback_policy: str = None,
        name: str = None,
        overdue_policy: str = None,
        owner: str = None,
        project_ids: List[int] = None,
        schedule_policy: main_models.CreateCalendarRequestSchedulePolicy = None,
        start_date: str = None,
        type: str = None,
    ):
        # Specifies whether the calendar applies to all workspaces. Default value: false.
        # 
        # - true: all workspaces.
        # - false: the workspaces specified by ProjectIds.
        self.all_projects = all_projects
        # The description of the scheduling calendar. The description must be 5 to 2,048 characters in length.
        # 
        # This parameter is required.
        self.description = description
        # The end date of the calendar validity period. Format: `yyyy-mm-dd`. This parameter is required when Type is set to StrongConstraint. The end date cannot be earlier than the start date, and the interval between the start date and the end date must be less than 5 years.
        self.end_date = end_date
        # The expiration reminder. This parameter is required when Type is set to StrongConstraint.
        # 
        # - OneMonthBefore: one month in advance.
        # - OneWeekBefore: one week in advance.
        # - ThreeDaysBefore: three days in advance.
        self.expiration_reminder = expiration_reminder
        # The default scheduling policy for dates that are not configured. This parameter is required when Type is set to WeakConstraint.
        # 
        # - Normal: normal scheduling.
        # - Pause: pause scheduling.
        # - Skip: dry run.
        self.fallback_policy = fallback_policy
        # The name of the scheduling calendar. The name must be unique within the current tenant and can be up to 100 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The scheduling policy after the calendar expires. This parameter is required when Type is set to StrongConstraint.
        # 
        # - Normal: normal scheduling.
        # - Pause: pause scheduling.
        # - Skip: dry run.
        self.overdue_policy = overdue_policy
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The list of applicable workspace IDs.
        # 
        # - If AllProjects is set to false or left empty: This parameter is required and cannot be empty.
        # - If AllProjects is set to true: Leave this parameter empty or pass an empty array.
        self.project_ids = project_ids
        # The date scheduling policy. For a strong constraint calendar, the normal scheduling dates and non-scheduling dates must cover every day within the validity period and cannot overlap.
        # 
        # This parameter is required.
        self.schedule_policy = schedule_policy
        # The start date of the calendar validity period. Format: `yyyy-mm-dd`. This parameter is required when Type is set to StrongConstraint.
        self.start_date = start_date
        # The type of the calendar.
        # 
        # - StrongConstraint: strong constraint calendar.
        # - WeakConstraint: weak constraint calendar.
        # 
        # This parameter is required.
        self.type = type

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverduePolicy') is not None:
            self.overdue_policy = m.get('OverduePolicy')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')

        if m.get('SchedulePolicy') is not None:
            temp_model = main_models.CreateCalendarRequestSchedulePolicy()
            self.schedule_policy = temp_model.from_map(m.get('SchedulePolicy'))

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCalendarRequestSchedulePolicy(DaraModel):
    def __init__(
        self,
        normal_dates: List[str] = None,
        skip_dates: List[str] = None,
    ):
        # The list of normal scheduling dates.
        self.normal_dates = normal_dates
        # The list of non-scheduling dates. Tasks perform dry runs on these dates. This parameter is used only for strong constraint calendars.
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

