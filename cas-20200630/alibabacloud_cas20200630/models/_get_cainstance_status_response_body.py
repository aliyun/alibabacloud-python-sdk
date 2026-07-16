# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class GetCAInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_status_list: List[main_models.GetCAInstanceStatusResponseBodyInstanceStatusList] = None,
        request_id: str = None,
    ):
        # The status details of the private CA instance.
        self.instance_status_list = instance_status_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_status_list:
            for v1 in self.instance_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k1 in self.instance_status_list:
                result['InstanceStatusList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k1 in m.get('InstanceStatusList'):
                temp_model = main_models.GetCAInstanceStatusResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCAInstanceStatusResponseBodyInstanceStatusList(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        before_time: int = None,
        cert_issued_count: int = None,
        cert_total_count: int = None,
        identifier: str = None,
        instance_id: str = None,
        status: str = None,
        type: str = None,
        use_expire_time: int = None,
    ):
        # The expiration date of the private CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > This parameter is returned only if **Status** is **USED** (the private CA instance is enabled) or **REVOKE** (the private CA instance is revoked).
        self.after_time = after_time
        # The issuance date of the private CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > This parameter is returned only if **Status** is **USED** (the private CA instance is enabled) or **REVOKE** (the private CA instance is revoked).
        self.before_time = before_time
        # The number of certificates that the private CA instance has issued.
        self.cert_issued_count = cert_issued_count
        # The number of certificates that the private CA instance can issue.
        # 
        # If the private CA is a root CA (**Type** is **ROOT**), this parameter indicates the number of intermediate CA certificates that can be issued. If the private CA is an intermediate CA (**Type** is **SUB_ROOT**), this parameter indicates the total number of client certificates and server-side certificates that can be issued.
        self.cert_total_count = cert_total_count
        # The unique identifier of the private CA certificate.
        # 
        # > This parameter is returned only if **Status** is **USED** (the private CA instance is enabled) or **REVOKE** (the private CA instance is revoked).
        self.identifier = identifier
        # The ID of the private CA instance.
        self.instance_id = instance_id
        # The status of the private CA instance. Valid values:
        # 
        # - **BUY**: The instance is purchased but not enabled.
        # 
        # - **USED**: The instance is enabled.
        # 
        # - **REFUND**: A refund has been issued for the instance.
        # 
        # - **REVOKE**: The instance is revoked.
        self.status = status
        # The type of the private CA instance. Valid values:
        # 
        # - **ROOT**: Root CA instance.
        # 
        # - **SUB_ROOT**: Intermediate CA instance.
        self.type = type
        # The expiration date of the private CA instance. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # > This parameter corresponds to the subscription duration that you selected for the Private Certificate Authority (PCA) service when you purchased the instance.
        self.use_expire_time = use_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_time is not None:
            result['AfterTime'] = self.after_time

        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.cert_issued_count is not None:
            result['CertIssuedCount'] = self.cert_issued_count

        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.use_expire_time is not None:
            result['UseExpireTime'] = self.use_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')

        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('CertIssuedCount') is not None:
            self.cert_issued_count = m.get('CertIssuedCount')

        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UseExpireTime') is not None:
            self.use_expire_time = m.get('UseExpireTime')

        return self

