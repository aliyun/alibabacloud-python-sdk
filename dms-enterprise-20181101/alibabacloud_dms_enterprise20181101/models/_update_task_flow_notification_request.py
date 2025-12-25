# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowNotificationRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        dag_notification_fail: bool = None,
        dag_notification_sla: bool = None,
        dag_notification_success: bool = None,
        tid: int = None,
    ):
        # The unique ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # Specifies whether to enable notifications for failed task flows. Notifications are disabled by default. You can enable notifications based on your business requirements.
        # 
        # This parameter is required.
        self.dag_notification_fail = dag_notification_fail
        # Specifies whether to enable SLA global notifications for task flows. Notifications are disabled by default. You can enable notifications based on your business requirements.
        # 
        # This parameter is required.
        self.dag_notification_sla = dag_notification_sla
        # Specifies whether to enable notifications for successful task flows. Notifications are disabled by default. You can enable notifications based on your business requirements.
        # 
        # This parameter is required.
        self.dag_notification_success = dag_notification_success
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.dag_notification_fail is not None:
            result['DagNotificationFail'] = self.dag_notification_fail

        if self.dag_notification_sla is not None:
            result['DagNotificationSla'] = self.dag_notification_sla

        if self.dag_notification_success is not None:
            result['DagNotificationSuccess'] = self.dag_notification_success

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('DagNotificationFail') is not None:
            self.dag_notification_fail = m.get('DagNotificationFail')

        if m.get('DagNotificationSla') is not None:
            self.dag_notification_sla = m.get('DagNotificationSla')

        if m.get('DagNotificationSuccess') is not None:
            self.dag_notification_success = m.get('DagNotificationSuccess')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

