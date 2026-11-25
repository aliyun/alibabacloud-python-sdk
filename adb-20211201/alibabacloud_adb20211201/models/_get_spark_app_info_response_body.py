# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkAppInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SparkAppInfo = None,
        request_id: str = None,
    ):
        # The information about the Spark application. Response parameter description:
        # - **Data**: the Spark application template data.
        # - **EstimateExecutionCpuTimeInSeconds**: the CPU time consumed to execute the Spark application, in milliseconds.
        # - **LogRootPath**: the storage path of the log file.
        # - **LastAttemptId**: the retry ID.
        # - **WebUiAddress**: the web UI address.
        # - **SubmittedTimeInMillis**: the time when the Spark application was submitted. The value is a UNIX timestamp in milliseconds.
        # - **StartedTimeInMillis**: the time when the Spark application was created. The value is a UNIX timestamp in milliseconds.
        # - **LastUpdatedTimeInMillis**: the time when the Spark application was last updated. The value is a UNIX timestamp in milliseconds.
        # - **TerminatedTimeInMillis**: the time when the execution of the Spark application was terminated. The value is a UNIX timestamp in milliseconds.
        # - **DBClusterId**: the ID of the cluster where the Spark application is executed.
        # - **ResourceGroupName**: the name of the job resource group.
        # - **DurationInMillis**: the execution duration of the Spark application, in milliseconds.
        self.data = data
        # The request ID.
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
            temp_model = main_models.SparkAppInfo()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

