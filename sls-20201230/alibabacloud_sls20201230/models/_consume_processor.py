# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ConsumeProcessor(DaraModel):
    def __init__(
        self,
        configuration: main_models.ConsumeProcessorConfiguration = None,
        create_time: int = None,
        description: str = None,
        display_name: str = None,
        processor_name: str = None,
        update_time: int = None,
    ):
        # This parameter is required.
        self.configuration = configuration
        self.create_time = create_time
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.processor_name = processor_name
        self.update_time = update_time

    def validate(self):
        if self.configuration:
            self.configuration.validate()

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

        if self.processor_name is not None:
            result['processorName'] = self.processor_name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.ConsumeProcessorConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('processorName') is not None:
            self.processor_name = m.get('processorName')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

