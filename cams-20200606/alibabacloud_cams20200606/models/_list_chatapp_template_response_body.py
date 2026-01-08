# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ListChatappTemplateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        list_template: List[main_models.ListChatappTemplateResponseBodyListTemplate] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The message templates.
        self.list_template = list_template
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.list_template:
            for v1 in self.list_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['ListTemplate'] = []
        if self.list_template is not None:
            for k1 in self.list_template:
                result['ListTemplate'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.list_template = []
        if m.get('ListTemplate') is not None:
            for k1 in m.get('ListTemplate'):
                temp_model = main_models.ListChatappTemplateResponseBodyListTemplate()
                self.list_template.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListChatappTemplateResponseBodyListTemplate(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        language: str = None,
        last_update_time: int = None,
        reason: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The review state of the template. Valid values:
        # 
        # *   **pass**: The template is approved.
        # *   **fail**: The template is rejected.
        # *   **auditing**: The template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the WhatsApp message template. Valid values:
        # 
        # *   **UTILITY**
        # *   **MARKETING**
        # *   **AUTHENTICATION**
        # 
        # The category of the Viber template. Valid values:
        # 
        # *   **text**: template that contains only text
        # *   **image**: template that contains only images
        # *   **text_image_button**: template that contains text, images, and buttons
        # *   **text_button**: template that contains text and buttons
        # *   **document**: template that contains only documents
        # *   **video**: template that contains only videos
        # *   **text_video**: template that contains text and videos
        # *   **text_video_button**: template that contains text, videos, and buttons
        # *   **text_image**: template that contains text and images
        self.category = category
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The time when the template was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.last_update_time = last_update_time
        # The reason why the template was rejected.
        self.reason = reason
        # The code of the message template.
        self.template_code = template_code
        # The name of the message template.
        self.template_name = template_name
        # The type of the template. Valid values: WHATSAPP and VIBER.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.category is not None:
            result['Category'] = self.category

        if self.language is not None:
            result['Language'] = self.language

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

