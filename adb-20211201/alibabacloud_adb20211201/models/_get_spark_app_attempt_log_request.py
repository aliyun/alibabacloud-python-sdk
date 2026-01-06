# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSparkAppAttemptLogRequest(DaraModel):
    def __init__(
        self,
        attempt_id: str = None,
        log_length: int = None,
        page_number: int = None,
        page_size: str = None,
    ):
        # The ID of the log.
        # 
        # > You can call the [ListSparkAppAttempts](https://help.aliyun.com/document_detail/455887.html) operation to query the information about the retry attempts of a Spark application, including the retry log IDs.
        # 
        # This parameter is required.
        self.attempt_id = attempt_id
        # The number of log entries to return. Valid values: 1 to 500. Default value: 300.
        self.log_length = log_length
        # The log offset.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id

        if self.log_length is not None:
            result['LogLength'] = self.log_length

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')

        if m.get('LogLength') is not None:
            self.log_length = m.get('LogLength')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

