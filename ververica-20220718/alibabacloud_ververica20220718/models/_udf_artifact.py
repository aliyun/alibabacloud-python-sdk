# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class UdfArtifact(DaraModel):
    def __init__(
        self,
        artifact_type: str = None,
        created_at: int = None,
        creator: str = None,
        dependency_jar_uris: List[str] = None,
        jar_url: str = None,
        modified_at: int = None,
        name: str = None,
        namespace: str = None,
        udf_classes: List[main_models.UdfClass] = None,
    ):
        # The type of the JAR file.
        self.artifact_type = artifact_type
        # The time when the JAR file was created.
        self.created_at = created_at
        # The user that creates the JAR file.
        self.creator = creator
        # The list of paths in which the additional dependencies of the JAR file are stored.
        self.dependency_jar_uris = dependency_jar_uris
        # The path in which the JAR file is stored.
        self.jar_url = jar_url
        # The time when the JAR file was modified.
        self.modified_at = modified_at
        # The name of the JAR file.
        self.name = name
        # The namespace.
        self.namespace = namespace
        # The list of the class name of the JAR file.
        self.udf_classes = udf_classes

    def validate(self):
        if self.udf_classes:
            for v1 in self.udf_classes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.dependency_jar_uris is not None:
            result['dependencyJarUris'] = self.dependency_jar_uris

        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        result['udfClasses'] = []
        if self.udf_classes is not None:
            for k1 in self.udf_classes:
                result['udfClasses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactType') is not None:
            self.artifact_type = m.get('artifactType')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('dependencyJarUris') is not None:
            self.dependency_jar_uris = m.get('dependencyJarUris')

        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        self.udf_classes = []
        if m.get('udfClasses') is not None:
            for k1 in m.get('udfClasses'):
                temp_model = main_models.UdfClass()
                self.udf_classes.append(temp_model.from_map(k1))

        return self

