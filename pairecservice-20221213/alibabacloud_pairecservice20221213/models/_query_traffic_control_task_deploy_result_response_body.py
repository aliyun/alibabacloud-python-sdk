# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTrafficControlTaskDeployResultResponseBody(DaraModel):
    def __init__(
        self,
        deploy_message: str = None,
        deploy_status: str = None,
        draft_message: str = None,
        draft_status: str = None,
        prepare_message: str = None,
        prepare_status: str = None,
        request_id: str = None,
        start_message: str = None,
        start_status: str = None,
        stop_message: str = None,
        stop_status: str = None,
        traffic_control_task_id: str = None,
    ):
        # The message returned for the Flink platform deployment operation.
        self.deploy_message = deploy_message
        # The status of deploying the draft. Valid values:
        # - Failed: failed.
        # - Running: running.
        # - Success: succeeded.
        self.deploy_status = deploy_status
        # The message returned for pushing the draft to Flink.
        self.draft_message = draft_message
        # The status of pushing the draft to Flink. Valid values:
        # - Failed: failed.
        # - Running: running.
        # - Success: succeeded.
        self.draft_status = draft_status
        # The message returned for the preparation phase.
        self.prepare_message = prepare_message
        # The status of the preparation phase. Valid values:
        # - Failed: failed.
        # - Running: running.
        # - Success: succeeded.
        self.prepare_status = prepare_status
        # The request ID.
        self.request_id = request_id
        # The message returned for starting the Flink task.
        self.start_message = start_message
        # The status of starting the Flink task. Valid values:
        # - Failed: failed.
        # - Running: running.
        # - Success: succeeded.
        self.start_status = start_status
        # The stop details.
        self.stop_message = stop_message
        # The stop status.
        self.stop_status = stop_status
        # The traffic control task ID.
        self.traffic_control_task_id = traffic_control_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deploy_message is not None:
            result['DeployMessage'] = self.deploy_message

        if self.deploy_status is not None:
            result['DeployStatus'] = self.deploy_status

        if self.draft_message is not None:
            result['DraftMessage'] = self.draft_message

        if self.draft_status is not None:
            result['DraftStatus'] = self.draft_status

        if self.prepare_message is not None:
            result['PrepareMessage'] = self.prepare_message

        if self.prepare_status is not None:
            result['PrepareStatus'] = self.prepare_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_message is not None:
            result['StartMessage'] = self.start_message

        if self.start_status is not None:
            result['StartStatus'] = self.start_status

        if self.stop_message is not None:
            result['StopMessage'] = self.stop_message

        if self.stop_status is not None:
            result['StopStatus'] = self.stop_status

        if self.traffic_control_task_id is not None:
            result['TrafficControlTaskId'] = self.traffic_control_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployMessage') is not None:
            self.deploy_message = m.get('DeployMessage')

        if m.get('DeployStatus') is not None:
            self.deploy_status = m.get('DeployStatus')

        if m.get('DraftMessage') is not None:
            self.draft_message = m.get('DraftMessage')

        if m.get('DraftStatus') is not None:
            self.draft_status = m.get('DraftStatus')

        if m.get('PrepareMessage') is not None:
            self.prepare_message = m.get('PrepareMessage')

        if m.get('PrepareStatus') is not None:
            self.prepare_status = m.get('PrepareStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartMessage') is not None:
            self.start_message = m.get('StartMessage')

        if m.get('StartStatus') is not None:
            self.start_status = m.get('StartStatus')

        if m.get('StopMessage') is not None:
            self.stop_message = m.get('StopMessage')

        if m.get('StopStatus') is not None:
            self.stop_status = m.get('StopStatus')

        if m.get('TrafficControlTaskId') is not None:
            self.traffic_control_task_id = m.get('TrafficControlTaskId')

        return self

