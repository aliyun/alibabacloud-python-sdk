# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructRefreshJobModel(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        processid: str = None,
        refresh_interval: str = None,
        refresh_model: str = None,
        resource_group: str = None,
        scheduled_start_time: str = None,
        schema_name: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.name = name
        self.processid = processid
        self.refresh_interval = refresh_interval
        self.refresh_model = refresh_model
        self.resource_group = resource_group
        self.scheduled_start_time = scheduled_start_time
        self.schema_name = schema_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.name is not None:
            result['Name'] = self.name

        if self.processid is not None:
            result['Processid'] = self.processid

        if self.refresh_interval is not None:
            result['RefreshInterval'] = self.refresh_interval

        if self.refresh_model is not None:
            result['RefreshModel'] = self.refresh_model

        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group

        if self.scheduled_start_time is not None:
            result['ScheduledStartTime'] = self.scheduled_start_time

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Processid') is not None:
            self.processid = m.get('Processid')

        if m.get('RefreshInterval') is not None:
            self.refresh_interval = m.get('RefreshInterval')

        if m.get('RefreshModel') is not None:
            self.refresh_model = m.get('RefreshModel')

        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')

        if m.get('ScheduledStartTime') is not None:
            self.scheduled_start_time = m.get('ScheduledStartTime')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

