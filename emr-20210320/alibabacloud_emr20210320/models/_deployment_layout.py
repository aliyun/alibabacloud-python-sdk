# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class DeploymentLayout(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        component_name: str = None,
        node_selector: main_models.NodeSelector = None,
    ):
        self.application_name = application_name
        self.component_name = component_name
        self.node_selector = node_selector

    def validate(self):
        if self.node_selector:
            self.node_selector.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.node_selector is not None:
            result['NodeSelector'] = self.node_selector.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('NodeSelector') is not None:
            temp_model = main_models.NodeSelector()
            self.node_selector = temp_model.from_map(m.get('NodeSelector'))

        return self

