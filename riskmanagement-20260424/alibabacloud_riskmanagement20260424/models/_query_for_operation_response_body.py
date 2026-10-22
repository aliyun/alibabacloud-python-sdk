# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QueryForOperationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryForOperationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryForOperationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryForOperationResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryForOperationResponseBodyDataList] = None,
        page_info: main_models.QueryForOperationResponseBodyDataPageInfo = None,
    ):
        self.list = list
        self.page_info = page_info

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryForOperationResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.QueryForOperationResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class QueryForOperationResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryForOperationResponseBodyDataList(DaraModel):
    def __init__(
        self,
        apply_time: int = None,
        asset_type: str = None,
        audit_memo: str = None,
        audit_time: int = None,
        auditor: str = None,
        customer_uid: str = None,
        email_type: str = None,
        has_unsubscribe: bool = None,
        id: int = None,
        ip: str = None,
        send_count: str = None,
        status: str = None,
        use_desc: str = None,
    ):
        self.apply_time = apply_time
        self.asset_type = asset_type
        self.audit_memo = audit_memo
        self.audit_time = audit_time
        self.auditor = auditor
        self.customer_uid = customer_uid
        self.email_type = email_type
        self.has_unsubscribe = has_unsubscribe
        self.id = id
        self.ip = ip
        self.send_count = send_count
        self.status = status
        self.use_desc = use_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.audit_memo is not None:
            result['AuditMemo'] = self.audit_memo

        if self.audit_time is not None:
            result['AuditTime'] = self.audit_time

        if self.auditor is not None:
            result['Auditor'] = self.auditor

        if self.customer_uid is not None:
            result['CustomerUid'] = self.customer_uid

        if self.email_type is not None:
            result['EmailType'] = self.email_type

        if self.has_unsubscribe is not None:
            result['HasUnsubscribe'] = self.has_unsubscribe

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.send_count is not None:
            result['SendCount'] = self.send_count

        if self.status is not None:
            result['Status'] = self.status

        if self.use_desc is not None:
            result['UseDesc'] = self.use_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AuditMemo') is not None:
            self.audit_memo = m.get('AuditMemo')

        if m.get('AuditTime') is not None:
            self.audit_time = m.get('AuditTime')

        if m.get('Auditor') is not None:
            self.auditor = m.get('Auditor')

        if m.get('CustomerUid') is not None:
            self.customer_uid = m.get('CustomerUid')

        if m.get('EmailType') is not None:
            self.email_type = m.get('EmailType')

        if m.get('HasUnsubscribe') is not None:
            self.has_unsubscribe = m.get('HasUnsubscribe')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('SendCount') is not None:
            self.send_count = m.get('SendCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UseDesc') is not None:
            self.use_desc = m.get('UseDesc')

        return self

