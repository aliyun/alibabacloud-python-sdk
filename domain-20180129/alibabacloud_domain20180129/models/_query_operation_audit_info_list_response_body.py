# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryOperationAuditInfoListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryOperationAuditInfoListResponseBodyData] = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

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
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryOperationAuditInfoListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryOperationAuditInfoListResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_info: str = None,
        audit_status: int = None,
        audit_type: int = None,
        business_name: str = None,
        create_time: int = None,
        domain_name: str = None,
        id: int = None,
        remark: str = None,
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

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

