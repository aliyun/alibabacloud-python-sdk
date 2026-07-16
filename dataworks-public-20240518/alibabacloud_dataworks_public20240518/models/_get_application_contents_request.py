# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApplicationContentsRequest(DaraModel):
    def __init__(
        self,
        process_instance_id: str = None,
    ):
        # The approval process instance ID of the submitted application.
        # 
        # This parameter is required.
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        return self

