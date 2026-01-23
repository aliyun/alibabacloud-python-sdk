# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class CouponApprovalStatusListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.CouponApprovalStatusListResponseBodyData] = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

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

        if self.message is not None:
            result['Message'] = self.message

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.CouponApprovalStatusListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self



class CouponApprovalStatusListResponseBodyData(DaraModel):
    def __init__(
        self,
        issuer_account: str = None,
        issuer_uid: str = None,
        note: str = None,
        template_id: str = None,
        template_name: str = None,
        template_status: int = None,
        time_of_request: str = None,
    ):
        self.issuer_account = issuer_account
        self.issuer_uid = issuer_uid
        self.note = note
        self.template_id = template_id
        self.template_name = template_name
        self.template_status = template_status
        self.time_of_request = time_of_request

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issuer_account is not None:
            result['IssuerAccount'] = self.issuer_account

        if self.issuer_uid is not None:
            result['IssuerUid'] = self.issuer_uid

        if self.note is not None:
            result['Note'] = self.note

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.time_of_request is not None:
            result['TimeOfRequest'] = self.time_of_request

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IssuerAccount') is not None:
            self.issuer_account = m.get('IssuerAccount')

        if m.get('IssuerUid') is not None:
            self.issuer_uid = m.get('IssuerUid')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TimeOfRequest') is not None:
            self.time_of_request = m.get('TimeOfRequest')

        return self

