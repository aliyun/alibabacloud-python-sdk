# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetSmsSignResponseBody(DaraModel):
    def __init__(
        self,
        app_icp_record_id: int = None,
        apply_scene: str = None,
        audit_info: main_models.GetSmsSignResponseBodyAuditInfo = None,
        authorization_letter_audit_pass: bool = None,
        authorization_letter_id: int = None,
        code: str = None,
        create_date: str = None,
        file_url_list: List[str] = None,
        message: str = None,
        order_id: str = None,
        qualification_id: int = None,
        register_result: int = None,
        remark: str = None,
        request_id: str = None,
        sign_code: str = None,
        sign_isp_register_detail_list: List[main_models.GetSmsSignResponseBodySignIspRegisterDetailList] = None,
        sign_name: str = None,
        sign_status: int = None,
        sign_tag: str = None,
        sign_usage: str = None,
        third_party: bool = None,
        trademark_id: int = None,
    ):
        # APP-ICP备案实体id。
        self.app_icp_record_id = app_icp_record_id
        # 应用场景内容。
        self.apply_scene = apply_scene
        # 审核信息。
        self.audit_info = audit_info
        # 委托授权书审核状态。取值：
        # - true：审核通过。
        # - false：审核未通过（包含审核通过外的其他所有状态）。
        self.authorization_letter_audit_pass = authorization_letter_audit_pass
        # 委托授权书ID。
        self.authorization_letter_id = authorization_letter_id
        # 请求状态码。取值：
        # 
        # - OK：代表请求成功。
        # - 其他错误码，请参见[API错误码](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 短信签名的创建日期和时间。
        self.create_date = create_date
        # 更多资料信息，补充上传业务证明文件或业务截图文件列表。
        self.file_url_list = file_url_list
        # 状态码的描述。
        self.message = message
        # 工单号。
        # 
        # 审核人员查询审核时会用到此参数。您需要审核加急时需要提供此工单号。
        self.order_id = order_id
        # 资质ID。申请签名时关联的资质ID。
        self.qualification_id = qualification_id
        # **已废弃，请使用`SignIspRegisterDetailList`查看各运营商实名报备结果。**
        # 
        # 签名实名制报备结果。取值：
        # - 0：报备失败。
        # - 1：报备成功。
        # - 2：报备失效。
        # - -1：无状态。
        # 
        # 建议您单击查看[更多签名实名制报备内容及建议操作](https://help.aliyun.com/document_detail/2873145.html)。
        self.register_result = register_result
        # 短信签名场景说明，长度不超过200个字符。
        self.remark = remark
        # 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。
        self.request_id = request_id
        # 短信签名Code。
        self.sign_code = sign_code
        # 运营商报备状态列表。获取此参数返回数据需要[更新SDK](https://api.aliyun.com/api-tools/sdk/Dysmsapi?version=2017-05-25&language=java-tea&tab=primer-doc)至4.1.2版本或以上。
        self.sign_isp_register_detail_list = sign_isp_register_detail_list
        # 短信签名名称。
        self.sign_name = sign_name
        # 签名审核状态。取值：
        # 
        # - **0**：审核中。
        # - **1**：审核通过。
        # - **2**：审核失败，请在返回参数`AuditInfo.RejectInfo`中查看审核失败原因。
        # - **10**：取消审核。
        self.sign_status = sign_status
        # 签名标识。取值：
        # 
        # - 2：用户自定义创建签名。
        # - 3：系统赠送签名。
        # - 4：测试签名。
        # - 5：试用签名。
        self.sign_tag = sign_tag
        # 签名使用场景。
        self.sign_usage = sign_usage
        # 签名为自用或他用。
        # 
        # - false：自用（默认值）。
        # 
        # - true：他用。
        self.third_party = third_party
        # 商标实体id。
        self.trademark_id = trademark_id

    def validate(self):
        if self.audit_info:
            self.audit_info.validate()
        if self.sign_isp_register_detail_list:
            for v1 in self.sign_isp_register_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icp_record_id is not None:
            result['AppIcpRecordId'] = self.app_icp_record_id

        if self.apply_scene is not None:
            result['ApplyScene'] = self.apply_scene

        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info.to_map()

        if self.authorization_letter_audit_pass is not None:
            result['AuthorizationLetterAuditPass'] = self.authorization_letter_audit_pass

        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id

        if self.code is not None:
            result['Code'] = self.code

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.file_url_list is not None:
            result['FileUrlList'] = self.file_url_list

        if self.message is not None:
            result['Message'] = self.message

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.register_result is not None:
            result['RegisterResult'] = self.register_result

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sign_code is not None:
            result['SignCode'] = self.sign_code

        result['SignIspRegisterDetailList'] = []
        if self.sign_isp_register_detail_list is not None:
            for k1 in self.sign_isp_register_detail_list:
                result['SignIspRegisterDetailList'].append(k1.to_map() if k1 else None)

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status

        if self.sign_tag is not None:
            result['SignTag'] = self.sign_tag

        if self.sign_usage is not None:
            result['SignUsage'] = self.sign_usage

        if self.third_party is not None:
            result['ThirdParty'] = self.third_party

        if self.trademark_id is not None:
            result['TrademarkId'] = self.trademark_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcpRecordId') is not None:
            self.app_icp_record_id = m.get('AppIcpRecordId')

        if m.get('ApplyScene') is not None:
            self.apply_scene = m.get('ApplyScene')

        if m.get('AuditInfo') is not None:
            temp_model = main_models.GetSmsSignResponseBodyAuditInfo()
            self.audit_info = temp_model.from_map(m.get('AuditInfo'))

        if m.get('AuthorizationLetterAuditPass') is not None:
            self.authorization_letter_audit_pass = m.get('AuthorizationLetterAuditPass')

        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('FileUrlList') is not None:
            self.file_url_list = m.get('FileUrlList')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('RegisterResult') is not None:
            self.register_result = m.get('RegisterResult')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignCode') is not None:
            self.sign_code = m.get('SignCode')

        self.sign_isp_register_detail_list = []
        if m.get('SignIspRegisterDetailList') is not None:
            for k1 in m.get('SignIspRegisterDetailList'):
                temp_model = main_models.GetSmsSignResponseBodySignIspRegisterDetailList()
                self.sign_isp_register_detail_list.append(temp_model.from_map(k1))

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')

        if m.get('SignTag') is not None:
            self.sign_tag = m.get('SignTag')

        if m.get('SignUsage') is not None:
            self.sign_usage = m.get('SignUsage')

        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')

        if m.get('TrademarkId') is not None:
            self.trademark_id = m.get('TrademarkId')

        return self

