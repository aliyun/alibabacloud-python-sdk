# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHealthCheckTemplateAttributeRequest(DaraModel):
    def __init__(
        self,
        health_check_template_id: str = None,
    ):
        # The ID of the health check template.
        # 
        # This parameter is required.
        self.health_check_template_id = health_check_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_check_template_id is not None:
            result['HealthCheckTemplateId'] = self.health_check_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckTemplateId') is not None:
            self.health_check_template_id = m.get('HealthCheckTemplateId')

        return self

