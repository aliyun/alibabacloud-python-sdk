# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebApplicationWithStatus(DaraModel):
    def __init__(
        self,
        status: main_models.WebApplicationStatus = None,
        web_application: main_models.WebApplication = None,
    ):
        self.status = status
        self.web_application = web_application

    def validate(self):
        if self.status:
            self.status.validate()
        if self.web_application:
            self.web_application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status.to_map()

        if self.web_application is not None:
            result['WebApplication'] = self.web_application.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = main_models.WebApplicationStatus()
            self.status = temp_model.from_map(m.get('Status'))

        if m.get('WebApplication') is not None:
            temp_model = main_models.WebApplication()
            self.web_application = temp_model.from_map(m.get('WebApplication'))

        return self

