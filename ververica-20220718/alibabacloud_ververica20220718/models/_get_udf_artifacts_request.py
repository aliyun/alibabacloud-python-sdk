# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUdfArtifactsRequest(DaraModel):
    def __init__(
        self,
        udf_artifact_name: str = None,
    ):
        # The name of the JAR or Python file that corresponds to the UDF.
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')

        return self

