# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobInstancesRequest(DaraModel):
    def __init__(
        self,
        caller_owner: str = None,
        end: int = None,
        offset: int = None,
        size: int = None,
        start: int = None,
        state: str = None,
    ):
        # The owner of the job.
        self.caller_owner = caller_owner
        # The end time.
        self.end = end
        # The start row of the query.
        self.offset = offset
        # The number of rows per page for a paged query.
        self.size = size
        # The start time.
        self.start = start
        # The current execution status.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_owner is not None:
            result['callerOwner'] = self.caller_owner

        if self.end is not None:
            result['end'] = self.end

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        if self.start is not None:
            result['start'] = self.start

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callerOwner') is not None:
            self.caller_owner = m.get('callerOwner')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

