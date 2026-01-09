# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateElasticsearchIngestionRequest(DaraModel):
    def __init__(
        self,
        configuration: main_models.ESIngestionConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        schedule: main_models.Schedule = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.schedule = schedule

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

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.ESIngestionConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schedule') is not None:
            temp_model = main_models.Schedule()
            self.schedule = temp_model.from_map(m.get('schedule'))

        return self

