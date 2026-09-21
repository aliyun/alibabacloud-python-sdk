# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBrowserInstanceGroupRequest(DaraModel):
    def __init__(
        self,
        browser_instance_group_id: str = None,
    ):
        # The cloud browser group ID. This parameter is required. Specify the ID of a browser group that is created under the current account.
        self.browser_instance_group_id = browser_instance_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        return self

