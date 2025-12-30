# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCommonLogDetailRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        hidden_process: bool = None,
        log_request_id: str = None,
        to: int = None,
    ):
        # The start time of the time range within which the logs that you want to query were generated. The time is a timestamp. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to hide the process of each step. Valid values:
        # 
        # *   true: hides the process and returns only the result log of each step.
        # *   false: does not hide the process and displays the start and result logs of each step.
        # 
        # Default value: true.
        self.hidden_process = hidden_process
        # The request ID.
        # 
        # This parameter is required.
        self.log_request_id = log_request_id
        # The end time of the time range within which the logs that you want to query were generated. The time is a timestamp. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.hidden_process is not None:
            result['HiddenProcess'] = self.hidden_process

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('HiddenProcess') is not None:
            self.hidden_process = m.get('HiddenProcess')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

