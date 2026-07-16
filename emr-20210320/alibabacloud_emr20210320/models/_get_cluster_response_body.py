# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster: main_models.Cluster = None,
        request_id: str = None,
    ):
        # The details of the cluster.
        self.cluster = cluster
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = main_models.Cluster()
            self.cluster = temp_model.from_map(m.get('Cluster'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

