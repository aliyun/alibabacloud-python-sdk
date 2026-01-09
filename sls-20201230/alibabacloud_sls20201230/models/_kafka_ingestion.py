# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class KafkaIngestion(DaraModel):
    def __init__(
        self,
        configuration: main_models.KafkaIngestionConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        last_modified_time: int = None,
        name: str = None,
        processor_id: str = None,
        schedule: main_models.Schedule = None,
        schedule_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        self.last_modified_time = last_modified_time
        # This parameter is required.
        self.name = name
        self.processor_id = processor_id
        # This parameter is required.
        self.schedule = schedule
        self.schedule_id = schedule_id
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.name is not None:
            result['name'] = self.name

        if self.processor_id is not None:
            result['processorId'] = self.processor_id

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        if self.schedule_id is not None:
            result['scheduleId'] = self.schedule_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.KafkaIngestionConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

        if m.get('schedule') is not None:
            temp_model = main_models.Schedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        if m.get('scheduleId') is not None:
            self.schedule_id = m.get('scheduleId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

