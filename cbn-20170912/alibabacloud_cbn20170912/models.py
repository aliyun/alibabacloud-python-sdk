# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActiveFlowLogRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        flow_log_id: str = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.flow_log_id = flow_log_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class ActiveFlowLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActiveFlowLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActiveFlowLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActiveFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateCenBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_bandwidth_package_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class AssociateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateCenBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateCenBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCenChildInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_owner_id = child_instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        return self


class AttachCenChildInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCenChildInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachCenChildInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachCenChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        name: str = None,
        description: str = None,
        protection_level: str = None,
        ipv_6level: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.protection_level = protection_level
        self.ipv_6level = ipv_6level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        return self


class CreateCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cen_id: str = None,
    ):
        self.request_id = request_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class CreateCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        name: str = None,
        description: str = None,
        bandwidth: int = None,
        geographic_region_aid: str = None,
        geographic_region_bid: str = None,
        bandwidth_package_charge_type: str = None,
        period: int = None,
        pricing_cycle: str = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.bandwidth = bandwidth
        self.geographic_region_aid = geographic_region_aid
        self.geographic_region_bid = geographic_region_bid
        self.bandwidth_package_charge_type = bandwidth_package_charge_type
        self.period = period
        self.pricing_cycle = pricing_cycle
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.auto_renew_duration = auto_renew_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')
        return self


class CreateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cen_bandwidth_package_id: str = None,
        cen_bandwidth_package_order_id: str = None,
    ):
        self.request_id = request_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.cen_bandwidth_package_order_id = cen_bandwidth_package_order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_bandwidth_package_order_id is not None:
            result['CenBandwidthPackageOrderId'] = self.cen_bandwidth_package_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenBandwidthPackageOrderId') is not None:
            self.cen_bandwidth_package_order_id = m.get('CenBandwidthPackageOrderId')
        return self


class CreateCenBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCenBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenChildInstanceRouteEntryToCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_ali_uid: int = None,
        route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_ali_uid = child_instance_ali_uid
        self.route_table_id = route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_ali_uid is not None:
            result['ChildInstanceAliUid'] = self.child_instance_ali_uid
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceAliUid') is not None:
            self.child_instance_ali_uid = m.get('ChildInstanceAliUid')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class CreateCenChildInstanceRouteEntryToCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCenChildInstanceRouteEntryToCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCenChildInstanceRouteEntryToCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCenChildInstanceRouteEntryToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCenRouteMapRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_region_id: str = None,
        transmit_direction: str = None,
        description: str = None,
        priority: int = None,
        map_result: str = None,
        next_priority: int = None,
        cidr_match_mode: str = None,
        as_path_match_mode: str = None,
        community_match_mode: str = None,
        community_operate_mode: str = None,
        preference: int = None,
        source_instance_ids_reverse_match: bool = None,
        destination_instance_ids_reverse_match: bool = None,
        gateway_zone_id: str = None,
        system_policy: bool = None,
        match_address_type: str = None,
        source_instance_ids: List[str] = None,
        destination_instance_ids: List[str] = None,
        source_route_table_ids: List[str] = None,
        destination_route_table_ids: List[str] = None,
        source_region_ids: List[str] = None,
        source_child_instance_types: List[str] = None,
        destination_child_instance_types: List[str] = None,
        destination_cidr_blocks: List[str] = None,
        route_types: List[str] = None,
        match_asns: List[int] = None,
        match_community_set: List[str] = None,
        operate_community_set: List[str] = None,
        prepend_as_path: List[int] = None,
        destination_region_ids: List[str] = None,
        source_zone_ids: List[str] = None,
        original_route_table_ids: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_region_id = cen_region_id
        self.transmit_direction = transmit_direction
        self.description = description
        self.priority = priority
        self.map_result = map_result
        self.next_priority = next_priority
        self.cidr_match_mode = cidr_match_mode
        self.as_path_match_mode = as_path_match_mode
        self.community_match_mode = community_match_mode
        self.community_operate_mode = community_operate_mode
        self.preference = preference
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        self.gateway_zone_id = gateway_zone_id
        self.system_policy = system_policy
        self.match_address_type = match_address_type
        self.source_instance_ids = source_instance_ids
        self.destination_instance_ids = destination_instance_ids
        self.source_route_table_ids = source_route_table_ids
        self.destination_route_table_ids = destination_route_table_ids
        self.source_region_ids = source_region_ids
        self.source_child_instance_types = source_child_instance_types
        self.destination_child_instance_types = destination_child_instance_types
        self.destination_cidr_blocks = destination_cidr_blocks
        self.route_types = route_types
        self.match_asns = match_asns
        self.match_community_set = match_community_set
        self.operate_community_set = operate_community_set
        self.prepend_as_path = prepend_as_path
        self.destination_region_ids = destination_region_ids
        self.source_zone_ids = source_zone_ids
        self.original_route_table_ids = original_route_table_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        if self.description is not None:
            result['Description'] = self.description
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.gateway_zone_id is not None:
            result['GatewayZoneId'] = self.gateway_zone_id
        if self.system_policy is not None:
            result['SystemPolicy'] = self.system_policy
        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path
        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids
        if self.source_zone_ids is not None:
            result['SourceZoneIds'] = self.source_zone_ids
        if self.original_route_table_ids is not None:
            result['OriginalRouteTableIds'] = self.original_route_table_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('GatewayZoneId') is not None:
            self.gateway_zone_id = m.get('GatewayZoneId')
        if m.get('SystemPolicy') is not None:
            self.system_policy = m.get('SystemPolicy')
        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')
        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')
        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')
        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')
        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')
        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')
        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')
        if m.get('DestinationChildInstanceTypes') is not None:
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')
        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')
        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')
        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')
        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')
        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')
        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')
        if m.get('SourceZoneIds') is not None:
            self.source_zone_ids = m.get('SourceZoneIds')
        if m.get('OriginalRouteTableIds') is not None:
            self.original_route_table_ids = m.get('OriginalRouteTableIds')
        return self


class CreateCenRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        route_map_id: str = None,
    ):
        self.request_id = request_id
        self.route_map_id = route_map_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class CreateCenRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCenRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowlogRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        flow_log_name: str = None,
        description: str = None,
        cen_id: str = None,
        project_name: str = None,
        log_store_name: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.flow_log_name = flow_log_name
        self.description = description
        self.cen_id = cen_id
        self.project_name = project_name
        self.log_store_name = log_store_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        return self


class CreateFlowlogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_log_id: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.flow_log_id = flow_log_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateFlowlogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowlogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFlowlogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeactiveFlowLogRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        flow_log_id: str = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.flow_log_id = flow_log_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DeactiveFlowLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeactiveFlowLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeactiveFlowLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeactiveFlowLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DeleteCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_bandwidth_package_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class DeleteCenBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCenBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCenBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenChildInstanceRouteEntryToCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_ali_uid: int = None,
        route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_ali_uid = child_instance_ali_uid
        self.route_table_id = route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_ali_uid is not None:
            result['ChildInstanceAliUid'] = self.child_instance_ali_uid
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceAliUid') is not None:
            self.child_instance_ali_uid = m.get('ChildInstanceAliUid')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DeleteCenChildInstanceRouteEntryToCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCenChildInstanceRouteEntryToCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCenChildInstanceRouteEntryToCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCenChildInstanceRouteEntryToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCenRouteMapRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_region_id: str = None,
        route_map_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_region_id = cen_region_id
        self.route_map_id = route_map_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        return self


class DeleteCenRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCenRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCenRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowlogRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        flow_log_id: str = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.flow_log_id = flow_log_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DeleteFlowlogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFlowlogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlowlogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFlowlogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRouteServiceInCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        host: str = None,
        host_region_id: str = None,
        access_region_id: str = None,
        host_vpc_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.host = host
        self.host_region_id = host_region_id
        self.access_region_id = access_region_id
        self.host_vpc_id = host_vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        return self


class DeleteRouteServiceInCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRouteServiceInCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRouteServiceInCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRouteServiceInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenAttachedChildInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        include_route_table: bool = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.include_route_table = include_route_table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.include_route_table is not None:
            result['IncludeRouteTable'] = self.include_route_table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('IncludeRouteTable') is not None:
            self.include_route_table = m.get('IncludeRouteTable')
        return self


class DescribeCenAttachedChildInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        child_instance_type: str = None,
        request_id: str = None,
        cen_id: str = None,
        child_instance_attach_time: str = None,
        child_instance_owner_id: int = None,
        child_instance_name: str = None,
        child_instance_id: str = None,
        child_instance_region_id: str = None,
    ):
        self.status = status
        self.child_instance_type = child_instance_type
        self.request_id = request_id
        self.cen_id = cen_id
        self.child_instance_attach_time = child_instance_attach_time
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_name = child_instance_name
        self.child_instance_id = child_instance_id
        self.child_instance_region_id = child_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_name is not None:
            result['ChildInstanceName'] = self.child_instance_name
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceName') is not None:
            self.child_instance_name = m.get('ChildInstanceName')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        return self


class DescribeCenAttachedChildInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenAttachedChildInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenAttachedChildInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenAttachedChildInstancesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        return self


class DescribeCenAttachedChildInstancesResponseBodyChildInstances(TeaModel):
    def __init__(
        self,
        child_instance_type: str = None,
        status: str = None,
        child_instance_region_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_id: str = None,
        cen_id: str = None,
        child_instance_attach_time: str = None,
    ):
        self.child_instance_type = child_instance_type
        self.status = status
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_id = child_instance_id
        self.cen_id = cen_id
        self.child_instance_attach_time = child_instance_attach_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.status is not None:
            result['Status'] = self.status
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')
        return self


class DescribeCenAttachedChildInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        child_instances: List[DescribeCenAttachedChildInstancesResponseBodyChildInstances] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.child_instances = child_instances

    def validate(self):
        if self.child_instances:
            for k in self.child_instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['ChildInstances'] = []
        if self.child_instances is not None:
            for k in self.child_instances:
                result['ChildInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.child_instances = []
        if m.get('ChildInstances') is not None:
            for k in m.get('ChildInstances'):
                temp_model = DescribeCenAttachedChildInstancesResponseBodyChildInstances()
                self.child_instances.append(temp_model.from_map(k))
        return self


class DescribeCenAttachedChildInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenAttachedChildInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenAttachedChildInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenBandwidthPackagesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class DescribeCenBandwidthPackagesRequest(TeaModel):
    def __init__(
        self,
        include_reservation_data: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        is_or_key: bool = None,
        filter: List[DescribeCenBandwidthPackagesRequestFilter] = None,
    ):
        self.include_reservation_data = include_reservation_data
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.is_or_key = is_or_key
        self.filter = filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_or_key is not None:
            result['IsOrKey'] = self.is_or_key
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsOrKey') is not None:
            self.is_or_key = m.get('IsOrKey')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeCenBandwidthPackagesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesOrginInterRegionBandwidthLimits(TeaModel):
    def __init__(
        self,
        opposite_region_id: str = None,
        geographic_span_id: str = None,
        local_region_id: str = None,
        bandwidth_limit: str = None,
    ):
        self.opposite_region_id = opposite_region_id
        self.geographic_span_id = geographic_span_id
        self.local_region_id = local_region_id
        self.bandwidth_limit = bandwidth_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        status: str = None,
        reservation_active_time: str = None,
        reservation_order_type: str = None,
        bandwidth_package_charge_type: str = None,
        cen_bandwidth_package_id: str = None,
        orgin_inter_region_bandwidth_limits: List[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesOrginInterRegionBandwidthLimits] = None,
        cen_ids: List[str] = None,
        geographic_region_aid: str = None,
        ratio: str = None,
        reservation_internet_charge_type: str = None,
        type_for_95: str = None,
        bandwidth: int = None,
        description: str = None,
        expired_time: str = None,
        reservation_bandwidth: str = None,
        geographic_span_id: str = None,
        geographic_region_bid: str = None,
        is_cross_border: bool = None,
        business_status: str = None,
        name: str = None,
        has_reservation_data: str = None,
    ):
        self.creation_time = creation_time
        self.status = status
        self.reservation_active_time = reservation_active_time
        self.reservation_order_type = reservation_order_type
        self.bandwidth_package_charge_type = bandwidth_package_charge_type
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.orgin_inter_region_bandwidth_limits = orgin_inter_region_bandwidth_limits
        self.cen_ids = cen_ids
        self.geographic_region_aid = geographic_region_aid
        self.ratio = ratio
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.type_for_95 = type_for_95
        self.bandwidth = bandwidth
        self.description = description
        self.expired_time = expired_time
        self.reservation_bandwidth = reservation_bandwidth
        self.geographic_span_id = geographic_span_id
        self.geographic_region_bid = geographic_region_bid
        self.is_cross_border = is_cross_border
        self.business_status = business_status
        self.name = name
        self.has_reservation_data = has_reservation_data

    def validate(self):
        if self.orgin_inter_region_bandwidth_limits:
            for k in self.orgin_inter_region_bandwidth_limits:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.status is not None:
            result['Status'] = self.status
        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time
        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type
        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        result['OrginInterRegionBandwidthLimits'] = []
        if self.orgin_inter_region_bandwidth_limits is not None:
            for k in self.orgin_inter_region_bandwidth_limits:
                result['OrginInterRegionBandwidthLimits'].append(k.to_map() if k else None)
        if self.cen_ids is not None:
            result['CenIds'] = self.cen_ids
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        if self.type_for_95 is not None:
            result['TypeFor95'] = self.type_for_95
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.reservation_bandwidth is not None:
            result['ReservationBandwidth'] = self.reservation_bandwidth
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        if self.is_cross_border is not None:
            result['IsCrossBorder'] = self.is_cross_border
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.name is not None:
            result['Name'] = self.name
        if self.has_reservation_data is not None:
            result['HasReservationData'] = self.has_reservation_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')
        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')
        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        self.orgin_inter_region_bandwidth_limits = []
        if m.get('OrginInterRegionBandwidthLimits') is not None:
            for k in m.get('OrginInterRegionBandwidthLimits'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesOrginInterRegionBandwidthLimits()
                self.orgin_inter_region_bandwidth_limits.append(temp_model.from_map(k))
        if m.get('CenIds') is not None:
            self.cen_ids = m.get('CenIds')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')
        if m.get('TypeFor95') is not None:
            self.type_for_95 = m.get('TypeFor95')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ReservationBandwidth') is not None:
            self.reservation_bandwidth = m.get('ReservationBandwidth')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        if m.get('IsCrossBorder') is not None:
            self.is_cross_border = m.get('IsCrossBorder')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('HasReservationData') is not None:
            self.has_reservation_data = m.get('HasReservationData')
        return self


class DescribeCenBandwidthPackagesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        cen_bandwidth_packages: List[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.cen_bandwidth_packages = cen_bandwidth_packages

    def validate(self):
        if self.cen_bandwidth_packages:
            for k in self.cen_bandwidth_packages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['CenBandwidthPackages'] = []
        if self.cen_bandwidth_packages is not None:
            for k in self.cen_bandwidth_packages:
                result['CenBandwidthPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.cen_bandwidth_packages = []
        if m.get('CenBandwidthPackages') is not None:
            for k in m.get('CenBandwidthPackages'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages()
                self.cen_bandwidth_packages.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenBandwidthPackagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenChildInstanceRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        status: str = None,
        page_number: int = None,
        page_size: int = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.status = status
        self.page_number = page_number
        self.page_size = page_size
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_route_table_id = child_instance_route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesConflicts(TeaModel):
    def __init__(
        self,
        status: str = None,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.destination_cidr_block = destination_cidr_block
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords(TeaModel):
    def __init__(
        self,
        route_map_id: str = None,
        region_id: str = None,
    ):
        self.route_map_id = route_map_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        publish_status: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        next_hop_region_id: str = None,
        next_hop_instance_id: str = None,
        route_table_id: str = None,
        as_paths: List[str] = None,
        conflicts: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesConflicts] = None,
        communities: List[str] = None,
        destination_cidr_block: str = None,
        cen_route_map_records: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords] = None,
    ):
        self.status = status
        self.type = type
        self.publish_status = publish_status
        self.next_hop_type = next_hop_type
        self.operational_mode = operational_mode
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_instance_id = next_hop_instance_id
        self.route_table_id = route_table_id
        self.as_paths = as_paths
        self.conflicts = conflicts
        self.communities = communities
        self.destination_cidr_block = destination_cidr_block
        self.cen_route_map_records = cen_route_map_records

    def validate(self):
        if self.conflicts:
            for k in self.conflicts:
                if k:
                    k.validate()
        if self.cen_route_map_records:
            for k in self.cen_route_map_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode
        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths
        result['Conflicts'] = []
        if self.conflicts is not None:
            for k in self.conflicts:
                result['Conflicts'].append(k.to_map() if k else None)
        if self.communities is not None:
            result['Communities'] = self.communities
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        result['CenRouteMapRecords'] = []
        if self.cen_route_map_records is not None:
            for k in self.cen_route_map_records:
                result['CenRouteMapRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')
        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('AsPaths') is not None:
            self.as_paths = m.get('AsPaths')
        self.conflicts = []
        if m.get('Conflicts') is not None:
            for k in m.get('Conflicts'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesConflicts()
                self.conflicts.append(temp_model.from_map(k))
        if m.get('Communities') is not None:
            self.communities = m.get('Communities')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        self.cen_route_map_records = []
        if m.get('CenRouteMapRecords') is not None:
            for k in m.get('CenRouteMapRecords'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords()
                self.cen_route_map_records.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        cen_route_entries: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.cen_route_entries = cen_route_entries

    def validate(self):
        if self.cen_route_entries:
            for k in self.cen_route_entries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['CenRouteEntries'] = []
        if self.cen_route_entries is not None:
            for k in self.cen_route_entries:
                result['CenRouteEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.cen_route_entries = []
        if m.get('CenRouteEntries') is not None:
            for k in m.get('CenRouteEntries'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries()
                self.cen_route_entries.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenChildInstanceRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenGeographicSpanRemainingBandwidthRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        geographic_region_aid: str = None,
        geographic_region_bid: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.geographic_region_aid = geographic_region_aid
        self.geographic_region_bid = geographic_region_bid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
        if self.geographic_region_bid is not None:
            result['GeographicRegionBId'] = self.geographic_region_bid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
        if m.get('GeographicRegionBId') is not None:
            self.geographic_region_bid = m.get('GeographicRegionBId')
        return self


class DescribeCenGeographicSpanRemainingBandwidthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        remaining_bandwidth: int = None,
    ):
        self.request_id = request_id
        self.remaining_bandwidth = remaining_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remaining_bandwidth is not None:
            result['RemainingBandwidth'] = self.remaining_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RemainingBandwidth') is not None:
            self.remaining_bandwidth = m.get('RemainingBandwidth')
        return self


class DescribeCenGeographicSpanRemainingBandwidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenGeographicSpanRemainingBandwidthResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenGeographicSpanRemainingBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenGeographicSpansRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        geographic_span_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.geographic_span_id = geographic_span_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        return self


class DescribeCenGeographicSpansResponseBodyGeographicSpanModels(TeaModel):
    def __init__(
        self,
        geographic_span_id: str = None,
        opposite_geo_region_id: str = None,
        local_geo_region_id: str = None,
    ):
        self.geographic_span_id = geographic_span_id
        self.opposite_geo_region_id = opposite_geo_region_id
        self.local_geo_region_id = local_geo_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.opposite_geo_region_id is not None:
            result['OppositeGeoRegionId'] = self.opposite_geo_region_id
        if self.local_geo_region_id is not None:
            result['LocalGeoRegionId'] = self.local_geo_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('OppositeGeoRegionId') is not None:
            self.opposite_geo_region_id = m.get('OppositeGeoRegionId')
        if m.get('LocalGeoRegionId') is not None:
            self.local_geo_region_id = m.get('LocalGeoRegionId')
        return self


class DescribeCenGeographicSpansResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        geographic_span_models: List[DescribeCenGeographicSpansResponseBodyGeographicSpanModels] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.geographic_span_models = geographic_span_models

    def validate(self):
        if self.geographic_span_models:
            for k in self.geographic_span_models:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['GeographicSpanModels'] = []
        if self.geographic_span_models is not None:
            for k in self.geographic_span_models:
                result['GeographicSpanModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.geographic_span_models = []
        if m.get('GeographicSpanModels') is not None:
            for k in m.get('GeographicSpanModels'):
                temp_model = DescribeCenGeographicSpansResponseBodyGeographicSpanModels()
                self.geographic_span_models.append(temp_model.from_map(k))
        return self


class DescribeCenGeographicSpansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenGeographicSpansResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenGeographicSpansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenInterRegionBandwidthLimitsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits(TeaModel):
    def __init__(
        self,
        status: str = None,
        bandwidth_package_id: str = None,
        opposite_region_id: str = None,
        geographic_span_id: str = None,
        cen_id: str = None,
        local_region_id: str = None,
        bandwidth_limit: int = None,
    ):
        self.status = status
        self.bandwidth_package_id = bandwidth_package_id
        self.opposite_region_id = opposite_region_id
        self.geographic_span_id = geographic_span_id
        self.cen_id = cen_id
        self.local_region_id = local_region_id
        self.bandwidth_limit = bandwidth_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBody(TeaModel):
    def __init__(
        self,
        cen_inter_region_bandwidth_limits: List[DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits] = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.cen_inter_region_bandwidth_limits = cen_inter_region_bandwidth_limits
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.cen_inter_region_bandwidth_limits:
            for k in self.cen_inter_region_bandwidth_limits:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CenInterRegionBandwidthLimits'] = []
        if self.cen_inter_region_bandwidth_limits is not None:
            for k in self.cen_inter_region_bandwidth_limits:
                result['CenInterRegionBandwidthLimits'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_inter_region_bandwidth_limits = []
        if m.get('CenInterRegionBandwidthLimits') is not None:
            for k in m.get('CenInterRegionBandwidthLimits'):
                temp_model = DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits()
                self.cen_inter_region_bandwidth_limits.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeCenInterRegionBandwidthLimitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenInterRegionBandwidthLimitsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenInterRegionBandwidthLimitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenPrivateZoneRoutesRequest(TeaModel):
    def __init__(
        self,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
    ):
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        return self


class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        host_vpc_id: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
    ):
        self.status = status
        self.host_vpc_id = host_vpc_id
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        return self


class DescribeCenPrivateZoneRoutesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        private_zone_infos: List[DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos] = None,
        page_number: int = None,
        cen_id: str = None,
        private_zone_dns_servers: str = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.private_zone_infos = private_zone_infos
        self.page_number = page_number
        self.cen_id = cen_id
        self.private_zone_dns_servers = private_zone_dns_servers

    def validate(self):
        if self.private_zone_infos:
            for k in self.private_zone_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PrivateZoneInfos'] = []
        if self.private_zone_infos is not None:
            for k in self.private_zone_infos:
                result['PrivateZoneInfos'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.private_zone_dns_servers is not None:
            result['PrivateZoneDnsServers'] = self.private_zone_dns_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.private_zone_infos = []
        if m.get('PrivateZoneInfos') is not None:
            for k in m.get('PrivateZoneInfos'):
                temp_model = DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos()
                self.private_zone_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('PrivateZoneDnsServers') is not None:
            self.private_zone_dns_servers = m.get('PrivateZoneDnsServers')
        return self


class DescribeCenPrivateZoneRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenPrivateZoneRoutesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenPrivateZoneRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenRegionDomainRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        destination_cidr_block: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_region_id = cen_region_id
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenOutRouteMapRecords(TeaModel):
    def __init__(
        self,
        route_map_id: str = None,
        region_id: str = None,
    ):
        self.route_map_id = route_map_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords(TeaModel):
    def __init__(
        self,
        route_map_id: str = None,
        region_id: str = None,
    ):
        self.route_map_id = route_map_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        cen_out_route_map_records: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenOutRouteMapRecords] = None,
        next_hop_type: str = None,
        next_hop_instance_id: str = None,
        next_hop_region_id: str = None,
        as_paths: List[str] = None,
        to_other_region_status: str = None,
        communities: List[str] = None,
        destination_cidr_block: str = None,
        preference: int = None,
        cen_route_map_records: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords] = None,
    ):
        self.type = type
        self.status = status
        self.cen_out_route_map_records = cen_out_route_map_records
        self.next_hop_type = next_hop_type
        self.next_hop_instance_id = next_hop_instance_id
        self.next_hop_region_id = next_hop_region_id
        self.as_paths = as_paths
        self.to_other_region_status = to_other_region_status
        self.communities = communities
        self.destination_cidr_block = destination_cidr_block
        self.preference = preference
        self.cen_route_map_records = cen_route_map_records

    def validate(self):
        if self.cen_out_route_map_records:
            for k in self.cen_out_route_map_records:
                if k:
                    k.validate()
        if self.cen_route_map_records:
            for k in self.cen_route_map_records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        result['CenOutRouteMapRecords'] = []
        if self.cen_out_route_map_records is not None:
            for k in self.cen_out_route_map_records:
                result['CenOutRouteMapRecords'].append(k.to_map() if k else None)
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths
        if self.to_other_region_status is not None:
            result['ToOtherRegionStatus'] = self.to_other_region_status
        if self.communities is not None:
            result['Communities'] = self.communities
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.preference is not None:
            result['Preference'] = self.preference
        result['CenRouteMapRecords'] = []
        if self.cen_route_map_records is not None:
            for k in self.cen_route_map_records:
                result['CenRouteMapRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.cen_out_route_map_records = []
        if m.get('CenOutRouteMapRecords') is not None:
            for k in m.get('CenOutRouteMapRecords'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenOutRouteMapRecords()
                self.cen_out_route_map_records.append(temp_model.from_map(k))
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')
        if m.get('AsPaths') is not None:
            self.as_paths = m.get('AsPaths')
        if m.get('ToOtherRegionStatus') is not None:
            self.to_other_region_status = m.get('ToOtherRegionStatus')
        if m.get('Communities') is not None:
            self.communities = m.get('Communities')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        self.cen_route_map_records = []
        if m.get('CenRouteMapRecords') is not None:
            for k in m.get('CenRouteMapRecords'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteMapRecords()
                self.cen_route_map_records.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        cen_route_entries: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.cen_route_entries = cen_route_entries

    def validate(self):
        if self.cen_route_entries:
            for k in self.cen_route_entries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['CenRouteEntries'] = []
        if self.cen_route_entries is not None:
            for k in self.cen_route_entries:
                result['CenRouteEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.cen_route_entries = []
        if m.get('CenRouteEntries') is not None:
            for k in m.get('CenRouteEntries'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries()
                self.cen_route_entries.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenRegionDomainRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenRouteMapsRequestFilter(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeCenRouteMapsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        route_map_id: str = None,
        cen_region_id: str = None,
        transmit_direction: str = None,
        filter: List[DescribeCenRouteMapsRequestFilter] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.route_map_id = route_map_id
        self.cen_region_id = cen_region_id
        self.transmit_direction = transmit_direction
        self.filter = filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeCenRouteMapsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class DescribeCenRouteMapsResponseBodyRouteMaps(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_instance_ids_reverse_match: bool = None,
        source_region_ids: List[str] = None,
        match_community_set: List[str] = None,
        priority: int = None,
        community_operate_mode: str = None,
        prepend_as_path: List[str] = None,
        route_types: List[str] = None,
        description: str = None,
        destination_instance_ids: List[str] = None,
        match_asns: List[str] = None,
        destination_instance_ids_reverse_match: bool = None,
        operate_community_set: List[str] = None,
        next_priority: int = None,
        route_map_id: str = None,
        transmit_direction: str = None,
        source_child_instance_types: List[str] = None,
        destination_route_table_ids: List[str] = None,
        source_instance_ids: List[str] = None,
        cen_region_id: str = None,
        destination_cidr_blocks: List[str] = None,
        cen_id: str = None,
        source_route_table_ids: List[str] = None,
        map_result: str = None,
        community_match_mode: str = None,
        destination_child_instance_types: List[str] = None,
        as_path_match_mode: str = None,
        preference: int = None,
        cidr_match_mode: str = None,
    ):
        self.status = status
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        self.source_region_ids = source_region_ids
        self.match_community_set = match_community_set
        self.priority = priority
        self.community_operate_mode = community_operate_mode
        self.prepend_as_path = prepend_as_path
        self.route_types = route_types
        self.description = description
        self.destination_instance_ids = destination_instance_ids
        self.match_asns = match_asns
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        self.operate_community_set = operate_community_set
        self.next_priority = next_priority
        self.route_map_id = route_map_id
        self.transmit_direction = transmit_direction
        self.source_child_instance_types = source_child_instance_types
        self.destination_route_table_ids = destination_route_table_ids
        self.source_instance_ids = source_instance_ids
        self.cen_region_id = cen_region_id
        self.destination_cidr_blocks = destination_cidr_blocks
        self.cen_id = cen_id
        self.source_route_table_ids = source_route_table_ids
        self.map_result = map_result
        self.community_match_mode = community_match_mode
        self.destination_child_instance_types = destination_child_instance_types
        self.as_path_match_mode = as_path_match_mode
        self.preference = preference
        self.cidr_match_mode = cidr_match_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')
        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')
        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')
        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')
        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')
        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('DestinationChildInstanceTypes') is not None:
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        return self


class DescribeCenRouteMapsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        route_maps: List[DescribeCenRouteMapsResponseBodyRouteMaps] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.route_maps = route_maps

    def validate(self):
        if self.route_maps:
            for k in self.route_maps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['RouteMaps'] = []
        if self.route_maps is not None:
            for k in self.route_maps:
                result['RouteMaps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.route_maps = []
        if m.get('RouteMaps') is not None:
            for k in m.get('RouteMaps'):
                temp_model = DescribeCenRouteMapsResponseBodyRouteMaps()
                self.route_maps.append(temp_model.from_map(k))
        return self


class DescribeCenRouteMapsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenRouteMapsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenRouteMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: List[str] = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class DescribeCensRequestTag(TeaModel):
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


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        filter: List[DescribeCensRequestFilter] = None,
        tag: List[DescribeCensRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.filter = filter
        self.tag = tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeCensRequestFilter()
                self.filter.append(temp_model.from_map(k))
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeCensRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBodyCensTags(TeaModel):
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


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        cen_bandwidth_package_ids: List[str] = None,
        description: str = None,
        cen_id: str = None,
        protection_level: str = None,
        tags: List[DescribeCensResponseBodyCensTags] = None,
        name: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.cen_bandwidth_package_ids = cen_bandwidth_package_ids
        self.description = description
        self.cen_id = cen_id
        self.protection_level = protection_level
        self.tags = tags
        self.name = name

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.cen_bandwidth_package_ids is not None:
            result['CenBandwidthPackageIds'] = self.cen_bandwidth_package_ids
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CenBandwidthPackageIds') is not None:
            self.cen_bandwidth_package_ids = m.get('CenBandwidthPackageIds')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCensResponseBodyCensTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        cens: List[DescribeCensResponseBodyCens] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.cens = cens

    def validate(self):
        if self.cens:
            for k in self.cens:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Cens'] = []
        if self.cens is not None:
            for k in self.cens:
                result['Cens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.cens = []
        if m.get('Cens') is not None:
            for k in m.get('Cens'):
                temp_model = DescribeCensResponseBodyCens()
                self.cens.append(temp_model.from_map(k))
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCensResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCenVbrHealthCheckRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        vbr_instance_region_id: str = None,
        vbr_instance_id: str = None,
        vbr_instance_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.vbr_instance_region_id = vbr_instance_region_id
        self.vbr_instance_id = vbr_instance_id
        self.vbr_instance_owner_id = vbr_instance_owner_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks(TeaModel):
    def __init__(
        self,
        health_check_target_ip: str = None,
        vbr_instance_id: str = None,
        vbr_instance_region_id: str = None,
        cen_id: str = None,
        healthy_threshold: int = None,
        health_check_interval: int = None,
        health_check_source_ip: str = None,
    ):
        self.health_check_target_ip = health_check_target_ip
        self.vbr_instance_id = vbr_instance_id
        self.vbr_instance_region_id = vbr_instance_region_id
        self.cen_id = cen_id
        self.healthy_threshold = healthy_threshold
        self.health_check_interval = health_check_interval
        self.health_check_source_ip = health_check_source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')
        return self


class DescribeCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        vbr_health_checks: List[DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.vbr_health_checks = vbr_health_checks

    def validate(self):
        if self.vbr_health_checks:
            for k in self.vbr_health_checks:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['VbrHealthChecks'] = []
        if self.vbr_health_checks is not None:
            for k in self.vbr_health_checks:
                result['VbrHealthChecks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.vbr_health_checks = []
        if m.get('VbrHealthChecks') is not None:
            for k in m.get('VbrHealthChecks'):
                temp_model = DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks()
                self.vbr_health_checks.append(temp_model.from_map(k))
        return self


class DescribeCenVbrHealthCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCenVbrHealthCheckResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChildInstanceRegionsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        product_type: str = None,
        child_instance_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.product_type = product_type
        self.child_instance_owner_id = child_instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        return self


class DescribeChildInstanceRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeChildInstanceRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeChildInstanceRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeChildInstanceRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeChildInstanceRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChildInstanceRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeChildInstanceRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowlogsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        region_id: str = None,
        flow_log_name: str = None,
        flow_log_id: str = None,
        description: str = None,
        cen_id: str = None,
        project_name: str = None,
        log_store_name: str = None,
        status: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.region_id = region_id
        self.flow_log_name = flow_log_name
        self.flow_log_id = flow_log_id
        self.description = description
        self.cen_id = cen_id
        self.project_name = project_name
        self.log_store_name = log_store_name
        self.status = status
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeFlowlogsResponseBodyFlowLogs(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        flow_log_name: str = None,
        description: str = None,
        project_name: str = None,
        cen_id: str = None,
        log_store_name: str = None,
        region_id: str = None,
        flow_log_id: str = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.flow_log_name = flow_log_name
        self.description = description
        self.project_name = project_name
        self.cen_id = cen_id
        self.log_store_name = log_store_name
        self.region_id = region_id
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.description is not None:
            result['Description'] = self.description
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        return self


class DescribeFlowlogsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: str = None,
        flow_logs: List[DescribeFlowlogsResponseBodyFlowLogs] = None,
        page_size: str = None,
        request_id: str = None,
        page_number: str = None,
        success: str = None,
    ):
        self.total_count = total_count
        self.flow_logs = flow_logs
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.success = success

    def validate(self):
        if self.flow_logs:
            for k in self.flow_logs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FlowLogs'] = []
        if self.flow_logs is not None:
            for k in self.flow_logs:
                result['FlowLogs'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.flow_logs = []
        if m.get('FlowLogs') is not None:
            for k in m.get('FlowLogs'):
                temp_model = DescribeFlowlogsResponseBodyFlowLogs()
                self.flow_logs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeFlowlogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowlogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFlowlogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGeographicRegionMembershipRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        geographic_region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.geographic_region_id = geographic_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.geographic_region_id is not None:
            result['GeographicRegionId'] = self.geographic_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('GeographicRegionId') is not None:
            self.geographic_region_id = m.get('GeographicRegionId')
        return self


class DescribeGeographicRegionMembershipResponseBodyRegionIds(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeGeographicRegionMembershipResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        region_ids: List[DescribeGeographicRegionMembershipResponseBodyRegionIds] = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.region_ids = region_ids
        self.page_number = page_number

    def validate(self):
        if self.region_ids:
            for k in self.region_ids:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RegionIds'] = []
        if self.region_ids is not None:
            for k in self.region_ids:
                result['RegionIds'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.region_ids = []
        if m.get('RegionIds') is not None:
            for k in m.get('RegionIds'):
                temp_model = DescribeGeographicRegionMembershipResponseBodyRegionIds()
                self.region_ids.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeGeographicRegionMembershipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGeographicRegionMembershipResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGeographicRegionMembershipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGrantRulesToCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        cen_id: str = None,
        product_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.cen_id = cen_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeGrantRulesToCenResponseBodyGrantRules(TeaModel):
    def __init__(
        self,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_id: str = None,
        cen_id: str = None,
    ):
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_id = child_instance_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DescribeGrantRulesToCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        grant_rules: List[DescribeGrantRulesToCenResponseBodyGrantRules] = None,
    ):
        self.request_id = request_id
        self.grant_rules = grant_rules

    def validate(self):
        if self.grant_rules:
            for k in self.grant_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['GrantRules'] = []
        if self.grant_rules is not None:
            for k in self.grant_rules:
                result['GrantRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.grant_rules = []
        if m.get('GrantRules') is not None:
            for k in m.get('GrantRules'):
                temp_model = DescribeGrantRulesToCenResponseBodyGrantRules()
                self.grant_rules.append(temp_model.from_map(k))
        return self


class DescribeGrantRulesToCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGrantRulesToCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGrantRulesToCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePublishedRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_route_table_id = child_instance_route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesConflicts(TeaModel):
    def __init__(
        self,
        status: str = None,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.destination_cidr_block = destination_cidr_block
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries(TeaModel):
    def __init__(
        self,
        next_hop_id: str = None,
        conflicts: List[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesConflicts] = None,
        publish_status: str = None,
        child_instance_route_table_id: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        destination_cidr_block: str = None,
        route_type: str = None,
    ):
        self.next_hop_id = next_hop_id
        self.conflicts = conflicts
        self.publish_status = publish_status
        self.child_instance_route_table_id = child_instance_route_table_id
        self.next_hop_type = next_hop_type
        self.operational_mode = operational_mode
        self.destination_cidr_block = destination_cidr_block
        self.route_type = route_type

    def validate(self):
        if self.conflicts:
            for k in self.conflicts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
        result['Conflicts'] = []
        if self.conflicts is not None:
            for k in self.conflicts:
                result['Conflicts'].append(k.to_map() if k else None)
        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.operational_mode is not None:
            result['OperationalMode'] = self.operational_mode
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
        self.conflicts = []
        if m.get('Conflicts') is not None:
            for k in m.get('Conflicts'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesConflicts()
                self.conflicts.append(temp_model.from_map(k))
        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('OperationalMode') is not None:
            self.operational_mode = m.get('OperationalMode')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class DescribePublishedRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        published_route_entries: List[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.published_route_entries = published_route_entries

    def validate(self):
        if self.published_route_entries:
            for k in self.published_route_entries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['PublishedRouteEntries'] = []
        if self.published_route_entries is not None:
            for k in self.published_route_entries:
                result['PublishedRouteEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.published_route_entries = []
        if m.get('PublishedRouteEntries') is not None:
            for k in m.get('PublishedRouteEntries'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries()
                self.published_route_entries.append(temp_model.from_map(k))
        return self


class DescribePublishedRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePublishedRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRouteConflictRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_route_table_id = child_instance_route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribeRouteConflictResponseBodyRouteConflicts(TeaModel):
    def __init__(
        self,
        status: str = None,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        self.status = status
        self.destination_cidr_block = destination_cidr_block
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRouteConflictResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        route_conflicts: List[DescribeRouteConflictResponseBodyRouteConflicts] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.route_conflicts = route_conflicts

    def validate(self):
        if self.route_conflicts:
            for k in self.route_conflicts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['RouteConflicts'] = []
        if self.route_conflicts is not None:
            for k in self.route_conflicts:
                result['RouteConflicts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.route_conflicts = []
        if m.get('RouteConflicts') is not None:
            for k in m.get('RouteConflicts'):
                temp_model = DescribeRouteConflictResponseBodyRouteConflicts()
                self.route_conflicts.append(temp_model.from_map(k))
        return self


class DescribeRouteConflictResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRouteConflictResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRouteConflictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRouteServicesInCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        cen_id: str = None,
        host: str = None,
        host_region_id: str = None,
        access_region_id: str = None,
        host_vpc_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.cen_id = cen_id
        self.host = host
        self.host_region_id = host_region_id
        self.access_region_id = access_region_id
        self.host_vpc_id = host_vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntries(TeaModel):
    def __init__(
        self,
        status: str = None,
        host: str = None,
        description: str = None,
        host_vpc_id: str = None,
        cidrs: List[str] = None,
        cen_id: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
        update_interval: str = None,
    ):
        self.status = status
        self.host = host
        self.description = description
        self.host_vpc_id = host_vpc_id
        self.cidrs = cidrs
        self.cen_id = cen_id
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id
        self.update_interval = update_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.host is not None:
            result['Host'] = self.host
        if self.description is not None:
            result['Description'] = self.description
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.update_interval is not None:
            result['UpdateInterval'] = self.update_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('UpdateInterval') is not None:
            self.update_interval = m.get('UpdateInterval')
        return self


class DescribeRouteServicesInCenResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        route_service_entries: List[DescribeRouteServicesInCenResponseBodyRouteServiceEntries] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.route_service_entries = route_service_entries

    def validate(self):
        if self.route_service_entries:
            for k in self.route_service_entries:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['RouteServiceEntries'] = []
        if self.route_service_entries is not None:
            for k in self.route_service_entries:
                result['RouteServiceEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.route_service_entries = []
        if m.get('RouteServiceEntries') is not None:
            for k in m.get('RouteServiceEntries'):
                temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntries()
                self.route_service_entries.append(temp_model.from_map(k))
        return self


class DescribeRouteServicesInCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRouteServicesInCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRouteServicesInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCenChildInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_owner_id: int = None,
        cen_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_owner_id = child_instance_owner_id
        self.cen_owner_id = cen_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        return self


class DetachCenChildInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCenChildInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetachCenChildInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachCenChildInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableCenVbrHealthCheckRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        vbr_instance_region_id: str = None,
        vbr_instance_id: str = None,
        vbr_instance_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.vbr_instance_region_id = vbr_instance_region_id
        self.vbr_instance_id = vbr_instance_id
        self.vbr_instance_owner_id = vbr_instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        return self


class DisableCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableCenVbrHealthCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableCenVbrHealthCheckResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableCenVbrHealthCheckRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        vbr_instance_region_id: str = None,
        vbr_instance_id: str = None,
        health_check_source_ip: str = None,
        health_check_target_ip: str = None,
        vbr_instance_owner_id: int = None,
        health_check_interval: int = None,
        healthy_threshold: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.vbr_instance_region_id = vbr_instance_region_id
        self.vbr_instance_id = vbr_instance_id
        self.health_check_source_ip = health_check_source_ip
        self.health_check_target_ip = health_check_target_ip
        self.vbr_instance_owner_id = vbr_instance_owner_id
        self.health_check_interval = health_check_interval
        self.healthy_threshold = healthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id
        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id
        if self.health_check_source_ip is not None:
            result['HealthCheckSourceIp'] = self.health_check_source_ip
        if self.health_check_target_ip is not None:
            result['HealthCheckTargetIp'] = self.health_check_target_ip
        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')
        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')
        if m.get('HealthCheckSourceIp') is not None:
            self.health_check_source_ip = m.get('HealthCheckSourceIp')
        if m.get('HealthCheckTargetIp') is not None:
            self.health_check_target_ip = m.get('HealthCheckTargetIp')
        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        return self


class EnableCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableCenVbrHealthCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableCenVbrHealthCheckResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableCenVbrHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        next_token: str = None,
        page_size: int = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.page_size = page_size
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        name: str = None,
        description: str = None,
        protection_level: str = None,
        ipv_6level: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.name = name
        self.description = description
        self.protection_level = protection_level
        self.ipv_6level = ipv_6level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        return self


class ModifyCenAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCenAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCenAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCenAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenBandwidthPackageAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        name: str = None,
        description: str = None,
        cen_bandwidth_package_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.name = name
        self.description = description
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class ModifyCenBandwidthPackageAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCenBandwidthPackageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCenBandwidthPackageAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCenBandwidthPackageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenBandwidthPackageSpecRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_bandwidth_package_id: str = None,
        bandwidth: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.bandwidth = bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        return self


class ModifyCenBandwidthPackageSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCenBandwidthPackageSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCenBandwidthPackageSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCenBandwidthPackageSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCenRouteMapRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_region_id: str = None,
        route_map_id: str = None,
        description: str = None,
        map_result: str = None,
        next_priority: int = None,
        cidr_match_mode: str = None,
        as_path_match_mode: str = None,
        community_match_mode: str = None,
        community_operate_mode: str = None,
        preference: int = None,
        priority: int = None,
        source_instance_ids_reverse_match: bool = None,
        destination_instance_ids_reverse_match: bool = None,
        gateway_zone_id: str = None,
        match_address_type: str = None,
        source_instance_ids: List[str] = None,
        destination_instance_ids: List[str] = None,
        source_route_table_ids: List[str] = None,
        destination_route_table_ids: List[str] = None,
        source_region_ids: List[str] = None,
        source_child_instance_types: List[str] = None,
        destination_child_instance_types: List[str] = None,
        destination_cidr_blocks: List[str] = None,
        route_types: List[str] = None,
        match_asns: List[int] = None,
        match_community_set: List[str] = None,
        operate_community_set: List[str] = None,
        prepend_as_path: List[int] = None,
        destination_region_ids: List[str] = None,
        source_zone_ids: List[str] = None,
        original_route_table_ids: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_region_id = cen_region_id
        self.route_map_id = route_map_id
        self.description = description
        self.map_result = map_result
        self.next_priority = next_priority
        self.cidr_match_mode = cidr_match_mode
        self.as_path_match_mode = as_path_match_mode
        self.community_match_mode = community_match_mode
        self.community_operate_mode = community_operate_mode
        self.preference = preference
        self.priority = priority
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        self.gateway_zone_id = gateway_zone_id
        self.match_address_type = match_address_type
        self.source_instance_ids = source_instance_ids
        self.destination_instance_ids = destination_instance_ids
        self.source_route_table_ids = source_route_table_ids
        self.destination_route_table_ids = destination_route_table_ids
        self.source_region_ids = source_region_ids
        self.source_child_instance_types = source_child_instance_types
        self.destination_child_instance_types = destination_child_instance_types
        self.destination_cidr_blocks = destination_cidr_blocks
        self.route_types = route_types
        self.match_asns = match_asns
        self.match_community_set = match_community_set
        self.operate_community_set = operate_community_set
        self.prepend_as_path = prepend_as_path
        self.destination_region_ids = destination_region_ids
        self.source_zone_ids = source_zone_ids
        self.original_route_table_ids = original_route_table_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.description is not None:
            result['Description'] = self.description
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.gateway_zone_id is not None:
            result['GatewayZoneId'] = self.gateway_zone_id
        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path
        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids
        if self.source_zone_ids is not None:
            result['SourceZoneIds'] = self.source_zone_ids
        if self.original_route_table_ids is not None:
            result['OriginalRouteTableIds'] = self.original_route_table_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('GatewayZoneId') is not None:
            self.gateway_zone_id = m.get('GatewayZoneId')
        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')
        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')
        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')
        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')
        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')
        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')
        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')
        if m.get('DestinationChildInstanceTypes') is not None:
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')
        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')
        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')
        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')
        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')
        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')
        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')
        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')
        if m.get('SourceZoneIds') is not None:
            self.source_zone_ids = m.get('SourceZoneIds')
        if m.get('OriginalRouteTableIds') is not None:
            self.original_route_table_ids = m.get('OriginalRouteTableIds')
        return self


class ModifyCenRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyCenRouteMapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCenRouteMapResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCenRouteMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowLogAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        flow_log_name: str = None,
        description: str = None,
        region_id: str = None,
        flow_log_id: str = None,
        cen_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.flow_log_name = flow_log_name
        self.description = description
        self.region_id = region_id
        self.flow_log_id = flow_log_id
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class ModifyFlowLogAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyFlowLogAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFlowLogAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyFlowLogAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_route_table_id = child_instance_route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class PublishRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PublishRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResolveAndRouteServiceInCenRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        client_token: str = None,
        cen_id: str = None,
        host: str = None,
        host_region_id: str = None,
        update_interval: int = None,
        host_vpc_id: str = None,
        description: str = None,
        access_region_ids: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.cen_id = cen_id
        self.host = host
        self.host_region_id = host_region_id
        self.update_interval = update_interval
        self.host_vpc_id = host_vpc_id
        self.description = description
        self.access_region_ids = access_region_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.host is not None:
            result['Host'] = self.host
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.update_interval is not None:
            result['UpdateInterval'] = self.update_interval
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.description is not None:
            result['Description'] = self.description
        if self.access_region_ids is not None:
            result['AccessRegionIds'] = self.access_region_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('UpdateInterval') is not None:
            self.update_interval = m.get('UpdateInterval')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccessRegionIds') is not None:
            self.access_region_ids = m.get('AccessRegionIds')
        return self


class ResolveAndRouteServiceInCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResolveAndRouteServiceInCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResolveAndRouteServiceInCenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResolveAndRouteServiceInCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RoutePrivateZoneInCenToVpcRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id
        self.host_vpc_id = host_vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        return self


class RoutePrivateZoneInCenToVpcResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RoutePrivateZoneInCenToVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RoutePrivateZoneInCenToVpcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RoutePrivateZoneInCenToVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCenInterRegionBandwidthLimitRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        local_region_id: str = None,
        opposite_region_id: str = None,
        bandwidth_limit: int = None,
        bandwidth_package_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.local_region_id = local_region_id
        self.opposite_region_id = opposite_region_id
        self.bandwidth_limit = bandwidth_limit
        self.bandwidth_package_id = bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        return self


class SetCenInterRegionBandwidthLimitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetCenInterRegionBandwidthLimitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetCenInterRegionBandwidthLimitResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCenInterRegionBandwidthLimitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempUpgradeCenBandwidthPackageSpecRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_bandwidth_package_id: str = None,
        bandwidth: int = None,
        end_time: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.bandwidth = bandwidth
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class TempUpgradeCenBandwidthPackageSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TempUpgradeCenBandwidthPackageSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TempUpgradeCenBandwidthPackageSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TempUpgradeCenBandwidthPackageSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassociateCenBandwidthPackageRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        cen_bandwidth_package_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class UnassociateCenBandwidthPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnassociateCenBandwidthPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassociateCenBandwidthPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassociateCenBandwidthPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnroutePrivateZoneInCenToVpcRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        access_region_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.access_region_id = access_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        return self


class UnroutePrivateZoneInCenToVpcResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnroutePrivateZoneInCenToVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnroutePrivateZoneInCenToVpcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnroutePrivateZoneInCenToVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawPublishedRouteEntriesRequest(TeaModel):
    def __init__(
        self,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        cen_id: str = None,
        child_instance_id: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        child_instance_route_table_id: str = None,
        destination_cidr_block: str = None,
    ):
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.child_instance_route_table_id = child_instance_route_table_id
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.child_instance_route_table_id is not None:
            result['ChildInstanceRouteTableId'] = self.child_instance_route_table_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('ChildInstanceRouteTableId') is not None:
            self.child_instance_route_table_id = m.get('ChildInstanceRouteTableId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class WithdrawPublishedRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class WithdrawPublishedRouteEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WithdrawPublishedRouteEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WithdrawPublishedRouteEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


