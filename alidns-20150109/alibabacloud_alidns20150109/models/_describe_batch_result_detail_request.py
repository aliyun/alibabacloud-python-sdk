# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBatchResultDetailRequest(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        task_id: int = None,
    ):
        # The type of the batch operation. Valid values:
        # 
        # *   **DOMAIN_ADD**: adds domain names in batches.
        # *   **DOMAIN_DEL**: deletes domain names in batches.
        # *   **RR_ADD**: adds Domain Name System (DNS) records in batches.
        # *   **RR_DEL**: deletes DNS records in batches.
        # 
        # >  Do not perform filtering when this field is empty.
        self.batch_type = batch_type
        # The language of the content within the request and response. Default: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The execution result. If you do not specify this parameter, all results are returned.
        self.status = status
        # The task ID.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

