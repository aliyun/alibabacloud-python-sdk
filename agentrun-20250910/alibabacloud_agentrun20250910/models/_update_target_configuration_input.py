# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateTargetConfigurationInput(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        target_configuration: main_models.TargetConfiguration = None,
    ):
        self.domain_id = domain_id
        self.target_configuration = target_configuration

    def validate(self):
        if self.target_configuration:
            self.target_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.target_configuration is not None:
            result['targetConfiguration'] = self.target_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('targetConfiguration') is not None:
            temp_model = main_models.TargetConfiguration()
            self.target_configuration = temp_model.from_map(m.get('targetConfiguration'))

        return self

