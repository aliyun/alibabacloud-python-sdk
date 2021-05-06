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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        success: str = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.client_token = client_token
        self.name = name
        self.description = description
        self.protection_level = protection_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class CreateCenResponseBody(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        request_id: str = None,
    ):
        self.cen_id = cen_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        cen_bandwidth_package_id: str = None,
        cen_bandwidth_package_order_id: str = None,
        request_id: str = None,
    ):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.cen_bandwidth_package_order_id = cen_bandwidth_package_order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.cen_bandwidth_package_order_id is not None:
            result['CenBandwidthPackageOrderId'] = self.cen_bandwidth_package_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('CenBandwidthPackageOrderId') is not None:
            self.cen_bandwidth_package_order_id = m.get('CenBandwidthPackageOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class CreateCenRouteMapResponseBody(TeaModel):
    def __init__(
        self,
        route_map_id: str = None,
        request_id: str = None,
    ):
        self.route_map_id = route_map_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        success: str = None,
        flow_log_id: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.flow_log_id = flow_log_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        success: str = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        success: str = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.child_instance_id = child_instance_id
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class DescribeCenAttachedChildInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        child_instance_type: str = None,
        child_instance_region_id: str = None,
        request_id: str = None,
        child_instance_owner_id: int = None,
        child_instance_id: str = None,
        cen_id: str = None,
        child_instance_name: str = None,
        child_instance_attach_time: str = None,
    ):
        self.status = status
        self.child_instance_type = child_instance_type
        self.child_instance_region_id = child_instance_region_id
        self.request_id = request_id
        self.child_instance_owner_id = child_instance_owner_id
        self.child_instance_id = child_instance_id
        self.cen_id = cen_id
        self.child_instance_name = child_instance_name
        self.child_instance_attach_time = child_instance_attach_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type
        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id
        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.child_instance_name is not None:
            result['ChildInstanceName'] = self.child_instance_name
        if self.child_instance_attach_time is not None:
            result['ChildInstanceAttachTime'] = self.child_instance_attach_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')
        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')
        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ChildInstanceName') is not None:
            self.child_instance_name = m.get('ChildInstanceName')
        if m.get('ChildInstanceAttachTime') is not None:
            self.child_instance_attach_time = m.get('ChildInstanceAttachTime')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenAttachedChildInstancesResponseBodyChildInstances(TeaModel):
    def __init__(
        self,
        child_instance: List[DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance] = None,
    ):
        self.child_instance = child_instance

    def validate(self):
        if self.child_instance:
            for k in self.child_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChildInstance'] = []
        if self.child_instance is not None:
            for k in self.child_instance:
                result['ChildInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_instance = []
        if m.get('ChildInstance') is not None:
            for k in m.get('ChildInstance'):
                temp_model = DescribeCenAttachedChildInstancesResponseBodyChildInstancesChildInstance()
                self.child_instance.append(temp_model.from_map(k))
        return self


class DescribeCenAttachedChildInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        child_instances: DescribeCenAttachedChildInstancesResponseBodyChildInstances = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.child_instances = child_instances

    def validate(self):
        if self.child_instances:
            self.child_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.child_instances is not None:
            result['ChildInstances'] = self.child_instances.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ChildInstances') is not None:
            temp_model = DescribeCenAttachedChildInstancesResponseBodyChildInstances()
            self.child_instances = temp_model.from_map(m['ChildInstances'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit(TeaModel):
    def __init__(
        self,
        bandwidth_limit: str = None,
        opposite_region_id: str = None,
        geographic_span_id: str = None,
        local_region_id: str = None,
    ):
        self.bandwidth_limit = bandwidth_limit
        self.opposite_region_id = opposite_region_id
        self.geographic_span_id = geographic_span_id
        self.local_region_id = local_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit
        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')
        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits(TeaModel):
    def __init__(
        self,
        orgin_inter_region_bandwidth_limit: List[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit] = None,
    ):
        self.orgin_inter_region_bandwidth_limit = orgin_inter_region_bandwidth_limit

    def validate(self):
        if self.orgin_inter_region_bandwidth_limit:
            for k in self.orgin_inter_region_bandwidth_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrginInterRegionBandwidthLimit'] = []
        if self.orgin_inter_region_bandwidth_limit is not None:
            for k in self.orgin_inter_region_bandwidth_limit:
                result['OrginInterRegionBandwidthLimit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.orgin_inter_region_bandwidth_limit = []
        if m.get('OrginInterRegionBandwidthLimit') is not None:
            for k in m.get('OrginInterRegionBandwidthLimit'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimitsOrginInterRegionBandwidthLimit()
                self.orgin_inter_region_bandwidth_limit.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds(TeaModel):
    def __init__(
        self,
        cen_id: List[str] = None,
    ):
        self.cen_id = cen_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage(TeaModel):
    def __init__(
        self,
        reservation_active_time: str = None,
        status: str = None,
        creation_time: str = None,
        reservation_order_type: str = None,
        bandwidth_package_charge_type: str = None,
        cen_bandwidth_package_id: str = None,
        reservation_internet_charge_type: str = None,
        ratio: str = None,
        geographic_region_aid: str = None,
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
        orgin_inter_region_bandwidth_limits: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits = None,
        cen_ids: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds = None,
    ):
        self.reservation_active_time = reservation_active_time
        self.status = status
        self.creation_time = creation_time
        self.reservation_order_type = reservation_order_type
        self.bandwidth_package_charge_type = bandwidth_package_charge_type
        self.cen_bandwidth_package_id = cen_bandwidth_package_id
        self.reservation_internet_charge_type = reservation_internet_charge_type
        self.ratio = ratio
        self.geographic_region_aid = geographic_region_aid
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
        self.orgin_inter_region_bandwidth_limits = orgin_inter_region_bandwidth_limits
        self.cen_ids = cen_ids

    def validate(self):
        if self.orgin_inter_region_bandwidth_limits:
            self.orgin_inter_region_bandwidth_limits.validate()
        if self.cen_ids:
            self.cen_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reservation_active_time is not None:
            result['ReservationActiveTime'] = self.reservation_active_time
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.reservation_order_type is not None:
            result['ReservationOrderType'] = self.reservation_order_type
        if self.bandwidth_package_charge_type is not None:
            result['BandwidthPackageChargeType'] = self.bandwidth_package_charge_type
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        if self.reservation_internet_charge_type is not None:
            result['ReservationInternetChargeType'] = self.reservation_internet_charge_type
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.geographic_region_aid is not None:
            result['GeographicRegionAId'] = self.geographic_region_aid
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
        if self.orgin_inter_region_bandwidth_limits is not None:
            result['OrginInterRegionBandwidthLimits'] = self.orgin_inter_region_bandwidth_limits.to_map()
        if self.cen_ids is not None:
            result['CenIds'] = self.cen_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservationActiveTime') is not None:
            self.reservation_active_time = m.get('ReservationActiveTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ReservationOrderType') is not None:
            self.reservation_order_type = m.get('ReservationOrderType')
        if m.get('BandwidthPackageChargeType') is not None:
            self.bandwidth_package_charge_type = m.get('BandwidthPackageChargeType')
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        if m.get('ReservationInternetChargeType') is not None:
            self.reservation_internet_charge_type = m.get('ReservationInternetChargeType')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('GeographicRegionAId') is not None:
            self.geographic_region_aid = m.get('GeographicRegionAId')
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
        if m.get('OrginInterRegionBandwidthLimits') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageOrginInterRegionBandwidthLimits()
            self.orgin_inter_region_bandwidth_limits = temp_model.from_map(m['OrginInterRegionBandwidthLimits'])
        if m.get('CenIds') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackageCenIds()
            self.cen_ids = temp_model.from_map(m['CenIds'])
        return self


class DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages(TeaModel):
    def __init__(
        self,
        cen_bandwidth_package: List[DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage] = None,
    ):
        self.cen_bandwidth_package = cen_bandwidth_package

    def validate(self):
        if self.cen_bandwidth_package:
            for k in self.cen_bandwidth_package:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenBandwidthPackage'] = []
        if self.cen_bandwidth_package is not None:
            for k in self.cen_bandwidth_package:
                result['CenBandwidthPackage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_bandwidth_package = []
        if m.get('CenBandwidthPackage') is not None:
            for k in m.get('CenBandwidthPackage'):
                temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackagesCenBandwidthPackage()
                self.cen_bandwidth_package.append(temp_model.from_map(k))
        return self


class DescribeCenBandwidthPackagesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cen_bandwidth_packages: DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cen_bandwidth_packages = cen_bandwidth_packages

    def validate(self):
        if self.cen_bandwidth_packages:
            self.cen_bandwidth_packages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cen_bandwidth_packages is not None:
            result['CenBandwidthPackages'] = self.cen_bandwidth_packages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CenBandwidthPackages') is not None:
            temp_model = DescribeCenBandwidthPackagesResponseBodyCenBandwidthPackages()
            self.cen_bandwidth_packages = temp_model.from_map(m['CenBandwidthPackages'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(TeaModel):
    def __init__(
        self,
        cen_route_map_record: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord] = None,
    ):
        self.cen_route_map_record = cen_route_map_record

    def validate(self):
        if self.cen_route_map_record:
            for k in self.cen_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteMapRecord'] = []
        if self.cen_route_map_record is not None:
            for k in self.cen_route_map_record:
                result['CenRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_map_record = []
        if m.get('CenRouteMapRecord') is not None:
            for k in m.get('CenRouteMapRecord'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts(TeaModel):
    def __init__(
        self,
        conflict: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict] = None,
    ):
        self.conflict = conflict

    def validate(self):
        if self.conflict:
            for k in self.conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conflict'] = []
        if self.conflict is not None:
            for k in self.conflict:
                result['Conflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k in m.get('Conflict'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(TeaModel):
    def __init__(
        self,
        community: List[str] = None,
    ):
        self.community = community

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.community is not None:
            result['Community'] = self.community
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Community') is not None:
            self.community = m.get('Community')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(TeaModel):
    def __init__(
        self,
        as_path: List[str] = None,
    ):
        self.as_path = as_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        publish_status: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        next_hop_region_id: str = None,
        next_hop_instance_id: str = None,
        destination_cidr_block: str = None,
        route_table_id: str = None,
        cen_route_map_records: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords = None,
        conflicts: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts = None,
        communities: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities = None,
        as_paths: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths = None,
    ):
        self.status = status
        self.type = type
        self.publish_status = publish_status
        self.next_hop_type = next_hop_type
        self.operational_mode = operational_mode
        self.next_hop_region_id = next_hop_region_id
        self.next_hop_instance_id = next_hop_instance_id
        self.destination_cidr_block = destination_cidr_block
        self.route_table_id = route_table_id
        self.cen_route_map_records = cen_route_map_records
        self.conflicts = conflicts
        self.communities = communities
        self.as_paths = as_paths

    def validate(self):
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.conflicts:
            self.conflicts.validate()
        if self.communities:
            self.communities.validate()
        if self.as_paths:
            self.as_paths.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id
        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()
        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()
        if self.communities is not None:
            result['Communities'] = self.communities.to_map()
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()
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
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')
        if m.get('CenRouteMapRecords') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m['CenRouteMapRecords'])
        if m.get('Conflicts') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m['Conflicts'])
        if m.get('Communities') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m['Communities'])
        if m.get('AsPaths') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m['AsPaths'])
        return self


class DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(
        self,
        cen_route_entry: List[DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry] = None,
    ):
        self.cen_route_entry = cen_route_entry

    def validate(self):
        if self.cen_route_entry:
            for k in self.cen_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteEntry'] = []
        if self.cen_route_entry is not None:
            for k in self.cen_route_entry:
                result['CenRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_entry = []
        if m.get('CenRouteEntry') is not None:
            for k in m.get('CenRouteEntry'):
                temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k))
        return self


class DescribeCenChildInstanceRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cen_route_entries: DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cen_route_entries = cen_route_entries

    def validate(self):
        if self.cen_route_entries:
            self.cen_route_entries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cen_route_entries is not None:
            result['CenRouteEntries'] = self.cen_route_entries.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CenRouteEntries') is not None:
            temp_model = DescribeCenChildInstanceRouteEntriesResponseBodyCenRouteEntries()
            self.cen_route_entries = temp_model.from_map(m['CenRouteEntries'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        remaining_bandwidth: int = None,
        request_id: str = None,
    ):
        self.remaining_bandwidth = remaining_bandwidth
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remaining_bandwidth is not None:
            result['RemainingBandwidth'] = self.remaining_bandwidth
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemainingBandwidth') is not None:
            self.remaining_bandwidth = m.get('RemainingBandwidth')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel(TeaModel):
    def __init__(
        self,
        local_geo_region_id: str = None,
        geographic_span_id: str = None,
        opposite_geo_region_id: str = None,
    ):
        self.local_geo_region_id = local_geo_region_id
        self.geographic_span_id = geographic_span_id
        self.opposite_geo_region_id = opposite_geo_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_geo_region_id is not None:
            result['LocalGeoRegionId'] = self.local_geo_region_id
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id
        if self.opposite_geo_region_id is not None:
            result['OppositeGeoRegionId'] = self.opposite_geo_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalGeoRegionId') is not None:
            self.local_geo_region_id = m.get('LocalGeoRegionId')
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')
        if m.get('OppositeGeoRegionId') is not None:
            self.opposite_geo_region_id = m.get('OppositeGeoRegionId')
        return self


class DescribeCenGeographicSpansResponseBodyGeographicSpanModels(TeaModel):
    def __init__(
        self,
        geographic_span_model: List[DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel] = None,
    ):
        self.geographic_span_model = geographic_span_model

    def validate(self):
        if self.geographic_span_model:
            for k in self.geographic_span_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GeographicSpanModel'] = []
        if self.geographic_span_model is not None:
            for k in self.geographic_span_model:
                result['GeographicSpanModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.geographic_span_model = []
        if m.get('GeographicSpanModel') is not None:
            for k in m.get('GeographicSpanModel'):
                temp_model = DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel()
                self.geographic_span_model.append(temp_model.from_map(k))
        return self


class DescribeCenGeographicSpansResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        geographic_span_models: DescribeCenGeographicSpansResponseBodyGeographicSpanModels = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.geographic_span_models = geographic_span_models

    def validate(self):
        if self.geographic_span_models:
            self.geographic_span_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.geographic_span_models is not None:
            result['GeographicSpanModels'] = self.geographic_span_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('GeographicSpanModels') is not None:
            temp_model = DescribeCenGeographicSpansResponseBodyGeographicSpanModels()
            self.geographic_span_models = temp_model.from_map(m['GeographicSpanModels'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits(TeaModel):
    def __init__(
        self,
        cen_inter_region_bandwidth_limit: List[DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit] = None,
    ):
        self.cen_inter_region_bandwidth_limit = cen_inter_region_bandwidth_limit

    def validate(self):
        if self.cen_inter_region_bandwidth_limit:
            for k in self.cen_inter_region_bandwidth_limit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenInterRegionBandwidthLimit'] = []
        if self.cen_inter_region_bandwidth_limit is not None:
            for k in self.cen_inter_region_bandwidth_limit:
                result['CenInterRegionBandwidthLimit'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_inter_region_bandwidth_limit = []
        if m.get('CenInterRegionBandwidthLimit') is not None:
            for k in m.get('CenInterRegionBandwidthLimit'):
                temp_model = DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimitsCenInterRegionBandwidthLimit()
                self.cen_inter_region_bandwidth_limit.append(temp_model.from_map(k))
        return self


class DescribeCenInterRegionBandwidthLimitsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cen_inter_region_bandwidth_limits: DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cen_inter_region_bandwidth_limits = cen_inter_region_bandwidth_limits

    def validate(self):
        if self.cen_inter_region_bandwidth_limits:
            self.cen_inter_region_bandwidth_limits.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cen_inter_region_bandwidth_limits is not None:
            result['CenInterRegionBandwidthLimits'] = self.cen_inter_region_bandwidth_limits.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CenInterRegionBandwidthLimits') is not None:
            temp_model = DescribeCenInterRegionBandwidthLimitsResponseBodyCenInterRegionBandwidthLimits()
            self.cen_inter_region_bandwidth_limits = temp_model.from_map(m['CenInterRegionBandwidthLimits'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
        host_vpc_id: str = None,
    ):
        self.status = status
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id
        self.host_vpc_id = host_vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('HostVpcId') is not None:
            self.host_vpc_id = m.get('HostVpcId')
        return self


class DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos(TeaModel):
    def __init__(
        self,
        private_zone_info: List[DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo] = None,
    ):
        self.private_zone_info = private_zone_info

    def validate(self):
        if self.private_zone_info:
            for k in self.private_zone_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrivateZoneInfo'] = []
        if self.private_zone_info is not None:
            for k in self.private_zone_info:
                result['PrivateZoneInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_zone_info = []
        if m.get('PrivateZoneInfo') is not None:
            for k in m.get('PrivateZoneInfo'):
                temp_model = DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfosPrivateZoneInfo()
                self.private_zone_info.append(temp_model.from_map(k))
        return self


class DescribeCenPrivateZoneRoutesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        private_zone_dns_servers: str = None,
        cen_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        private_zone_infos: DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos = None,
    ):
        self.request_id = request_id
        self.private_zone_dns_servers = private_zone_dns_servers
        self.cen_id = cen_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.private_zone_infos = private_zone_infos

    def validate(self):
        if self.private_zone_infos:
            self.private_zone_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.private_zone_dns_servers is not None:
            result['PrivateZoneDnsServers'] = self.private_zone_dns_servers
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.private_zone_infos is not None:
            result['PrivateZoneInfos'] = self.private_zone_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrivateZoneDnsServers') is not None:
            self.private_zone_dns_servers = m.get('PrivateZoneDnsServers')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PrivateZoneInfos') is not None:
            temp_model = DescribeCenPrivateZoneRoutesResponseBodyPrivateZoneInfos()
            self.private_zone_infos = temp_model.from_map(m['PrivateZoneInfos'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords(TeaModel):
    def __init__(
        self,
        cen_route_map_record: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord] = None,
    ):
        self.cen_route_map_record = cen_route_map_record

    def validate(self):
        if self.cen_route_map_record:
            for k in self.cen_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteMapRecord'] = []
        if self.cen_route_map_record is not None:
            for k in self.cen_route_map_record:
                result['CenRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_map_record = []
        if m.get('CenRouteMapRecord') is not None:
            for k in m.get('CenRouteMapRecord'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecordsCenRouteMapRecord()
                self.cen_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords(TeaModel):
    def __init__(
        self,
        cen_out_route_map_record: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord] = None,
    ):
        self.cen_out_route_map_record = cen_out_route_map_record

    def validate(self):
        if self.cen_out_route_map_record:
            for k in self.cen_out_route_map_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenOutRouteMapRecord'] = []
        if self.cen_out_route_map_record is not None:
            for k in self.cen_out_route_map_record:
                result['CenOutRouteMapRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_out_route_map_record = []
        if m.get('CenOutRouteMapRecord') is not None:
            for k in m.get('CenOutRouteMapRecord'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecordsCenOutRouteMapRecord()
                self.cen_out_route_map_record.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities(TeaModel):
    def __init__(
        self,
        community: List[str] = None,
    ):
        self.community = community

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.community is not None:
            result['Community'] = self.community
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Community') is not None:
            self.community = m.get('Community')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths(TeaModel):
    def __init__(
        self,
        as_path: List[str] = None,
    ):
        self.as_path = as_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry(TeaModel):
    def __init__(
        self,
        to_other_region_status: str = None,
        type: str = None,
        status: str = None,
        next_hop_type: str = None,
        next_hop_instance_id: str = None,
        next_hop_region_id: str = None,
        destination_cidr_block: str = None,
        preference: int = None,
        cen_route_map_records: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords = None,
        cen_out_route_map_records: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords = None,
        communities: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities = None,
        as_paths: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths = None,
    ):
        self.to_other_region_status = to_other_region_status
        self.type = type
        self.status = status
        self.next_hop_type = next_hop_type
        self.next_hop_instance_id = next_hop_instance_id
        self.next_hop_region_id = next_hop_region_id
        self.destination_cidr_block = destination_cidr_block
        self.preference = preference
        self.cen_route_map_records = cen_route_map_records
        self.cen_out_route_map_records = cen_out_route_map_records
        self.communities = communities
        self.as_paths = as_paths

    def validate(self):
        if self.cen_route_map_records:
            self.cen_route_map_records.validate()
        if self.cen_out_route_map_records:
            self.cen_out_route_map_records.validate()
        if self.communities:
            self.communities.validate()
        if self.as_paths:
            self.as_paths.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.to_other_region_status is not None:
            result['ToOtherRegionStatus'] = self.to_other_region_status
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.cen_route_map_records is not None:
            result['CenRouteMapRecords'] = self.cen_route_map_records.to_map()
        if self.cen_out_route_map_records is not None:
            result['CenOutRouteMapRecords'] = self.cen_out_route_map_records.to_map()
        if self.communities is not None:
            result['Communities'] = self.communities.to_map()
        if self.as_paths is not None:
            result['AsPaths'] = self.as_paths.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToOtherRegionStatus') is not None:
            self.to_other_region_status = m.get('ToOtherRegionStatus')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('CenRouteMapRecords') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenRouteMapRecords()
            self.cen_route_map_records = temp_model.from_map(m['CenRouteMapRecords'])
        if m.get('CenOutRouteMapRecords') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCenOutRouteMapRecords()
            self.cen_out_route_map_records = temp_model.from_map(m['CenOutRouteMapRecords'])
        if m.get('Communities') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryCommunities()
            self.communities = temp_model.from_map(m['Communities'])
        if m.get('AsPaths') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntryAsPaths()
            self.as_paths = temp_model.from_map(m['AsPaths'])
        return self


class DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries(TeaModel):
    def __init__(
        self,
        cen_route_entry: List[DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry] = None,
    ):
        self.cen_route_entry = cen_route_entry

    def validate(self):
        if self.cen_route_entry:
            for k in self.cen_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CenRouteEntry'] = []
        if self.cen_route_entry is not None:
            for k in self.cen_route_entry:
                result['CenRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen_route_entry = []
        if m.get('CenRouteEntry') is not None:
            for k in m.get('CenRouteEntry'):
                temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntriesCenRouteEntry()
                self.cen_route_entry.append(temp_model.from_map(k))
        return self


class DescribeCenRegionDomainRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cen_route_entries: DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cen_route_entries = cen_route_entries

    def validate(self):
        if self.cen_route_entries:
            self.cen_route_entries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cen_route_entries is not None:
            result['CenRouteEntries'] = self.cen_route_entries.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('CenRouteEntries') is not None:
            temp_model = DescribeCenRegionDomainRouteEntriesResponseBodyCenRouteEntries()
            self.cen_route_entries = temp_model.from_map(m['CenRouteEntries'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds(TeaModel):
    def __init__(
        self,
        source_region_id: List[str] = None,
    ):
        self.source_region_id = source_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes(TeaModel):
    def __init__(
        self,
        source_child_instance_type: List[str] = None,
    ):
        self.source_child_instance_type = source_child_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_child_instance_type is not None:
            result['SourceChildInstanceType'] = self.source_child_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceChildInstanceType') is not None:
            self.source_child_instance_type = m.get('SourceChildInstanceType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds(TeaModel):
    def __init__(
        self,
        destination_route_table_id: List[str] = None,
    ):
        self.destination_route_table_id = destination_route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_route_table_id is not None:
            result['DestinationRouteTableId'] = self.destination_route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRouteTableId') is not None:
            self.destination_route_table_id = m.get('DestinationRouteTableId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds(TeaModel):
    def __init__(
        self,
        source_instance_id: List[str] = None,
    ):
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks(TeaModel):
    def __init__(
        self,
        destination_cidr_block: List[str] = None,
    ):
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds(TeaModel):
    def __init__(
        self,
        source_route_table_id: List[str] = None,
    ):
        self.source_route_table_id = source_route_table_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_route_table_id is not None:
            result['SourceRouteTableId'] = self.source_route_table_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceRouteTableId') is not None:
            self.source_route_table_id = m.get('SourceRouteTableId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet(TeaModel):
    def __init__(
        self,
        match_community: List[str] = None,
    ):
        self.match_community = match_community

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_community is not None:
            result['MatchCommunity'] = self.match_community
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCommunity') is not None:
            self.match_community = m.get('MatchCommunity')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath(TeaModel):
    def __init__(
        self,
        as_path: List[str] = None,
    ):
        self.as_path = as_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.as_path is not None:
            result['AsPath'] = self.as_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes(TeaModel):
    def __init__(
        self,
        route_type: List[str] = None,
    ):
        self.route_type = route_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes(TeaModel):
    def __init__(
        self,
        destination_child_instance_type: List[str] = None,
    ):
        self.destination_child_instance_type = destination_child_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_child_instance_type is not None:
            result['DestinationChildInstanceType'] = self.destination_child_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationChildInstanceType') is not None:
            self.destination_child_instance_type = m.get('DestinationChildInstanceType')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds(TeaModel):
    def __init__(
        self,
        destination_instance_id: List[str] = None,
    ):
        self.destination_instance_id = destination_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns(TeaModel):
    def __init__(
        self,
        match_asn: List[str] = None,
    ):
        self.match_asn = match_asn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_asn is not None:
            result['MatchAsn'] = self.match_asn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchAsn') is not None:
            self.match_asn = m.get('MatchAsn')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet(TeaModel):
    def __init__(
        self,
        operate_community: List[str] = None,
    ):
        self.operate_community = operate_community

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_community is not None:
            result['OperateCommunity'] = self.operate_community
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCommunity') is not None:
            self.operate_community = m.get('OperateCommunity')
        return self


class DescribeCenRouteMapsResponseBodyRouteMapsRouteMap(TeaModel):
    def __init__(
        self,
        route_map_id: str = None,
        status: str = None,
        transmit_direction: str = None,
        source_instance_ids_reverse_match: bool = None,
        cen_region_id: str = None,
        cen_id: str = None,
        priority: int = None,
        community_operate_mode: str = None,
        map_result: str = None,
        community_match_mode: str = None,
        description: str = None,
        as_path_match_mode: str = None,
        preference: int = None,
        destination_instance_ids_reverse_match: bool = None,
        cidr_match_mode: str = None,
        next_priority: int = None,
        source_region_ids: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds = None,
        source_child_instance_types: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes = None,
        destination_route_table_ids: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds = None,
        source_instance_ids: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds = None,
        destination_cidr_blocks: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks = None,
        source_route_table_ids: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds = None,
        match_community_set: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet = None,
        prepend_as_path: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath = None,
        route_types: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes = None,
        destination_child_instance_types: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes = None,
        destination_instance_ids: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds = None,
        match_asns: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns = None,
        operate_community_set: DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet = None,
    ):
        self.route_map_id = route_map_id
        self.status = status
        self.transmit_direction = transmit_direction
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        self.cen_region_id = cen_region_id
        self.cen_id = cen_id
        self.priority = priority
        self.community_operate_mode = community_operate_mode
        self.map_result = map_result
        self.community_match_mode = community_match_mode
        self.description = description
        self.as_path_match_mode = as_path_match_mode
        self.preference = preference
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        self.cidr_match_mode = cidr_match_mode
        self.next_priority = next_priority
        self.source_region_ids = source_region_ids
        self.source_child_instance_types = source_child_instance_types
        self.destination_route_table_ids = destination_route_table_ids
        self.source_instance_ids = source_instance_ids
        self.destination_cidr_blocks = destination_cidr_blocks
        self.source_route_table_ids = source_route_table_ids
        self.match_community_set = match_community_set
        self.prepend_as_path = prepend_as_path
        self.route_types = route_types
        self.destination_child_instance_types = destination_child_instance_types
        self.destination_instance_ids = destination_instance_ids
        self.match_asns = match_asns
        self.operate_community_set = operate_community_set

    def validate(self):
        if self.source_region_ids:
            self.source_region_ids.validate()
        if self.source_child_instance_types:
            self.source_child_instance_types.validate()
        if self.destination_route_table_ids:
            self.destination_route_table_ids.validate()
        if self.source_instance_ids:
            self.source_instance_ids.validate()
        if self.destination_cidr_blocks:
            self.destination_cidr_blocks.validate()
        if self.source_route_table_ids:
            self.source_route_table_ids.validate()
        if self.match_community_set:
            self.match_community_set.validate()
        if self.prepend_as_path:
            self.prepend_as_path.validate()
        if self.route_types:
            self.route_types.validate()
        if self.destination_child_instance_types:
            self.destination_child_instance_types.validate()
        if self.destination_instance_ids:
            self.destination_instance_ids.validate()
        if self.match_asns:
            self.match_asns.validate()
        if self.operate_community_set:
            self.operate_community_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id
        if self.status is not None:
            result['Status'] = self.status
        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction
        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match
        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode
        if self.map_result is not None:
            result['MapResult'] = self.map_result
        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode
        if self.preference is not None:
            result['Preference'] = self.preference
        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match
        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode
        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority
        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids.to_map()
        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types.to_map()
        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids.to_map()
        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids.to_map()
        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks.to_map()
        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids.to_map()
        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set.to_map()
        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path.to_map()
        if self.route_types is not None:
            result['RouteTypes'] = self.route_types.to_map()
        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types.to_map()
        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids.to_map()
        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns.to_map()
        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')
        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')
        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')
        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')
        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')
        if m.get('Preference') is not None:
            self.preference = m.get('Preference')
        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')
        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')
        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')
        if m.get('SourceRegionIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds()
            self.source_region_ids = temp_model.from_map(m['SourceRegionIds'])
        if m.get('SourceChildInstanceTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes()
            self.source_child_instance_types = temp_model.from_map(m['SourceChildInstanceTypes'])
        if m.get('DestinationRouteTableIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds()
            self.destination_route_table_ids = temp_model.from_map(m['DestinationRouteTableIds'])
        if m.get('SourceInstanceIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds()
            self.source_instance_ids = temp_model.from_map(m['SourceInstanceIds'])
        if m.get('DestinationCidrBlocks') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks()
            self.destination_cidr_blocks = temp_model.from_map(m['DestinationCidrBlocks'])
        if m.get('SourceRouteTableIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds()
            self.source_route_table_ids = temp_model.from_map(m['SourceRouteTableIds'])
        if m.get('MatchCommunitySet') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet()
            self.match_community_set = temp_model.from_map(m['MatchCommunitySet'])
        if m.get('PrependAsPath') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath()
            self.prepend_as_path = temp_model.from_map(m['PrependAsPath'])
        if m.get('RouteTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes()
            self.route_types = temp_model.from_map(m['RouteTypes'])
        if m.get('DestinationChildInstanceTypes') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes()
            self.destination_child_instance_types = temp_model.from_map(m['DestinationChildInstanceTypes'])
        if m.get('DestinationInstanceIds') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds()
            self.destination_instance_ids = temp_model.from_map(m['DestinationInstanceIds'])
        if m.get('MatchAsns') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns()
            self.match_asns = temp_model.from_map(m['MatchAsns'])
        if m.get('OperateCommunitySet') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet()
            self.operate_community_set = temp_model.from_map(m['OperateCommunitySet'])
        return self


class DescribeCenRouteMapsResponseBodyRouteMaps(TeaModel):
    def __init__(
        self,
        route_map: List[DescribeCenRouteMapsResponseBodyRouteMapsRouteMap] = None,
    ):
        self.route_map = route_map

    def validate(self):
        if self.route_map:
            for k in self.route_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteMap'] = []
        if self.route_map is not None:
            for k in self.route_map:
                result['RouteMap'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_map = []
        if m.get('RouteMap') is not None:
            for k in m.get('RouteMap'):
                temp_model = DescribeCenRouteMapsResponseBodyRouteMapsRouteMap()
                self.route_map.append(temp_model.from_map(k))
        return self


class DescribeCenRouteMapsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        route_maps: DescribeCenRouteMapsResponseBodyRouteMaps = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.route_maps = route_maps

    def validate(self):
        if self.route_maps:
            self.route_maps.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RouteMaps') is not None:
            temp_model = DescribeCenRouteMapsResponseBodyRouteMaps()
            self.route_maps = temp_model.from_map(m['RouteMaps'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCensResponseBodyCensCenTagsTag(TeaModel):
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


class DescribeCensResponseBodyCensCenTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeCensResponseBodyCensCenTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeCensResponseBodyCensCenTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBodyCensCenCenBandwidthPackageIds(TeaModel):
    def __init__(
        self,
        cen_bandwidth_package_id: List[str] = None,
    ):
        self.cen_bandwidth_package_id = cen_bandwidth_package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_bandwidth_package_id is not None:
            result['CenBandwidthPackageId'] = self.cen_bandwidth_package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenBandwidthPackageId') is not None:
            self.cen_bandwidth_package_id = m.get('CenBandwidthPackageId')
        return self


class DescribeCensResponseBodyCensCen(TeaModel):
    def __init__(
        self,
        status: str = None,
        creation_time: str = None,
        description: str = None,
        cen_id: str = None,
        protection_level: str = None,
        name: str = None,
        tags: DescribeCensResponseBodyCensCenTags = None,
        cen_bandwidth_package_ids: DescribeCensResponseBodyCensCenCenBandwidthPackageIds = None,
    ):
        self.status = status
        self.creation_time = creation_time
        self.description = description
        self.cen_id = cen_id
        self.protection_level = protection_level
        self.name = name
        self.tags = tags
        self.cen_bandwidth_package_ids = cen_bandwidth_package_ids

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.cen_bandwidth_package_ids:
            self.cen_bandwidth_package_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.cen_bandwidth_package_ids is not None:
            result['CenBandwidthPackageIds'] = self.cen_bandwidth_package_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            temp_model = DescribeCensResponseBodyCensCenTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('CenBandwidthPackageIds') is not None:
            temp_model = DescribeCensResponseBodyCensCenCenBandwidthPackageIds()
            self.cen_bandwidth_package_ids = temp_model.from_map(m['CenBandwidthPackageIds'])
        return self


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(
        self,
        cen: List[DescribeCensResponseBodyCensCen] = None,
    ):
        self.cen = cen

    def validate(self):
        if self.cen:
            for k in self.cen:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cen'] = []
        if self.cen is not None:
            for k in self.cen:
                result['Cen'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cen = []
        if m.get('Cen') is not None:
            for k in m.get('Cen'):
                temp_model = DescribeCensResponseBodyCensCen()
                self.cen.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        cens: DescribeCensResponseBodyCens = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.cens = cens

    def validate(self):
        if self.cens:
            self.cens.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cens is not None:
            result['Cens'] = self.cens.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Cens') is not None:
            temp_model = DescribeCensResponseBodyCens()
            self.cens = temp_model.from_map(m['Cens'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks(TeaModel):
    def __init__(
        self,
        vbr_health_check: List[DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck] = None,
    ):
        self.vbr_health_check = vbr_health_check

    def validate(self):
        if self.vbr_health_check:
            for k in self.vbr_health_check:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VbrHealthCheck'] = []
        if self.vbr_health_check is not None:
            for k in self.vbr_health_check:
                result['VbrHealthCheck'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vbr_health_check = []
        if m.get('VbrHealthCheck') is not None:
            for k in m.get('VbrHealthCheck'):
                temp_model = DescribeCenVbrHealthCheckResponseBodyVbrHealthChecksVbrHealthCheck()
                self.vbr_health_check.append(temp_model.from_map(k))
        return self


class DescribeCenVbrHealthCheckResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        vbr_health_checks: DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.vbr_health_checks = vbr_health_checks

    def validate(self):
        if self.vbr_health_checks:
            self.vbr_health_checks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vbr_health_checks is not None:
            result['VbrHealthChecks'] = self.vbr_health_checks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VbrHealthChecks') is not None:
            temp_model = DescribeCenVbrHealthCheckResponseBodyVbrHealthChecks()
            self.vbr_health_checks = temp_model.from_map(m['VbrHealthChecks'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        return self


class DescribeChildInstanceRegionsResponseBodyRegionsRegion(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeChildInstanceRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeChildInstanceRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeChildInstanceRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeChildInstanceRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeChildInstanceRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeChildInstanceRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeFlowlogsResponseBodyFlowLogsFlowLog(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeFlowlogsResponseBodyFlowLogs(TeaModel):
    def __init__(
        self,
        flow_log: List[DescribeFlowlogsResponseBodyFlowLogsFlowLog] = None,
    ):
        self.flow_log = flow_log

    def validate(self):
        if self.flow_log:
            for k in self.flow_log:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FlowLog'] = []
        if self.flow_log is not None:
            for k in self.flow_log:
                result['FlowLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_log = []
        if m.get('FlowLog') is not None:
            for k in m.get('FlowLog'):
                temp_model = DescribeFlowlogsResponseBodyFlowLogsFlowLog()
                self.flow_log.append(temp_model.from_map(k))
        return self


class DescribeFlowlogsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: str = None,
        page_number: str = None,
        request_id: str = None,
        total_count: str = None,
        success: str = None,
        flow_logs: DescribeFlowlogsResponseBodyFlowLogs = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.request_id = request_id
        self.total_count = total_count
        self.success = success
        self.flow_logs = flow_logs

    def validate(self):
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.success is not None:
            result['Success'] = self.success
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('FlowLogs') is not None:
            temp_model = DescribeFlowlogsResponseBodyFlowLogs()
            self.flow_logs = temp_model.from_map(m['FlowLogs'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeGeographicRegionMembershipResponseBodyRegionIds(TeaModel):
    def __init__(
        self,
        region_id: List[DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId] = None,
    ):
        self.region_id = region_id

    def validate(self):
        if self.region_id:
            for k in self.region_id:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionId'] = []
        if self.region_id is not None:
            for k in self.region_id:
                result['RegionId'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_id = []
        if m.get('RegionId') is not None:
            for k in m.get('RegionId'):
                temp_model = DescribeGeographicRegionMembershipResponseBodyRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k))
        return self


class DescribeGeographicRegionMembershipResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        region_ids: DescribeGeographicRegionMembershipResponseBodyRegionIds = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.region_ids = region_ids

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RegionIds') is not None:
            temp_model = DescribeGeographicRegionMembershipResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m['RegionIds'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeGrantRulesToCenResponseBodyGrantRules(TeaModel):
    def __init__(
        self,
        grant_rule: List[DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule] = None,
    ):
        self.grant_rule = grant_rule

    def validate(self):
        if self.grant_rule:
            for k in self.grant_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GrantRule'] = []
        if self.grant_rule is not None:
            for k in self.grant_rule:
                result['GrantRule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_rule = []
        if m.get('GrantRule') is not None:
            for k in m.get('GrantRule'):
                temp_model = DescribeGrantRulesToCenResponseBodyGrantRulesGrantRule()
                self.grant_rule.append(temp_model.from_map(k))
        return self


class DescribeGrantRulesToCenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        grant_rules: DescribeGrantRulesToCenResponseBodyGrantRules = None,
    ):
        self.request_id = request_id
        self.grant_rules = grant_rules

    def validate(self):
        if self.grant_rules:
            self.grant_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.grant_rules is not None:
            result['GrantRules'] = self.grant_rules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GrantRules') is not None:
            temp_model = DescribeGrantRulesToCenResponseBodyGrantRules()
            self.grant_rules = temp_model.from_map(m['GrantRules'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts(TeaModel):
    def __init__(
        self,
        conflict: List[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict] = None,
    ):
        self.conflict = conflict

    def validate(self):
        if self.conflict:
            for k in self.conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conflict'] = []
        if self.conflict is not None:
            for k in self.conflict:
                result['Conflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflict = []
        if m.get('Conflict') is not None:
            for k in m.get('Conflict'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflictsConflict()
                self.conflict.append(temp_model.from_map(k))
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry(TeaModel):
    def __init__(
        self,
        next_hop_id: str = None,
        publish_status: str = None,
        child_instance_route_table_id: str = None,
        next_hop_type: str = None,
        operational_mode: bool = None,
        destination_cidr_block: str = None,
        route_type: str = None,
        conflicts: DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts = None,
    ):
        self.next_hop_id = next_hop_id
        self.publish_status = publish_status
        self.child_instance_route_table_id = child_instance_route_table_id
        self.next_hop_type = next_hop_type
        self.operational_mode = operational_mode
        self.destination_cidr_block = destination_cidr_block
        self.route_type = route_type
        self.conflicts = conflicts

    def validate(self):
        if self.conflicts:
            self.conflicts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id
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
        if self.conflicts is not None:
            result['Conflicts'] = self.conflicts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')
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
        if m.get('Conflicts') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntryConflicts()
            self.conflicts = temp_model.from_map(m['Conflicts'])
        return self


class DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries(TeaModel):
    def __init__(
        self,
        published_route_entry: List[DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry] = None,
    ):
        self.published_route_entry = published_route_entry

    def validate(self):
        if self.published_route_entry:
            for k in self.published_route_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublishedRouteEntry'] = []
        if self.published_route_entry is not None:
            for k in self.published_route_entry:
                result['PublishedRouteEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.published_route_entry = []
        if m.get('PublishedRouteEntry') is not None:
            for k in m.get('PublishedRouteEntry'):
                temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntriesPublishedRouteEntry()
                self.published_route_entry.append(temp_model.from_map(k))
        return self


class DescribePublishedRouteEntriesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        published_route_entries: DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.published_route_entries = published_route_entries

    def validate(self):
        if self.published_route_entries:
            self.published_route_entries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.published_route_entries is not None:
            result['PublishedRouteEntries'] = self.published_route_entries.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PublishedRouteEntries') is not None:
            temp_model = DescribePublishedRouteEntriesResponseBodyPublishedRouteEntries()
            self.published_route_entries = temp_model.from_map(m['PublishedRouteEntries'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeRouteConflictResponseBodyRouteConflictsRouteConflict(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeRouteConflictResponseBodyRouteConflicts(TeaModel):
    def __init__(
        self,
        route_conflict: List[DescribeRouteConflictResponseBodyRouteConflictsRouteConflict] = None,
    ):
        self.route_conflict = route_conflict

    def validate(self):
        if self.route_conflict:
            for k in self.route_conflict:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteConflict'] = []
        if self.route_conflict is not None:
            for k in self.route_conflict:
                result['RouteConflict'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_conflict = []
        if m.get('RouteConflict') is not None:
            for k in m.get('RouteConflict'):
                temp_model = DescribeRouteConflictResponseBodyRouteConflictsRouteConflict()
                self.route_conflict.append(temp_model.from_map(k))
        return self


class DescribeRouteConflictResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        route_conflicts: DescribeRouteConflictResponseBodyRouteConflicts = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.route_conflicts = route_conflicts

    def validate(self):
        if self.route_conflicts:
            self.route_conflicts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.route_conflicts is not None:
            result['RouteConflicts'] = self.route_conflicts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RouteConflicts') is not None:
            temp_model = DescribeRouteConflictResponseBodyRouteConflicts()
            self.route_conflicts = temp_model.from_map(m['RouteConflicts'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs(TeaModel):
    def __init__(
        self,
        cidr: List[str] = None,
    ):
        self.cidr = cidr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry(TeaModel):
    def __init__(
        self,
        status: str = None,
        host: str = None,
        description: str = None,
        host_vpc_id: str = None,
        cen_id: str = None,
        access_region_id: str = None,
        host_region_id: str = None,
        update_interval: str = None,
        cidrs: DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs = None,
    ):
        self.status = status
        self.host = host
        self.description = description
        self.host_vpc_id = host_vpc_id
        self.cen_id = cen_id
        self.access_region_id = access_region_id
        self.host_region_id = host_region_id
        self.update_interval = update_interval
        self.cidrs = cidrs

    def validate(self):
        if self.cidrs:
            self.cidrs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.host is not None:
            result['Host'] = self.host
        if self.description is not None:
            result['Description'] = self.description
        if self.host_vpc_id is not None:
            result['HostVpcId'] = self.host_vpc_id
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.access_region_id is not None:
            result['AccessRegionId'] = self.access_region_id
        if self.host_region_id is not None:
            result['HostRegionId'] = self.host_region_id
        if self.update_interval is not None:
            result['UpdateInterval'] = self.update_interval
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs.to_map()
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
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('AccessRegionId') is not None:
            self.access_region_id = m.get('AccessRegionId')
        if m.get('HostRegionId') is not None:
            self.host_region_id = m.get('HostRegionId')
        if m.get('UpdateInterval') is not None:
            self.update_interval = m.get('UpdateInterval')
        if m.get('Cidrs') is not None:
            temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntryCidrs()
            self.cidrs = temp_model.from_map(m['Cidrs'])
        return self


class DescribeRouteServicesInCenResponseBodyRouteServiceEntries(TeaModel):
    def __init__(
        self,
        route_service_entry: List[DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry] = None,
    ):
        self.route_service_entry = route_service_entry

    def validate(self):
        if self.route_service_entry:
            for k in self.route_service_entry:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RouteServiceEntry'] = []
        if self.route_service_entry is not None:
            for k in self.route_service_entry:
                result['RouteServiceEntry'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_service_entry = []
        if m.get('RouteServiceEntry') is not None:
            for k in m.get('RouteServiceEntry'):
                temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntriesRouteServiceEntry()
                self.route_service_entry.append(temp_model.from_map(k))
        return self


class DescribeRouteServicesInCenResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_count: int = None,
        route_service_entries: DescribeRouteServicesInCenResponseBodyRouteServiceEntries = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_count = total_count
        self.route_service_entries = route_service_entries

    def validate(self):
        if self.route_service_entries:
            self.route_service_entries.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.route_service_entries is not None:
            result['RouteServiceEntries'] = self.route_service_entries.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RouteServiceEntries') is not None:
            temp_model = DescribeRouteServicesInCenResponseBodyRouteServiceEntries()
            self.route_service_entries = temp_model.from_map(m['RouteServiceEntries'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.name = name
        self.description = description
        self.protection_level = protection_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        success: str = None,
        request_id: str = None,
    ):
        self.success = success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.host_vpc_id = host_vpc_id
        self.description = description
        self.access_region_ids = access_region_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.cen_id = cen_id
        self.local_region_id = local_region_id
        self.opposite_region_id = opposite_region_id
        self.bandwidth_limit = bandwidth_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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


