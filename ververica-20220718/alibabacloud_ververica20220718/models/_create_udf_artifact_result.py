# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class CreateUdfArtifactResult(DaraModel):
    def __init__(
        self,
        colliding_classes: List[main_models.UdfClass] = None,
        create_success: bool = None,
        message: str = None,
        udf_artifact: main_models.UdfArtifact = None,
    ):
        # All classes in conflict.
        self.colliding_classes = colliding_classes
        # Indicates whether the JAR file was created.
        self.create_success = create_success
        # The message used to create the JAR file.
        self.message = message
        # The JAR file that you created.
        self.udf_artifact = udf_artifact

    def validate(self):
        if self.colliding_classes:
            for v1 in self.colliding_classes:
                 if v1:
                    v1.validate()
        if self.udf_artifact:
            self.udf_artifact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['collidingClasses'] = []
        if self.colliding_classes is not None:
            for k1 in self.colliding_classes:
                result['collidingClasses'].append(k1.to_map() if k1 else None)

        if self.create_success is not None:
            result['createSuccess'] = self.create_success

        if self.message is not None:
            result['message'] = self.message

        if self.udf_artifact is not None:
            result['udfArtifact'] = self.udf_artifact.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.colliding_classes = []
        if m.get('collidingClasses') is not None:
            for k1 in m.get('collidingClasses'):
                temp_model = main_models.UdfClass()
                self.colliding_classes.append(temp_model.from_map(k1))

        if m.get('createSuccess') is not None:
            self.create_success = m.get('createSuccess')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('udfArtifact') is not None:
            temp_model = main_models.UdfArtifact()
            self.udf_artifact = temp_model.from_map(m.get('udfArtifact'))

        return self

