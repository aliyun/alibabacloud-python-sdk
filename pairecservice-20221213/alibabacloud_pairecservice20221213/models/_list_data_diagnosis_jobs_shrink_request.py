# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataDiagnosisJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        status: str = None,
        types_shrink: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The task status. Valid values:
        # 
        # - Initializing: The job is being initialized.
        # 
        # - Running: The job is in progress.
        # 
        # - Success: The job succeeded.
        # 
        # - Failure: The job failed to complete.
        self.status = status
        # A list of data diagnosis types.
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.types_shrink is not None:
            result['Types'] = self.types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')

        return self

