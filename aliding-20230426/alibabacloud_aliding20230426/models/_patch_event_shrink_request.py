# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PatchEventShrinkRequest(DaraModel):
    def __init__(
        self,
        attendees_shrink: str = None,
        calendar_id: str = None,
        card_instances_shrink: str = None,
        description: str = None,
        end_shrink: str = None,
        event_id: str = None,
        extra_shrink: str = None,
        is_all_day: bool = None,
        location_shrink: str = None,
        recurrence_shrink: str = None,
        reminders_shrink: str = None,
        start_shrink: str = None,
        summary: str = None,
        categories_shrink: str = None,
        free_busy_status: str = None,
        online_meeting_info_shrink: str = None,
        rich_text_description_shrink: str = None,
        ui_configs_shrink: str = None,
    ):
        self.attendees_shrink = attendees_shrink
        # This parameter is required.
        self.calendar_id = calendar_id
        self.card_instances_shrink = card_instances_shrink
        self.description = description
        self.end_shrink = end_shrink
        # This parameter is required.
        self.event_id = event_id
        self.extra_shrink = extra_shrink
        self.is_all_day = is_all_day
        self.location_shrink = location_shrink
        self.recurrence_shrink = recurrence_shrink
        self.reminders_shrink = reminders_shrink
        self.start_shrink = start_shrink
        self.summary = summary
        self.categories_shrink = categories_shrink
        self.free_busy_status = free_busy_status
        self.online_meeting_info_shrink = online_meeting_info_shrink
        self.rich_text_description_shrink = rich_text_description_shrink
        self.ui_configs_shrink = ui_configs_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attendees_shrink is not None:
            result['Attendees'] = self.attendees_shrink

        if self.calendar_id is not None:
            result['CalendarId'] = self.calendar_id

        if self.card_instances_shrink is not None:
            result['CardInstances'] = self.card_instances_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.end_shrink is not None:
            result['End'] = self.end_shrink

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.is_all_day is not None:
            result['IsAllDay'] = self.is_all_day

        if self.location_shrink is not None:
            result['Location'] = self.location_shrink

        if self.recurrence_shrink is not None:
            result['Recurrence'] = self.recurrence_shrink

        if self.reminders_shrink is not None:
            result['Reminders'] = self.reminders_shrink

        if self.start_shrink is not None:
            result['Start'] = self.start_shrink

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.categories_shrink is not None:
            result['categories'] = self.categories_shrink

        if self.free_busy_status is not None:
            result['freeBusyStatus'] = self.free_busy_status

        if self.online_meeting_info_shrink is not None:
            result['onlineMeetingInfo'] = self.online_meeting_info_shrink

        if self.rich_text_description_shrink is not None:
            result['richTextDescription'] = self.rich_text_description_shrink

        if self.ui_configs_shrink is not None:
            result['uiConfigs'] = self.ui_configs_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attendees') is not None:
            self.attendees_shrink = m.get('Attendees')

        if m.get('CalendarId') is not None:
            self.calendar_id = m.get('CalendarId')

        if m.get('CardInstances') is not None:
            self.card_instances_shrink = m.get('CardInstances')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('End') is not None:
            self.end_shrink = m.get('End')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')

        if m.get('IsAllDay') is not None:
            self.is_all_day = m.get('IsAllDay')

        if m.get('Location') is not None:
            self.location_shrink = m.get('Location')

        if m.get('Recurrence') is not None:
            self.recurrence_shrink = m.get('Recurrence')

        if m.get('Reminders') is not None:
            self.reminders_shrink = m.get('Reminders')

        if m.get('Start') is not None:
            self.start_shrink = m.get('Start')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('categories') is not None:
            self.categories_shrink = m.get('categories')

        if m.get('freeBusyStatus') is not None:
            self.free_busy_status = m.get('freeBusyStatus')

        if m.get('onlineMeetingInfo') is not None:
            self.online_meeting_info_shrink = m.get('onlineMeetingInfo')

        if m.get('richTextDescription') is not None:
            self.rich_text_description_shrink = m.get('richTextDescription')

        if m.get('uiConfigs') is not None:
            self.ui_configs_shrink = m.get('uiConfigs')

        return self

