# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTreeDataResponseBody(DaraModel):
    def __init__(
        self,
        playbooks: str = None,
        request_id: str = None,
    ):
        # A list of playbooks in JSON string format. The string contains the following fields:
        # 
        # - **active**: Indicates whether the playbook is active. A value of **true** means the playbook is active. A value of **false** means the playbook is inactive.
        # 
        # - **displayName**: The name of the playbook.
        # 
        # - **playbookUuid**: The UUID of the playbook.
        self.playbooks = playbooks
        # The ID of the request. Alibaba Cloud generates this unique ID for each request. Use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbooks is not None:
            result['Playbooks'] = self.playbooks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Playbooks') is not None:
            self.playbooks = m.get('Playbooks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

