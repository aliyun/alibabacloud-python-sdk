# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UdfClass(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        class_type: str = None,
        function_names: List[str] = None,
        udf_artifact_name: str = None,
    ):
        # The name of the class.
        self.class_name = class_name
        # The type of the class.
        self.class_type = class_type
        # The list of UDF names.
        self.function_names = function_names
        # The name of the UDF JAR file.
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

        if self.class_type is not None:
            result['classType'] = self.class_type

        if self.function_names is not None:
            result['functionNames'] = self.function_names

        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')

        if m.get('classType') is not None:
            self.class_type = m.get('classType')

        if m.get('functionNames') is not None:
            self.function_names = m.get('functionNames')

        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')

        return self

