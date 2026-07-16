# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class ListSmsTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSmsTemplateResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSmsTemplateResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSmsTemplateResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_result: str = None,
        biz_url: str = None,
        business_type: int = None,
        create_date: int = None,
        default_flag: bool = None,
        remark: str = None,
        sms_template_code: str = None,
        sms_template_content: str = None,
        sms_template_name: str = None,
        status: str = None,
    ):
        self.audit_result = audit_result
        self.biz_url = biz_url
        self.business_type = business_type
        self.create_date = create_date
        self.default_flag = default_flag
        self.remark = remark
        self.sms_template_code = sms_template_code
        self.sms_template_content = sms_template_content
        self.sms_template_name = sms_template_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result

        if self.biz_url is not None:
            result['BizUrl'] = self.biz_url

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.default_flag is not None:
            result['DefaultFlag'] = self.default_flag

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code

        if self.sms_template_content is not None:
            result['SmsTemplateContent'] = self.sms_template_content

        if self.sms_template_name is not None:
            result['SmsTemplateName'] = self.sms_template_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')

        if m.get('BizUrl') is not None:
            self.biz_url = m.get('BizUrl')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DefaultFlag') is not None:
            self.default_flag = m.get('DefaultFlag')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')

        if m.get('SmsTemplateContent') is not None:
            self.sms_template_content = m.get('SmsTemplateContent')

        if m.get('SmsTemplateName') is not None:
            self.sms_template_name = m.get('SmsTemplateName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

