# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateMaxComputeExportRequest(DaraModel):
    def __init__(
        self,
        configuration: main_models.MaxComputeExportConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # The setting of the MaxCompute data shipping job.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the MaxCompute data shipping job.
        self.description = description
        # The display name of the MaxCompute data shipping job.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The unique identifier of the MaxCompute data shipping job.
        # 
        # This parameter is required.
        self.name = name

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

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.MaxComputeExportConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

