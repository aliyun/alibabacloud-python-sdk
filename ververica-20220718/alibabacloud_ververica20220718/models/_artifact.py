# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Artifact(DaraModel):
    def __init__(
        self,
        jar_artifact: main_models.JarArtifact = None,
        kind: str = None,
        python_artifact: main_models.PythonArtifact = None,
        sql_artifact: main_models.SqlArtifact = None,
    ):
        # The information required for the SQL deployment.
        self.jar_artifact = jar_artifact
        # The type of the deployment. This parameter is required and cannot be modified after the deployment is created.
        # 
        # *   SQLSCRIPT
        # *   JAR
        # *   PYTHON
        self.kind = kind
        # The information required for the Python deployment.
        self.python_artifact = python_artifact
        # The information required for the JAR deployment.
        self.sql_artifact = sql_artifact

    def validate(self):
        if self.jar_artifact:
            self.jar_artifact.validate()
        if self.python_artifact:
            self.python_artifact.validate()
        if self.sql_artifact:
            self.sql_artifact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.jar_artifact is not None:
            result['jarArtifact'] = self.jar_artifact.to_map()

        if self.kind is not None:
            result['kind'] = self.kind

        if self.python_artifact is not None:
            result['pythonArtifact'] = self.python_artifact.to_map()

        if self.sql_artifact is not None:
            result['sqlArtifact'] = self.sql_artifact.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarArtifact') is not None:
            temp_model = main_models.JarArtifact()
            self.jar_artifact = temp_model.from_map(m.get('jarArtifact'))

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('pythonArtifact') is not None:
            temp_model = main_models.PythonArtifact()
            self.python_artifact = temp_model.from_map(m.get('pythonArtifact'))

        if m.get('sqlArtifact') is not None:
            temp_model = main_models.SqlArtifact()
            self.sql_artifact = temp_model.from_map(m.get('sqlArtifact'))

        return self

