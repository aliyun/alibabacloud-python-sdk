# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        task_no: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.task_no = task_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        return self

