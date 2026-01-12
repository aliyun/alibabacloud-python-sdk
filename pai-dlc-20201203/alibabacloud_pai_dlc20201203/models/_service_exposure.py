# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ServiceExposure(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        job_id: str = None,
        message: str = None,
        pod_id: str = None,
        port: int = None,
        service_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.display_name = display_name
        self.job_id = job_id
        self.message = message
        self.pod_id = pod_id
        self.port = port
        self.service_id = service_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.pod_id is not None:
            result['PodId'] = self.pod_id

        if self.port is not None:
            result['Port'] = self.port

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PodId') is not None:
            self.pod_id = m.get('PodId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

