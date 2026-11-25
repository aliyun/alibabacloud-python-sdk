# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkSQLEngineStateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSparkSQLEngineStateResponseBodyData = None,
        request_id: str = None,
    ):
        # The status details of the Spark SQL engine.
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetSparkSQLEngineStateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSparkSQLEngineStateResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        config: str = None,
        jars: str = None,
        max_executor: str = None,
        min_executor: str = None,
        slot_num: str = None,
        state: str = None,
        submitted_time_in_millis: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The configuration of the Spark application.
        self.config = config
        # The third-party JAR packages.
        self.jars = jars
        # The maximum number of Spark executors to start.
        self.max_executor = max_executor
        # The minimum number of Spark executors to start.
        self.min_executor = min_executor
        # The slot value of the Spark application.
        self.slot_num = slot_num
        # The execution status of the application. Valid values:
        # * SUBMITTED: Submitted.
        # * STARTING: Starting.
        # * RUNNING: Running.
        # * FAILING: The task failed and the environment is being cleaned up.
        # * FAILED: Failed.
        # * KILLING: The task is being terminated and the environment is being cleaned up.
        # * KILLED: Terminated.
        # * SUCCEEDING: The task execution is complete and the environment is being cleaned up.
        # * COMPLETED: Completed.
        # * FATAL: Unexpected failure.
        # * UNKNOWN: Unknown error.
        self.state = state
        # The submission time of the Spark SQL application. The value is a UNIX timestamp in milliseconds.
        self.submitted_time_in_millis = submitted_time_in_millis

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.config is not None:
            result['Config'] = self.config

        if self.jars is not None:
            result['Jars'] = self.jars

        if self.max_executor is not None:
            result['MaxExecutor'] = self.max_executor

        if self.min_executor is not None:
            result['MinExecutor'] = self.min_executor

        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num

        if self.state is not None:
            result['State'] = self.state

        if self.submitted_time_in_millis is not None:
            result['SubmittedTimeInMillis'] = self.submitted_time_in_millis

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Jars') is not None:
            self.jars = m.get('Jars')

        if m.get('MaxExecutor') is not None:
            self.max_executor = m.get('MaxExecutor')

        if m.get('MinExecutor') is not None:
            self.min_executor = m.get('MinExecutor')

        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('SubmittedTimeInMillis') is not None:
            self.submitted_time_in_millis = m.get('SubmittedTimeInMillis')

        return self

