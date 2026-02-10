# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarPlaybookTaskDetailRequest(DaraModel):
    def __init__(
        self,
        playbook_id: int = None,
        record_id: int = None,
        request_uuid: str = None,
    ):
        # Playbook ID.
        # > You can obtain this parameter by calling the [DescribePlaybooks](https://help.aliyun.com/document_detail/2627461.html) interface.
        # 
        # This parameter is required.
        self.playbook_id = playbook_id
        # The vulnerability ID passed when creating the policy task.
        # > You can obtain this parameter by calling the [DescribeVulList](~~DescribeVulList~~) interface.
        # 
        # This parameter is required.
        self.record_id = record_id
        # UUID of the playbook task execution.
        # > You can obtain this parameter by calling the [DescribeSoarRecords](https://help.aliyun.com/document_detail/2627455.html) interface.
        # 
        # This parameter is required.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.playbook_id is not None:
            result['PlaybookId'] = self.playbook_id

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlaybookId') is not None:
            self.playbook_id = m.get('PlaybookId')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        return self

