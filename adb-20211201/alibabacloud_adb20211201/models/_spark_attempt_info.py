# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SparkAttemptInfo(DaraModel):
    def __init__(
        self,
        attempt_id: str = None,
        detail: main_models.Detail = None,
        message: str = None,
        priority: str = None,
        state: str = None,
    ):
        # The attempt ID of the Spark application.
        self.attempt_id = attempt_id
        # The information about the Spark application.
        self.detail = detail
        # The alert message returned, such as task execution failure or insufficient resources. If no alert occurs, null is returned.
        self.message = message
        # The attempt priority of the Spark application.
        self.priority = priority
        # The state of the Spark application. Valid values:
        # 
        # *   **SUBMITTED**
        # *   **STARTING**
        # *   **RUNNING**
        # *   **FAILING**
        # *   **FAILED**
        # *   **KILLING**
        # *   **KILLED**
        # *   **SUCCEEDING**
        # *   **COMPLETED**
        # *   **FATAL**
        # *   **UNKNOWN**
        self.state = state

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')

        if m.get('Detail') is not None:
            temp_model = main_models.Detail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

