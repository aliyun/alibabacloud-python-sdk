# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNotificationTypesResponseBody(DaraModel):
    def __init__(
        self,
        notification_types: List[str] = None,
        request_id: str = None,
    ):
        # The types of the notifications.
        # 
        # *   AUTOSCALING:SCALE_OUT_SUCCESS: The scale-out activity succeeds.
        # *   AUTOSCALING:SCALE_IN_SUCCESS: The scale-in activity succeeds.
        # *   AUTOSCALING:SCALE_OUT_ERROR: The scale-out activity fails.
        # *   AUTOSCALING:SCALE_IN_ERROR: The scale-in activity fails.
        # *   AUTOSCALING:SCALE_REJECT: The request for scaling activities is rejected.
        # *   AUTOSCALING:SCALE_OUT_START: The scale-out activity starts.
        # *   AUTOSCALING:SCALE_IN_START: The scale-in activity starts.
        # *   AUTOSCALING:SCHEDULE_TASK_EXPIRING: Auto Scaling sends a notification when a scheduled task is about to expire.
        self.notification_types = notification_types
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_types is not None:
            result['NotificationTypes'] = self.notification_types

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationTypes') is not None:
            self.notification_types = m.get('NotificationTypes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

