# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccountResponseBody(DaraModel):
    def __init__(
        self,
        deletion_type: str = None,
        request_id: str = None,
    ):
        # The deletion type. Valid values:
        # 
        # - 0: Direct deletion. If the member has no pay-as-you-go resources in the last 30 days, the system directly deletes the member.
        # - 1: Cool-down period deletion. If the member has pay-as-you-go resources in the last 30 days, the member enters a cool-down period. The system starts to delete the member after the cool-down period ends. For more information about the cool-down period, see [What is the cool-down period for member deletion](https://help.aliyun.com/document_detail/446079.html).
        self.deletion_type = deletion_type
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_type is not None:
            result['DeletionType'] = self.deletion_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionType') is not None:
            self.deletion_type = m.get('DeletionType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

