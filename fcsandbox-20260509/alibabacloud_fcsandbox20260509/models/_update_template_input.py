# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class UpdateTemplateInput(DaraModel):
    def __init__(
        self,
        container_configuration: main_models.ContainerConfiguration = None,
        log_configuration: main_models.LogConfiguration = None,
        network_configuration: main_models.NetworkConfiguration = None,
        team_id: str = None,
    ):
        self.container_configuration = container_configuration
        self.log_configuration = log_configuration
        self.network_configuration = network_configuration
        self.team_id = team_id

    def validate(self):
        if self.container_configuration:
            self.container_configuration.validate()
        if self.log_configuration:
            self.log_configuration.validate()
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_configuration is not None:
            result['containerConfiguration'] = self.container_configuration.to_map()

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.team_id is not None:
            result['teamID'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerConfiguration') is not None:
            temp_model = main_models.ContainerConfiguration()
            self.container_configuration = temp_model.from_map(m.get('containerConfiguration'))

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.NetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        return self

