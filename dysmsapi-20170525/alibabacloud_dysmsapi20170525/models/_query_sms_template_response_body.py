# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySmsTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_date: str = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_status: int = None,
        template_type: int = None,
    ):
        # The status code of the request.
        # 
        # - OK indicates that the request was successful.
        # 
        # - For a list of other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The time when the template was created.
        self.create_date = create_date
        # The description of the status code.
        self.message = message
        # The review notes for the template.
        # 
        # - If the review status is **Approved** or **Reviewing**, the message "No review remarks" is returned.
        # 
        # - If the review status is **Rejected**, the reason for the rejection is returned.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The template code.
        self.template_code = template_code
        # The template content.
        self.template_content = template_content
        # The template name.
        self.template_name = template_name
        # The review status of the template. Valid values:
        # 
        # - **0**: Reviewing.
        # 
        # - **1**: Approved.
        # 
        # - **2**: Rejected. The reason for the rejection is returned in the response. For more information, see [Suggestions for handling a failed review](https://help.aliyun.com/document_detail/65990.html). You can then call the [ModifySmsTemplate](https://help.aliyun.com/document_detail/419287.html) API or modify the template on the [Template Management](https://dysms.console.aliyun.com/domestic/text/template) page.
        # 
        # - **10**: Canceled.
        self.template_status = template_status
        # The message type. Valid values:
        # 
        # - **0**: Verification code.
        # 
        # - **1**: Message notification.
        # 
        # - **2**: Promotional message.
        # 
        # - **3**: International message.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.message is not None:
            result['Message'] = self.message

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

