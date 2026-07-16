# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class ListEnterpriseInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListEnterpriseInfoResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEnterpriseInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEnterpriseInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_desc: str = None,
        enterprise_id: int = None,
        enterprise_name: str = None,
        manager_contact_number: str = None,
        manager_name: str = None,
        organization_code: str = None,
        status: int = None,
    ):
        self.audit_desc = audit_desc
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        self.manager_contact_number = manager_contact_number
        self.manager_name = manager_name
        self.organization_code = organization_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_desc is not None:
            result['AuditDesc'] = self.audit_desc

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name

        if self.manager_contact_number is not None:
            result['ManagerContactNumber'] = self.manager_contact_number

        if self.manager_name is not None:
            result['ManagerName'] = self.manager_name

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDesc') is not None:
            self.audit_desc = m.get('AuditDesc')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')

        if m.get('ManagerContactNumber') is not None:
            self.manager_contact_number = m.get('ManagerContactNumber')

        if m.get('ManagerName') is not None:
            self.manager_name = m.get('ManagerName')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

