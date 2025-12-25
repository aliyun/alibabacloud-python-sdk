# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListUserTenantsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant_list: List[main_models.ListUserTenantsResponseBodyTenantList] = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success
        # The details of the tenants that were returned.
        self.tenant_list = tenant_list

    def validate(self):
        if self.tenant_list:
            for v1 in self.tenant_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TenantList'] = []
        if self.tenant_list is not None:
            for k1 in self.tenant_list:
                result['TenantList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tenant_list = []
        if m.get('TenantList') is not None:
            for k1 in m.get('TenantList'):
                temp_model = main_models.ListUserTenantsResponseBodyTenantList()
                self.tenant_list.append(temp_model.from_map(k1))

        return self

class ListUserTenantsResponseBodyTenantList(DaraModel):
    def __init__(
        self,
        status: str = None,
        tenant_name: str = None,
        tid: int = None,
    ):
        # The status of the tenant. Valid values:
        # 
        # *   **ACTIVE**: The tenant is used to access DMS.
        # *   **IN_ACTIVE**: The tenant is not used.
        self.status = status
        # The name of the tenant.
        self.tenant_name = tenant_name
        # The ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

