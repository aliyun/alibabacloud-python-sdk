# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SavepointStatus(DaraModel):
    def __init__(
        self,
        failure: main_models.SavepointFailure = None,
        state: str = None,
    ):
        # The details of the failure to create a savepoint for the deployment.
        self.failure = failure
        # The status of the savepoint that is created for the deployment. Valid values:
        # 
        # *   STARTED
        # *   COMPLETED
        # *   FAILED
        self.state = state

    def validate(self):
        if self.failure:
            self.failure.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure is not None:
            result['failure'] = self.failure.to_map()

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failure') is not None:
            temp_model = main_models.SavepointFailure()
            self.failure = temp_model.from_map(m.get('failure'))

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

