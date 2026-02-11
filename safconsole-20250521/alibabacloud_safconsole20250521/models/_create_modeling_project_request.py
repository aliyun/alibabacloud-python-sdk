# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelingProjectRequest(DaraModel):
    def __init__(
        self,
        instance_spec: str = None,
        project_name: str = None,
        remark: str = None,
    ):
        # Instance specification.
        # 
        # This parameter is required.
        self.instance_spec = instance_spec
        # Project name
        # 
        # This parameter is required.
        self.project_name = project_name
        # Remark.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

