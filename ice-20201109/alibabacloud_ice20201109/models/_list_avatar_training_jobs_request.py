# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAvatarTrainingJobsRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        status: str = None,
    ):
        # *   The page number.
        # *   Default value: 1.
        self.page_no = page_no
        # *   The number of entries per page.
        # *   Default value: 10.
        # *   Valid values: 1 to 100.
        self.page_size = page_size
        # *   The job state.
        # *   Valid values: Init, Queuing, Training, Success, and Fail.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

