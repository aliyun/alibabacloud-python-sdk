# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateQuotaAlarmRequestQuotaDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[CreateQuotaAlarmRequestQuotaDimensions] = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        self.alarm_name = alarm_name
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_dimensions = quota_dimensions
        self.threshold = threshold
        self.threshold_percent = threshold_percent
        self.threshold_type = threshold_type
        self.web_hook = web_hook

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = CreateQuotaAlarmRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class CreateQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        request_id: str = None,
    ):
        self.alarm_id = alarm_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaApplicationRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # > This parameter is required if you set the ProductCode parameter to ecs, ecs-spec, actiontrail, or ess.
        self.key = key
        # The value of the dimension.
        # 
        # The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # > This parameter is required if you set the ProductCode parameter to ecs, ecs-spec, actiontrail, or ess.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateQuotaApplicationRequest(TeaModel):
    def __init__(
        self,
        audit_mode: str = None,
        desire_value: float = None,
        dimensions: List[CreateQuotaApplicationRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        # The mode in which you want the application to be reviewed. Valid values:
        # 
        # *   Sync: The application is reviewed in a synchronous manner. Quota Center automatically reviews the application. The result is returned immediately after you submit the application. However, the chance of an approval for an application that is reviewed in Sync mode is lower than the chance of an approval for an application that is reviewed in Async mode. The validity period of the new quota value is 1 hour.
        # *   Async: The application is reviewed in an asynchronous manner. An Alibaba Cloud support engineer reviews the application. The chance of an approval for an application that is reviewed in Async mode is higher than the chance of an approval for an application that is reviewed in Sync mode. The validity period of the new quota value is one month.
        # 
        # > This parameter is available only for ECS Quotas by Instance Type.
        self.audit_mode = audit_mode
        # The requested value of the quota.
        # 
        # > Applications are reviewed by the technical support team of each Alibaba Cloud service. To increase the success rate of your application, you must specify a reasonable quota value and detailed reasons when you submit an application to increase the value of the quota.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimensions = dimensions
        # The end time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # > If you do not specify an end time, the default end time is 99 years after the quota application is submitted.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # *   zh (default value): Chinese
        # *   en: English
        self.env_language = env_language
        # The start time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # > If you do not specify a start time, the default start time is the time when the quota application is submitted.
        self.expire_time = expire_time
        # Specifies whether to send a notification about the application result. Valid values:
        # 
        # *   0 (default value): sends a notification about the application result.
        # *   3: A notification about the application result is sent.
        self.notice_type = notice_type
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota.
        # 
        # *   CommonQuota (default value): general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: whitelist quota
        self.quota_category = quota_category
        # The reason for the application.
        # 
        # > Applications are reviewed by the technical support team of each Alibaba Cloud service. To increase the success rate of your application, you must specify a reasonable quota value and detailed reasons when you submit an application to increase the value of the quota.
        self.reason = reason

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateQuotaApplicationRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        desire_value: int = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The time when the application was submitted.
        self.apply_time = apply_time
        # The quota value that is approved.
        self.approve_value = approve_value
        # The result of the application.
        self.audit_reason = audit_reason
        # The requested value of the quota.
        self.desire_value = desire_value
        # The quota dimension.
        self.dimension = dimension
        # The time when the new quota value takes effect.
        self.effective_time = effective_time
        # The time when the new quota expires.
        self.expire_time = expire_time
        # Indicates whether Quota Center sends a notification about the application result. Valid values:
        # 
        # *   0: Quota Center does not send a notification.
        # *   3: Quota Center sends a notification.
        self.notice_type = notice_type
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the new quota value.
        self.quota_unit = quota_unit
        # The reason for the application.
        self.reason = reason
        # The ID of the request.
        self.request_id = request_id
        # The status of the application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is being reviewed.
        # *   Cancel: The application is canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQuotaApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaApplicationsForTemplateRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # The value range of N varies based on the number of dimensions that are supported by the Alibaba Cloud service.
        # 
        # >  This parameter is required if you set the ProductCode parameter to ecs, ecs-spec, actiontrail, or ess.
        self.key = key
        # The value of the quota dimension.
        # 
        # >  The value range of N varies based on the number of dimensions that are supported by the Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateQuotaApplicationsForTemplateRequest(TeaModel):
    def __init__(
        self,
        aliyun_uids: List[str] = None,
        desire_value: float = None,
        dimensions: List[CreateQuotaApplicationsForTemplateRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        # The Alibaba Cloud accounts for which the quotas are applied.
        # 
        # >  For more information about the members of a resource directory, see [Query all the members in a resource directory](~~604207~~).
        self.aliyun_uids = aliyun_uids
        # The requested value of the quota.
        # 
        # >  Applications are reviewed by the technical support team of each Alibaba Cloud service. To increase the success rate of your application, you must specify a reasonable quota value and detailed reasons when you submit the application.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # >  If you do not specify a start time, the value is the time when the quota application is submitted.
        self.effective_time = effective_time
        # The language of the notification about the application result. Valid values:
        # 
        # *   zh (default): Chinese
        # *   en: English
        self.env_language = env_language
        # The end time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # >  If you do not specify an end time, the value is 99 years after the start time of the validity period.
        self.expire_time = expire_time
        # Specifies whether to send a notification about the application result. Valid values:
        # 
        # *   0 (default): no
        # *   3: yes
        self.notice_type = notice_type
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # >  For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # *   CommonQuota (default): general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category
        # The reason for the quota application.
        # 
        # >  Applications are reviewed by the technical support team of each Alibaba Cloud service. To increase the success rate of your application, you must specify a reasonable quota value and detailed reasons when you submit the application.
        self.reason = reason

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uids is not None:
            result['AliyunUids'] = self.aliyun_uids
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUids') is not None:
            self.aliyun_uids = m.get('AliyunUids')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateQuotaApplicationsForTemplateRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateQuotaApplicationsForTemplateResponseBodyFailResults(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        reason: str = None,
    ):
        self.aliyun_uid = aliyun_uid
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateQuotaApplicationsForTemplateResponseBody(TeaModel):
    def __init__(
        self,
        aliyun_uids: List[str] = None,
        batch_quota_application_id: str = None,
        fail_results: List[CreateQuotaApplicationsForTemplateResponseBodyFailResults] = None,
        request_id: str = None,
    ):
        # The Alibaba Cloud accounts for which the quotas are applied.
        self.aliyun_uids = aliyun_uids
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        self.fail_results = fail_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.fail_results:
            for k in self.fail_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uids is not None:
            result['AliyunUids'] = self.aliyun_uids
        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id
        result['FailResults'] = []
        if self.fail_results is not None:
            for k in self.fail_results:
                result['FailResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUids') is not None:
            self.aliyun_uids = m.get('AliyunUids')
        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')
        self.fail_results = []
        if m.get('FailResults') is not None:
            for k in m.get('FailResults'):
                temp_model = CreateQuotaApplicationsForTemplateResponseBodyFailResults()
                self.fail_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQuotaApplicationsForTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaApplicationsForTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQuotaApplicationsForTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateQuotaItemRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # > This parameter is required if you set the ProductCode parameter to ecs, ecs-spec, actiontrail, or ess.
        self.key = key
        # The value of the dimension.
        # 
        # The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # 
        # > This parameter is required if you set the ProductCode parameter to ecs, ecs-spec, actiontrail, or ess.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        desire_value: float = None,
        dimensions: List[CreateTemplateQuotaItemRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The requested value of the quota.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # > If you leave this parameter empty, the quota takes effect immediately.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # *   zh (default value): Chinese
        # *   en: English
        self.env_language = env_language
        # The end time of the validity period of the quota. Specify the value in UTC. This parameter is valid only if you set the QuotaCategory parameter to WhiteListLabel.
        # 
        # > If you leave this parameter empty, no end time is specified.
        self.expire_time = expire_time
        # Specifies whether to send a notification about the application result. Valid values:
        # 
        # *   0 (default value): no
        # *   3: yes
        self.notice_type = notice_type
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   WhiteListLabel: privilege
        # *   FlowControl: API rate limit
        self.quota_category = quota_category

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = CreateTemplateQuotaItemRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class CreateTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the quota template.
        self.id = id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateQuotaItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
    ):
        # The ID of the quota alert.
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class DeleteQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQuotaAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID of the quota template.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the quota template.
        self.id = id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateQuotaItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductQuotaRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # >- The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # >- If you call the operation to query the details of a quota that belongs to a cloud service that supports dimensions, you must configure this parameter. You must configure the `Dimensions.N.Key` and `Dimensions.N.Value` parameters at the same time. The following cloud services support dimensions: ECS whose service code is ecs, Enterprise Distributed Application Service (EDAS) whose service code is edas, ECS Quotas by Instance Type whose service code is ecs-spec, and Auto Scaling (ESS) whose service code is ess.
        self.key = key
        # The value of the dimension.
        # 
        # > - The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        # > - If you call the operation to query the details of a quota that belongs to a cloud service that supports dimensions, you must configure this parameter. You must configure the `Dimensions.N.Key` and `Dimensions.N.Value` parameters at the same time. The following cloud services support dimensions: ECS whose service code is ecs, EDAS whose service code is edas, ECS Quotas by Instance Type whose service code is ecs-spec, and ESS whose service code is ess.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProductQuotaRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[GetProductQuotaRequestDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = GetProductQuotaRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class GetProductQuotaResponseBodyQuotaPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle of the quota. Valid values:
        # 
        # *   second
        # *   minute
        # *   hour
        # *   day
        # *   week
        self.period_unit = period_unit
        # The value of the calculation cycle of the quota.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class GetProductQuotaResponseBodyQuotaQuotaItems(TeaModel):
    def __init__(
        self,
        quota: str = None,
        quota_unit: str = None,
        type: str = None,
        usage: str = None,
    ):
        # The value of the quota.
        self.quota = quota
        # The unit of the quota.
        # 
        # >  The unit of each quota is unique. For example, the quota whose ID is `q_cbdch3` represents the maximum number of ACK clusters. The unit of this quota is clusters. The quota whose ID is `q_security-groups` represents the maximum number of security groups. The unit of this quota is security groups.
        self.quota_unit = quota_unit
        # The category of the quota. Valid values:
        # 
        # *   BaseQuota: base quota.
        # *   ReservedQuota: reserved quota.
        self.type = type
        # The used quota.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class GetProductQuotaResponseBodyQuota(TeaModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        apply_reason_tips: str = None,
        consumable: bool = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        global_quota: bool = None,
        period: GetProductQuotaResponseBodyQuotaPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_items: List[GetProductQuotaResponseBodyQuotaQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        supported_range: List[float] = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
    ):
        # Indicates whether the quota is adjustable. Valid values:
        # 
        # *   true
        # *   false
        self.adjustable = adjustable
        # The range of the quota value.
        self.applicable_range = applicable_range
        # The type of the adjustable value. Valid values:
        # 
        # *   continuous
        # *   discontinuous
        self.applicable_type = applicable_type
        # The reason for submitting a quota increase request.
        self.apply_reason_tips = apply_reason_tips
        # Indicates whether the system shows the used value of the quota. Valid values:
        # 
        # *   true
        # *   false
        self.consumable = consumable
        # The quota dimension. Format: `{"regionId":"Region"}`.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. Specify the value in UTC.
        self.effective_time = effective_time
        # The end time of the validity period of the quota. Specify the value in UTC.
        self.expire_time = expire_time
        # Indicates whether the quota is a global quota. Valid values:
        # 
        # *   true: The quota is shared in all regions.
        # *   false: The quota is independently used in a region.
        self.global_quota = global_quota
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: whitelist quota
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The details of the quotas.
        self.quota_items = quota_items
        # The name of the quota.
        self.quota_name = quota_name
        # The type of the quota. Valid values:
        # 
        # *   privilege
        # *   normal (default value)
        self.quota_type = quota_type
        # The unit of the new quota value.
        # 
        # > The unit of each quota is unique.** For example, the quota whose ID is `q_cbdch3` represents the maximum number of Container Service for Kubernetes (ACK) clusters. The unit of this quota is clusters. The quota whose ID is `q_security-groups` represents the maximum number of security groups. The unit of this quota is security groups.
        self.quota_unit = quota_unit
        # The range of the quota value.
        self.supported_range = supported_range
        # The value of the quota.
        self.total_quota = total_quota
        # The used quota.
        self.total_usage = total_usage
        # The reason why the quota is not adjustable. Valid values:
        # 
        # *   nonactivated: The service is not activated.
        # *   applicationProcess: The application is being processed.
        # *   limitReached: The quota limit is reached.
        # *   supportTicketRequired: The quota can be increased only by submitting a ticket.
        self.unadjustable_detail = unadjustable_detail

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.apply_reason_tips is not None:
            result['ApplyReasonTips'] = self.apply_reason_tips
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.global_quota is not None:
            result['GlobalQuota'] = self.global_quota
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.supported_range is not None:
            result['SupportedRange'] = self.supported_range
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('ApplyReasonTips') is not None:
            self.apply_reason_tips = m.get('ApplyReasonTips')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GlobalQuota') is not None:
            self.global_quota = m.get('GlobalQuota')
        if m.get('Period') is not None:
            temp_model = GetProductQuotaResponseBodyQuotaPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = GetProductQuotaResponseBodyQuotaQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('SupportedRange') is not None:
            self.supported_range = m.get('SupportedRange')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        return self


class GetProductQuotaResponseBody(TeaModel):
    def __init__(
        self,
        quota: GetProductQuotaResponseBodyQuota = None,
        request_id: str = None,
    ):
        # The details of the quota.
        self.quota = quota
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = GetProductQuotaResponseBodyQuota()
            self.quota = temp_model.from_map(m['Quota'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductQuotaDimensionRequestDependentDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension on which the quota dimension that you want to query is dependent.
        # 
        # > The value range of N varies based on the number of quota dimensions that are supported by the specified Alibaba Cloud service.
        self.key = key
        # The value of the quota dimension on which the quota dimension that you want to query is dependent.
        # 
        # > The value range of N varies based on the number of quota dimensions that are supported by the specified Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProductQuotaDimensionRequest(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[GetProductQuotaDimensionRequestDependentDimensions] = None,
        dimension_key: str = None,
        product_code: str = None,
    ):
        # The information about quota dimensions.
        self.dependent_dimensions = dependent_dimensions
        # The key of the quota dimension.
        self.dimension_key = dimension_key
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code

    def validate(self):
        if self.dependent_dimensions:
            for k in self.dependent_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DependentDimensions'] = []
        if self.dependent_dimensions is not None:
            for k in self.dependent_dimensions:
                result['DependentDimensions'].append(k.to_map() if k else None)
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dependent_dimensions = []
        if m.get('DependentDimensions') is not None:
            for k in m.get('DependentDimensions'):
                temp_model = GetProductQuotaDimensionRequestDependentDimensions()
                self.dependent_dimensions.append(temp_model.from_map(k))
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the quota dimension.
        self.name = name
        # The value of the quota dimension.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProductQuotaDimensionResponseBodyQuotaDimension(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
    ):
        # The quota dimensions on which the quota dimension that you want to query is dependent.
        self.dependent_dimensions = dependent_dimensions
        # The key of the quota dimension. Valid values:
        # 
        # *   regionId: the region ID.
        # *   zoneId: the zone ID.
        # *   chargeType: the billing method.
        # *   networkType: the network type.
        self.dimension_key = dimension_key
        # The details of the quota dimension value.
        self.dimension_value_detail = dimension_value_detail
        # The values of the quota dimension.
        self.dimension_values = dimension_values
        # The name of the quota dimension.
        self.name = name

    def validate(self):
        if self.dimension_value_detail:
            for k in self.dimension_value_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        result['DimensionValueDetail'] = []
        if self.dimension_value_detail is not None:
            for k in self.dimension_value_detail:
                result['DimensionValueDetail'].append(k.to_map() if k else None)
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        self.dimension_value_detail = []
        if m.get('DimensionValueDetail') is not None:
            for k in m.get('DimensionValueDetail'):
                temp_model = GetProductQuotaDimensionResponseBodyQuotaDimensionDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k))
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetProductQuotaDimensionResponseBody(TeaModel):
    def __init__(
        self,
        quota_dimension: GetProductQuotaDimensionResponseBodyQuotaDimension = None,
        request_id: str = None,
    ):
        # The details of the quota dimension.
        self.quota_dimension = quota_dimension
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.quota_dimension:
            self.quota_dimension.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaDimension') is not None:
            temp_model = GetProductQuotaDimensionResponseBodyQuotaDimension()
            self.quota_dimension = temp_model.from_map(m['QuotaDimension'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductQuotaDimensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductQuotaDimensionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductQuotaDimensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
    ):
        # The ID of the request.
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class GetQuotaAlarmResponseBodyQuotaAlarm(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimension: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        webhook: str = None,
    ):
        # The numeric value of the alert threshold.
        self.alarm_id = alarm_id
        # security_groups
        self.alarm_name = alarm_name
        # The ID of the quota.
        self.create_time = create_time
        # The alert notification methods.
        self.notify_channels = notify_channels
        # The used quota.
        self.notify_target = notify_target
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The name of the quota alert.
        self.quota_action_code = quota_action_code
        # The time when the quota alert was created.
        self.quota_dimension = quota_dimension
        # The value of the quota.
        self.quota_usage = quota_usage
        # The ID of the quota alert.
        self.quota_value = quota_value
        # The abbreviation of the Alibaba Cloud service name.
        self.threshold = threshold
        # The type of the quota alert. Valid values:
        # 
        # *   used: The alert is created for the used quota.
        # *   usable: The alert is created for the available quota.
        self.threshold_percent = threshold_percent
        # The quota dimension.
        self.threshold_type = threshold_type
        # The webhook URL. Quota Center sends alert notifications to the specified URL by using HTTP POST requests.
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class GetQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        quota_alarm: GetQuotaAlarmResponseBodyQuotaAlarm = None,
        request_id: str = None,
    ):
        # The details of the quota alert rule.
        self.quota_alarm = quota_alarm
        # The details of the quota alert.
        self.request_id = request_id

    def validate(self):
        if self.quota_alarm:
            self.quota_alarm.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_alarm is not None:
            result['QuotaAlarm'] = self.quota_alarm.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaAlarm') is not None:
            temp_model = GetQuotaAlarmResponseBodyQuotaAlarm()
            self.quota_alarm = temp_model.from_map(m['QuotaAlarm'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class GetQuotaApplicationResponseBodyQuotaApplication(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        desire_value: int = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The time when the application was submitted.
        self.apply_time = apply_time
        # The approved quota value.
        self.approve_value = approve_value
        # The result of the application.
        self.audit_reason = audit_reason
        # The expected value of the quota.
        self.desire_value = desire_value
        # The dimension.
        # 
        # Format: `{"regionId":"Region"}`.
        self.dimension = dimension
        # The time when the new quota value takes effect.
        self.effective_time = effective_time
        # The time when the new quota expires.
        self.expire_time = expire_time
        # The method of that is used to send alert notifications. Valid values:
        # 
        # *   0: Quota Center does not send a notification.
        # *   1: Quota Center sends an email notification.
        # *   2: Quota Center sends an SMS notification.
        self.notice_type = notice_type
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the new quota value.
        self.quota_unit = quota_unit
        # The reason for the application.
        self.reason = reason
        # The status of the application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is being reviewed.
        # *   Cancel: The application is closed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetQuotaApplicationResponseBody(TeaModel):
    def __init__(
        self,
        quota_application: GetQuotaApplicationResponseBodyQuotaApplication = None,
        request_id: str = None,
    ):
        # The details about the application.
        self.quota_application = quota_application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.quota_application:
            self.quota_application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_application is not None:
            result['QuotaApplication'] = self.quota_application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaApplication') is not None:
            temp_model = GetQuotaApplicationResponseBodyQuotaApplication()
            self.quota_application = temp_model.from_map(m['QuotaApplication'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetQuotaApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaTemplateServiceStatusRequest(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
    ):
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        return self


class GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        service_status: int = None,
    ):
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The state of the quota template. Valid values:
        # 
        # *   \-1: The quota template is disabled.
        # *   1: The quota template is enabled.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetQuotaTemplateServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_service_status: GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the quota template.
        self.template_service_status = template_service_status

    def validate(self):
        if self.template_service_status:
            self.template_service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_service_status is not None:
            result['TemplateServiceStatus'] = self.template_service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateServiceStatus') is not None:
            temp_model = GetQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus()
            self.template_service_status = temp_model.from_map(m['TemplateServiceStatus'])
        return self


class GetQuotaTemplateServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaTemplateServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaTemplateServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmHistoriesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query.
        self.end_time = end_time
        # The keyword that is used for the query.
        self.keyword = keyword
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The beginning of the time range to query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAlarmHistoriesResponseBodyAlarmHistories(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        create_time: str = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_usage: float = None,
        threshold: float = None,
        threshold_percent: float = None,
    ):
        # The name of the quota alert.
        self.alarm_name = alarm_name
        # The time when the quota alert rule was created.
        self.create_time = create_time
        # The notification methods of the quota alert.
        self.notify_channels = notify_channels
        # The quota alert contact.
        self.notify_target = notify_target
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The used quota.
        self.quota_usage = quota_usage
        # The threshold to trigger quota alerts.
        self.threshold = threshold
        # The percentage of the quota alert threshold.
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        return self


class ListAlarmHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        alarm_histories: List[ListAlarmHistoriesResponseBodyAlarmHistories] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the quota alert records.
        self.alarm_histories = alarm_histories
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = ListAlarmHistoriesResponseBodyAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlarmHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDependentQuotasRequest(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        quota_action_code: str = None,
    ):
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        return self


class ListDependentQuotasResponseBodyQuotasDimensions(TeaModel):
    def __init__(
        self,
        dependent_dimension: List[str] = None,
        dimension_key: str = None,
        dimension_values: List[str] = None,
    ):
        # The dimensions of the quotas on which the specified quota depends.
        self.dependent_dimension = dependent_dimension
        # The key of the quota dimension.
        self.dimension_key = dimension_key
        # The dimension values.
        self.dimension_values = dimension_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimension is not None:
            result['DependentDimension'] = self.dependent_dimension
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimension') is not None:
            self.dependent_dimension = m.get('DependentDimension')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        return self


class ListDependentQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        dimensions: List[ListDependentQuotasResponseBodyQuotasDimensions] = None,
        product_code: str = None,
        quota_action_code: str = None,
        scale: float = None,
    ):
        # The dimensions of the quotas on which the specified quota depends.
        self.dimensions = dimensions
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The relationship percentage between the specified quota and the quotas on which the specified quota depends.
        self.scale = scale

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.scale is not None:
            result['Scale'] = self.scale
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListDependentQuotasResponseBodyQuotasDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('Scale') is not None:
            self.scale = m.get('Scale')
        return self


class ListDependentQuotasResponseBody(TeaModel):
    def __init__(
        self,
        quotas: List[ListDependentQuotasResponseBodyQuotas] = None,
        request_id: str = None,
    ):
        # The quotas on which the specified quota depends.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListDependentQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDependentQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDependentQuotasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDependentQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductDimensionGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
    ):
        # The maximum number of records that can be returned for the query. Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The service code.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductDimensionGroupsResponseBodyDimensionGroups(TeaModel):
    def __init__(
        self,
        dimension_keys: List[str] = None,
        group_code: str = None,
        group_name: str = None,
        product_code: str = None,
    ):
        # The key of the dimension group.
        self.dimension_keys = dimension_keys
        # The code of the dimension group.
        self.group_code = group_code
        # The name of the dimension group.
        self.group_name = group_name
        # The service code.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension_keys is not None:
            result['DimensionKeys'] = self.dimension_keys
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionKeys') is not None:
            self.dimension_keys = m.get('DimensionKeys')
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class ListProductDimensionGroupsResponseBody(TeaModel):
    def __init__(
        self,
        dimension_groups: List[ListProductDimensionGroupsResponseBodyDimensionGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The dimension groups.
        self.dimension_groups = dimension_groups
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.dimension_groups:
            for k in self.dimension_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DimensionGroups'] = []
        if self.dimension_groups is not None:
            for k in self.dimension_groups:
                result['DimensionGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimension_groups = []
        if m.get('DimensionGroups') is not None:
            for k in m.get('DimensionGroups'):
                temp_model = ListProductDimensionGroupsResponseBodyDimensionGroups()
                self.dimension_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductDimensionGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductDimensionGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductDimensionGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductQuotaDimensionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_category: str = None,
    ):
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The type of the quota. Valid values:
        # 
        # *   FlowControl: API rate limit.
        # *   CommonQuota: general quota. This is the default value.
        self.quota_category = quota_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the quota dimension.
        self.name = name
        # The value of the quota dimension.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductQuotaDimensionsResponseBodyQuotaDimensions(TeaModel):
    def __init__(
        self,
        dependent_dimensions: List[str] = None,
        dimension_key: str = None,
        dimension_value_detail: List[ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail] = None,
        dimension_values: List[str] = None,
        name: str = None,
        requisite: bool = None,
    ):
        # The quota dimensions on which the quota dimension that you want to query is dependent.
        self.dependent_dimensions = dependent_dimensions
        # The key of the quota dimension. Valid values:
        # 
        # *   regionId: the region ID.
        # *   zoneId: the zone ID.
        # *   chargeType: the billing method.
        # *   networkType: the network type.
        self.dimension_key = dimension_key
        # The details about the dimension value.
        self.dimension_value_detail = dimension_value_detail
        # The dimension values.
        self.dimension_values = dimension_values
        # The name of the quota dimension.
        self.name = name
        # Indicates whether the quota dimension is required when you query quota dimensions. Valid values:
        # 
        # *   true
        # *   false
        self.requisite = requisite

    def validate(self):
        if self.dimension_value_detail:
            for k in self.dimension_value_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependent_dimensions is not None:
            result['DependentDimensions'] = self.dependent_dimensions
        if self.dimension_key is not None:
            result['DimensionKey'] = self.dimension_key
        result['DimensionValueDetail'] = []
        if self.dimension_value_detail is not None:
            for k in self.dimension_value_detail:
                result['DimensionValueDetail'].append(k.to_map() if k else None)
        if self.dimension_values is not None:
            result['DimensionValues'] = self.dimension_values
        if self.name is not None:
            result['Name'] = self.name
        if self.requisite is not None:
            result['Requisite'] = self.requisite
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependentDimensions') is not None:
            self.dependent_dimensions = m.get('DependentDimensions')
        if m.get('DimensionKey') is not None:
            self.dimension_key = m.get('DimensionKey')
        self.dimension_value_detail = []
        if m.get('DimensionValueDetail') is not None:
            for k in m.get('DimensionValueDetail'):
                temp_model = ListProductQuotaDimensionsResponseBodyQuotaDimensionsDimensionValueDetail()
                self.dimension_value_detail.append(temp_model.from_map(k))
        if m.get('DimensionValues') is not None:
            self.dimension_values = m.get('DimensionValues')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Requisite') is not None:
            self.requisite = m.get('Requisite')
        return self


class ListProductQuotaDimensionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_dimensions: List[ListProductQuotaDimensionsResponseBodyQuotaDimensions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions
        # The ID of the request.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = ListProductQuotaDimensionsResponseBodyQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductQuotaDimensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductQuotaDimensionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductQuotaDimensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductQuotasRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.key = key
        # The value of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductQuotasRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListProductQuotasRequestDimensions] = None,
        group_code: str = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        sort_field: str = None,
        sort_order: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The code of the dimension group.
        self.group_code = group_code
        # The keyword that you want to use to search for the quotas.
        self.key_word = key_word
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota (default value): general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: whitelist quota
        self.quota_category = quota_category
        # The field based on which you want to sort the returned records. This parameter is available only for quotas that belong to ECS Quotas by Instance Type. Valid values:
        # 
        # *   TIME: The returned records are sorted by the last update time.
        # *   TOTAL: The returned records are sorted by the usage of the total quota.
        # *   RESERVED: The returned records are sorted by the usage of the reserved quota.
        self.sort_field = sort_field
        # The order in which you want to sort the returned records. This parameter is available only for quotas that belong to ECS Quotas by Instance Type. Valid values:
        # 
        # *   Ascending: ascending order
        # *   Descending: descending order
        self.sort_order = sort_order

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.group_code is not None:
            result['GroupCode'] = self.group_code
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListProductQuotasRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductQuotasResponseBodyQuotasPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle. Valid values:
        # 
        # *   second
        # *   minute
        # *   hour
        # *   day
        # *   week
        self.period_unit = period_unit
        # The value of the calculation cycle.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListProductQuotasResponseBodyQuotasQuotaItems(TeaModel):
    def __init__(
        self,
        quota: str = None,
        quota_unit: str = None,
        type: str = None,
        usage: str = None,
    ):
        # The quota value.
        self.quota = quota
        # The unit of the quota.
        # 
        # >  The unit of each quota is unique. For example, the quota whose ID is `q_cbdch3` represents the maximum number of Container Service for Kubernetes (ACK) clusters. The unit of this quota is clusters. The quota whose ID is `q_security-groups` represents the maximum number of security groups. The unit of this quota is security groups.
        self.quota_unit = quota_unit
        # The category of the quota. Valid values:
        # 
        # *   BaseQuota: base quota
        # *   ReservedQuota: reserved quota
        self.type = type
        # The quota usage.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.type is not None:
            result['Type'] = self.type
        if self.usage is not None:
            result['Usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        return self


class ListProductQuotasResponseBodyQuotas(TeaModel):
    def __init__(
        self,
        adjustable: bool = None,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        apply_reason_tips: str = None,
        consumable: bool = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        global_quota: bool = None,
        period: ListProductQuotasResponseBodyQuotasPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_items: List[ListProductQuotasResponseBodyQuotasQuotaItems] = None,
        quota_name: str = None,
        quota_type: str = None,
        quota_unit: str = None,
        supported_range: List[float] = None,
        total_quota: float = None,
        total_usage: float = None,
        unadjustable_detail: str = None,
    ):
        # Indicates whether the quota is adjustable. Valid values:
        # 
        # *   true: The quota is adjustable.
        # *   false: The quota is not adjustable.
        self.adjustable = adjustable
        # None.
        self.applicable_range = applicable_range
        # The type of the adjustable value. Valid values:
        # 
        # *   continuous
        # *   discontinuous
        self.applicable_type = applicable_type
        # The reason for submitting a quota increase request.
        self.apply_reason_tips = apply_reason_tips
        # Indicates whether the system shows the used value of the quota. Valid values:
        # 
        # *   true: The system shows the used value of the quota.
        # *   false: The system does not show the used value of the quota.
        self.consumable = consumable
        # The quota dimensions. Format: `{"regionId":"Region"}`.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. The value is displayed in UTC.
        self.effective_time = effective_time
        # The end time of the validity period of the quota. The value is displayed in UTC.
        self.expire_time = expire_time
        self.global_quota = global_quota
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The details of the quota.
        self.quota_items = quota_items
        # The quota name.
        self.quota_name = quota_name
        # The type of the quota. Valid values:
        # 
        # *   privilege
        # *   normal
        self.quota_type = quota_type
        # The unit of the quota.
        # 
        # >  The unit of each quota is unique. For example, the quota whose ID is `q_cbdch3` represents the maximum number of Container Service for Kubernetes (ACK) clusters. The unit of this quota is clusters. The quota whose ID is `q_security-groups` represents the maximum number of security groups. The unit of this quota is security groups.
        self.quota_unit = quota_unit
        # None.
        self.supported_range = supported_range
        # The quota value.
        self.total_quota = total_quota
        # The quota usage.
        self.total_usage = total_usage
        # The reason why the quota is not adjustable. Valid values:
        # 
        # *   nonactivated: The service is not activated.
        # *   applicationProcess: The application is being processed.
        # *   limitReached: The quota limit is reached.
        self.unadjustable_detail = unadjustable_detail

    def validate(self):
        if self.period:
            self.period.validate()
        if self.quota_items:
            for k in self.quota_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adjustable is not None:
            result['Adjustable'] = self.adjustable
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.apply_reason_tips is not None:
            result['ApplyReasonTips'] = self.apply_reason_tips
        if self.consumable is not None:
            result['Consumable'] = self.consumable
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.global_quota is not None:
            result['GlobalQuota'] = self.global_quota
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k in self.quota_items:
                result['QuotaItems'].append(k.to_map() if k else None)
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.supported_range is not None:
            result['SupportedRange'] = self.supported_range
        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota
        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage
        if self.unadjustable_detail is not None:
            result['UnadjustableDetail'] = self.unadjustable_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adjustable') is not None:
            self.adjustable = m.get('Adjustable')
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('ApplyReasonTips') is not None:
            self.apply_reason_tips = m.get('ApplyReasonTips')
        if m.get('Consumable') is not None:
            self.consumable = m.get('Consumable')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GlobalQuota') is not None:
            self.global_quota = m.get('GlobalQuota')
        if m.get('Period') is not None:
            temp_model = ListProductQuotasResponseBodyQuotasPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k in m.get('QuotaItems'):
                temp_model = ListProductQuotasResponseBodyQuotasQuotaItems()
                self.quota_items.append(temp_model.from_map(k))
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('SupportedRange') is not None:
            self.supported_range = m.get('SupportedRange')
        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')
        if m.get('TotalUsage') is not None:
            self.total_usage = m.get('TotalUsage')
        if m.get('UnadjustableDetail') is not None:
            self.unadjustable_detail = m.get('UnadjustableDetail')
        return self


class ListProductQuotasResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quotas: List[ListProductQuotasResponseBodyQuotas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The queried quotas.
        self.quotas = quotas
        # The ID of the request.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quotas:
            for k in self.quotas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Quotas'] = []
        if self.quotas is not None:
            for k in self.quotas:
                result['Quotas'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quotas = []
        if m.get('Quotas') is not None:
            for k in m.get('Quotas'):
                temp_model = ListProductQuotasResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductQuotasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListProductsResponseBodyProductInfo(TeaModel):
    def __init__(
        self,
        common_quota_support: str = None,
        dynamic: bool = None,
        flow_control_support: str = None,
        product_code: str = None,
        product_name: str = None,
        product_name_en: str = None,
        second_category_id: int = None,
        second_category_name: str = None,
        second_category_name_en: str = None,
        white_list_label_quota_support: str = None,
    ):
        # Indicates whether the Alibaba Cloud service supports general quotas. Valid values:
        # 
        # *   support: The Alibaba Cloud service supports general quotas.
        # *   unsupport: The Alibaba Cloud service does not support general quotas.
        self.common_quota_support = common_quota_support
        # Indicates whether the Alibaba Cloud service supports dynamic quota adjustment. Valid values:
        # 
        # *   true
        # *   false
        self.dynamic = dynamic
        # Indicates whether the Alibaba Cloud service supports API rate limits. Valid values:
        # 
        # *   support: The Alibaba Cloud service supports API rate limits.
        # *   unsupport: The Alibaba Cloud service does not support API rate limits.
        self.flow_control_support = flow_control_support
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The name of the Alibaba Cloud service.
        self.product_name = product_name
        # The English name of the Alibaba Cloud service.
        self.product_name_en = product_name_en
        # The ID of the service category.
        self.second_category_id = second_category_id
        # The name of the service category.
        self.second_category_name = second_category_name
        # The English name of the service category.
        self.second_category_name_en = second_category_name_en
        # Indicates whether the Alibaba Cloud service supports whitelist quotas. Valid values:
        # 
        # *   support: The Alibaba Cloud service supports whitelist quotas.
        # *   unsupport: The Alibaba Cloud service does not support whitelist quotas.
        self.white_list_label_quota_support = white_list_label_quota_support

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_quota_support is not None:
            result['CommonQuotaSupport'] = self.common_quota_support
        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic
        if self.flow_control_support is not None:
            result['FlowControlSupport'] = self.flow_control_support
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_name_en is not None:
            result['ProductNameEn'] = self.product_name_en
        if self.second_category_id is not None:
            result['SecondCategoryId'] = self.second_category_id
        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name
        if self.second_category_name_en is not None:
            result['SecondCategoryNameEn'] = self.second_category_name_en
        if self.white_list_label_quota_support is not None:
            result['WhiteListLabelQuotaSupport'] = self.white_list_label_quota_support
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonQuotaSupport') is not None:
            self.common_quota_support = m.get('CommonQuotaSupport')
        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')
        if m.get('FlowControlSupport') is not None:
            self.flow_control_support = m.get('FlowControlSupport')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductNameEn') is not None:
            self.product_name_en = m.get('ProductNameEn')
        if m.get('SecondCategoryId') is not None:
            self.second_category_id = m.get('SecondCategoryId')
        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')
        if m.get('SecondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('SecondCategoryNameEn')
        if m.get('WhiteListLabelQuotaSupport') is not None:
            self.white_list_label_quota_support = m.get('WhiteListLabelQuotaSupport')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        product_info: List[ListProductsResponseBodyProductInfo] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The information of the Alibaba Cloud service.
        self.product_info = product_info
        # The ID of the request.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.product_info:
            for k in self.product_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ProductInfo'] = []
        if self.product_info is not None:
            for k in self.product_info:
                result['ProductInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.product_info = []
        if m.get('ProductInfo') is not None:
            for k in m.get('ProductInfo'):
                temp_model = ListProductsResponseBodyProductInfo()
                self.product_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaAlarmsRequestQuotaDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.key = key
        # The value of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListQuotaAlarmsRequest(TeaModel):
    def __init__(
        self,
        alarm_name: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[ListQuotaAlarmsRequestQuotaDimensions] = None,
    ):
        # The name of the alert.
        self.alarm_name = alarm_name
        # The maximum number of records that you want to return for the query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        # 
        # > An empty value indicates that the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        # 
        # > The `ProductCode` parameter is required if you specify this parameter.
        self.quota_action_code = quota_action_code
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions

    def validate(self):
        if self.quota_dimensions:
            for k in self.quota_dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k in self.quota_dimensions:
                result['QuotaDimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k in m.get('QuotaDimensions'):
                temp_model = ListQuotaAlarmsRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k))
        return self


class ListQuotaAlarmsResponseBodyQuotaAlarms(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        create_time: str = None,
        exceed_threshold: bool = None,
        notify_channels: List[str] = None,
        notify_target: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: Dict[str, Any] = None,
        quota_usage: float = None,
        quota_value: float = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        # The ID of the alert.
        self.alarm_id = alarm_id
        # The name of the alert event.
        self.alarm_name = alarm_name
        # The time when the quota alert was created.
        self.create_time = create_time
        # Indicates whether the alert threshold was reached. Valid values:
        # 
        # *   false
        # *   true
        self.exceed_threshold = exceed_threshold
        # The alert notification methods.
        self.notify_channels = notify_channels
        # The alert contact. The value is accountContact.
        self.notify_target = notify_target
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The quota dimensions.
        self.quota_dimensions = quota_dimensions
        # The used quota.
        self.quota_usage = quota_usage
        # The value of the quota.
        self.quota_value = quota_value
        # The numeric value of the alert threshold.
        self.threshold = threshold
        # The percentage of the alert threshold.
        self.threshold_percent = threshold_percent
        # The type of the quota alert. Valid values:
        # 
        # *   used: The alert is created for the used quota.
        # *   usable: The alert is created for the available quota.
        self.threshold_type = threshold_type
        # The webhook URL.
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exceed_threshold is not None:
            result['ExceedThreshold'] = self.exceed_threshold
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        if self.notify_target is not None:
            result['NotifyTarget'] = self.notify_target
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_dimensions is not None:
            result['QuotaDimensions'] = self.quota_dimensions
        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage
        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExceedThreshold') is not None:
            self.exceed_threshold = m.get('ExceedThreshold')
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        if m.get('NotifyTarget') is not None:
            self.notify_target = m.get('NotifyTarget')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaDimensions') is not None:
            self.quota_dimensions = m.get('QuotaDimensions')
        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')
        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class ListQuotaAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_alarms: List[ListQuotaAlarmsResponseBodyQuotaAlarms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends.
        # 
        # > An empty value indicates that all data is returned.
        self.next_token = next_token
        # The details about the quota alert.
        self.quota_alarms = quota_alarms
        # The ID of the request.
        self.request_id = request_id
        # The total number of quota alerts.
        self.total_count = total_count

    def validate(self):
        if self.quota_alarms:
            for k in self.quota_alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaAlarms'] = []
        if self.quota_alarms is not None:
            for k in self.quota_alarms:
                result['QuotaAlarms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_alarms = []
        if m.get('QuotaAlarms') is not None:
            for k in m.get('QuotaAlarms'):
                temp_model = ListQuotaAlarmsResponseBodyQuotaAlarms()
                self.quota_alarms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaAlarmsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationTemplatesRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.key = key
        # The value of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListQuotaApplicationTemplatesRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListQuotaApplicationTemplatesRequestDimensions] = None,
        id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The ID of the quota item.
        self.id = id
        # The maximum number of records that can be returned for the query. Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        # 
        # > If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   WhiteListLabel: privilege
        # *   FlowControl: API rate limit
        self.quota_category = quota_category

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListQuotaApplicationTemplatesRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle. Valid values:
        # 
        # *   second
        # *   minute
        # *   hour
        # *   day
        # *   week
        self.period_unit = period_unit
        # The value of the calculation cycle.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates(TeaModel):
    def __init__(
        self,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        desire_value: float = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        id: str = None,
        notice_type: int = None,
        period: ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_name: str = None,
    ):
        # None
        self.applicable_range = applicable_range
        # The type of the adjustable value. Valid values:
        # 
        # *   continuous
        # *   discontinuous
        self.applicable_type = applicable_type
        # The requested value of the quota.
        self.desire_value = desire_value
        # The quota dimensions.
        # 
        # Format: {"regionId":"Region"}.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. The value is displayed in UTC.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.env_language = env_language
        # The end time of the validity period of the quota. The value is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the quota template.
        self.id = id
        # Indicates whether Quota Center sends a notification about the application result. Valid values:
        # 
        # *   0: no
        # *   3: yes
        self.notice_type = notice_type
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range
        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.id is not None:
            result['Id'] = self.id
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')
        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('Period') is not None:
            temp_model = ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        return self


class ListQuotaApplicationTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_application_templates: List[ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends.
        # 
        # > An empty value indicates that all data is returned.
        self.next_token = next_token
        # The queried quota templates.
        self.quota_application_templates = quota_application_templates
        # The request ID.
        self.request_id = request_id
        # The total number of records returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quota_application_templates:
            for k in self.quota_application_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaApplicationTemplates'] = []
        if self.quota_application_templates is not None:
            for k in self.quota_application_templates:
                result['QuotaApplicationTemplates'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_application_templates = []
        if m.get('QuotaApplicationTemplates') is not None:
            for k in m.get('QuotaApplicationTemplates'):
                temp_model = ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates()
                self.quota_application_templates.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaApplicationTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationsRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.key = key
        # The value of the dimension.
        # 
        # > The value range of N varies based on the number of dimensions that are supported by the related Alibaba Cloud service.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListQuotaApplicationsRequest(TeaModel):
    def __init__(
        self,
        dimensions: List[ListQuotaApplicationsRequestDimensions] = None,
        key_word: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        status: str = None,
    ):
        # The quota dimensions.
        self.dimensions = dimensions
        # The keyword that you want to use to search for the application.
        self.key_word = key_word
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 200. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: whitelist quota
        self.quota_category = quota_category
        # The status of the application. Valid values:
        # 
        # *   Disagree: rejects the application.
        # *   Agree: approves the application.
        # *   Process: reviews the application.
        # *   Cancel: cancels the application.
        self.status = status

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ListQuotaApplicationsRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle. Valid values:
        # 
        # *   second
        # *   minute
        # *   hour
        # *   day
        # *   week
        self.period_unit = period_unit
        # The value of the calculation cycle.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListQuotaApplicationsResponseBodyQuotaApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        comment: str = None,
        desire_value: float = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        period: ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The ID of the application.
        self.application_id = application_id
        # The time when the application was submitted.
        self.apply_time = apply_time
        # The quota value that is approved.
        self.approve_value = approve_value
        # The result of the application.
        self.audit_reason = audit_reason
        # The remarks of the application.
        self.comment = comment
        # The quota value that is approved.
        self.desire_value = desire_value
        # The dimension of the application.
        self.dimension = dimension
        # The time when the application took effect.
        self.effective_time = effective_time
        # The time when the application expired.
        self.expire_time = expire_time
        # Indicates whether Quota Center sends a notification about the application result. Valid values:
        # 
        # *   0: A notification about the application result is not sent.
        # *   3: A notification about the application result is sent.
        self.notice_type = notice_type
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the new quota value.
        self.quota_unit = quota_unit
        # The reason for the application.
        self.reason = reason
        # The status of the application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is being reviewed.
        # *   Cancel: The application is canceled.
        self.status = status

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('Period') is not None:
            temp_model = ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_applications: List[ListQuotaApplicationsResponseBodyQuotaApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that are returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends. An empty value indicates that all data is returned.
        self.next_token = next_token
        # The details of the applications.
        self.quota_applications = quota_applications
        # The ID of the request.
        self.request_id = request_id
        # The total number of applications.
        self.total_count = total_count

    def validate(self):
        if self.quota_applications:
            for k in self.quota_applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaApplications'] = []
        if self.quota_applications is not None:
            for k in self.quota_applications:
                result['QuotaApplications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_applications = []
        if m.get('QuotaApplications') is not None:
            for k in m.get('QuotaApplications'):
                temp_model = ListQuotaApplicationsResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationsDetailForTemplateRequest(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        batch_quota_application_id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        status: str = None,
    ):
        # The Alibaba Cloud account that is used to submit the quota increase application.
        self.aliyun_uid = aliyun_uid
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The maximum number of records that can be returned for the query.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        # 
        # >  An empty value indicates that the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # >  For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category
        # The approval status of the quota increase application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is pending approval.
        # *   Cancel: The application is canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod(TeaModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle of the quota.
        self.period_unit = period_unit
        # The value of the calculation cycle of the quota.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period_value is not None:
            result['PeriodValue'] = self.period_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')
        return self


class ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications(TeaModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        batch_quota_application_id: str = None,
        desire_value: float = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        period: ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_dimension: Dict[str, str] = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliyun_uid = aliyun_uid
        # The ID of the quota increase application.
        self.application_id = application_id
        # The time when the quota increase application was submitted. The value is displayed in UTC.
        self.apply_time = apply_time
        # The quota value that is approved.
        self.approve_value = approve_value
        # The approval result of the quota increase application.
        self.audit_reason = audit_reason
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The requested value of the quota.
        self.desire_value = desire_value
        # The start time of the validity period of the quota. The value is displayed in UTC.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.env_language = env_language
        # The end time of the validity period of the quota. The value is displayed in UTC.
        self.expire_time = expire_time
        # Indicates whether Quota Center sends a notification about the application result. Valid values:
        # 
        # *   0: no
        # *   3: yes
        self.notice_type = notice_type
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The quota type. Valid values:
        # 
        # *   CommonQuota (default): general quota
        # *   WhiteListLabel: privilege
        # *   FlowControl: API rate limit
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The quota dimensions.
        self.quota_dimension = quota_dimension
        # The quota name.
        self.quota_name = quota_name
        # The unit of the quota.
        self.quota_unit = quota_unit
        # The reason for the quota increase application.
        self.reason = reason
        # The approval status of the quota increase application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is pending approval.
        # *   Cancel: The application is canceled.
        self.status = status

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value
        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason
        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.period is not None:
            result['Period'] = self.period.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description
        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name
        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')
        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')
        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('Period') is not None:
            temp_model = ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod()
            self.period = temp_model.from_map(m['Period'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')
        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')
        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsDetailForTemplateResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_applications: List[ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that can be returned for the query.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        self.next_token = next_token
        # The details of the quota increase application.
        self.quota_applications = quota_applications
        # The request ID.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quota_applications:
            for k in self.quota_applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaApplications'] = []
        if self.quota_applications is not None:
            for k in self.quota_applications:
                result['QuotaApplications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_applications = []
        if m.get('QuotaApplications') is not None:
            for k in m.get('QuotaApplications'):
                temp_model = ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationsDetailForTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationsDetailForTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaApplicationsDetailForTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotaApplicationsForTemplateRequest(TeaModel):
    def __init__(
        self,
        apply_end_time: str = None,
        apply_start_time: str = None,
        batch_quota_application_id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The UTC time when the quota application ends.
        self.apply_end_time = apply_end_time
        # The UTC time when the quota application starts.
        self.apply_start_time = apply_start_time
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        # 
        # >  An empty value indicates that the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # >  For more information, see [Alibaba Cloud services that support Quota Center](~~182368~~).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_end_time is not None:
            result['ApplyEndTime'] = self.apply_end_time
        if self.apply_start_time is not None:
            result['ApplyStartTime'] = self.apply_start_time
        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyEndTime') is not None:
            self.apply_end_time = m.get('ApplyEndTime')
        if m.get('ApplyStartTime') is not None:
            self.apply_start_time = m.get('ApplyStartTime')
        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos(TeaModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        # The number of approval documents.
        self.count = count
        # The approval status of the quota increase application. Valid values:
        # 
        # *   Disagree: The application is rejected.
        # *   Agree: The application is approved.
        # *   Process: The application is pending approval.
        # *   Cancel: The application is canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications(TeaModel):
    def __init__(
        self,
        apply_time: str = None,
        audit_status_vos: List[ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos] = None,
        batch_quota_application_id: str = None,
        desire_value: float = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The time when the quota increase application was submitted. The value is displayed in UTC.
        self.apply_time = apply_time
        # The number of applications in different approval states.
        self.audit_status_vos = audit_status_vos
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The requested value of the quota.
        self.desire_value = desire_value
        # The quota dimensions.
        # 
        # Format: {"regionId":"cn-hangzhou"}.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. The value is displayed in UTC.
        self.effective_time = effective_time
        # The end time of the validity period of the quota. The value is displayed in UTC.
        self.expire_time = expire_time
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # *   CommonQuota: general quota
        # *   FlowControl: API rate limit
        # *   WhiteListLabel: privilege
        self.quota_category = quota_category

    def validate(self):
        if self.audit_status_vos:
            for k in self.audit_status_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time
        result['AuditStatusVos'] = []
        if self.audit_status_vos is not None:
            for k in self.audit_status_vos:
                result['AuditStatusVos'].append(k.to_map() if k else None)
        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')
        self.audit_status_vos = []
        if m.get('AuditStatusVos') is not None:
            for k in m.get('AuditStatusVos'):
                temp_model = ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos()
                self.audit_status_vos.append(temp_model.from_map(k))
        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ListQuotaApplicationsForTemplateResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_batch_applications: List[ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records that can be returned for the query.
        self.max_results = max_results
        # The token that marks the position from which you want to start the query.
        self.next_token = next_token
        # The queried quota application records.
        self.quota_batch_applications = quota_batch_applications
        # The request ID.
        self.request_id = request_id
        # The total number of records that are returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quota_batch_applications:
            for k in self.quota_batch_applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['QuotaBatchApplications'] = []
        if self.quota_batch_applications is not None:
            for k in self.quota_batch_applications:
                result['QuotaBatchApplications'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.quota_batch_applications = []
        if m.get('QuotaBatchApplications') is not None:
            for k in m.get('QuotaBatchApplications'):
                temp_model = ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications()
                self.quota_batch_applications.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListQuotaApplicationsForTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotaApplicationsForTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotaApplicationsForTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyQuotaTemplateServiceStatusRequest(TeaModel):
    def __init__(
        self,
        service_status: int = None,
    ):
        # The state of the quota template. Valid values:
        # 
        # *   \-1: The quota template is disabled.
        # *   1: The quota template is enabled.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus(TeaModel):
    def __init__(
        self,
        resource_directory_id: str = None,
        service_status: int = None,
    ):
        # The ID of the resource directory.
        self.resource_directory_id = resource_directory_id
        # The state of the quota template. Valid values:
        # 
        # *   \-1: The quota template is disabled.
        # *   1: The quota template is enabled.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class ModifyQuotaTemplateServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_service_status: ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the quota template.
        self.template_service_status = template_service_status

    def validate(self):
        if self.template_service_status:
            self.template_service_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_service_status is not None:
            result['TemplateServiceStatus'] = self.template_service_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateServiceStatus') is not None:
            temp_model = ModifyQuotaTemplateServiceStatusResponseBodyTemplateServiceStatus()
            self.template_service_status = temp_model.from_map(m['TemplateServiceStatus'])
        return self


class ModifyQuotaTemplateServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyQuotaTemplateServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyQuotaTemplateServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTemplateQuotaItemRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyTemplateQuotaItemRequest(TeaModel):
    def __init__(
        self,
        desire_value: float = None,
        dimensions: List[ModifyTemplateQuotaItemRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        id: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        self.desire_value = desire_value
        self.dimensions = dimensions
        self.effective_time = effective_time
        self.env_language = env_language
        self.expire_time = expire_time
        self.id = id
        self.notice_type = notice_type
        self.product_code = product_code
        self.quota_action_code = quota_action_code
        self.quota_category = quota_category

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.id is not None:
            result['Id'] = self.id
        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code
        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = ModifyTemplateQuotaItemRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')
        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')
        return self


class ModifyTemplateQuotaItemResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTemplateQuotaItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTemplateQuotaItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyTemplateQuotaItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaAlarmRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_name: str = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        # The ID of the quota alert.
        self.alarm_id = alarm_id
        # The name of the quota alert.
        self.alarm_name = alarm_name
        # The numeric value of the alert threshold. Valid values:
        # 
        # *   If you set the `ThresholdType` parameter to `used`, you will receive an alert notification when the used quota is greater than or equal to the preset alert threshold. The alert threshold must be greater than the current used quota.
        # *   If you set the `ThresholdType` parameter to `usable`, you will receive an alert notification when the available quota is less than or equal to the preset alert threshold. The alert threshold must be less than the current available quota.
        # 
        # > You must set one of the Threshold and ThresholdPercent parameters.
        self.threshold = threshold
        # The percentage of the alert threshold. Valid values:
        # 
        # *   If you set the `ThresholdType` parameter to `used`, you will receive an alert notification when the used quota is greater than or equal to the preset percentage of the alert threshold. Value range: (50%, 100%].
        # *   If you set the `ThresholdType` parameter to `usable`, you will receive an alert notification when the available quota is less than or equal to the preset percentage of the alert threshold. Value range: (0%, 50%].
        # 
        # > You must set one of the Threshold and ThresholdPercent parameters.
        self.threshold_percent = threshold_percent
        # The type of the quota alert. Valid values:
        # 
        # *   used: The alert is created for the used quota.
        # *   usable: The alert is created for the available quota.
        self.threshold_type = threshold_type
        # The webhook URL. Quota Center sends alert notifications to the specified URL by using HTTP POST requests.
        self.web_hook = web_hook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent
        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type
        if self.web_hook is not None:
            result['WebHook'] = self.web_hook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')
        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')
        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')
        return self


class UpdateQuotaAlarmResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateQuotaAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQuotaAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


