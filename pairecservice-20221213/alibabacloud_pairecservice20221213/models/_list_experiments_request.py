# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperimentsRequest(DaraModel):
    def __init__(
        self,
        experiment_group_id: str = None,
        instance_id: str = None,
        query: str = None,
        status: str = None,
    ):
        self.experiment_group_id = experiment_group_id
        # This parameter is required.
        self.instance_id = instance_id
        self.query = query
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_group_id is not None:
            result['ExperimentGroupId'] = self.experiment_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.query is not None:
            result['Query'] = self.query

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentGroupId') is not None:
            self.experiment_group_id = m.get('ExperimentGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

