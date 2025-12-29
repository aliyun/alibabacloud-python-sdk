# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListInstancesOutput(DaraModel):
    def __init__(
        self,
        current_error: str = None,
        instances: List[main_models.InstanceInfo] = None,
        request_id: str = None,
        version_status: Dict[str, main_models.VersionStatus] = None,
    ):
        self.current_error = current_error
        self.instances = instances
        self.request_id = request_id
        self.version_status = version_status

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.version_status:
            for v1 in self.version_status.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_error is not None:
            result['currentError'] = self.current_error

        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['versionStatus'] = {}
        if self.version_status is not None:
            for k1, v1 in self.version_status.items():
                result['versionStatus'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentError') is not None:
            self.current_error = m.get('currentError')

        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.InstanceInfo()
                self.instances.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.version_status = {}
        if m.get('versionStatus') is not None:
            for k1, v1 in m.get('versionStatus').items():
                temp_model = main_models.VersionStatus()
                self.version_status[k1] = temp_model.from_map(v1)

        return self

