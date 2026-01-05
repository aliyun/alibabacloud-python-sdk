# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        sms_template_list: List[main_models.QuerySmsTemplateListResponseBodySmsTemplateList] = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of templates per page. Valid values: **1 to 50**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried message templates.
        self.sms_template_list = sms_template_list
        # The total number of templates.
        self.total_count = total_count

    def validate(self):
        if self.sms_template_list:
            for v1 in self.sms_template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SmsTemplateList'] = []
        if self.sms_template_list is not None:
            for k1 in self.sms_template_list:
                result['SmsTemplateList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sms_template_list = []
        if m.get('SmsTemplateList') is not None:
            for k1 in m.get('SmsTemplateList'):
                temp_model = main_models.QuerySmsTemplateListResponseBodySmsTemplateList()
                self.sms_template_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySmsTemplateListResponseBodySmsTemplateList(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        create_date: str = None,
        order_id: str = None,
        outer_template_type: int = None,
        reason: main_models.QuerySmsTemplateListResponseBodySmsTemplateListReason = None,
        signature_name: str = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_type: int = None,
        traffic_driving: str = None,
    ):
        # The approval status of the message template. Valid values:
        # 
        # *   **AUDIT_STATE_INIT**: The message template is pending approval.
        # *   **AUDIT_STATE_PASS**: The message template is approved.
        # *   **AUDIT_STATE_NOT_PASS**: The message template is rejected. You can view the reason in the Reason response parameter.
        # *   **AUDIT_STATE_CANCEL** or **AUDIT_SATE_CANCEL**: The approval is canceled.
        self.audit_status = audit_status
        # The time when the message template was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.create_date = create_date
        # The ticket ID.
        self.order_id = order_id
        # The type of the message template. We recommend that you specify this parameter. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: notification message
        # *   **2**: promotional message
        # *   **3**: message sent to countries or regions outside the Chinese mainland
        # *   **7**: digital message
        # 
        # > The template type is the same as the value of the TemplateType parameter in the AddSmsTemplate and ModifySmsTemplate operations.
        self.outer_template_type = outer_template_type
        # The approval remarks.
        # 
        # *   If the value of AuditStatus is **AUDIT_STATE_PASS** or **AUDIT_STATE_INIT**, the value of Reason is No Approval Remarks.
        # *   If the value of AuditStatus is **AUDIT_STATE_NOT_PASS**, the reason why the message template is rejected is returned.
        self.reason = reason
        self.signature_name = signature_name
        # The code of the message template.
        # 
        # You can log on to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/dysms.htm), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the template code on the **Templates** tab. You can also call the [AddSmsTemplate](https://help.aliyun.com/document_detail/121208.html) operation to obtain the template code.
        self.template_code = template_code
        # The content of the message template.
        self.template_content = template_content
        # The name of the message template.
        self.template_name = template_name
        # The type of the message template. Valid values:
        # 
        # *   **0**: notification message
        # *   **1**: promotional message
        # *   **2**: verification code
        # *   **6**: message sent to countries or regions outside the Chinese mainland
        # *   **7**: digital message
        self.template_type = template_type
        self.traffic_driving = traffic_driving

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.outer_template_type is not None:
            result['OuterTemplateType'] = self.outer_template_type

        if self.reason is not None:
            result['Reason'] = self.reason.to_map()

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.traffic_driving is not None:
            result['TrafficDriving'] = self.traffic_driving

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OuterTemplateType') is not None:
            self.outer_template_type = m.get('OuterTemplateType')

        if m.get('Reason') is not None:
            temp_model = main_models.QuerySmsTemplateListResponseBodySmsTemplateListReason()
            self.reason = temp_model.from_map(m.get('Reason'))

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TrafficDriving') is not None:
            self.traffic_driving = m.get('TrafficDriving')

        return self

class QuerySmsTemplateListResponseBodySmsTemplateListReason(DaraModel):
    def __init__(
        self,
        reject_date: str = None,
        reject_info: str = None,
        reject_sub_info: str = None,
    ):
        # The time when the message template was rejected. Format: yyyy-MM-dd HH:mm:ss.
        self.reject_date = reject_date
        # The reason why the message template was rejected.
        self.reject_info = reject_info
        # The remarks about the rejection.
        self.reject_sub_info = reject_sub_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reject_date is not None:
            result['RejectDate'] = self.reject_date

        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info

        if self.reject_sub_info is not None:
            result['RejectSubInfo'] = self.reject_sub_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RejectDate') is not None:
            self.reject_date = m.get('RejectDate')

        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')

        if m.get('RejectSubInfo') is not None:
            self.reject_sub_info = m.get('RejectSubInfo')

        return self

