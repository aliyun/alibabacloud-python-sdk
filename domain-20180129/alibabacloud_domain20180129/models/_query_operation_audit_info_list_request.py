# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOperationAuditInfoListRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        audit_type: int = None,
        domain_name: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # Review status. Valid values:
        # 
        # - **0**: Information pending completion.
        # - **1**, **2**, **3**, **4**: Under review.
        # - **5**: Review failed.
        # - **6**: Review succeeded.
        # - **7**: Review canceled.
        self.audit_status = audit_status
        # Review type. Valid value:
        # 
        # **1**: Offline domain name transfer.
        self.audit_type = audit_type
        # Domain name to query.
        self.domain_name = domain_name
        # Language of error messages returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # Page number.
        self.page_num = page_num
        # Number of records per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

