# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateWebApplicationInput(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        description: str = None,
        revision_config: main_models.RevisionConfig = None,
        web_network_config: main_models.WebNetworkConfig = None,
        web_scaling_config: main_models.WebScalingConfig = None,
        web_traffic_config: main_models.WebTrafficConfig = None,
    ):
        # This parameter is required.
        self.application_name = application_name
        self.description = description
        # This parameter is required.
        self.revision_config = revision_config
        self.web_network_config = web_network_config
        self.web_scaling_config = web_scaling_config
        self.web_traffic_config = web_traffic_config

    def validate(self):
        if self.revision_config:
            self.revision_config.validate()
        if self.web_network_config:
            self.web_network_config.validate()
        if self.web_scaling_config:
            self.web_scaling_config.validate()
        if self.web_traffic_config:
            self.web_traffic_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.description is not None:
            result['Description'] = self.description

        if self.revision_config is not None:
            result['RevisionConfig'] = self.revision_config.to_map()

        if self.web_network_config is not None:
            result['WebNetworkConfig'] = self.web_network_config.to_map()

        if self.web_scaling_config is not None:
            result['WebScalingConfig'] = self.web_scaling_config.to_map()

        if self.web_traffic_config is not None:
            result['WebTrafficConfig'] = self.web_traffic_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RevisionConfig') is not None:
            temp_model = main_models.RevisionConfig()
            self.revision_config = temp_model.from_map(m.get('RevisionConfig'))

        if m.get('WebNetworkConfig') is not None:
            temp_model = main_models.WebNetworkConfig()
            self.web_network_config = temp_model.from_map(m.get('WebNetworkConfig'))

        if m.get('WebScalingConfig') is not None:
            temp_model = main_models.WebScalingConfig()
            self.web_scaling_config = temp_model.from_map(m.get('WebScalingConfig'))

        if m.get('WebTrafficConfig') is not None:
            temp_model = main_models.WebTrafficConfig()
            self.web_traffic_config = temp_model.from_map(m.get('WebTrafficConfig'))

        return self

