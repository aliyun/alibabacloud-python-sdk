# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloneExperimentGroupResponseBody(DaraModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        request_id: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

