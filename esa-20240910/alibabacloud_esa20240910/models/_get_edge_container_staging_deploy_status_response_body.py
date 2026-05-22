# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetEdgeContainerStagingDeployStatusResponseBody(DaraModel):
    def __init__(
        self,
        containers_ready: str = None,
        creation_timestamp: str = None,
        initialized: str = None,
        phase: str = None,
        pod_restart_state: main_models.GetEdgeContainerStagingDeployStatusResponseBodyPodRestartState = None,
        ready: str = None,
        request_id: str = None,
        scheduled: str = None,
        vips: List[str] = None,
    ):
        # Indicates whether the container is ready.
        # 
        # *   ok
        # *   unready
        self.containers_ready = containers_ready
        # The time when the container was created. The value is a timestamp.
        self.creation_timestamp = creation_timestamp
        # The initialization status of the container.
        # 
        # *   ok
        # *   unready
        self.initialized = initialized
        # The status of the container in the staging environment.
        # 
        # *   NoContainer: created.
        # *   Running: running.
        # *   Failed: abnormal.
        self.phase = phase
        # The details of container restart.
        self.pod_restart_state = pod_restart_state
        # Indicates whether domain names are associated with the container.
        # 
        # *   ok
        # *   unready
        self.ready = ready
        # The request ID.
        self.request_id = request_id
        # The scheduling status of the container.
        # 
        # *   ok
        # *   unready
        self.scheduled = scheduled
        # The virtual IP addresses.
        self.vips = vips

    def validate(self):
        if self.pod_restart_state:
            self.pod_restart_state.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.containers_ready is not None:
            result['ContainersReady'] = self.containers_ready

        if self.creation_timestamp is not None:
            result['CreationTimestamp'] = self.creation_timestamp

        if self.initialized is not None:
            result['Initialized'] = self.initialized

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.pod_restart_state is not None:
            result['PodRestartState'] = self.pod_restart_state.to_map()

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scheduled is not None:
            result['Scheduled'] = self.scheduled

        if self.vips is not None:
            result['VIPs'] = self.vips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainersReady') is not None:
            self.containers_ready = m.get('ContainersReady')

        if m.get('CreationTimestamp') is not None:
            self.creation_timestamp = m.get('CreationTimestamp')

        if m.get('Initialized') is not None:
            self.initialized = m.get('Initialized')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('PodRestartState') is not None:
            temp_model = main_models.GetEdgeContainerStagingDeployStatusResponseBodyPodRestartState()
            self.pod_restart_state = temp_model.from_map(m.get('PodRestartState'))

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduled') is not None:
            self.scheduled = m.get('Scheduled')

        if m.get('VIPs') is not None:
            self.vips = m.get('VIPs')

        return self

class GetEdgeContainerStagingDeployStatusResponseBodyPodRestartState(DaraModel):
    def __init__(
        self,
        last_terminated_reason: str = None,
        restart_count: int = None,
    ):
        # The reason for the last restart.
        self.last_terminated_reason = last_terminated_reason
        # The number of times that the container restarted.
        self.restart_count = restart_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_terminated_reason is not None:
            result['LastTerminatedReason'] = self.last_terminated_reason

        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTerminatedReason') is not None:
            self.last_terminated_reason = m.get('LastTerminatedReason')

        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')

        return self