class GetSmsSignResponseBodySignIspRegisterDetailList(DaraModel):
    def __init__(
        self,
        operator_code: str = None,
        operator_complete_time: str = None,
        register_status: int = None,
        register_status_reasons: List[main_models.GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons] = None,
    ):
        # 运营商类型。取值：
        # - **mobile**：中国移动；
        # - **unicom**：中国联通；
        # - **telecom**：中国电信。
        self.operator_code = operator_code
        # 运营商反馈时间，格式为yyyy-MM-dd HH:mm:ss。
        self.operator_complete_time = operator_complete_time
        # 报备状态。取值：
        # 
        # - **0**：报备失败，原因可能为资质信息与工信注册信息不一致或运营商侧无法支持等。建议您登录[短信服务控制台](https://dysms.console.aliyun.com/domestic/text/sign)查看具体失败原因，并依据提示进行操作；
        # - **1**：已报备待验证，当前至少有一个子端口号运营商已返回报备通过，建议您少量多次向不同运营商手机号发送验证码、通知短信进行验证；
        # - **2**：报备失效，签名超过 6 个月无发送记录时，报备结果失效。如您需要重新启用该签名，请在[短信服务控制台](https://dysms.console.aliyun.com/domestic/text/sign)重新发起报备；
        # - **3**：报备成功，当前至少有一个子端口号运营商已返回报备通过，经验证短信发送成功率符合预期，建议您持续关注发送成功率；
        # - **-1**：报备中，当前尚未收到运营商反馈的报备结果，建议您等待签名报备状态变更为“已报备待验证”后再批量发送，当前可少量多次尝试使用该签名发送，观察短信发送效果；
        # - **-2**：未报备，原因可能为当前签名未关联实名资质或关联资质信息不全，建议您修改当前资质或编辑签名绑定其他资质以重新发起报备。
        # 
        # 建议您单击查看[更多签名实名制报备内容及建议操作](https://help.aliyun.com/document_detail/2873145.html)。
        self.register_status = register_status
        # 报备状态原因列表。
        self.register_status_reasons = register_status_reasons

    def validate(self):
        if self.register_status_reasons:
            for v1 in self.register_status_reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code

        if self.operator_complete_time is not None:
            result['OperatorCompleteTime'] = self.operator_complete_time

        if self.register_status is not None:
            result['RegisterStatus'] = self.register_status

        result['RegisterStatusReasons'] = []
        if self.register_status_reasons is not None:
            for k1 in self.register_status_reasons:
                result['RegisterStatusReasons'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')

        if m.get('OperatorCompleteTime') is not None:
            self.operator_complete_time = m.get('OperatorCompleteTime')

        if m.get('RegisterStatus') is not None:
            self.register_status = m.get('RegisterStatus')

        self.register_status_reasons = []
        if m.get('RegisterStatusReasons') is not None:
            for k1 in m.get('RegisterStatusReasons'):
                temp_model = main_models.GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons()
                self.register_status_reasons.append(temp_model.from_map(k1))

        return self

class GetSmsSignResponseBodySignIspRegisterDetailListRegisterStatusReasons(DaraModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_desc_list: List[str] = None,
    ):
        # 报备状态原因码。取值：
        # - **UNBINDING_QUA**：签名未关联资质；
        # - **BINDING_INCOMPLETE_QUA**：关联资质信息不全；
        # - **NON_REGISTER**：未发起报备；
        # - **REGISTERING**：签名报备中；
        # - **DETECTING**：未发起探测或探测中；
        # - **DETECT_SUCCESS**：报备成功；
        # - **QUALIFICATION_ERROR**：资质原因；
        # - **SIGNATURE_ERROR**：签名原因；
        # - **SIGNATURE_QUALIFICATION_ERROR**：签名与资质关系不符；
        # - **ONE_CODE_MULTIPLE_SIGN**：扩展码原因；
        # - **OTHERS_ERROR**：其他原因；
        # - **REGISTER_TIMEOUT**：报备超时；
        # - **NO_SEND_RECORD**：签名超过6个月无发送记录；
        # - **EXT_CODE_RECYCLE**：扩展码收回。
        # - **SUBPORT_RECYCLE**：子端口被运营商治理。
        self.reason_code = reason_code
        # 原因说明列表。可能返回0个或者多个原因说明，返回原因码不一定会返回原因说明。
        self.reason_desc_list = reason_desc_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_desc_list is not None:
            result['ReasonDescList'] = self.reason_desc_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonDescList') is not None:
            self.reason_desc_list = m.get('ReasonDescList')

        return self

class GetSmsSignResponseBodyAuditInfo(DaraModel):
    def __init__(
        self,
        audit_date: str = None,
        reject_info: str = None,
    ):
        # 审核时间。
        self.audit_date = audit_date
        # 审批未通过的原因。
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

