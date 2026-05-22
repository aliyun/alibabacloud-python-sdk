# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSiteDeliveryTaskStatusRequest(DaraModel):
    def __init__(
        self,
        method: str = None,
        site_id: int = None,
        task_name: str = None,
    ):
        # Specifies whether to enable the delivery task.
        # 
        # This parameter is required.
        self.method = method
        # The website ID.
        self.site_id = site_id
        # The name of the delivery task.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method is not None:
            result['Method'] = self.method

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

