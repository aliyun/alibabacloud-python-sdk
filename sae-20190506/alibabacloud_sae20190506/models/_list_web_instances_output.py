# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListWebInstancesOutput(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        web_instances: List[main_models.WebInstanceInfo] = None,
        web_version_status: Dict[str, main_models.WebVersionStatus] = None,
    ):
        self.current_error = current_error
        self.web_instances = web_instances
        self.web_version_status = web_version_status

    def validate(self):
        if self.web_instances:
            for v1 in self.web_instances:
                 if v1:
                    v1.validate()
        if self.web_version_status:
            for v1 in self.web_version_status.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_error is not None:
            result['CurrentError'] = self.current_error

        result['WebInstances'] = []
        if self.web_instances is not None:
            for k1 in self.web_instances:
                result['WebInstances'].append(k1.to_map() if k1 else None)

        result['WebVersionStatus'] = {}
        if self.web_version_status is not None:
            for k1, v1 in self.web_version_status.items():
                result['WebVersionStatus'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentError') is not None:
            self.current_error = m.get('CurrentError')

        self.web_instances = []
        if m.get('WebInstances') is not None:
            for k1 in m.get('WebInstances'):
                temp_model = main_models.WebInstanceInfo()
                self.web_instances.append(temp_model.from_map(k1))

        self.web_version_status = {}
        if m.get('WebVersionStatus') is not None:
            for k1, v1 in m.get('WebVersionStatus').items():
                temp_model = main_models.WebVersionStatus()
                self.web_version_status[k1] = temp_model.from_map(v1)

        return self

