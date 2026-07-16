# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Artifact(DaraModel):
    def __init__(
        self,
        cdc_yaml_artifact: main_models.CdcYamlArtifact = None,
        jar_artifact: main_models.JarArtifact = None,
        kind: str = None,
        python_artifact: main_models.PythonArtifact = None,
        sql_artifact: main_models.SqlArtifact = None,
    ):
        # Required for a data ingestion job.
        self.cdc_yaml_artifact = cdc_yaml_artifact
        # Required for a JAR job.
        self.jar_artifact = jar_artifact
        # Specifies the kind of job. This field is required and cannot be changed after creation.
        # 
        # - SQLSCRIPT: An SQL job.
        # 
        # - JAR: A JAR job.
        # 
        # - PYTHON: A Python job.
        # 
        # - CDCYAML: A CDC data ingestion job.
        self.kind = kind
        # Required for a Python job.
        self.python_artifact = python_artifact
        # Required for an SQL job.
        self.sql_artifact = sql_artifact

    def validate(self):
        if self.cdc_yaml_artifact:
            self.cdc_yaml_artifact.validate()
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
        if self.cdc_yaml_artifact is not None:
            result['cdcYamlArtifact'] = self.cdc_yaml_artifact.to_map()

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
        if m.get('cdcYamlArtifact') is not None:
            temp_model = main_models.CdcYamlArtifact()
            self.cdc_yaml_artifact = temp_model.from_map(m.get('cdcYamlArtifact'))

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

