# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateFlowLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        return self


class ActivateFlowLogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateFlowLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateFlowLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ActivateFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(
        self,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The VBR ID.
        # 
        # This parameter is required.
        self.child_instance_id = child_instance_id
        # The ID of the Alibaba Cloud account to which the VBR belongs.
        # 
        # >  If you want to connect to a network instance that belongs to a different account, this parameter is required.
        self.child_instance_owner_id = child_instance_owner_id
        # The region ID of the VBR.
        # 
        # This parameter is required.
        self.child_instance_region_id = child_instance_region_id
        # The type of the network instance. Set the value to **VBR**.
        # 
        # This parameter is required.
        self.child_instance_type = child_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the sub-instance. It must be 0 to 128 characters in length.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class AttachExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AttachExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachExpressConnectRouterChildInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AttachExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAddRegionToExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        fresh_region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run.
        # *   false (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the region for which you want to check whether the CDT service is enabled for the ECR feature.
        # 
        # This parameter is required.
        self.fresh_region_id = fresh_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.fresh_region_id is not None:
            result['FreshRegionId'] = self.fresh_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FreshRegionId') is not None:
            self.fresh_region_id = m.get('FreshRegionId')
        return self


class CheckAddRegionToExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        any_cross_border_link: bool = None,
        any_inter_region_link: bool = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        is_cdt_cross_border_enabled: bool = None,
        is_cdt_inter_region_enabled: bool = None,
        is_user_allowed_to_create_cross_border_link: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether the ECR is used to establish connections between regions in the Chinese mainland and regions outside China. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.any_cross_border_link = any_cross_border_link
        # Indicates whether the ECR is used to establish connections between regions in the Chinese mainland. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.any_inter_region_link = any_inter_region_link
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsInstanceId**, the request parameter **DtsInstanceId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether the cross-border CDT service is activated for the account to which the ECR belongs. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_cdt_cross_border_enabled = is_cdt_cross_border_enabled
        # Indicates whether the CDT service is activated for the account to which the ECR belongs. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_cdt_inter_region_enabled = is_cdt_inter_region_enabled
        # Indicates whether the account to which the ECR belongs can create cross-border connections. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_user_allowed_to_create_cross_border_link = is_user_allowed_to_create_cross_border_link
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.any_cross_border_link is not None:
            result['AnyCrossBorderLink'] = self.any_cross_border_link
        if self.any_inter_region_link is not None:
            result['AnyInterRegionLink'] = self.any_inter_region_link
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.is_cdt_cross_border_enabled is not None:
            result['IsCdtCrossBorderEnabled'] = self.is_cdt_cross_border_enabled
        if self.is_cdt_inter_region_enabled is not None:
            result['IsCdtInterRegionEnabled'] = self.is_cdt_inter_region_enabled
        if self.is_user_allowed_to_create_cross_border_link is not None:
            result['IsUserAllowedToCreateCrossBorderLink'] = self.is_user_allowed_to_create_cross_border_link
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AnyCrossBorderLink') is not None:
            self.any_cross_border_link = m.get('AnyCrossBorderLink')
        if m.get('AnyInterRegionLink') is not None:
            self.any_inter_region_link = m.get('AnyInterRegionLink')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IsCdtCrossBorderEnabled') is not None:
            self.is_cdt_cross_border_enabled = m.get('IsCdtCrossBorderEnabled')
        if m.get('IsCdtInterRegionEnabled') is not None:
            self.is_cdt_inter_region_enabled = m.get('IsCdtInterRegionEnabled')
        if m.get('IsUserAllowedToCreateCrossBorderLink') is not None:
            self.is_user_allowed_to_create_cross_border_link = m.get('IsUserAllowedToCreateCrossBorderLink')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckAddRegionToExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAddRegionToExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckAddRegionToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExpressConnectRouterRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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


class CreateExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        alibaba_side_asn: int = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        resource_group_id: str = None,
        tag: List[CreateExpressConnectRouterRequestTag] = None,
    ):
        # The autonomous system number (ASN) of the ECR. Valid values: 45104, 64512 to 65534, and 4200000000 to 4294967294. Default value: 45104. The value 65025 is reserved by Alibaba Cloud.
        # 
        # This parameter is required.
        self.alibaba_side_asn = alibaba_side_asn
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the ECR.
        # 
        # >  The description can be empty or 0 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The name of the ECR.
        # 
        # >  The name must be 0 to 128 characters in length, and cannot start with http:// or https://.
        self.name = name
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateExpressConnectRouterRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_id: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The ECR ID.
        self.ecr_id = ecr_id
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the ECR is created. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_region_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        create_attachment: bool = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        transit_router_id: str = None,
        transit_router_owner_id: int = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The route prefix mode. Valid values:
        # 
        # - **MatchMode**: After you distribute new route CIDR blocks to data centers, original specific routes that are distributed are withdrawn.
        # 
        # - **IncrementalMode**: After you distribute new route CIDR blocks to data centers, the original specific routes that fall in the CIDR blocks that you configure are withdrawn, and the original specific routes that do not fall in the CIDR blocks are still distributed.
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The region ID of the resource to be associated.
        # 
        # This parameter is required.
        self.association_region_id = association_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to initiate an association on the TR when the ECR is associated with the TR. Valid values:
        # 
        # *   **true**: You do not need to initiate an association on the TR.
        # *   **false**: You need to initiate an association on the TR.
        self.create_attachment = create_attachment
        # The information about the associated resource. It must be 0 to 128 characters in length.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The TR ID.
        self.transit_router_id = transit_router_id
        # The ID of the Alibaba Cloud account that owns the TR. Default value: ID of the Alibaba Cloud account that logs in.
        # 
        # >  If you want to connect to a network instance that belongs to a different account, this parameter is required.
        self.transit_router_owner_id = transit_router_owner_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account that owns the VPC. Default value: ID of the Alibaba Cloud account that logs in.
        # 
        # >  If you want to connect to a network instance that belongs to a different account, this parameter is required.
        self.vpc_owner_id = vpc_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode
        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_attachment is not None:
            result['CreateAttachment'] = self.create_attachment
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')
        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateAttachment') is not None:
            self.create_attachment = m.get('CreateAttachment')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        return self


class CreateExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        association_id: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The ID of the association between the ECR and the VPC or TR.
        self.association_id = association_id
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateExpressConnectRouterAssociationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowLogRequestTag(TeaModel):
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


class CreateFlowLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        interval: int = None,
        log_store_name: str = None,
        project_name: str = None,
        resource_group_id: str = None,
        sampling_rate: str = None,
        tag: List[CreateFlowLogRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the flow log.
        # 
        # > The description can be empty or 1 to 256 characters in length. It cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ID of the ECR.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The name of the flow log.
        # 
        # > The name can be empty or 1 to 128 characters in length and cannot start with http:// or https://.
        self.flow_log_name = flow_log_name
        # The VBR ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of network instance. Valid values:
        # 
        # *   **VBR**\
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The time window for collecting log data. Unit: seconds. Valid values:
        # 
        # - **60**\
        # - **600**\
        # 
        # Default value: **600**.
        self.interval = interval
        # The Logstore that stores the captured traffic data.
        # 
        # *   If a Logstore is already created in the selected region, enter the name of the Logstore.
        # *   If no Logstores are created in the selected region, enter a name and the system automatically creates a Logstore. The name of the Logstore. The name must meet the following requirements:
        # *   The name must be unique in a project.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.log_store_name = log_store_name
        # The project that stores the captured traffic data.
        # 
        # *   If a project is already created in the selected region, enter the name of the project.
        # *   If no projects are created in the selected region, enter a name and the system automatically creates a project.
        # 
        # The project name must be unique in a region. You cannot change the name after the project is created. The name must meet the following requirements:
        # 
        # *   The name must be globally unique.
        # *   The name can contain only lowercase letters,
        # *   digits, and hyphens (-).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.project_name = project_name
        self.resource_group_id = resource_group_id
        # The sampling proportion. Valid values:
        # 
        # - **1:4096**\
        # - **1:2048**\
        # - **1:1024**\
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateFlowLogRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateFlowLogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        flow_log_id: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The queried information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message. This parameter is used to replace the % **s** in the **ErrMessage** error message of the response parameter.
        # 
        # > For example, if the value of **ErrMessage** is **The Value of Input Parameter** %**s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **True**\
        # - **False**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFlowLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFlowLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactivateFlowLogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        return self


class DeactivateFlowLogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeactivateFlowLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeactivateFlowLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeactivateFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DeleteExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(
        self,
        association_id: str = None,
        client_token: str = None,
        delete_attachment: bool = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The ID of the association between the ECR and the VPC or TR.
        # 
        # This parameter is required.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to delete the association between the ECR and the VPC or TR. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.delete_attachment = delete_attachment
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.delete_attachment is not None:
            result['DeleteAttachment'] = self.delete_attachment
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeleteAttachment') is not None:
            self.delete_attachment = m.get('DeleteAttachment')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DeleteExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExpressConnectRouterAssociationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowlogRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run.
        # *   false (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        return self


class DeleteFlowlogResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **True**\
        # - **False**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowlogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFlowlogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteFlowlogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        nexthop_instance_id: str = None,
        nexthop_instance_region_id: str = None,
    ):
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the route entry was created.
        self.gmt_create = gmt_create
        # The ID of the next-hop instance.
        self.nexthop_instance_id = nexthop_instance_id
        # The region ID of the next-hop instance.
        self.nexthop_instance_region_id = nexthop_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        disabled_route_entry_list: List[DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The routes that are queried.
        self.disabled_route_entry_list = disabled_route_entry_list
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsInstanceId**, the request parameter **DtsInstanceId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether routes are disabled by the ECR. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of routes.
        self.total_count = total_count

    def validate(self):
        if self.disabled_route_entry_list:
            for k in self.disabled_route_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['DisabledRouteEntryList'] = []
        if self.disabled_route_entry_list is not None:
            for k in self.disabled_route_entry_list:
                result['DisabledRouteEntryList'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.disabled_route_entry_list = []
        if m.get('DisabledRouteEntryList') is not None:
            for k in m.get('DisabledRouteEntryList'):
                temp_model = DescribeDisabledExpressConnectRouterRouteEntriesResponseBodyDisabledRouteEntryList()
                self.disabled_route_entry_list.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDisabledExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDisabledExpressConnectRouterRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeDisabledExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys.
        # 
        # The tag keys cannot be an empty string. The tag keys can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # A tag value.
        # 
        # A tag value can be a maximum of 128 characters in length. It cannot contain `http://` or `https://` and cannot start with `acs:`.
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


class DescribeExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        resource_group_id: str = None,
        tag: List[DescribeExpressConnectRouterRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The name of the ECR. The name must be 0 to 128 characters in length.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The resource tags. You can specify up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeExpressConnectRouterRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeExpressConnectRouterResponseBodyEcrListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeExpressConnectRouterResponseBodyEcrList(TeaModel):
    def __init__(
        self,
        alibaba_side_asn: int = None,
        biz_status: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[DescribeExpressConnectRouterResponseBodyEcrListTags] = None,
    ):
        # The autonomous system number (ASN) of the ECR.
        self.alibaba_side_asn = alibaba_side_asn
        # The business state of the ECR. Valid values:
        # 
        # *   **Normal:** The ECR is running as expected.
        # *   **FinancialLocked**: The ECR is locked due to overdue payments.
        self.biz_status = biz_status
        # The description of the ECR.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the ECR was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the ECR was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The name of the ECR.
        self.name = name
        # The ID of the Alibaba Cloud account that owns the ECR.
        self.owner_id = owner_id
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The deployment state of the ECR. Valid values:
        # 
        # *   **ACTIVE**: The ECR is created.
        # *   **UPDATING**: The ECR is being modified.
        # *   **ASSOCIATING**: The ECR is being associated with resources.
        # *   **DISSOCIATING**: The resource is being disassociated from resources.
        # *   **LOCKED_ATTACHING**: The ECR is locked because it is being associated with an external system.
        # *   **LOCKED_DETACHING**: The ECR is locked because it is being disassociated from an external system.
        # *   **RECLAIMING**: The ECR is waiting to release resources.
        # *   **DELETING**: The ECR is being deleted.
        self.status = status
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.description is not None:
            result['Description'] = self.description
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeExpressConnectRouterResponseBodyEcrListTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_list: List[DescribeExpressConnectRouterResponseBodyEcrList] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The ECRs.
        self.ecr_list = ecr_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of ECRs.
        self.total_count = total_count

    def validate(self):
        if self.ecr_list:
            for k in self.ecr_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['EcrList'] = []
        if self.ecr_list is not None:
            for k in self.ecr_list:
                result['EcrList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.ecr_list = []
        if m.get('EcrList') is not None:
            for k in m.get('EcrList'):
                temp_model = DescribeExpressConnectRouterResponseBodyEcrList()
                self.ecr_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryRequest(TeaModel):
    def __init__(
        self,
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # The ID of the association between the ECR and the virtual private cloud (VPC) or transit router (TR).
        # 
        # >  You must specify either **InstanceId** or **AssociationId**.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the network instance that is associated with the ECR.
        # 
        # >  You must specify either **InstanceId** or **AssociationId**.
        self.instance_id = instance_id
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**\
        # *   **TR**\
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList(TeaModel):
    def __init__(
        self,
        allowed_prefix: List[str] = None,
        gmt_create: str = None,
    ):
        # The route prefix.
        self.allowed_prefix = allowed_prefix
        # The time when the historical route prefix entry was created.
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefix is not None:
            result['AllowedPrefix'] = self.allowed_prefix
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefix') is not None:
            self.allowed_prefix = m.get('AllowedPrefix')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allowed_prefix_history_list: List[DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The historical route prefixes.
        self.allowed_prefix_history_list = allowed_prefix_history_list
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.allowed_prefix_history_list:
            for k in self.allowed_prefix_history_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['AllowedPrefixHistoryList'] = []
        if self.allowed_prefix_history_list is not None:
            for k in self.allowed_prefix_history_list:
                result['AllowedPrefixHistoryList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.allowed_prefix_history_list = []
        if m.get('AllowedPrefixHistoryList') is not None:
            for k in m.get('AllowedPrefixHistoryList'):
                temp_model = DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList()
                self.allowed_prefix_history_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterAllowedPrefixHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterAssociationRequest(TeaModel):
    def __init__(
        self,
        association_id: str = None,
        association_node_type: str = None,
        association_region_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        transit_router_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the association between the ECR and the VPC or TR.
        self.association_id = association_id
        # The type of the associated resource. Valid values:
        # 
        # *   **VPC**\
        # *   **TR**\
        self.association_node_type = association_node_type
        # The region ID of the VPC or TR.
        self.association_region_id = association_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The TR ID.
        self.transit_router_id = transit_router_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type
        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')
        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeExpressConnectRouterAssociationResponseBodyAssociationList(TeaModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_id: str = None,
        association_node_type: str = None,
        cen_id: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: int = None,
        region_id: str = None,
        status: str = None,
        transit_router_id: str = None,
        transit_router_owner_id: int = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The prefix route mode. Valid values:
        # 
        # *   MatchMode
        # *   IncrementalMode
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The ID of the association between the ECR and the VPC or TR.
        self.association_id = association_id
        # The type of the associated resource. Valid values:
        # 
        # *   **VPC**\
        # *   **TR**\
        self.association_node_type = association_node_type
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The description of the associated resource.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the association was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the association was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the Alibaba Cloud account that owns the resource.
        self.owner_id = owner_id
        # The region ID of the resource.
        self.region_id = region_id
        # The deployment state of the associated resource. Valid values:
        # 
        # *   **CREATING**: The resource is being created.
        # *   **ACTIVE**: The resource is created.
        # *   **INACTIVE**: The TR is pending to be associated with the ECR.
        # *   **ASSOCIATING**: The resource is being associated.
        # *   **DISSOCIATING**: The resource is being disassociated.
        # *   **UPDATING**: The resource is being modified.
        # *   **DELETING**: The resource is being deleted.
        self.status = status
        # The TR ID.
        self.transit_router_id = transit_router_id
        # The ID of the Alibaba Cloud account that owns the TR.
        self.transit_router_owner_id = transit_router_owner_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.description is not None:
            result['Description'] = self.description
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id
        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')
        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')
        return self


class DescribeExpressConnectRouterAssociationResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        association_list: List[DescribeExpressConnectRouterAssociationResponseBodyAssociationList] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The associated resources.
        self.association_list = association_list
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of DynamicMessage is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of associated resources.
        self.total_count = total_count

    def validate(self):
        if self.association_list:
            for k in self.association_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['AssociationList'] = []
        if self.association_list is not None:
            for k in self.association_list:
                result['AssociationList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.association_list = []
        if m.get('AssociationList') is not None:
            for k in m.get('AssociationList'):
                temp_model = DescribeExpressConnectRouterAssociationResponseBodyAssociationList()
                self.association_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterAssociationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterAssociationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterAssociationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(
        self,
        association_id: str = None,
        child_instance_id: str = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the association between the ECR and the virtual private cloud (VPC) or transit router (TR).
        self.association_id = association_id
        # The ID of the network instance to be queried.
        self.child_instance_id = child_instance_id
        # The region ID of the network instance.
        self.child_instance_region_id = child_instance_region_id
        # The type of network instance. Set the value to VBR.
        self.child_instance_type = child_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList(TeaModel):
    def __init__(
        self,
        association_id: str = None,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: int = None,
        region_id: str = None,
        status: str = None,
    ):
        # The ID of the association between the ECR and the VPC or TR.
        self.association_id = association_id
        # The VBR ID.
        self.child_instance_id = child_instance_id
        # The ID of the Alibaba Cloud account that owns the VBR.
        self.child_instance_owner_id = child_instance_owner_id
        # The region ID of the VBR.
        self.child_instance_region_id = child_instance_region_id
        # The type of the VBR. The value is **VBR**.
        self.child_instance_type = child_instance_type
        # The description of the ECR.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the association was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the association was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the Alibaba Cloud account that owns the VBR.
        self.owner_id = owner_id
        # The region ID of the VBR.
        self.region_id = region_id
        # The deployment state of the associated resource. Valid values:
        # 
        # - **CREATING**: The resource is being created.
        # - **ACTIVE**: The resource is created.
        # - **ASSOCIATING**: The resource is being associated.
        # - **DISSOCIATING**: The resource is being disassociated.
        # - **UPDATING**: The resource is being modified.
        # - **DELETING**: The resource is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.description is not None:
            result['Description'] = self.description
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        child_instance_list: List[DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The VBRs.
        self.child_instance_list = child_instance_list
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of associated resources.
        self.total_count = total_count

    def validate(self):
        if self.child_instance_list:
            for k in self.child_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['ChildInstanceList'] = []
        if self.child_instance_list is not None:
            for k in self.child_instance_list:
                result['ChildInstanceList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.child_instance_list = []
        if m.get('ChildInstanceList') is not None:
            for k in m.get('ChildInstanceList'):
                temp_model = DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList()
                self.child_instance_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterChildInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterInterRegionTransitModeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList(TeaModel):
    def __init__(
        self,
        mode: str = None,
        region_id: str = None,
    ):
        # The cross-region forwarding mode of the ECR. Valid values:
        # 
        # *   **ECMP**: the load balancing mode.
        # *   **NearBy**: the nearby forwarding mode.
        self.mode = mode
        # The region ID of the ECR.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        inter_region_transit_mode_list: List[DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The cross-region forwarding modes.
        self.inter_region_transit_mode_list = inter_region_transit_mode_list
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        if self.inter_region_transit_mode_list:
            for k in self.inter_region_transit_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['InterRegionTransitModeList'] = []
        if self.inter_region_transit_mode_list is not None:
            for k in self.inter_region_transit_mode_list:
                result['InterRegionTransitModeList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.inter_region_transit_mode_list = []
        if m.get('InterRegionTransitModeList') is not None:
            for k in m.get('InterRegionTransitModeList'):
                temp_model = DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList()
                self.inter_region_transit_mode_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterInterRegionTransitModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterInterRegionTransitModeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterInterRegionTransitModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRegionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run.
        # *   false (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ID of the ECR that you want to query.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DescribeExpressConnectRouterRegionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        region_id_list: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The region in which the ECR feature is activated.
        self.region_id_list = region_id_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id_list is not None:
            result['RegionIdList'] = self.region_id_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionIdList') is not None:
            self.region_id_list = m.get('RegionIdList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeExpressConnectRouterRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        as_path: str = None,
        client_token: str = None,
        community: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
        nexthop_instance_id: str = None,
        query_region_id: str = None,
    ):
        # The Autonomous System (AS) path of the route.
        self.as_path = as_path
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The community value that is carried in the Border Gateway Protocol (BGP) route.
        self.community = community
        # The destination CIDR block of the route that you want to query.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the next-hop instance.
        self.nexthop_instance_id = nexthop_instance_id
        # The region ID of the ECR.
        self.query_region_id = query_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.community is not None:
            result['Community'] = self.community
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Community') is not None:
            self.community = m.get('Community')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')
        return self


class DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList(TeaModel):
    def __init__(
        self,
        as_path: str = None,
        community: str = None,
        destination_cidr_block: str = None,
        med: int = None,
        nexthop_instance_id: str = None,
        nexthop_instance_region_id: str = None,
        status: str = None,
    ):
        # The AS path of the route.
        self.as_path = as_path
        # The community value that is carried in the BGP route.
        self.community = community
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The MED value of the BGP route, which is used between the ECR and the transit router.
        # 
        # *   You can set the MED value to 2000. In this case, the transit router and the ECR are used as default paths.
        # *   If a non-default path is used, the MED value is empty.
        # *   You can set the MED value to 2000 only for one object associated with a transit router of a CEN instance.
        self.med = med
        # The ID of the next-hop instance.
        self.nexthop_instance_id = nexthop_instance_id
        # The region ID of the next-hop instance.
        self.nexthop_instance_region_id = nexthop_instance_region_id
        # The state of the ECR.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        if self.community is not None:
            result['Community'] = self.community
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.med is not None:
            result['Med'] = self.med
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        if self.nexthop_instance_region_id is not None:
            result['NexthopInstanceRegionId'] = self.nexthop_instance_region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        if m.get('Community') is not None:
            self.community = m.get('Community')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('Med') is not None:
            self.med = m.get('Med')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        if m.get('NexthopInstanceRegionId') is not None:
            self.nexthop_instance_region_id = m.get('NexthopInstanceRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        route_entries_list: List[DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 10
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The routes.
        self.route_entries_list = route_entries_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of route entries.
        self.total_count = total_count

    def validate(self):
        if self.route_entries_list:
            for k in self.route_entries_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RouteEntriesList'] = []
        if self.route_entries_list is not None:
            for k in self.route_entries_list:
                result['RouteEntriesList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.route_entries_list = []
        if m.get('RouteEntriesList') is not None:
            for k in m.get('RouteEntriesList'):
                temp_model = DescribeExpressConnectRouterRouteEntriesResponseBodyRouteEntriesList()
                self.route_entries_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExpressConnectRouterRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowLogsRequestTag(TeaModel):
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


class DescribeFlowLogsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        log_store_name: str = None,
        max_results: int = None,
        next_token: str = None,
        project_name: str = None,
        resource_group_id: str = None,
        tag: List[DescribeFlowLogsRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The flow log name. The name must be 0 to 128 characters in length.
        self.flow_log_name = flow_log_name
        # The ID of the VBR associated with the ECR.
        self.instance_id = instance_id
        # The Logstore that stores the captured traffic data.
        # 
        # *   If a Logstore is already created in the selected region, enter the name of the Logstore.
        # *   If no Logstores are created in the selected region, enter a name and the system automatically creates a Logstore. The name of the Logstore. The name must meet the following requirements:
        # *   The name must be unique in a project.
        # *   It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.log_store_name = log_store_name
        # The maximum number of entries to return. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # - You do not need to specify this parameter for the first request.
        # - You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The project that stores the captured traffic data.
        # 
        # *   If a project is already created in the selected region, enter the name of the project.
        # *   If no projects are created in the selected region, enter a name and the system automatically creates a project.
        # 
        # The project name must be unique in a region. You cannot change the name after the project is created. The name must meet the following requirements:
        # 
        # *   The name must be globally unique.
        # *   The name can contain only lowercase letters,
        # *   digits, and hyphens (-).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.project_name = project_name
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeFlowLogsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeFlowLogsResponseBodyFlowLogsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the instance. The tag key cannot be an empty string.
        # 
        # > It can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # > It can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`. The tag value can be an empty string.
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


class DescribeFlowLogsResponseBodyFlowLogs(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        interval: int = None,
        log_store_name: str = None,
        project_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sampling_rate: str = None,
        sls_region_id: str = None,
        status: str = None,
        tags: List[DescribeFlowLogsResponseBodyFlowLogsTags] = None,
    ):
        # The time when the flow log was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        self.creation_time = creation_time
        # The description of the flow log.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The name of the flow log.
        self.flow_log_name = flow_log_name
        # The ID of the network instance.
        self.instance_id = instance_id
        # The type of the network instance. Valid values:
        # 
        # - **VBR**: virtual border router (VBR)
        self.instance_type = instance_type
        # The time window for collecting log data. Unit: seconds. Valid values:
        # 
        # - **60**\
        # - **600**\
        # 
        # Default value: **600**.
        self.interval = interval
        # The Logstore that stores the captured traffic data.
        self.log_store_name = log_store_name
        # The name of the project that stores the captured traffic data.
        self.project_name = project_name
        # The region ID of the flow log.
        self.region_id = region_id
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The sampling proportion. Valid values:
        # 
        # - **1:4096**\
        # - **1:2048**\
        # - **1:1024**\
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        # The ID of the region where Log Service is deployed.
        self.sls_region_id = sls_region_id
        # The status of the flow log. Valid values:
        # 
        # *   **Active**\
        # 
        # *   **Inactive**\
        self.status = status
        # The tag key.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeFlowLogsResponseBodyFlowLogsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeFlowLogsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        flow_logs: List[DescribeFlowLogsResponseBodyFlowLogs] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The queried information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The information about the flow logs.
        self.flow_logs = flow_logs
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **True**\
        # - **False**\
        self.success = success
        # The total number of records that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.flow_logs:
            for k in self.flow_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['FlowLogs'] = []
        if self.flow_logs is not None:
            for k in self.flow_logs:
                result['FlowLogs'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.flow_logs = []
        if m.get('FlowLogs') is not None:
            for k in m.get('FlowLogs'):
                temp_model = DescribeFlowLogsResponseBodyFlowLogs()
                self.flow_logs.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeFlowLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeFlowLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceGrantedToExpressConnectRouterRequestTagModels(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.tag_key = tag_key
        # The tag value. You can specify up to 20 tag values. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeInstanceGrantedToExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        caller_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        instance_id: str = None,
        instance_owner_id: int = None,
        instance_region_id: str = None,
        instance_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tag_models: List[DescribeInstanceGrantedToExpressConnectRouterRequestTagModels] = None,
    ):
        # The type of the user account. Valid values:
        # 
        # *   **sub**: a Resource Access Management (RAM) user.
        # *   **parent**: an Alibaba Cloud account.
        self.caller_type = caller_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the network instance.
        self.instance_id = instance_id
        # The ID of the Alibaba Cloud account that owns the network instance.
        self.instance_owner_id = instance_owner_id
        # The region ID of the network instance.
        self.instance_region_id = instance_region_id
        # The type of the network instance. Valid values:
        # 
        # *   **VBR**\
        # *   **VPC**\
        self.instance_type = instance_type
        # The maximum number of entries to read. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the resource group to which the network instance belongs.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag_models = tag_models

    def validate(self):
        if self.tag_models:
            for k in self.tag_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['TagModels'] = []
        if self.tag_models is not None:
            for k in self.tag_models:
                result['TagModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag_models = []
        if m.get('TagModels') is not None:
            for k in m.get('TagModels'):
                temp_model = DescribeInstanceGrantedToExpressConnectRouterRequestTagModels()
                self.tag_models.append(temp_model.from_map(k))
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList(TeaModel):
    def __init__(
        self,
        ecr_id: str = None,
        ecr_owner_ali_uid: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grant_id: str = None,
        node_id: str = None,
        node_owner_bid: str = None,
        node_owner_uid: int = None,
        node_region_id: str = None,
        node_type: str = None,
        status: str = None,
    ):
        # The ECR ID.
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account that owns the ECR to which you want to grant permissions.
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        # The time when the network instance was created.
        self.gmt_create = gmt_create
        # The time when the network instance was modified.
        self.gmt_modified = gmt_modified
        # The authorization ID.
        self.grant_id = grant_id
        # The ID of the network instance.
        self.node_id = node_id
        # The ID of the Alibaba Cloud enterprise account that owns the network instance.
        self.node_owner_bid = node_owner_bid
        # The ID of the Alibaba Cloud account that owns the network instance.
        self.node_owner_uid = node_owner_uid
        # The region ID of the network instance.
        self.node_region_id = node_region_id
        # The type of the network instance. Valid values:
        # 
        # *   **VBR**\
        # *   **VPC**\
        self.node_type = node_type
        # The state of the network instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.grant_id is not None:
            result['GrantId'] = self.grant_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_owner_bid is not None:
            result['NodeOwnerBid'] = self.node_owner_bid
        if self.node_owner_uid is not None:
            result['NodeOwnerUid'] = self.node_owner_uid
        if self.node_region_id is not None:
            result['NodeRegionId'] = self.node_region_id
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GrantId') is not None:
            self.grant_id = m.get('GrantId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeOwnerBid') is not None:
            self.node_owner_bid = m.get('NodeOwnerBid')
        if m.get('NodeOwnerUid') is not None:
            self.node_owner_uid = m.get('NodeOwnerUid')
        if m.get('NodeRegionId') is not None:
            self.node_region_id = m.get('NodeRegionId')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_granted_instance_list: List[DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The network instances whose permissions are granted to the ECR.
        self.ecr_granted_instance_list = ecr_granted_instance_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The total number of network instances whose permissions are granted to the ECR.
        self.total_count = total_count

    def validate(self):
        if self.ecr_granted_instance_list:
            for k in self.ecr_granted_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['EcrGrantedInstanceList'] = []
        if self.ecr_granted_instance_list is not None:
            for k in self.ecr_granted_instance_list:
                result['EcrGrantedInstanceList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.ecr_granted_instance_list = []
        if m.get('EcrGrantedInstanceList') is not None:
            for k in m.get('EcrGrantedInstanceList'):
                temp_model = DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList()
                self.ecr_granted_instance_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstanceGrantedToExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceGrantedToExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeInstanceGrantedToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(
        self,
        child_instance_id: str = None,
        child_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The VBR ID.
        # 
        # This parameter is required.
        self.child_instance_id = child_instance_id
        # The type of the network instance. Set the value to **VBR**.
        # 
        # This parameter is required.
        self.child_instance_type = child_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class DetachExpressConnectRouterChildInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetachExpressConnectRouterChildInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachExpressConnectRouterChildInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DetachExpressConnectRouterChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        nexthop_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The destination CIDR block of the route entry in the route table of the ECR.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the next-hop instance.
        # 
        # This parameter is required.
        self.nexthop_instance_id = nexthop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        return self


class DisableExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableExpressConnectRouterRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DisableExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        destination_cidr_block: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        nexthop_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The destination CIDR block of the route entry in the route table of the ECR.
        # 
        # This parameter is required.
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the next-hop instance.
        # 
        # This parameter is required.
        self.nexthop_instance_id = nexthop_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.nexthop_instance_id is not None:
            result['NexthopInstanceId'] = self.nexthop_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('NexthopInstanceId') is not None:
            self.nexthop_instance_id = m.get('NexthopInstanceId')
        return self


class EnableExpressConnectRouterRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableExpressConnectRouterRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableExpressConnectRouterRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = EnableExpressConnectRouterRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForceDeleteExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class ForceDeleteExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ForceDeleteExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ForceDeleteExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ForceDeleteExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantInstanceToExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        ecr_owner_ali_uid: int = None,
        instance_id: str = None,
        instance_region_id: str = None,
        instance_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account that owns the ECR to which you want to grant permissions.
        # 
        # This parameter is required.
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        # The ID of the network instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the network instance.
        # 
        # This parameter is required.
        self.instance_region_id = instance_region_id
        # The type of the network instance. Valid values:
        # 
        # *   **VBR**\
        # *   **VPC**\
        # 
        # This parameter is required.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class GrantInstanceToExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantInstanceToExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantInstanceToExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GrantInstanceToExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExpressConnectRouterSupportedRegionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        node_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The type of the network instance. Valid values:
        # 
        # *   **TR**\
        # *   **VBR**\
        # *   **VPC**\
        # 
        # This parameter is required.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class ListExpressConnectRouterSupportedRegionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        supported_region_id_list: List[str] = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   True
        # *   False
        self.success = success
        # The regions in which the ECR feature is activated.
        self.supported_region_id_list = supported_region_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.supported_region_id_list is not None:
            result['SupportedRegionIdList'] = self.supported_region_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SupportedRegionIdList') is not None:
            self.supported_region_id_list = m.get('SupportedRegionIdList')
        return self


class ListExpressConnectRouterSupportedRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExpressConnectRouterSupportedRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListExpressConnectRouterSupportedRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys in each call.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`. The tag value can be an empty string.
        # 
        # You can specify up to 20 tag values in each call.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The maximum number of entries to return for a single request. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ECR IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to EXPRESSCONNECTROUTER.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag.
        # 
        # You can specify at most 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
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
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. The value is **EXPRESSCONNECTROUTER**.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The number of entries per page.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success
        # The tags.
        self.tag_resources = tag_resources
        # The total number of records that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the ECR.
        # 
        # >  The description can be empty or 0 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The name of the ECR.
        # 
        # >  The name must be 0 to 128 characters in length, and cannot start with http:// or https://.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixRequest(TeaModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        owner_account: str = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The route prefix mode.
        # 
        # *   MatchMode: After you distribute new route CIDR blocks to data centers, original specific routes that are distributed are withdrawn.
        # *   IncrementalMode: After you distribute new route CIDR blocks to data centers, the original specific routes that fall in the CIDR blocks that you configure are withdrawn, and the original specific routes that do not fall in the CIDR blocks are still distributed.
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The ID of the association between the ECR and the VPC or TR.
        # 
        # This parameter is required.
        self.association_id = association_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        self.owner_account = owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes
        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')
        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterAssociationAllowedPrefixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyExpressConnectRouterAssociationAllowedPrefixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList(TeaModel):
    def __init__(
        self,
        mode: str = None,
        region_id: str = None,
    ):
        # The cross-domain forwarding mode of the ECR. Valid values:
        # 
        # *   **ECMP**: the load balancing mode.
        # *   **NearBy**: the nearby forwarding mode.
        self.mode = mode
        # The region ID of the ECR.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyExpressConnectRouterInterRegionTransitModeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        transit_mode_list: List[ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The cross-region forwarding modes.
        self.transit_mode_list = transit_mode_list

    def validate(self):
        if self.transit_mode_list:
            for k in self.transit_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        result['TransitModeList'] = []
        if self.transit_mode_list is not None:
            for k in self.transit_mode_list:
                result['TransitModeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        self.transit_mode_list = []
        if m.get('TransitModeList') is not None:
            for k in m.get('TransitModeList'):
                temp_model = ModifyExpressConnectRouterInterRegionTransitModeRequestTransitModeList()
                self.transit_mode_list.append(temp_model.from_map(k))
        return self


class ModifyExpressConnectRouterInterRegionTransitModeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyExpressConnectRouterInterRegionTransitModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyExpressConnectRouterInterRegionTransitModeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyExpressConnectRouterInterRegionTransitModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowLogAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        interval: int = None,
        sampling_rate: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the flow log.
        # The description can be empty or 0 to 256 characters in length.
        self.description = description
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        # 
        # This parameter is required.
        self.flow_log_id = flow_log_id
        # The new name of the flow log. The name must be 0 to 128 characters in length.
        self.flow_log_name = flow_log_name
        # The time window for collecting log data. Unit: seconds. Valid values:
        # 
        # - **60**\
        # - **600**\
        # 
        # Default value: **600**.
        self.interval = interval
        # The sampling proportion. Valid values:
        # 
        # - **1:4096**\
        # - **1:2048**\
        # - **1:1024**\
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')
        return self


class ModifyFlowLogAttributeResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether routes are disabled by the ECR. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyFlowLogAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFlowLogAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyFlowLogAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the new resource group. For more information about resource groups, see the "Resource Group" section of the [What is Resource Management?](https://help.aliyun.com/document_detail/94475.html) topic.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The ECR ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to EXPRESSCONNECTROUTER.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeInstanceFromExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        ecr_owner_ali_uid: int = None,
        instance_id: str = None,
        instance_region_id: str = None,
        instance_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account that owns the ECR from which you want to revoke permissions.
        # 
        # This parameter is required.
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        # The ID of the network instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the network instance.
        # 
        # This parameter is required.
        self.instance_region_id = instance_region_id
        # The type of the network instance. Valid values:
        # 
        # *   **VBR**\
        # *   **VPC**\
        # 
        # This parameter is required.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class RevokeInstanceFromExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokeInstanceFromExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeInstanceFromExpressConnectRouterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RevokeInstanceFromExpressConnectRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR ID.
        # 
        # This parameter is required.
        self.ecr_id = ecr_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsInstanceId**, the request parameter **DtsInstanceId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SynchronizeExpressConnectRouterInterRegionBandwidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SynchronizeExpressConnectRouterInterRegionBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys in each call.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`. The tag value can be an empty string.
        # 
        # You can add up to 20 tag values in each call.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to **EXPRESSCONNECTROUTER**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags to be added.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags. This parameter is valid only when the **TagKey** parameter is not specified. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        # 
        # >  You must specify one of **TagKey** and **All**.
        self.all = all
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run.
        # *   **false** (default): performs a dry run and performs the actual request.
        self.dry_run = dry_run
        # The ECR IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Set the value to **EXPRESSCONNECTROUTER**.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of the tags that you want to remove from the ECRs.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


