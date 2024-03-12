# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AttachExpressConnectRouterChildInstanceRequest(TeaModel):
    def __init__(
        self,
        child_instance_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        self.child_instance_id = child_instance_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_type = child_instance_type
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
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
        self.access_denied_detail = access_denied_detail
        self.any_cross_border_link = any_cross_border_link
        self.any_inter_region_link = any_inter_region_link
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.is_cdt_cross_border_enabled = is_cdt_cross_border_enabled
        self.is_cdt_inter_region_enabled = is_cdt_inter_region_enabled
        self.is_user_allowed_to_create_cross_border_link = is_user_allowed_to_create_cross_border_link
        self.message = message
        self.request_id = request_id
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


class CreateExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        alibaba_side_asn: int = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        name: str = None,
        resource_group_id: str = None,
    ):
        self.alibaba_side_asn = alibaba_side_asn
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.name = name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.ecr_id = ecr_id
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        association_region_id: str = None,
        cen_id: str = None,
        client_token: str = None,
        create_attachment: bool = None,
        dry_run: bool = None,
        ecr_id: str = None,
        transit_router_id: str = None,
        transit_router_owner_id: int = None,
        vpc_id: str = None,
        vpc_owner_id: int = None,
    ):
        self.allowed_prefixes = allowed_prefixes
        self.association_region_id = association_region_id
        self.cen_id = cen_id
        self.client_token = client_token
        self.create_attachment = create_attachment
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.transit_router_id = transit_router_id
        self.transit_router_owner_id = transit_router_owner_id
        self.vpc_id = vpc_id
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
        if self.association_region_id is not None:
            result['AssociationRegionId'] = self.association_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.create_attachment is not None:
            result['CreateAttachment'] = self.create_attachment
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
        if m.get('AssociationRegionId') is not None:
            self.association_region_id = m.get('AssociationRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CreateAttachment') is not None:
            self.create_attachment = m.get('CreateAttachment')
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
        self.access_denied_detail = access_denied_detail
        self.association_id = association_id
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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


class DeleteExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.association_id = association_id
        self.client_token = client_token
        self.delete_attachment = delete_attachment
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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


class DescribeDisabledExpressConnectRouterRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.max_results = max_results
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
        self.destination_cidr_block = destination_cidr_block
        self.ecr_id = ecr_id
        self.gmt_create = gmt_create
        self.nexthop_instance_id = nexthop_instance_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.disabled_route_entry_list = disabled_route_entry_list
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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


