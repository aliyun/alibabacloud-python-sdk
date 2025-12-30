# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGtmAvailableAlertGroupResponseBody(DaraModel):
    def __init__(
        self,
        available_alert_group: str = None,
        request_id: str = None,
    ):
        # The available alert groups of the GTM instance.
        self.available_alert_group = available_alert_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_alert_group is not None:
            result['AvailableAlertGroup'] = self.available_alert_group

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAlertGroup') is not None:
            self.available_alert_group = m.get('AvailableAlertGroup')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

