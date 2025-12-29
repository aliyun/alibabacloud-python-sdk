# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterDiagnosisResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        diagnosis_id: str = None,
        request_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The diagnostic ID.
        self.diagnosis_id = diagnosis_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.diagnosis_id is not None:
            result['diagnosis_id'] = self.diagnosis_id

        if self.request_id is not None:
            result['request_id'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('diagnosis_id') is not None:
            self.diagnosis_id = m.get('diagnosis_id')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        return self

