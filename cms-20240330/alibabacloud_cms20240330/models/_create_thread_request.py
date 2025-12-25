# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateThreadRequest(DaraModel):
    def __init__(
        self,
        title: str = None,
        variables: main_models.CreateThreadRequestVariables = None,
    ):
        self.title = title
        self.variables = variables

    def validate(self):
        if self.variables:
            self.variables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.variables is not None:
            result['variables'] = self.variables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('variables') is not None:
            temp_model = main_models.CreateThreadRequestVariables()
            self.variables = temp_model.from_map(m.get('variables'))

        return self

class CreateThreadRequestVariables(DaraModel):
    def __init__(
        self,
        project: str = None,
        workspace: str = None,
    ):
        self.project = project
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['project'] = self.project

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

