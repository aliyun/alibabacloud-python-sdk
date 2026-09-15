# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PublicUpdateTemplateBuildConfig(DaraModel):
    def __init__(
        self,
        copy: main_models.PublicUpdateTemplateCopyAction = None,
        envd_inject: main_models.PublicUpdateTemplateEnvdInjectAction = None,
    ):
        # The image copy action configuration.
        self.copy = copy
        # The envd injection action configuration.
        self.envd_inject = envd_inject

    def validate(self):
        if self.copy:
            self.copy.validate()
        if self.envd_inject:
            self.envd_inject.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy is not None:
            result['copy'] = self.copy.to_map()

        if self.envd_inject is not None:
            result['envdInject'] = self.envd_inject.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            temp_model = main_models.PublicUpdateTemplateCopyAction()
            self.copy = temp_model.from_map(m.get('copy'))

        if m.get('envdInject') is not None:
            temp_model = main_models.PublicUpdateTemplateEnvdInjectAction()
            self.envd_inject = temp_model.from_map(m.get('envdInject'))

        return self

