# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetPodLogsResponseBody(DaraModel):
    def __init__(
        self,
        container_info: main_models.ContainerInfo = None,
        containers: str = None,
        job_id: str = None,
        logs: List[str] = None,
        pod_id: str = None,
        pod_uid: str = None,
        request_id: str = None,
    ):
        # The container information that may be associated with the node.
        self.container_info = container_info
        # The containers used to filter logs. Separate multiple container names with commas (,).
        self.containers = containers
        # The job ID.
        self.job_id = job_id
        # The log list.
        self.logs = logs
        # The node ID.
        self.pod_id = pod_id
        # The instance UID.
        self.pod_uid = pod_uid
        # The request ID for this call, used for diagnostics and troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.container_info:
            self.container_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_info is not None:
            result['ContainerInfo'] = self.container_info.to_map()

        if self.containers is not None:
            result['Containers'] = self.containers

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.logs is not None:
            result['Logs'] = self.logs

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        if self.pod_uid is not None:
            result['PodUid'] = self.pod_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerInfo') is not None:
            temp_model = main_models.ContainerInfo()
            self.container_info = temp_model.from_map(m.get('ContainerInfo'))

        if m.get('Containers') is not None:
            self.containers = m.get('Containers')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Logs') is not None:
            self.logs = m.get('Logs')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        if m.get('PodUid') is not None:
            self.pod_uid = m.get('PodUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

