# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetMaintainWindowResponseBody(DaraModel):
    def __init__(
        self,
        maintain_window: main_models.MaintainWindowForView = None,
        request_id: str = None,
    ):
        # The details of the silence policy, including the policy ID, name, description, enabled status, filterSetting, effective period configuration, creation time, and update time. workspaceFilterSetting is not returned.
        self.maintain_window = maintain_window
        # The unique ID of the request. You can use this ID for troubleshooting and ticket submission.
        self.request_id = request_id

    def validate(self):
        if self.maintain_window:
            self.maintain_window.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maintain_window is not None:
            result['maintainWindow'] = self.maintain_window.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintainWindow') is not None:
            temp_model = main_models.MaintainWindowForView()
            self.maintain_window = temp_model.from_map(m.get('maintainWindow'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

