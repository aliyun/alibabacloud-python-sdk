# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTaskFlowNotificationResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        notification: main_models.GetTaskFlowNotificationResponseBodyNotification = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The notification settings specified by the user.
        self.notification = notification
        # The ID of the request. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.notification:
            self.notification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Notification') is not None:
            temp_model = main_models.GetTaskFlowNotificationResponseBodyNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTaskFlowNotificationResponseBodyNotification(DaraModel):
    def __init__(
        self,
        dag_notification_fail: bool = None,
        dag_notification_sla: bool = None,
        dag_notification_success: bool = None,
    ):
        # Indicates whether notifications for failed task flows are enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.dag_notification_fail = dag_notification_fail
        # Indicates whether service level agreement (SLA) global notifications for task flows are enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.dag_notification_sla = dag_notification_sla
        # Indicates whether notifications for successful task flows are enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.dag_notification_success = dag_notification_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_notification_fail is not None:
            result['DagNotificationFail'] = self.dag_notification_fail

        if self.dag_notification_sla is not None:
            result['DagNotificationSla'] = self.dag_notification_sla

        if self.dag_notification_success is not None:
            result['DagNotificationSuccess'] = self.dag_notification_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagNotificationFail') is not None:
            self.dag_notification_fail = m.get('DagNotificationFail')

        if m.get('DagNotificationSla') is not None:
            self.dag_notification_sla = m.get('DagNotificationSla')

        if m.get('DagNotificationSuccess') is not None:
            self.dag_notification_success = m.get('DagNotificationSuccess')

        return self

