# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Event(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        event_id: str = None,
        event_name: str = None,
        job_id: str = None,
        message: str = None,
        namespace: str = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.event_id = event_id
        self.event_name = event_name
        self.job_id = job_id
        self.message = message
        self.namespace = namespace
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.event_id is not None:
            result['eventId'] = self.event_id

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.message is not None:
            result['message'] = self.message

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

