# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSignalResponseBody(DaraModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        job_id: str = None,
        message: str = None,
        pod_names: List[str] = None,
        reason: str = None,
        request_id: str = None,
        roles: List[str] = None,
        scope: str = None,
        signal: str = None,
        signal_id: str = None,
        status: str = None,
    ):
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The job ID.
        self.job_id = job_id
        # The status description, which contains a summary for each pod (number of successful deliveries, names of failed or pending pods, etc.).
        self.message = message
        # The list of pod names.
        self.pod_names = pod_names
        # The status reason code, such as `Completed`, `SignalFailed`, or `StoppedByJobEnded`.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The list of role objects.
        self.roles = roles
        # The delivery scope.
        self.scope = scope
        # The signal.
        self.signal = signal
        # The signal ID.
        self.signal_id = signal_id
        # The signal status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.pod_names is not None:
            result['PodNames'] = self.pod_names

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.roles is not None:
            result['Roles'] = self.roles

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.signal is not None:
            result['Signal'] = self.signal

        if self.signal_id is not None:
            result['SignalId'] = self.signal_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PodNames') is not None:
            self.pod_names = m.get('PodNames')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Roles') is not None:
            self.roles = m.get('Roles')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Signal') is not None:
            self.signal = m.get('Signal')

        if m.get('SignalId') is not None:
            self.signal_id = m.get('SignalId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

