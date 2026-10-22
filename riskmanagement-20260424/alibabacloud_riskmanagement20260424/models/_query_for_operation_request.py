# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryForOperationRequest(DaraModel):
    def __init__(
        self,
        apply_time_end: int = None,
        apply_time_start: int = None,
        asset_type: str = None,
        audit_time_end: int = None,
        audit_time_start: int = None,
        current_page: int = None,
        customer_uid: str = None,
        ip: str = None,
        page_size: int = None,
        status: str = None,
    ):
        self.apply_time_end = apply_time_end
        self.apply_time_start = apply_time_start
        self.asset_type = asset_type
        self.audit_time_end = audit_time_end
        self.audit_time_start = audit_time_start
        self.current_page = current_page
        self.customer_uid = customer_uid
        self.ip = ip
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time_end is not None:
            result['ApplyTimeEnd'] = self.apply_time_end

        if self.apply_time_start is not None:
            result['ApplyTimeStart'] = self.apply_time_start

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.audit_time_end is not None:
            result['AuditTimeEnd'] = self.audit_time_end

        if self.audit_time_start is not None:
            result['AuditTimeStart'] = self.audit_time_start

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTimeEnd') is not None:
            self.apply_time_end = m.get('ApplyTimeEnd')

        if m.get('ApplyTimeStart') is not None:
            self.apply_time_start = m.get('ApplyTimeStart')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuditTimeEnd') is not None:
            self.audit_time_end = m.get('AuditTimeEnd')

        if m.get('AuditTimeStart') is not None:
            self.audit_time_start = m.get('AuditTimeStart')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

