# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListSparkAppAttemptsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSparkAppAttemptsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = main_models.ListSparkAppAttemptsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSparkAppAttemptsResponseBodyData(DaraModel):
    def __init__(
        self,
        attempt_info_list: List[main_models.SparkAttemptInfo] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of retry information. Metric description:
        # - **AttemptId**: the retry ID.
        # - **State**: the execute status of the application. Valid values:
        #     - **SUBMITTED**: commit.
        #     - **STARTING**: starting.
        #     - **RUNNING**: executing.
        #     - **FAILING**: the node failed and the environment is being cleaned up.
        #     - **FAILED**: failed.
        #     - **KILLING**: aborting the task and cleaning up the environment.
        #     - **KILLED**: the task is aborted.
        #     - **SUCCEEDING**: the node execution is complete and the environment is being cleaned up.
        #     - **COMPLETED**: the node execution is complete.
        #     - **FATAL**: unexpected failure.
        #     - **UNKNOWN**: unknown fault.
        # - **Message**: the alerting message. This parameter is empty if no alerting is generated.
        # - **Data**: the Spark application template data.
        # - **EstimateExecutionCpuTimeInSeconds**: the CPU time consumed to execute the Spark application, in milliseconds (ms).
        # - **LogRootPath**: the storage path of log files.
        # - **LastAttemptId**: the ID of the last retry.
        # - **WebUiAddress**: the web UI address.
        # - **SubmittedTimeInMillis**: the time when the Spark application was committed. This value is a UNIX timestamp in milliseconds (ms).
        # - **StartedTimeInMillis**: the time when the Spark application was created. This value is a UNIX timestamp in milliseconds (ms).
        # - **LastUpdatedTimeInMillis**: the time when the Spark application was last updated. This value is a UNIX timestamp in milliseconds (ms).
        # - **TerminatedTimeInMillis**: the time when the Spark application stopped executing. This value is a UNIX timestamp in milliseconds (ms).
        # - **DBClusterId**: the ID of the cluster that executes the Spark application.
        # - **ResourceGroupName**: the name of the Job-type resource group.
        # - **DurationInMillis**: the execution duration of the Spark application, in milliseconds (ms).
        self.attempt_info_list = attempt_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.attempt_info_list:
            for v1 in self.attempt_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttemptInfoList'] = []
        if self.attempt_info_list is not None:
            for k1 in self.attempt_info_list:
                result['AttemptInfoList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attempt_info_list = []
        if m.get('AttemptInfoList') is not None:
            for k1 in m.get('AttemptInfoList'):
                temp_model = main_models.SparkAttemptInfo()
                self.attempt_info_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

