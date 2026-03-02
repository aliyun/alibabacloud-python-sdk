# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UdfFunction(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        function_name: str = None,
        udf_artifact_name: str = None,
    ):
        self.class_name = class_name
        self.function_name = function_name
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['className'] = self.class_name

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')

        return self

