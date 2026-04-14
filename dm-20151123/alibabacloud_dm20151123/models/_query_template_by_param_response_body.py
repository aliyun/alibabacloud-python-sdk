# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class QueryTemplateByParamResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        data: main_models.QueryTemplateByParamResponseBodyData = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('data') is not None:
            temp_model = main_models.QueryTemplateByParamResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class QueryTemplateByParamResponseBodyData(DaraModel):
    def __init__(
        self,
        template: List[main_models.QueryTemplateByParamResponseBodyDataTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('template') is not None:
            for k1 in m.get('template'):
                temp_model = main_models.QueryTemplateByParamResponseBodyDataTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class QueryTemplateByParamResponseBodyDataTemplate(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        sms_status: int = None,
        sms_template_code: int = None,
        smsrejectinfo: int = None,
        template_comment: str = None,
        template_id: str = None,
        template_name: str = None,
        template_status: str = None,
        template_type: int = None,
        utc_createtime: int = None,
    ):
        self.create_time = create_time
        self.sms_status = sms_status
        self.sms_template_code = sms_template_code
        self.smsrejectinfo = smsrejectinfo
        self.template_comment = template_comment
        self.template_id = template_id
        self.template_name = template_name
        self.template_status = template_status
        self.template_type = template_type
        self.utc_createtime = utc_createtime

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status

        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code

        if self.smsrejectinfo is not None:
            result['Smsrejectinfo'] = self.smsrejectinfo

        if self.template_comment is not None:
            result['TemplateComment'] = self.template_comment

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.utc_createtime is not None:
            result['UtcCreatetime'] = self.utc_createtime

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')

        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')

        if m.get('Smsrejectinfo') is not None:
            self.smsrejectinfo = m.get('Smsrejectinfo')

        if m.get('TemplateComment') is not None:
            self.template_comment = m.get('TemplateComment')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('UtcCreatetime') is not None:
            self.utc_createtime = m.get('UtcCreatetime')

        return self

