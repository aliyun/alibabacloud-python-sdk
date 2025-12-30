# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBatchResultCountRequest(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        lang: str = None,
        task_id: int = None,
    ):
        # The type of the batch operation. Valid values:
        # 
        # *   **DOMAIN_ADD**: adds domain names in batches.
        # *   **DOMAIN_DEL**: deletes domain names in batches.
        # *   **RR_ADD**: adds Domain Name System (DNS) records in batches.
        # *   **RR_DEL**: deletes DNS records in batches.
        # 
        # >  If you do not specify this parameter, filtering is not required.
        self.batch_type = batch_type
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The task ID.
        # 
        # >  If you specify TaskId, the execution result of the specified task is returned. If you do not specify TaskId, the execution result of the last task is returned.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

