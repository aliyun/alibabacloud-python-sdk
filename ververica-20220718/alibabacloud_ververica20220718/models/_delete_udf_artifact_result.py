# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DeleteUdfArtifactResult(DaraModel):
    def __init__(
        self,
        delete_success: bool = None,
        message: str = None,
        referenced_classes: List[main_models.UdfClass] = None,
    ):
        # Indicates whether the JAR file was deleted.
        self.delete_success = delete_success
        # The message used to delete the JAR file.
        self.message = message
        # All associated classes.
        self.referenced_classes = referenced_classes

    def validate(self):
        if self.referenced_classes:
            for v1 in self.referenced_classes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_success is not None:
            result['deleteSuccess'] = self.delete_success

        if self.message is not None:
            result['message'] = self.message

        result['referencedClasses'] = []
        if self.referenced_classes is not None:
            for k1 in self.referenced_classes:
                result['referencedClasses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleteSuccess') is not None:
            self.delete_success = m.get('deleteSuccess')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.referenced_classes = []
        if m.get('referencedClasses') is not None:
            for k1 in m.get('referencedClasses'):
                temp_model = main_models.UdfClass()
                self.referenced_classes.append(temp_model.from_map(k1))

        return self

