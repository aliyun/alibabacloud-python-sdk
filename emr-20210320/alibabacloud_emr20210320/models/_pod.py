# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Pod(DaraModel):
    def __init__(
        self,
        message: str = None,
        pod_name: str = None,
        pod_status: str = None,
        reason: str = None,
    ):
        self.message = message
        self.pod_name = pod_name
        self.pod_status = pod_status
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('PodStatus') is not None:
            self.pod_status = m.get('PodStatus')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

