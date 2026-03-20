# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateServiceInstanceTokenResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        streamlog_url: str = None,
        token: str = None,
        url: str = None,
        workbench_url: str = None,
    ):
        self.request_id = request_id
        self.streamlog_url = streamlog_url
        self.token = token
        self.url = url
        self.workbench_url = workbench_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.streamlog_url is not None:
            result['StreamlogUrl'] = self.streamlog_url

        if self.token is not None:
            result['Token'] = self.token

        if self.url is not None:
            result['Url'] = self.url

        if self.workbench_url is not None:
            result['WorkbenchUrl'] = self.workbench_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamlogUrl') is not None:
            self.streamlog_url = m.get('StreamlogUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('WorkbenchUrl') is not None:
            self.workbench_url = m.get('WorkbenchUrl')

        return self

