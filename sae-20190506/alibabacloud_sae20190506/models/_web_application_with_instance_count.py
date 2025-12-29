# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebApplicationWithInstanceCount(DaraModel):
    def __init__(
        self,
        instance_count: int = None,
        web_application: main_models.WebApplication = None,
    ):
        self.instance_count = instance_count
        self.web_application = web_application

    def validate(self):
        if self.web_application:
            self.web_application.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.web_application is not None:
            result['WebApplication'] = self.web_application.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('WebApplication') is not None:
            temp_model = main_models.WebApplication()
            self.web_application = temp_model.from_map(m.get('WebApplication'))

        return self

