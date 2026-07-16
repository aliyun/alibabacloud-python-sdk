# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class SetWorkspaceQuotaResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.SetWorkspaceQuotaResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # A human-readable message about the request\\"s outcome.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.SetWorkspaceQuotaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SetWorkspaceQuotaResponseBodyData(DaraModel):
    def __init__(
        self,
        cu_quota: int = None,
        cu_quota_usage: int = None,
        instance_id: str = None,
        order_id: str = None,
        state: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The compute unit (CU) quota.
        self.cu_quota = cu_quota
        # The amount of compute unit (CU) quota used.
        self.cu_quota_usage = cu_quota_usage
        # The ID of the billing instance.
        self.instance_id = instance_id
        # The order ID.
        self.order_id = order_id
        # The status of the order.
        self.state = state
        # The status of the instance.
        self.status = status
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu_quota is not None:
            result['CuQuota'] = self.cu_quota

        if self.cu_quota_usage is not None:
            result['CuQuotaUsage'] = self.cu_quota_usage

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CuQuota') is not None:
            self.cu_quota = m.get('CuQuota')

        if m.get('CuQuotaUsage') is not None:
            self.cu_quota_usage = m.get('CuQuotaUsage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