class DescribeExpressConnectRouterRequestTagModels(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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
        tag_models: List[DescribeExpressConnectRouterRequestTagModels] = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.resource_group_id = resource_group_id
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
        result['TagModels'] = []
        if self.tag_models is not None:
            for k in self.tag_models:
                result['TagModels'].append(k.to_map() if k else None)
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
        self.tag_models = []
        if m.get('TagModels') is not None:
            for k in m.get('TagModels'):
                temp_model = DescribeExpressConnectRouterRequestTagModels()
                self.tag_models.append(temp_model.from_map(k))
        return self


class DescribeExpressConnectRouterResponseBodyEcrListTags(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        category: int = None,
        id: int = None,
        region_no: str = None,
        resource_id: str = None,
        resuorce_type: str = None,
        scope: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.ali_uid = ali_uid
        self.category = category
        self.id = id
        self.region_no = region_no
        self.resource_id = resource_id
        self.resuorce_type = resuorce_type
        self.scope = scope
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resuorce_type is not None:
            result['ResuorceType'] = self.resuorce_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResuorceType') is not None:
            self.resuorce_type = m.get('ResuorceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
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
        self.alibaba_side_asn = alibaba_side_asn
        self.biz_status = biz_status
        self.description = description
        self.ecr_id = ecr_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.owner_id = owner_id
        self.resource_group_id = resource_group_id
        self.status = status
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.ecr_list = ecr_list
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        associaton_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.associaton_id = associaton_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associaton_id is not None:
            result['AssociatonId'] = self.associaton_id
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
        if m.get('AssociatonId') is not None:
            self.associaton_id = m.get('AssociatonId')
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
        self.allowed_prefix = allowed_prefix
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
        self.access_denied_detail = access_denied_detail
        self.allowed_prefix_history_list = allowed_prefix_history_list
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.association_id = association_id
        self.association_node_type = association_node_type
        self.association_region_id = association_region_id
        self.cen_id = cen_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.max_results = max_results
        self.next_token = next_token
        self.transit_router_id = transit_router_id
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
        association_id: str = None,
        association_node_type: str = None,
        cen_id: str = None,
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
        self.allowed_prefixes = allowed_prefixes
        self.association_id = association_id
        self.association_node_type = association_node_type
        self.cen_id = cen_id
        self.ecr_id = ecr_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.region_id = region_id
        self.status = status
        self.transit_router_id = transit_router_id
        self.transit_router_owner_id = transit_router_owner_id
        self.vpc_id = vpc_id
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
        if self.association_id is not None:
            result['AssociationId'] = self.association_id
        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
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
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')
        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
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
        self.access_denied_detail = access_denied_detail
        self.association_list = association_list
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        self.association_id = association_id
        self.child_instance_id = child_instance_id
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_type = child_instance_type
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.max_results = max_results
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
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: int = None,
        region_id: str = None,
        status: str = None,
    ):
        self.association_id = association_id
        self.child_instance_id = child_instance_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_type = child_instance_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.region_id = region_id
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
        self.access_denied_detail = access_denied_detail
        self.child_instance_list = child_instance_list
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.mode = mode
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.inter_region_transit_mode_list = inter_region_transit_mode_list
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.region_id_list = region_id_list
        self.request_id = request_id
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
        self.as_path = as_path
        self.client_token = client_token
        self.community = community
        self.destination_cidr_block = destination_cidr_block
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.max_results = max_results
        self.next_token = next_token
        self.nexthop_instance_id = nexthop_instance_id
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
        nexthop_instance_id: str = None,
        nexthop_instance_region_id: str = None,
        status: str = None,
    ):
        self.as_path = as_path
        self.community = community
        self.destination_cidr_block = destination_cidr_block
        self.nexthop_instance_id = nexthop_instance_id
        self.nexthop_instance_region_id = nexthop_instance_region_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.route_entries_list = route_entries_list
        self.success = success
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


class DescribeInstanceGrantedToExpressConnectRouterRequestTagModels(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
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
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.instance_id = instance_id
        self.instance_owner_id = instance_owner_id
        self.instance_region_id = instance_region_id
        self.instance_type = instance_type
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id
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
        self.ecr_id = ecr_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grant_id = grant_id
        self.node_id = node_id
        self.node_owner_bid = node_owner_bid
        self.node_owner_uid = node_owner_uid
        self.node_region_id = node_region_id
        self.node_type = node_type
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.ecr_granted_instance_list = ecr_granted_instance_list
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.destination_cidr_block = destination_cidr_block
        self.dry_run = dry_run
        self.ecr_id = ecr_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.destination_cidr_block = destination_cidr_block
        self.dry_run = dry_run
        self.ecr_id = ecr_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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


class GetExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
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


class GetExpressConnectRouterResponseBodyTags(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        category: int = None,
        id: int = None,
        region_no: str = None,
        resource_id: str = None,
        resuorce_type: str = None,
        scope: int = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.ali_uid = ali_uid
        self.category = category
        self.id = id
        self.region_no = region_no
        self.resource_id = resource_id
        self.resuorce_type = resuorce_type
        self.scope = scope
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resuorce_type is not None:
            result['ResuorceType'] = self.resuorce_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResuorceType') is not None:
            self.resuorce_type = m.get('ResuorceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetExpressConnectRouterResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        alibaba_side_asn: int = None,
        biz_status: str = None,
        code: str = None,
        description: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        http_status_code: int = None,
        message: str = None,
        name: str = None,
        owner_id: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        success: bool = None,
        tags: List[GetExpressConnectRouterResponseBodyTags] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.alibaba_side_asn = alibaba_side_asn
        self.biz_status = biz_status
        self.code = code
        self.description = description
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.ecr_id = ecr_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.http_status_code = http_status_code
        self.message = message
        self.name = name
        self.owner_id = owner_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.success = success
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetExpressConnectRouterResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetExpressConnectRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExpressConnectRouterResponseBody = None,
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
            temp_model = GetExpressConnectRouterResponseBody()
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
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        self.instance_id = instance_id
        self.instance_region_id = instance_region_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
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
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
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


class ModifyExpressConnectRouterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.ecr_id = ecr_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        association_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ecr_id: str = None,
        owner_account: str = None,
    ):
        self.allowed_prefixes = allowed_prefixes
        self.association_id = association_id
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.mode = mode
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
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.dry_run = dry_run
        self.ecr_id = ecr_id
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        self.instance_id = instance_id
        self.instance_region_id = instance_region_id
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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
        self.client_token = client_token
        self.dry_run = dry_run
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
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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


