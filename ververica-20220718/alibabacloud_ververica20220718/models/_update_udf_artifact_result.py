# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class UpdateUdfArtifactResult(DaraModel):
    def __init__(
        self,
        colliding_classes: List[main_models.UdfClass] = None,
        message: str = None,
        missing_classes: List[main_models.UdfClass] = None,
        udf_artifact: main_models.UdfArtifact = None,
        update_success: bool = None,
    ):
        self.colliding_classes = colliding_classes
        self.message = message
        self.missing_classes = missing_classes
        self.udf_artifact = udf_artifact
        self.update_success = update_success

    def validate(self):
        if self.colliding_classes:
            for v1 in self.colliding_classes:
                 if v1:
                    v1.validate()
        if self.missing_classes:
            for v1 in self.missing_classes:
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

        if self.message is not None:
            result['message'] = self.message

        result['missingClasses'] = []
        if self.missing_classes is not None:
            for k1 in self.missing_classes:
                result['missingClasses'].append(k1.to_map() if k1 else None)

        if self.udf_artifact is not None:
            result['udfArtifact'] = self.udf_artifact.to_map()

        if self.update_success is not None:
            result['updateSuccess'] = self.update_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.colliding_classes = []
        if m.get('collidingClasses') is not None:
            for k1 in m.get('collidingClasses'):
                temp_model = main_models.UdfClass()
                self.colliding_classes.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        self.missing_classes = []
        if m.get('missingClasses') is not None:
            for k1 in m.get('missingClasses'):
                temp_model = main_models.UdfClass()
                self.missing_classes.append(temp_model.from_map(k1))

        if m.get('udfArtifact') is not None:
            temp_model = main_models.UdfArtifact()
            self.udf_artifact = temp_model.from_map(m.get('udfArtifact'))

        if m.get('updateSuccess') is not None:
            self.update_success = m.get('updateSuccess')

        return self

