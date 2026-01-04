# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebAccessLogStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        sls_status: bool = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The Logstore of the instance.
        self.sls_logstore = sls_logstore
        # The Log Service project of the instance.
        self.sls_project = sls_project
        # Indicates whether the Log Analysis feature is enabled for the website. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.sls_status = sls_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore

        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project

        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')

        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')

        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')

        return self

