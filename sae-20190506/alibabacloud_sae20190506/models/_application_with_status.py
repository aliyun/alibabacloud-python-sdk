# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ApplicationWithStatus(DaraModel):
    def __init__(
        self,
        application: main_models.Application = None,
        status: main_models.ApplicationStatus = None,
    ):
        self.application = application
        self.status = status

    def validate(self):
        if self.application:
            self.application.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application is not None:
            result['application'] = self.application.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = main_models.Application()
            self.application = temp_model.from_map(m.get('application'))

        if m.get('status') is not None:
            temp_model = main_models.ApplicationStatus()
            self.status = temp_model.from_map(m.get('status'))

        return self

