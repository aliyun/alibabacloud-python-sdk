# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOperationAuditInfoDetailResponseBody(DaraModel):
    def __init__(
        self,
        audit_info: str = None,
        audit_status: int = None,
        audit_type: int = None,
        business_name: str = None,
        create_time: int = None,
        domain_name: str = None,
        id: str = None,
        remark: str = None,
        request_id: str = None,
        update_time: int = None,
    ):
        self.audit_info = audit_info
        self.audit_status = audit_status
        self.audit_type = audit_type
        self.business_name = business_name
        self.create_time = create_time
        self.domain_name = domain_name
        self.id = id
        self.remark = remark
        self.request_id = request_id
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditInfo') is not None:
            self.audit_info = m.get('AuditInfo')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

