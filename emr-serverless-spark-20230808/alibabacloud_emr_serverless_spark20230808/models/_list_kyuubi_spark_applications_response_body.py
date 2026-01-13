# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListKyuubiSparkApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListKyuubiSparkApplicationsResponseBodyApplications] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the applications.
        self.applications = applications
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['applications'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('applications') is not None:
            for k1 in m.get('applications'):
                temp_model = main_models.ListKyuubiSparkApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListKyuubiSparkApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        cu_hours: float = None,
        end_time: str = None,
        exit_reason: str = None,
        kyuubi_service_id: str = None,
        latest_sql_statement_status: str = None,
        mb_seconds: int = None,
        resource_queue_id: str = None,
        run_log: main_models.RunLog = None,
        start_time: str = None,
        state: str = None,
        tags: List[main_models.Tag] = None,
        vcore_seconds: int = None,
        web_ui: str = None,
    ):
        # The ID of the application that is submitted by using a Kyuubi gateway.
        self.application_id = application_id
        # The name of the Spark application that is submitted by using a Kyuubi gateway.
        self.application_name = application_name
        # The number of CUs consumed during a specified cycle of a task. The value is an estimated value. Refer to your Alibaba Cloud bill for the actual number of consumed CUs.
        self.cu_hours = cu_hours
        # The time when the task ended.
        self.end_time = end_time
        self.exit_reason = exit_reason
        self.kyuubi_service_id = kyuubi_service_id
        self.latest_sql_statement_status = latest_sql_statement_status
        # The total amount of memory allocated to the job multiplied by the running duration (seconds).
        self.mb_seconds = mb_seconds
        # The name of the resource queue on which the Spark jobs run.
        self.resource_queue_id = resource_queue_id
        self.run_log = run_log
        # The time when the task started.
        self.start_time = start_time
        # The status of the Spark application.
        # 
        # *   STARTING
        # *   RUNNING
        # *   TERMINATED
        self.state = state
        self.tags = tags
        # The total number of CPU cores allocated to the job multiplied by the running duration (seconds).
        self.vcore_seconds = vcore_seconds
        # The URL of the web UI for the Spark application.
        self.web_ui = web_ui

    def validate(self):
        if self.run_log:
            self.run_log.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['applicationId'] = self.application_id

        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.exit_reason is not None:
            result['exitReason'] = self.exit_reason

        if self.kyuubi_service_id is not None:
            result['kyuubiServiceId'] = self.kyuubi_service_id

        if self.latest_sql_statement_status is not None:
            result['latestSqlStatementStatus'] = self.latest_sql_statement_status

        if self.mb_seconds is not None:
            result['mbSeconds'] = self.mb_seconds

        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id

        if self.run_log is not None:
            result['runLog'] = self.run_log.to_map()

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.state is not None:
            result['state'] = self.state

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.vcore_seconds is not None:
            result['vcoreSeconds'] = self.vcore_seconds

        if self.web_ui is not None:
            result['webUI'] = self.web_ui

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')

        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('exitReason') is not None:
            self.exit_reason = m.get('exitReason')

        if m.get('kyuubiServiceId') is not None:
            self.kyuubi_service_id = m.get('kyuubiServiceId')

        if m.get('latestSqlStatementStatus') is not None:
            self.latest_sql_statement_status = m.get('latestSqlStatementStatus')

        if m.get('mbSeconds') is not None:
            self.mb_seconds = m.get('mbSeconds')

        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')

        if m.get('runLog') is not None:
            temp_model = main_models.RunLog()
            self.run_log = temp_model.from_map(m.get('runLog'))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('state') is not None:
            self.state = m.get('state')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('vcoreSeconds') is not None:
            self.vcore_seconds = m.get('vcoreSeconds')

        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')

        return self

