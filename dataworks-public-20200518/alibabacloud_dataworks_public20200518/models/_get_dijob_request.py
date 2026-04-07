# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDIJobRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        with_details: bool = None,
    ):
        # The ID of the synchronization task.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # Specifies whether to return detailed configuration information, including TransformationRules, TableMappings, and JobSettings. Valid values: true and false. Default value: true.
        self.with_details = with_details

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.with_details is not None:
            result['WithDetails'] = self.with_details

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('WithDetails') is not None:
            self.with_details = m.get('WithDetails')

        return self

