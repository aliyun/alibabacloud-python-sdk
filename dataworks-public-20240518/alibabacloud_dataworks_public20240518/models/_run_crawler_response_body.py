# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunCrawlerResponseBody(DaraModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
        run_accepted: bool = None,
        run_status: str = None,
        success: bool = None,
        task_instance_id: int = None,
    ):
        # The ID of the metadata crawler.
        self.id = id
        # The request ID. Used for locating logs and troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the run request was accepted. A value of true indicates that the request was accepted, but does not indicate that the collection task is complete.
        self.run_accepted = run_accepted
        # The initial run status after submission. The value is WAITING when the run request is successfully accepted. To query the final status, call ListCrawlerRuns.
        self.run_status = run_status
        # Indicates whether the request was successful.
        self.success = success
        # The associated DataWorks task instance ID. This field may be empty. To query the final run record, call ListCrawlerRuns.
        self.task_instance_id = task_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.run_accepted is not None:
            result['RunAccepted'] = self.run_accepted

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        if self.success is not None:
            result['Success'] = self.success

        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunAccepted') is not None:
            self.run_accepted = m.get('RunAccepted')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')

        return self

