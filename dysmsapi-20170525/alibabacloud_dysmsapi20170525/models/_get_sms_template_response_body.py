# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetSmsTemplateResponseBody(DaraModel):
    def __init__(
        self,
        apply_scene: str = None,
        audit_info: main_models.GetSmsTemplateResponseBodyAuditInfo = None,
        code: str = None,
        create_date: str = None,
        file_url_list: main_models.GetSmsTemplateResponseBodyFileUrlList = None,
        intl_type: int = None,
        message: str = None,
        more_data_file_url_list: main_models.GetSmsTemplateResponseBodyMoreDataFileUrlList = None,
        order_id: str = None,
        related_sign_name: str = None,
        remark: str = None,
        request_id: str = None,
        sign_list: main_models.GetSmsTemplateResponseBodySignList = None,
        template_code: str = None,
        template_content: str = None,
        template_name: str = None,
        template_status: str = None,
        template_tag: int = None,
        template_type: str = None,
        variable_attribute: str = None,
        vendor_audit_status: Dict[str, Any] = None,
    ):
        # 应用场景内容。
        self.apply_scene = apply_scene
        # 审核信息。
        self.audit_info = audit_info
        # 请求状态码。取值：
        # 
        # * OK：代表请求成功。
        # * 其他错误码，请参见[API错误码](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 创建短信模板的时间。
        self.create_date = create_date
        self.file_url_list = file_url_list
        # 国际/港澳台模板类型。当**TemplateType**参数返回值为**3**时，此参数取值：
        # - **0**：短信通知。
        # - **1**：推广短信。
        # - **2**：验证码。
        self.intl_type = intl_type
        # 状态码的描述。
        self.message = message
        self.more_data_file_url_list = more_data_file_url_list
        # 工单号。
        # 
        # 审核人员查询审核时会用到此参数。您需要审核加急时需要提供此工单号。
        self.order_id = order_id
        # 申请模板时，关联的短信签名。
        self.related_sign_name = related_sign_name
        # 短信模板申请说明，是模板审核的参考信息之一。
        self.remark = remark
        # 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。
        self.request_id = request_id
        self.sign_list = sign_list
        # 短信模板Code。
        self.template_code = template_code
        # 短信模板内容。
        self.template_content = template_content
        # 短信模板名称。
        self.template_name = template_name
        # 模板审核状态。返回值：
        # 
        # - **0**：审核中。
        # - **1**：通过审核。
        # - **2**：未通过审核，会返回审核失败的原因，请参考[短信审核失败的处理建议](https://www.alibabacloud.com/help/en/sms/user-guide/causes-of-application-failures-and-suggestions)，调用[UpdateSmsTemplate](https://www.alibabacloud.com/help/en/sms/developer-reference/api-dysmsapi-2017-05-25-updatesmstemplate)接口或在[模板管理](https://dysms.console.aliyun.com/domestic/text/template)页面修改短信模板。
        # - **10**：取消审核。
        self.template_status = template_status
        # 模板标识。取值：
        # 
        # - 2：用户自定义创建模板。
        # 
        # - 3：系统赠送模板。
        # 
        # - 4：测试模板。
        self.template_tag = template_tag
        # 短信类型。取值：
        # 
        # - **0**：验证码。
        # - **1**：短信通知。
        # - **2**：推广短信。
        # - **3**：国际/港澳台消息。
        # 
        # > 仅支持企业认证用户申请推广短信和国际/港澳台消息。个人用户与企业用户权益区别详情请参见[使用须知](https://www.alibabacloud.com/help/en/sms/user-guide/usage-notes)。
        self.template_type = template_type
        # 模板变量规则。
        # 
        # 模板变量规则详情，请参见[示例文档](https://www.alibabacloud.com/help/en/sms/templaterule-template-variable-parameter-filling-example)。
        self.variable_attribute = variable_attribute
        # 各运营商审核状态，仅数字短信会返回该参数。
        # 
        # 
        # key代表运营商。取值：
        # 
        # - MOBILE_VENDOR：中国移动。
        # 
        # - TELECOM_VENDOR：中国电信。
        # 
        # - UNICOM_VENDOR：中国联通。
        # 
        #  value代表审核状态。取值： 
        # 
        # - 0：审核中。
        # 
        # - 1：通过。
        # 
        #  - 2：不通过。
        # 
        #  - 15：已失效。
        self.vendor_audit_status = vendor_audit_status

    def validate(self):
        if self.audit_info:
            self.audit_info.validate()
        if self.file_url_list:
            self.file_url_list.validate()
        if self.more_data_file_url_list:
            self.more_data_file_url_list.validate()
        if self.sign_list:
            self.sign_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_scene is not None:
            result['ApplyScene'] = self.apply_scene

        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.file_url_list is not None:
            result['FileUrlList'] = self.file_url_list.to_map()

        if self.intl_type is not None:
            result['IntlType'] = self.intl_type

        if self.message is not None:
            result['Message'] = self.message

        if self.more_data_file_url_list is not None:
            result['MoreDataFileUrlList'] = self.more_data_file_url_list.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.related_sign_name is not None:
            result['RelatedSignName'] = self.related_sign_name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sign_list is not None:
            result['SignList'] = self.sign_list.to_map()

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.variable_attribute is not None:
            result['VariableAttribute'] = self.variable_attribute

        if self.vendor_audit_status is not None:
            result['VendorAuditStatus'] = self.vendor_audit_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyScene') is not None:
            self.apply_scene = m.get('ApplyScene')

        if m.get('AuditInfo') is not None:
            temp_model = main_models.GetSmsTemplateResponseBodyAuditInfo()
            self.audit_info = temp_model.from_map(m.get('AuditInfo'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('FileUrlList') is not None:
            temp_model = main_models.GetSmsTemplateResponseBodyFileUrlList()
            self.file_url_list = temp_model.from_map(m.get('FileUrlList'))

        if m.get('IntlType') is not None:
            self.intl_type = m.get('IntlType')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MoreDataFileUrlList') is not None:
            temp_model = main_models.GetSmsTemplateResponseBodyMoreDataFileUrlList()
            self.more_data_file_url_list = temp_model.from_map(m.get('MoreDataFileUrlList'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RelatedSignName') is not None:
            self.related_sign_name = m.get('RelatedSignName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignList') is not None:
            temp_model = main_models.GetSmsTemplateResponseBodySignList()
            self.sign_list = temp_model.from_map(m.get('SignList'))

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('VariableAttribute') is not None:
            self.variable_attribute = m.get('VariableAttribute')

        if m.get('VendorAuditStatus') is not None:
            self.vendor_audit_status = m.get('VendorAuditStatus')

        return self

class GetSmsTemplateResponseBodySignList(DaraModel):
    def __init__(
        self,
        sign_list: List[str] = None,
    ):
        self.sign_list = sign_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sign_list is not None:
            result['SignList'] = self.sign_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignList') is not None:
            self.sign_list = m.get('SignList')

        return self

class GetSmsTemplateResponseBodyMoreDataFileUrlList(DaraModel):
    def __init__(
        self,
        more_data_file_url: List[str] = None,
    ):
        self.more_data_file_url = more_data_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.more_data_file_url is not None:
            result['MoreDataFileUrl'] = self.more_data_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MoreDataFileUrl') is not None:
            self.more_data_file_url = m.get('MoreDataFileUrl')

        return self

class GetSmsTemplateResponseBodyFileUrlList(DaraModel):
    def __init__(
        self,
        file_url: List[str] = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

class GetSmsTemplateResponseBodyAuditInfo(DaraModel):
    def __init__(
        self,
        audit_date: str = None,
        reject_info: str = None,
    ):
        # 审核时间。
        self.audit_date = audit_date
        # 审核未通过的原因。
        self.reject_info = reject_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_date is not None:
            result['AuditDate'] = self.audit_date

        if self.reject_info is not None:
            result['RejectInfo'] = self.reject_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditDate') is not None:
            self.audit_date = m.get('AuditDate')

        if m.get('RejectInfo') is not None:
            self.reject_info = m.get('RejectInfo')

        return self

