# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescTemplateResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        remark: str = None,
        request_id: str = None,
        sms_content: str = None,
        sms_type: str = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_status: str = None,
        template_subject: str = None,
        template_text: str = None,
        template_type: str = None,
    ):
        self.create_time = create_time
        self.remark = remark
        self.request_id = request_id
        self.sms_content = sms_content
        self.sms_type = sms_type
        self.template_name = template_name
        self.template_nick_name = template_nick_name
        self.template_status = template_status
        self.template_subject = template_subject
        self.template_text = template_text
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content

        if self.sms_type is not None:
            result['SmsType'] = self.sms_type

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject

        if self.template_text is not None:
            result['TemplateText'] = self.template_text

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')

        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')

        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

