# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ActivateOfficeSiteResponseBody(TeaModel):
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


class ActivateOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateOfficeSiteResponseBody = None,
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
            temp_model = ActivateOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserToDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.desktop_group_id = desktop_group_id
        self.desktop_group_ids = desktop_group_ids
        self.end_user_ids = end_user_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddUserToDesktopGroupResponseBody(TeaModel):
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


class AddUserToDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserToDesktopGroupResponseBody = None,
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
            temp_model = AddUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyCoordinationForMonitoringRequestResourceCandidates(TeaModel):
    def __init__(
        self,
        owner_ali_uid: int = None,
        owner_end_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_properties: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        self.owner_ali_uid = owner_ali_uid
        self.owner_end_user_id = owner_end_user_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_properties = resource_properties
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        if self.owner_end_user_id is not None:
            result['OwnerEndUserId'] = self.owner_end_user_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_properties is not None:
            result['ResourceProperties'] = self.resource_properties
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        if m.get('OwnerEndUserId') is not None:
            self.owner_end_user_id = m.get('OwnerEndUserId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceProperties') is not None:
            self.resource_properties = m.get('ResourceProperties')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ApplyCoordinationForMonitoringRequest(TeaModel):
    def __init__(
        self,
        coordinate_policy_type: str = None,
        end_user_id: str = None,
        initiator_type: str = None,
        region_id: str = None,
        resource_candidates: List[ApplyCoordinationForMonitoringRequestResourceCandidates] = None,
        uuid: str = None,
    ):
        self.coordinate_policy_type = coordinate_policy_type
        self.end_user_id = end_user_id
        self.initiator_type = initiator_type
        self.region_id = region_id
        self.resource_candidates = resource_candidates
        self.uuid = uuid

    def validate(self):
        if self.resource_candidates:
            for k in self.resource_candidates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinate_policy_type is not None:
            result['CoordinatePolicyType'] = self.coordinate_policy_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.initiator_type is not None:
            result['InitiatorType'] = self.initiator_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourceCandidates'] = []
        if self.resource_candidates is not None:
            for k in self.resource_candidates:
                result['ResourceCandidates'].append(k.to_map() if k else None)
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatePolicyType') is not None:
            self.coordinate_policy_type = m.get('CoordinatePolicyType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InitiatorType') is not None:
            self.initiator_type = m.get('InitiatorType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_candidates = []
        if m.get('ResourceCandidates') is not None:
            for k in m.get('ResourceCandidates'):
                temp_model = ApplyCoordinationForMonitoringRequestResourceCandidates()
                self.resource_candidates.append(temp_model.from_map(k))
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels(TeaModel):
    def __init__(
        self,
        co_id: str = None,
        coordinate_status: str = None,
        coordinate_ticket: str = None,
        initiator_type: str = None,
        owner_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.co_id = co_id
        self.coordinate_status = coordinate_status
        self.coordinate_ticket = coordinate_ticket
        self.initiator_type = initiator_type
        self.owner_user_id = owner_user_id
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_id is not None:
            result['CoId'] = self.co_id
        if self.coordinate_status is not None:
            result['CoordinateStatus'] = self.coordinate_status
        if self.coordinate_ticket is not None:
            result['CoordinateTicket'] = self.coordinate_ticket
        if self.initiator_type is not None:
            result['InitiatorType'] = self.initiator_type
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')
        if m.get('CoordinateStatus') is not None:
            self.coordinate_status = m.get('CoordinateStatus')
        if m.get('CoordinateTicket') is not None:
            self.coordinate_ticket = m.get('CoordinateTicket')
        if m.get('InitiatorType') is not None:
            self.initiator_type = m.get('InitiatorType')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class ApplyCoordinationForMonitoringResponseBody(TeaModel):
    def __init__(
        self,
        coordinate_flow_models: List[ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels] = None,
        request_id: str = None,
    ):
        self.coordinate_flow_models = coordinate_flow_models
        self.request_id = request_id

    def validate(self):
        if self.coordinate_flow_models:
            for k in self.coordinate_flow_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoordinateFlowModels'] = []
        if self.coordinate_flow_models is not None:
            for k in self.coordinate_flow_models:
                result['CoordinateFlowModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordinate_flow_models = []
        if m.get('CoordinateFlowModels') is not None:
            for k in m.get('CoordinateFlowModels'):
                temp_model = ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels()
                self.coordinate_flow_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyCoordinationForMonitoringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCoordinationForMonitoringResponseBody = None,
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
            temp_model = ApplyCoordinationForMonitoringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveFotaUpdateRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        desktop_id: str = None,
        region_id: str = None,
    ):
        self.app_version = app_version
        self.desktop_id = desktop_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ApproveFotaUpdateResponseBody(TeaModel):
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


class ApproveFotaUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveFotaUpdateResponseBody = None,
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
            temp_model = ApproveFotaUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateNetworkPackageRequest(TeaModel):
    def __init__(
        self,
        network_package_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.network_package_id = network_package_id
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateNetworkPackageResponseBody(TeaModel):
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


class AssociateNetworkPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateNetworkPackageResponseBody = None,
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
            temp_model = AssociateNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCenRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        office_site_id: str = None,
        region_id: str = None,
        verify_code: str = None,
    ):
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.office_site_id = office_site_id
        self.region_id = region_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class AttachCenResponseBody(TeaModel):
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


class AttachCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachCenResponseBody = None,
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
            temp_model = AttachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCoordinationForMonitoringRequest(TeaModel):
    def __init__(
        self,
        co_ids: List[str] = None,
        end_user_id: str = None,
        region_id: str = None,
        user_type: str = None,
    ):
        self.co_ids = co_ids
        self.end_user_id = end_user_id
        self.region_id = region_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_ids is not None:
            result['CoIds'] = self.co_ids
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoIds') is not None:
            self.co_ids = m.get('CoIds')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CancelCoordinationForMonitoringResponseBody(TeaModel):
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


class CancelCoordinationForMonitoringResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCoordinationForMonitoringResponseBody = None,
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
            temp_model = CancelCoordinationForMonitoringResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCopyImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        region_id: str = None,
    ):
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelCopyImageResponseBody(TeaModel):
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


class CancelCopyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCopyImageResponseBody = None,
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
            temp_model = CancelCopyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClonePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        policy_group_id: str = None,
        region_id: str = None,
    ):
        self.name = name
        self.policy_group_id = policy_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ClonePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClonePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClonePolicyGroupResponseBody = None,
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
            temp_model = ClonePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigADConnectorTrustRequest(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
        trust_key: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id
        self.trust_key = trust_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trust_key is not None:
            result['TrustKey'] = self.trust_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TrustKey') is not None:
            self.trust_key = m.get('TrustKey')
        return self


class ConfigADConnectorTrustResponseBody(TeaModel):
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


class ConfigADConnectorTrustResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigADConnectorTrustResponseBody = None,
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
            temp_model = ConfigADConnectorTrustResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigADConnectorUserRequest(TeaModel):
    def __init__(
        self,
        domain_password: str = None,
        domain_user_name: str = None,
        ouname: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.ouname = ouname
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.ouname is not None:
            result['OUName'] = self.ouname
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigADConnectorUserResponseBody(TeaModel):
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


class ConfigADConnectorUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigADConnectorUserResponseBody = None,
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
            temp_model = ConfigADConnectorUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyImageRequest(TeaModel):
    def __init__(
        self,
        destination_description: str = None,
        destination_image_name: str = None,
        destination_region_id: str = None,
        image_id: str = None,
        region_id: str = None,
    ):
        self.destination_description = destination_description
        self.destination_image_name = destination_image_name
        self.destination_region_id = destination_region_id
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_description is not None:
            result['DestinationDescription'] = self.destination_description
        if self.destination_image_name is not None:
            result['DestinationImageName'] = self.destination_image_name
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDescription') is not None:
            self.destination_description = m.get('DestinationDescription')
        if m.get('DestinationImageName') is not None:
            self.destination_image_name = m.get('DestinationImageName')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CopyImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CopyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyImageResponseBody = None,
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
            temp_model = CopyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        directory_name: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        mfa_enabled: bool = None,
        region_id: str = None,
        specification: int = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
        v_switch_id: List[str] = None,
    ):
        self.desktop_access_type = desktop_access_type
        self.directory_name = directory_name
        self.dns_address = dns_address
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.enable_admin_access = enable_admin_access
        self.mfa_enabled = mfa_enabled
        self.region_id = region_id
        self.specification = specification
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateADConnectorDirectoryResponseBodyAdConnectors(TeaModel):
    def __init__(
        self,
        address: str = None,
    ):
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class CreateADConnectorDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        ad_connectors: List[CreateADConnectorDirectoryResponseBodyAdConnectors] = None,
        directory_id: str = None,
        request_id: str = None,
        trust_password: str = None,
    ):
        self.ad_connectors = ad_connectors
        self.directory_id = directory_id
        self.request_id = request_id
        self.trust_password = trust_password

    def validate(self):
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ad_connectors = []
        if m.get('AdConnectors') is not None:
            for k in m.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseBodyAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateADConnectorDirectoryResponseBody = None,
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
            temp_model = CreateADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateADConnectorOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        ad_hostname: str = None,
        bandwidth: int = None,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        desktop_access_type: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        mfa_enabled: bool = None,
        office_site_name: str = None,
        protocol_type: str = None,
        region_id: str = None,
        specification: int = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
        verify_code: str = None,
    ):
        self.ad_hostname = ad_hostname
        self.bandwidth = bandwidth
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.cidr_block = cidr_block
        self.desktop_access_type = desktop_access_type
        self.dns_address = dns_address
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.enable_admin_access = enable_admin_access
        self.enable_internet_access = enable_internet_access
        self.mfa_enabled = mfa_enabled
        self.office_site_name = office_site_name
        self.protocol_type = protocol_type
        self.region_id = region_id
        self.specification = specification
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class CreateADConnectorOfficeSiteResponseBody(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        request_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateADConnectorOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateADConnectorOfficeSiteResponseBody = None,
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
            temp_model = CreateADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBundleRequest(TeaModel):
    def __init__(
        self,
        bundle_name: str = None,
        description: str = None,
        desktop_type: str = None,
        image_id: str = None,
        language: str = None,
        region_id: str = None,
        root_disk_performance_level: str = None,
        root_disk_size_gib: int = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: List[int] = None,
    ):
        self.bundle_name = bundle_name
        self.description = description
        self.desktop_type = desktop_type
        self.image_id = image_id
        self.language = language
        self.region_id = region_id
        self.root_disk_performance_level = root_disk_performance_level
        self.root_disk_size_gib = root_disk_size_gib
        self.user_disk_performance_level = user_disk_performance_level
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.language is not None:
            result['Language'] = self.language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class CreateBundleResponseBody(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        request_id: str = None,
    ):
        self.bundle_id = bundle_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBundleResponseBody = None,
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
            temp_model = CreateBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        all_classify_users: bool = None,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        auto_pay: bool = None,
        bind_amount: int = None,
        bundle_id: str = None,
        charge_type: str = None,
        classify: str = None,
        client_token: str = None,
        comments: str = None,
        connect_duration: int = None,
        default_init_desktop_count: int = None,
        desktop_group_name: str = None,
        directory_id: str = None,
        end_user_ids: List[str] = None,
        idle_disconnect_duration: int = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        min_desktops_count: int = None,
        office_site_id: str = None,
        own_type: int = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        ratio_threshold: float = None,
        region_id: str = None,
        reset_type: int = None,
        scale_strategy_id: str = None,
        stop_duration: int = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        vpc_id: str = None,
    ):
        self.all_classify_users = all_classify_users
        self.allow_auto_setup = allow_auto_setup
        self.allow_buffer_count = allow_buffer_count
        self.auto_pay = auto_pay
        self.bind_amount = bind_amount
        self.bundle_id = bundle_id
        self.charge_type = charge_type
        self.classify = classify
        self.client_token = client_token
        self.comments = comments
        self.connect_duration = connect_duration
        self.default_init_desktop_count = default_init_desktop_count
        self.desktop_group_name = desktop_group_name
        self.directory_id = directory_id
        self.end_user_ids = end_user_ids
        self.idle_disconnect_duration = idle_disconnect_duration
        self.keep_duration = keep_duration
        self.load_policy = load_policy
        self.max_desktops_count = max_desktops_count
        self.min_desktops_count = min_desktops_count
        self.office_site_id = office_site_id
        self.own_type = own_type
        self.period = period
        self.period_unit = period_unit
        self.policy_group_id = policy_group_id
        self.ratio_threshold = ratio_threshold
        self.region_id = region_id
        self.reset_type = reset_type
        self.scale_strategy_id = scale_strategy_id
        self.stop_duration = stop_duration
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_classify_users is not None:
            result['AllClassifyUsers'] = self.all_classify_users
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.default_init_desktop_count is not None:
            result['DefaultInitDesktopCount'] = self.default_init_desktop_count
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllClassifyUsers') is not None:
            self.all_classify_users = m.get('AllClassifyUsers')
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('DefaultInitDesktopCount') is not None:
            self.default_init_desktop_count = m.get('DefaultInitDesktopCount')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateDesktopGroupResponseBody(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        order_ids: List[str] = None,
        request_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.order_ids = order_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDesktopGroupResponseBody = None,
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
            temp_model = CreateDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDesktopsRequestTag(TeaModel):
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


class CreateDesktopsRequestUserCommands(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_encoding: str = None,
        content_type: str = None,
    ):
        self.content = content
        self.content_encoding = content_encoding
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        return self


class CreateDesktopsRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bundle_id: str = None,
        charge_type: str = None,
        desktop_name: str = None,
        desktop_name_suffix: bool = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
        group_id: str = None,
        hostname: str = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
        region_id: str = None,
        tag: List[CreateDesktopsRequestTag] = None,
        user_assign_mode: str = None,
        user_commands: List[CreateDesktopsRequestUserCommands] = None,
        user_name: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        vpc_id: str = None,
    ):
        self.amount = amount
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.bundle_id = bundle_id
        self.charge_type = charge_type
        self.desktop_name = desktop_name
        self.desktop_name_suffix = desktop_name_suffix
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.group_id = group_id
        self.hostname = hostname
        self.office_site_id = office_site_id
        self.period = period
        self.period_unit = period_unit
        self.policy_group_id = policy_group_id
        self.promotion_id = promotion_id
        self.region_id = region_id
        self.tag = tag
        self.user_assign_mode = user_assign_mode
        self.user_commands = user_commands
        self.user_name = user_name
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.user_commands:
            for k in self.user_commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_name_suffix is not None:
            result['DesktopNameSuffix'] = self.desktop_name_suffix
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_assign_mode is not None:
            result['UserAssignMode'] = self.user_assign_mode
        result['UserCommands'] = []
        if self.user_commands is not None:
            for k in self.user_commands:
                result['UserCommands'].append(k.to_map() if k else None)
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopNameSuffix') is not None:
            self.desktop_name_suffix = m.get('DesktopNameSuffix')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserAssignMode') is not None:
            self.user_assign_mode = m.get('UserAssignMode')
        self.user_commands = []
        if m.get('UserCommands') is not None:
            for k in m.get('UserCommands'):
                temp_model = CreateDesktopsRequestUserCommands()
                self.user_commands.append(temp_model.from_map(k))
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDesktopsResponseBody = None,
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
            temp_model = CreateDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiskEncryptionServiceRequest(TeaModel):
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


class CreateDiskEncryptionServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDiskEncryptionServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDiskEncryptionServiceResponseBody = None,
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
            temp_model = CreateDiskEncryptionServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDriveRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        domain_id: str = None,
        drive_name: str = None,
        external_domain_id: str = None,
        profile_roaming: bool = None,
        region_id: str = None,
        resource_type: str = None,
        total_size: int = None,
        type: str = None,
        used_size: int = None,
        user_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.description = description
        self.domain_id = domain_id
        self.drive_name = drive_name
        self.external_domain_id = external_domain_id
        self.profile_roaming = profile_roaming
        self.region_id = region_id
        self.resource_type = resource_type
        self.total_size = total_size
        self.type = type
        self.used_size = used_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.drive_name is not None:
            result['DriveName'] = self.drive_name
        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id
        if self.profile_roaming is not None:
            result['ProfileRoaming'] = self.profile_roaming
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.type is not None:
            result['Type'] = self.type
        if self.used_size is not None:
            result['UsedSize'] = self.used_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DriveName') is not None:
            self.drive_name = m.get('DriveName')
        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')
        if m.get('ProfileRoaming') is not None:
            self.profile_roaming = m.get('ProfileRoaming')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateDriveResponseBodyDrive(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        external_drive_id: str = None,
        external_user_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        name: str = None,
        profile_roaming: bool = None,
        status: str = None,
        total_size: int = None,
        type: str = None,
        used_size: int = None,
        user_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.description = description
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.external_drive_id = external_drive_id
        self.external_user_id = external_user_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.profile_roaming = profile_roaming
        self.status = status
        self.total_size = total_size
        self.type = type
        self.used_size = used_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.drive_id is not None:
            result['DriveId'] = self.drive_id
        if self.external_drive_id is not None:
            result['ExternalDriveId'] = self.external_drive_id
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.profile_roaming is not None:
            result['ProfileRoaming'] = self.profile_roaming
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.type is not None:
            result['Type'] = self.type
        if self.used_size is not None:
            result['UsedSize'] = self.used_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')
        if m.get('ExternalDriveId') is not None:
            self.external_drive_id = m.get('ExternalDriveId')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProfileRoaming') is not None:
            self.profile_roaming = m.get('ProfileRoaming')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateDriveResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        drive: CreateDriveResponseBodyDrive = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.drive = drive
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.drive:
            self.drive.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.drive is not None:
            result['Drive'] = self.drive.to_map()
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
        if m.get('Drive') is not None:
            temp_model = CreateDriveResponseBodyDrive()
            self.drive = temp_model.from_map(m['Drive'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDriveResponseBody = None,
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
            temp_model = CreateDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        auto_clean_userdata: bool = None,
        description: str = None,
        desktop_id: str = None,
        disk_type: str = None,
        image_name: str = None,
        image_resource_type: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        snapshot_ids: List[str] = None,
    ):
        self.auto_clean_userdata = auto_clean_userdata
        self.description = description
        self.desktop_id = desktop_id
        self.disk_type = disk_type
        self.image_name = image_name
        self.image_resource_type = image_resource_type
        self.region_id = region_id
        self.snapshot_id = snapshot_id
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_clean_userdata is not None:
            result['AutoCleanUserdata'] = self.auto_clean_userdata
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_resource_type is not None:
            result['ImageResourceType'] = self.image_resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanUserdata') is not None:
            self.auto_clean_userdata = m.get('AutoCleanUserdata')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageResourceType') is not None:
            self.image_resource_type = m.get('ImageResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageResponseBody = None,
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
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNASFileSystemRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        name: str = None,
        office_site_id: str = None,
        region_id: str = None,
        storage_type: str = None,
    ):
        self.description = description
        self.encrypt_type = encrypt_type
        self.name = name
        self.office_site_id = office_site_id
        self.region_id = region_id
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.name is not None:
            result['Name'] = self.name
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class CreateNASFileSystemResponseBody(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_name: str = None,
        mount_target_domain: str = None,
        office_site_id: str = None,
        request_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.mount_target_domain = mount_target_domain
        self.office_site_id = office_site_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNASFileSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNASFileSystemResponseBody = None,
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
            temp_model = CreateNASFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkPackageRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth: int = None,
        internet_charge_type: str = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.bandwidth = bandwidth
        self.internet_charge_type = internet_charge_type
        self.office_site_id = office_site_id
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNetworkPackageResponseBody(TeaModel):
    def __init__(
        self,
        network_package_id: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.network_package_id = network_package_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNetworkPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetworkPackageResponseBody = None,
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
            temp_model = CreateNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreatePolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        type: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreatePolicyGroupRequestClientType(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        self.client_type = client_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreatePolicyGroupRequestUsbSupplyRedirectRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_class: str = None,
        device_subclass: str = None,
        product_id: str = None,
        usb_redirect_type: int = None,
        usb_rule_type: int = None,
        vendor_id: str = None,
    ):
        self.description = description
        self.device_class = device_class
        self.device_subclass = device_subclass
        self.product_id = product_id
        self.usb_redirect_type = usb_redirect_type
        self.usb_rule_type = usb_rule_type
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_class is not None:
            result['DeviceClass'] = self.device_class
        if self.device_subclass is not None:
            result['DeviceSubclass'] = self.device_subclass
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.usb_redirect_type is not None:
            result['UsbRedirectType'] = self.usb_redirect_type
        if self.usb_rule_type is not None:
            result['UsbRuleType'] = self.usb_rule_type
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')
        if m.get('DeviceSubclass') is not None:
            self.device_subclass = m.get('DeviceSubclass')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UsbRedirectType') is not None:
            self.usb_redirect_type = m.get('UsbRedirectType')
        if m.get('UsbRuleType') is not None:
            self.usb_rule_type = m.get('UsbRuleType')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rule: List[CreatePolicyGroupRequestAuthorizeAccessPolicyRule] = None,
        authorize_security_policy_rule: List[CreatePolicyGroupRequestAuthorizeSecurityPolicyRule] = None,
        camera_redirect: str = None,
        client_type: List[CreatePolicyGroupRequestClientType] = None,
        clipboard: str = None,
        domain_list: str = None,
        gpu_acceleration: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        name: str = None,
        net_redirect: str = None,
        preempt_login: str = None,
        preempt_login_user: List[str] = None,
        printer_redirection: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        recording: str = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: int = None,
        recording_start_time: str = None,
        region_id: str = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[CreatePolicyGroupRequestUsbSupplyRedirectRule] = None,
        visual_quality: str = None,
        watermark: str = None,
        watermark_transparency: str = None,
        watermark_type: str = None,
    ):
        self.app_content_protection = app_content_protection
        self.authorize_access_policy_rule = authorize_access_policy_rule
        self.authorize_security_policy_rule = authorize_security_policy_rule
        self.camera_redirect = camera_redirect
        self.client_type = client_type
        self.clipboard = clipboard
        self.domain_list = domain_list
        self.gpu_acceleration = gpu_acceleration
        self.html_5access = html_5access
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.name = name
        self.net_redirect = net_redirect
        self.preempt_login = preempt_login
        self.preempt_login_user = preempt_login_user
        self.printer_redirection = printer_redirection
        self.record_content = record_content
        self.record_content_expires = record_content_expires
        self.recording = recording
        self.recording_end_time = recording_end_time
        self.recording_expires = recording_expires
        self.recording_fps = recording_fps
        self.recording_start_time = recording_start_time
        self.region_id = region_id
        self.usb_redirect = usb_redirect
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.visual_quality = visual_quality
        self.watermark = watermark
        self.watermark_transparency = watermark_transparency
        self.watermark_type = watermark_type

    def validate(self):
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.client_type:
            for k in self.client_type:
                if k:
                    k.validate()
        if self.usb_supply_redirect_rule:
            for k in self.usb_supply_redirect_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        result['ClientType'] = []
        if self.client_type is not None:
            for k in self.client_type:
                result['ClientType'].append(k.to_map() if k else None)
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.name is not None:
            result['Name'] = self.name
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        if self.printer_redirection is not None:
            result['PrinterRedirection'] = self.printer_redirection
        if self.record_content is not None:
            result['RecordContent'] = self.record_content
        if self.record_content_expires is not None:
            result['RecordContentExpires'] = self.record_content_expires
        if self.recording is not None:
            result['Recording'] = self.recording
        if self.recording_end_time is not None:
            result['RecordingEndTime'] = self.recording_end_time
        if self.recording_expires is not None:
            result['RecordingExpires'] = self.recording_expires
        if self.recording_fps is not None:
            result['RecordingFps'] = self.recording_fps
        if self.recording_start_time is not None:
            result['RecordingStartTime'] = self.recording_start_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        result['UsbSupplyRedirectRule'] = []
        if self.usb_supply_redirect_rule is not None:
            for k in self.usb_supply_redirect_rule:
                result['UsbSupplyRedirectRule'].append(k.to_map() if k else None)
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = CreatePolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        self.client_type = []
        if m.get('ClientType') is not None:
            for k in m.get('ClientType'):
                temp_model = CreatePolicyGroupRequestClientType()
                self.client_type.append(temp_model.from_map(k))
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        if m.get('PrinterRedirection') is not None:
            self.printer_redirection = m.get('PrinterRedirection')
        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')
        if m.get('RecordContentExpires') is not None:
            self.record_content_expires = m.get('RecordContentExpires')
        if m.get('Recording') is not None:
            self.recording = m.get('Recording')
        if m.get('RecordingEndTime') is not None:
            self.recording_end_time = m.get('RecordingEndTime')
        if m.get('RecordingExpires') is not None:
            self.recording_expires = m.get('RecordingExpires')
        if m.get('RecordingFps') is not None:
            self.recording_fps = m.get('RecordingFps')
        if m.get('RecordingStartTime') is not None:
            self.recording_start_time = m.get('RecordingStartTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k in m.get('UsbSupplyRedirectRule'):
                temp_model = CreatePolicyGroupRequestUsbSupplyRedirectRule()
                self.usb_supply_redirect_rule.append(temp_model.from_map(k))
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class CreatePolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        policy_group_id: str = None,
        request_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyGroupResponseBody = None,
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
            temp_model = CreatePolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRAMDirectoryRequest(TeaModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        directory_name: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        region_id: str = None,
        v_switch_id: List[str] = None,
    ):
        self.desktop_access_type = desktop_access_type
        self.directory_name = directory_name
        self.enable_admin_access = enable_admin_access
        self.enable_internet_access = enable_internet_access
        self.region_id = region_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateRAMDirectoryResponseBody(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        request_id: str = None,
    ):
        self.directory_id = directory_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRAMDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRAMDirectoryResponseBody = None,
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
            temp_model = CreateRAMDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimpleOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        cloud_box_office_site: bool = None,
        desktop_access_type: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        need_verify_zero_device: bool = None,
        office_site_name: str = None,
        region_id: str = None,
        v_switch_id: List[str] = None,
        verify_code: str = None,
    ):
        self.bandwidth = bandwidth
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.cidr_block = cidr_block
        self.cloud_box_office_site = cloud_box_office_site
        self.desktop_access_type = desktop_access_type
        self.enable_admin_access = enable_admin_access
        self.enable_internet_access = enable_internet_access
        self.need_verify_zero_device = need_verify_zero_device
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cloud_box_office_site is not None:
            result['CloudBoxOfficeSite'] = self.cloud_box_office_site
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CloudBoxOfficeSite') is not None:
            self.cloud_box_office_site = m.get('CloudBoxOfficeSite')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class CreateSimpleOfficeSiteResponseBody(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        request_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSimpleOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSimpleOfficeSiteResponseBody = None,
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
            temp_model = CreateSimpleOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        desktop_id: str = None,
        region_id: str = None,
        snapshot_name: str = None,
        source_disk_type: str = None,
    ):
        self.description = description
        self.desktop_id = desktop_id
        self.region_id = region_id
        self.snapshot_name = snapshot_name
        self.source_disk_type = source_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        self.request_id = request_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSnapshotResponseBody = None,
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBundlesRequest(TeaModel):
    def __init__(
        self,
        bundle_id: List[str] = None,
        region_id: str = None,
    ):
        self.bundle_id = bundle_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBundlesResponseBody(TeaModel):
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


class DeleteBundlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBundlesResponseBody = None,
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
            temp_model = DeleteBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCloudDriveUsersRequest(TeaModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: List[str] = None,
        region_id: str = None,
    ):
        self.cds_id = cds_id
        self.end_user_id = end_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCloudDriveUsersResponseBody(TeaModel):
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


class DeleteCloudDriveUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCloudDriveUsersResponseBody = None,
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
            temp_model = DeleteCloudDriveUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDesktopGroupResponseBody(TeaModel):
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


class DeleteDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDesktopGroupResponseBody = None,
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
            temp_model = DeleteDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDesktopsResponseBody(TeaModel):
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


class DeleteDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDesktopsResponseBody = None,
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
            temp_model = DeleteDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(
        self,
        directory_id: List[str] = None,
        region_id: str = None,
    ):
        self.directory_id = directory_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDirectoriesResponseBody(TeaModel):
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


class DeleteDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDirectoriesResponseBody = None,
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
            temp_model = DeleteDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDriveRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        region_id: str = None,
    ):
        self.drive_id = drive_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['DriveId'] = self.drive_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDriveResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDriveResponseBody = None,
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
            temp_model = DeleteDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(
        self,
        image_id: List[str] = None,
        region_id: str = None,
    ):
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteImagesResponseBody(TeaModel):
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


class DeleteImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImagesResponseBody = None,
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
            temp_model = DeleteImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNASFileSystemsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: List[str] = None,
        region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNASFileSystemsResponseBody(TeaModel):
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


class DeleteNASFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNASFileSystemsResponseBody = None,
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
            temp_model = DeleteNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkPackagesRequest(TeaModel):
    def __init__(
        self,
        network_package_id: List[str] = None,
        region_id: str = None,
    ):
        self.network_package_id = network_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteNetworkPackagesResponseBody(TeaModel):
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


class DeleteNetworkPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetworkPackagesResponseBody = None,
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
            temp_model = DeleteNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOfficeSitesRequest(TeaModel):
    def __init__(
        self,
        office_site_id: List[str] = None,
        region_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteOfficeSitesResponseBody(TeaModel):
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


class DeleteOfficeSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteOfficeSitesResponseBody = None,
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
            temp_model = DeleteOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        policy_group_id: List[str] = None,
        region_id: str = None,
    ):
        self.policy_group_id = policy_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePolicyGroupsResponseBody(TeaModel):
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


class DeletePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyGroupsResponseBody = None,
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
            temp_model = DeletePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: List[str] = None,
    ):
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotResponseBody = None,
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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class DeleteVirtualMFADeviceResponseBody(TeaModel):
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


class DeleteVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVirtualMFADeviceResponseBody = None,
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
            temp_model = DeleteVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmEventStackInfoRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        event_name: str = None,
        lang: str = None,
        region_id: str = None,
        unique_info: str = None,
    ):
        self.desktop_id = desktop_id
        self.event_name = event_name
        self.lang = lang
        self.region_id = region_id
        self.unique_info = unique_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        return self


class DescribeAlarmEventStackInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_info: str = None,
    ):
        self.request_id = request_id
        self.stack_info = stack_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stack_info is not None:
            result['StackInfo'] = self.stack_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StackInfo') is not None:
            self.stack_info = m.get('StackInfo')
        return self


class DescribeAlarmEventStackInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmEventStackInfoResponseBody = None,
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
            temp_model = DescribeAlarmEventStackInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(
        self,
        bundle_id: List[str] = None,
        bundle_type: str = None,
        check_stock: bool = None,
        cpu_count: int = None,
        desktop_type_family: str = None,
        fota_channel: str = None,
        from_desktop_group: bool = None,
        gpu_count: float = None,
        max_results: int = None,
        memory_size: int = None,
        next_token: str = None,
        protocol_type: str = None,
        region_id: str = None,
        support_multi_session: bool = None,
        volume_encryption_enabled: bool = None,
    ):
        self.bundle_id = bundle_id
        self.bundle_type = bundle_type
        self.check_stock = check_stock
        self.cpu_count = cpu_count
        self.desktop_type_family = desktop_type_family
        self.fota_channel = fota_channel
        self.from_desktop_group = from_desktop_group
        self.gpu_count = gpu_count
        self.max_results = max_results
        self.memory_size = memory_size
        self.next_token = next_token
        self.protocol_type = protocol_type
        self.region_id = region_id
        self.support_multi_session = support_multi_session
        self.volume_encryption_enabled = volume_encryption_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.check_stock is not None:
            result['CheckStock'] = self.check_stock
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family
        if self.fota_channel is not None:
            result['FotaChannel'] = self.fota_channel
        if self.from_desktop_group is not None:
            result['FromDesktopGroup'] = self.from_desktop_group
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.support_multi_session is not None:
            result['SupportMultiSession'] = self.support_multi_session
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('CheckStock') is not None:
            self.check_stock = m.get('CheckStock')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')
        if m.get('FotaChannel') is not None:
            self.fota_channel = m.get('FotaChannel')
        if m.get('FromDesktopGroup') is not None:
            self.from_desktop_group = m.get('FromDesktopGroup')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupportMultiSession') is not None:
            self.support_multi_session = m.get('SupportMultiSession')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        return self


class DescribeBundlesResponseBodyBundlesDesktopTypeAttribute(TeaModel):
    def __init__(
        self,
        cpu_count: int = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        memory_size: int = None,
    ):
        self.cpu_count = cpu_count
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        return self


class DescribeBundlesResponseBodyBundlesDisks(TeaModel):
    def __init__(
        self,
        disk_performance_level: str = None,
        disk_size: int = None,
        disk_type: str = None,
    ):
        self.disk_performance_level = disk_performance_level
        self.disk_size = disk_size
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        return self


class DescribeBundlesResponseBodyBundles(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        bundle_name: str = None,
        bundle_type: str = None,
        creation_time: str = None,
        description: str = None,
        desktop_type: str = None,
        desktop_type_attribute: DescribeBundlesResponseBodyBundlesDesktopTypeAttribute = None,
        desktop_type_family: str = None,
        disks: List[DescribeBundlesResponseBodyBundlesDisks] = None,
        image_id: str = None,
        image_name: str = None,
        language: str = None,
        os_type: str = None,
        protocol_type: str = None,
        session_type: str = None,
        stock_state: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        self.bundle_id = bundle_id
        self.bundle_name = bundle_name
        self.bundle_type = bundle_type
        self.creation_time = creation_time
        self.description = description
        self.desktop_type = desktop_type
        self.desktop_type_attribute = desktop_type_attribute
        self.desktop_type_family = desktop_type_family
        self.disks = disks
        self.image_id = image_id
        self.image_name = image_name
        self.language = language
        self.os_type = os_type
        self.protocol_type = protocol_type
        self.session_type = session_type
        self.stock_state = stock_state
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()
        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.language is not None:
            result['Language'] = self.language
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        if self.stock_state is not None:
            result['StockState'] = self.stock_state
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('DesktopTypeAttribute') is not None:
            temp_model = DescribeBundlesResponseBodyBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m['DesktopTypeAttribute'])
        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeBundlesResponseBodyBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        if m.get('StockState') is not None:
            self.stock_state = m.get('StockState')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        return self


class DescribeBundlesResponseBody(TeaModel):
    def __init__(
        self,
        bundles: List[DescribeBundlesResponseBodyBundles] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.bundles = bundles
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bundles'] = []
        if self.bundles is not None:
            for k in self.bundles:
                result['Bundles'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bundles = []
        if m.get('Bundles') is not None:
            for k in m.get('Bundles'):
                temp_model = DescribeBundlesResponseBodyBundles()
                self.bundles.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBundlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBundlesResponseBody = None,
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
            temp_model = DescribeBundlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCensResponseBodyCensPackageIds(TeaModel):
    def __init__(
        self,
        package_id: str = None,
    ):
        self.package_id = package_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_id is not None:
            result['PackageId'] = self.package_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')
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


class DescribeCensResponseBodyCens(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        creation_time: str = None,
        description: str = None,
        ipv_6level: str = None,
        name: str = None,
        package_ids: List[DescribeCensResponseBodyCensPackageIds] = None,
        protection_level: str = None,
        status: str = None,
        tags: List[DescribeCensResponseBodyCensTags] = None,
    ):
        self.cen_id = cen_id
        self.creation_time = creation_time
        self.description = description
        self.ipv_6level = ipv_6level
        self.name = name
        self.package_ids = package_ids
        self.protection_level = protection_level
        self.status = status
        self.tags = tags

    def validate(self):
        if self.package_ids:
            for k in self.package_ids:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.ipv_6level is not None:
            result['Ipv6Level'] = self.ipv_6level
        if self.name is not None:
            result['Name'] = self.name
        result['PackageIds'] = []
        if self.package_ids is not None:
            for k in self.package_ids:
                result['PackageIds'].append(k.to_map() if k else None)
        if self.protection_level is not None:
            result['ProtectionLevel'] = self.protection_level
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Ipv6Level') is not None:
            self.ipv_6level = m.get('Ipv6Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.package_ids = []
        if m.get('PackageIds') is not None:
            for k in m.get('PackageIds'):
                temp_model = DescribeCensResponseBodyCensPackageIds()
                self.package_ids.append(temp_model.from_map(k))
        if m.get('ProtectionLevel') is not None:
            self.protection_level = m.get('ProtectionLevel')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeCensResponseBodyCensTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        cens: List[DescribeCensResponseBodyCens] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cens = cens
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cens:
            for k in self.cens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cens'] = []
        if self.cens is not None:
            for k in self.cens:
                result['Cens'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cens = []
        if m.get('Cens') is not None:
            for k in m.get('Cens'):
                temp_model = DescribeCensResponseBodyCens()
                self.cens.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCensResponseBody = None,
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
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientEventsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_ip: str = None,
        desktop_name: str = None,
        directory_id: str = None,
        end_time: str = None,
        end_user_id: str = None,
        event_type: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.desktop_id = desktop_id
        self.desktop_ip = desktop_ip
        self.desktop_name = desktop_name
        self.directory_id = directory_id
        self.end_time = end_time
        self.end_user_id = end_user_id
        self.event_type = event_type
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeClientEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bytes_received: str = None,
        bytes_send: str = None,
        client_ip: str = None,
        client_os: str = None,
        client_version: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        desktop_id: str = None,
        desktop_ip: str = None,
        desktop_name: str = None,
        directory_id: str = None,
        directory_type: str = None,
        end_user_id: str = None,
        event_id: str = None,
        event_time: str = None,
        event_type: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.ali_uid = ali_uid
        self.bytes_received = bytes_received
        self.bytes_send = bytes_send
        self.client_ip = client_ip
        self.client_os = client_os
        self.client_version = client_version
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.desktop_id = desktop_id
        self.desktop_ip = desktop_ip
        self.desktop_name = desktop_name
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.end_user_id = end_user_id
        self.event_id = event_id
        self.event_time = event_time
        self.event_type = event_type
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bytes_received is not None:
            result['BytesReceived'] = self.bytes_received
        if self.bytes_send is not None:
            result['BytesSend'] = self.bytes_send
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_os is not None:
            result['ClientOS'] = self.client_os
        if self.client_version is not None:
            result['ClientVersion'] = self.client_version
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_ip is not None:
            result['DesktopIp'] = self.desktop_ip
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BytesReceived') is not None:
            self.bytes_received = m.get('BytesReceived')
        if m.get('BytesSend') is not None:
            self.bytes_send = m.get('BytesSend')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')
        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopIp') is not None:
            self.desktop_ip = m.get('DesktopIp')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeClientEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeClientEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.events = events
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeClientEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClientEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClientEventsResponseBody = None,
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
            temp_model = DescribeClientEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudDrivePermissionsRequest(TeaModel):
    def __init__(
        self,
        cds_id: str = None,
        region_id: str = None,
    ):
        self.cds_id = cds_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels(TeaModel):
    def __init__(
        self,
        end_users: List[str] = None,
        permission: str = None,
    ):
        self.end_users = end_users
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_users is not None:
            result['EndUsers'] = self.end_users
        if self.permission is not None:
            result['Permission'] = self.permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUsers') is not None:
            self.end_users = m.get('EndUsers')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        return self


class DescribeCloudDrivePermissionsResponseBody(TeaModel):
    def __init__(
        self,
        cloud_drive_permission_models: List[DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels] = None,
        request_id: str = None,
    ):
        self.cloud_drive_permission_models = cloud_drive_permission_models
        self.request_id = request_id

    def validate(self):
        if self.cloud_drive_permission_models:
            for k in self.cloud_drive_permission_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudDrivePermissionModels'] = []
        if self.cloud_drive_permission_models is not None:
            for k in self.cloud_drive_permission_models:
                result['CloudDrivePermissionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_drive_permission_models = []
        if m.get('CloudDrivePermissionModels') is not None:
            for k in m.get('CloudDrivePermissionModels'):
                temp_model = DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels()
                self.cloud_drive_permission_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCloudDrivePermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudDrivePermissionsResponseBody = None,
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
            temp_model = DescribeCloudDrivePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopGroupsRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        end_user_ids: List[str] = None,
        excluded_end_user_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        own_type: int = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        status: int = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.end_user_ids = end_user_ids
        self.excluded_end_user_ids = excluded_end_user_ids
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.own_type = own_type
        self.period = period
        self.period_unit = period_unit
        self.policy_group_id = policy_group_id
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.excluded_end_user_ids is not None:
            result['ExcludedEndUserIds'] = self.excluded_end_user_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExcludedEndUserIds') is not None:
            self.excluded_end_user_ids = m.get('ExcludedEndUserIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDesktopGroupsResponseBodyDesktopGroups(TeaModel):
    def __init__(
        self,
        bind_amount: int = None,
        comments: str = None,
        connect_duration: int = None,
        cpu: int = None,
        create_time: str = None,
        creator: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        end_user_count: int = None,
        expired_time: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        memory: int = None,
        min_desktops_count: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        own_bundle_id: str = None,
        own_bundle_name: str = None,
        own_type: int = None,
        pay_type: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        ratio_threshold: float = None,
        reset_type: int = None,
        status: int = None,
        stop_duration: int = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        version: int = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        self.bind_amount = bind_amount
        self.comments = comments
        self.connect_duration = connect_duration
        self.cpu = cpu
        self.create_time = create_time
        self.creator = creator
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.end_user_count = end_user_count
        self.expired_time = expired_time
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.idle_disconnect_duration = idle_disconnect_duration
        self.image_id = image_id
        self.keep_duration = keep_duration
        self.load_policy = load_policy
        self.max_desktops_count = max_desktops_count
        self.memory = memory
        self.min_desktops_count = min_desktops_count
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        self.own_bundle_id = own_bundle_id
        self.own_bundle_name = own_bundle_name
        self.own_type = own_type
        self.pay_type = pay_type
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.ratio_threshold = ratio_threshold
        self.reset_type = reset_type
        self.status = status
        self.stop_duration = stop_duration
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.version = version
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.end_user_count is not None:
            result['EndUserCount'] = self.end_user_count
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.version is not None:
            result['Version'] = self.version
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('EndUserCount') is not None:
            self.end_user_count = m.get('EndUserCount')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        return self


class DescribeDesktopGroupsResponseBody(TeaModel):
    def __init__(
        self,
        desktop_groups: List[DescribeDesktopGroupsResponseBodyDesktopGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.desktop_groups = desktop_groups
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.desktop_groups:
            for k in self.desktop_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DesktopGroups'] = []
        if self.desktop_groups is not None:
            for k in self.desktop_groups:
                result['DesktopGroups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_groups = []
        if m.get('DesktopGroups') is not None:
            for k in m.get('DesktopGroups'):
                temp_model = DescribeDesktopGroupsResponseBodyDesktopGroups()
                self.desktop_groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDesktopGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopGroupsResponseBody = None,
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
            temp_model = DescribeDesktopGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopIdsByVulNamesRequest(TeaModel):
    def __init__(
        self,
        necessity: str = None,
        office_site_id: str = None,
        region_id: str = None,
        type: str = None,
        vul_name: List[str] = None,
    ):
        self.necessity = necessity
        self.office_site_id = office_site_id
        self.region_id = region_id
        self.type = type
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        return self


class DescribeDesktopIdsByVulNamesResponseBodyDesktopItems(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
    ):
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        return self


class DescribeDesktopIdsByVulNamesResponseBody(TeaModel):
    def __init__(
        self,
        desktop_items: List[DescribeDesktopIdsByVulNamesResponseBodyDesktopItems] = None,
        request_id: str = None,
    ):
        self.desktop_items = desktop_items
        self.request_id = request_id

    def validate(self):
        if self.desktop_items:
            for k in self.desktop_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DesktopItems'] = []
        if self.desktop_items is not None:
            for k in self.desktop_items:
                result['DesktopItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_items = []
        if m.get('DesktopItems') is not None:
            for k in m.get('DesktopItems'):
                temp_model = DescribeDesktopIdsByVulNamesResponseBodyDesktopItems()
                self.desktop_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDesktopIdsByVulNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopIdsByVulNamesResponseBody = None,
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
            temp_model = DescribeDesktopIdsByVulNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(
        self,
        applied_scope: str = None,
        cpu_count: int = None,
        desktop_id_for_modify: str = None,
        desktop_type_id: str = None,
        gpu_count: float = None,
        instance_type_family: str = None,
        memory_size: int = None,
        order_type: str = None,
        region_id: str = None,
    ):
        self.applied_scope = applied_scope
        self.cpu_count = cpu_count
        self.desktop_id_for_modify = desktop_id_for_modify
        self.desktop_type_id = desktop_type_id
        self.gpu_count = gpu_count
        self.instance_type_family = instance_type_family
        self.memory_size = memory_size
        self.order_type = order_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_scope is not None:
            result['AppliedScope'] = self.applied_scope
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.desktop_id_for_modify is not None:
            result['DesktopIdForModify'] = self.desktop_id_for_modify
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedScope') is not None:
            self.applied_scope = m.get('AppliedScope')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DesktopIdForModify') is not None:
            self.desktop_id_for_modify = m.get('DesktopIdForModify')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDesktopTypesResponseBodyDesktopTypes(TeaModel):
    def __init__(
        self,
        cpu_count: str = None,
        data_disk_size: str = None,
        desktop_type_id: str = None,
        desktop_type_status: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        instance_type_family: str = None,
        memory_size: str = None,
        system_disk_size: str = None,
    ):
        self.cpu_count = cpu_count
        self.data_disk_size = data_disk_size
        self.desktop_type_id = desktop_type_id
        self.desktop_type_status = desktop_type_status
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.instance_type_family = instance_type_family
        self.memory_size = memory_size
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_type_id is not None:
            result['DesktopTypeId'] = self.desktop_type_id
        if self.desktop_type_status is not None:
            result['DesktopTypeStatus'] = self.desktop_type_status
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopTypeId') is not None:
            self.desktop_type_id = m.get('DesktopTypeId')
        if m.get('DesktopTypeStatus') is not None:
            self.desktop_type_status = m.get('DesktopTypeStatus')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeDesktopTypesResponseBody(TeaModel):
    def __init__(
        self,
        desktop_types: List[DescribeDesktopTypesResponseBodyDesktopTypes] = None,
        request_id: str = None,
    ):
        self.desktop_types = desktop_types
        self.request_id = request_id

    def validate(self):
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DesktopTypes'] = []
        if self.desktop_types is not None:
            for k in self.desktop_types:
                result['DesktopTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_types = []
        if m.get('DesktopTypes') is not None:
            for k in m.get('DesktopTypes'):
                temp_model = DescribeDesktopTypesResponseBodyDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDesktopTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopTypesResponseBody = None,
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
            temp_model = DescribeDesktopTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsRequestTag(TeaModel):
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


class DescribeDesktopsRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_status: str = None,
        directory_id: str = None,
        end_user_id: List[str] = None,
        excluded_end_user_id: List[str] = None,
        expired_time: str = None,
        filter_desktop_group: bool = None,
        group_id: str = None,
        management_flag: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        policy_group_id: str = None,
        protocol_type: str = None,
        query_fota_update: bool = None,
        region_id: str = None,
        tag: List[DescribeDesktopsRequestTag] = None,
        user_name: str = None,
    ):
        self.charge_type = charge_type
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.excluded_end_user_id = excluded_end_user_id
        self.expired_time = expired_time
        self.filter_desktop_group = filter_desktop_group
        self.group_id = group_id
        self.management_flag = management_flag
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.policy_group_id = policy_group_id
        self.protocol_type = protocol_type
        self.query_fota_update = query_fota_update
        self.region_id = region_id
        self.tag = tag
        self.user_name = user_name

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.excluded_end_user_id is not None:
            result['ExcludedEndUserId'] = self.excluded_end_user_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.filter_desktop_group is not None:
            result['FilterDesktopGroup'] = self.filter_desktop_group
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.query_fota_update is not None:
            result['QueryFotaUpdate'] = self.query_fota_update
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExcludedEndUserId') is not None:
            self.excluded_end_user_id = m.get('ExcludedEndUserId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FilterDesktopGroup') is not None:
            self.filter_desktop_group = m.get('FilterDesktopGroup')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('QueryFotaUpdate') is not None:
            self.query_fota_update = m.get('QueryFotaUpdate')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDesktopsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDesktopsResponseBodyDesktopsDisks(TeaModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        disk_type: str = None,
        performance_level: str = None,
    ):
        self.disk_id = disk_id
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.performance_level = performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        return self


class DescribeDesktopsResponseBodyDesktopsFotaUpdate(TeaModel):
    def __init__(
        self,
        current_app_version: str = None,
        new_app_version: str = None,
        release_note: str = None,
        size: int = None,
    ):
        self.current_app_version = current_app_version
        self.new_app_version = new_app_version
        self.release_note = release_note
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version
        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')
        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeDesktopsResponseBodyDesktopsSessions(TeaModel):
    def __init__(
        self,
        end_user_id: str = None,
        establishment_time: str = None,
        external_user_name: str = None,
    ):
        self.end_user_id = end_user_id
        self.establishment_time = establishment_time
        self.external_user_name = external_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.establishment_time is not None:
            result['EstablishmentTime'] = self.establishment_time
        if self.external_user_name is not None:
            result['ExternalUserName'] = self.external_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EstablishmentTime') is not None:
            self.establishment_time = m.get('EstablishmentTime')
        if m.get('ExternalUserName') is not None:
            self.external_user_name = m.get('ExternalUserName')
        return self


class DescribeDesktopsResponseBodyDesktopsTags(TeaModel):
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


class DescribeDesktopsResponseBodyDesktops(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        bundle_name: str = None,
        charge_type: str = None,
        connection_status: str = None,
        cpu: int = None,
        creation_time: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        desktop_type: str = None,
        directory_id: str = None,
        directory_type: str = None,
        disks: List[DescribeDesktopsResponseBodyDesktopsDisks] = None,
        downgrade_quota: int = None,
        downgraded_times: int = None,
        end_user_ids: List[str] = None,
        expired_time: str = None,
        fota_update: DescribeDesktopsResponseBodyDesktopsFotaUpdate = None,
        gpu_category: int = None,
        gpu_count: float = None,
        gpu_driver_version: str = None,
        gpu_spec: str = None,
        host_name: str = None,
        image_id: str = None,
        management_flag: str = None,
        memory: int = None,
        network_interface_id: str = None,
        network_interface_ip: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        office_site_vpc_type: str = None,
        os_type: str = None,
        platform: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        progress: str = None,
        protocol_type: str = None,
        session_type: str = None,
        sessions: List[DescribeDesktopsResponseBodyDesktopsSessions] = None,
        start_time: str = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        tags: List[DescribeDesktopsResponseBodyDesktopsTags] = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
        zone_type: str = None,
    ):
        self.bundle_id = bundle_id
        self.bundle_name = bundle_name
        self.charge_type = charge_type
        self.connection_status = connection_status
        self.cpu = cpu
        self.creation_time = creation_time
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.desktop_type = desktop_type
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.disks = disks
        self.downgrade_quota = downgrade_quota
        self.downgraded_times = downgraded_times
        self.end_user_ids = end_user_ids
        self.expired_time = expired_time
        self.fota_update = fota_update
        self.gpu_category = gpu_category
        self.gpu_count = gpu_count
        self.gpu_driver_version = gpu_driver_version
        self.gpu_spec = gpu_spec
        self.host_name = host_name
        self.image_id = image_id
        self.management_flag = management_flag
        self.memory = memory
        self.network_interface_id = network_interface_id
        self.network_interface_ip = network_interface_ip
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        self.office_site_vpc_type = office_site_vpc_type
        self.os_type = os_type
        self.platform = platform
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.progress = progress
        self.protocol_type = protocol_type
        self.session_type = session_type
        self.sessions = sessions
        self.start_time = start_time
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key
        self.zone_type = zone_type

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        if self.fota_update:
            self.fota_update.validate()
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.downgrade_quota is not None:
            result['DowngradeQuota'] = self.downgrade_quota
        if self.downgraded_times is not None:
            result['DowngradedTimes'] = self.downgraded_times
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.fota_update is not None:
            result['FotaUpdate'] = self.fota_update.to_map()
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.network_interface_ip is not None:
            result['NetworkInterfaceIp'] = self.network_interface_ip
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.office_site_vpc_type is not None:
            result['OfficeSiteVpcType'] = self.office_site_vpc_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDesktopsResponseBodyDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('DowngradeQuota') is not None:
            self.downgrade_quota = m.get('DowngradeQuota')
        if m.get('DowngradedTimes') is not None:
            self.downgraded_times = m.get('DowngradedTimes')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FotaUpdate') is not None:
            temp_model = DescribeDesktopsResponseBodyDesktopsFotaUpdate()
            self.fota_update = temp_model.from_map(m['FotaUpdate'])
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('NetworkInterfaceIp') is not None:
            self.network_interface_ip = m.get('NetworkInterfaceIp')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('OfficeSiteVpcType') is not None:
            self.office_site_vpc_type = m.get('OfficeSiteVpcType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = DescribeDesktopsResponseBodyDesktopsSessions()
                self.sessions.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDesktopsResponseBodyDesktopsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        desktops: List[DescribeDesktopsResponseBodyDesktops] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.desktops = desktops
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k in m.get('Desktops'):
                temp_model = DescribeDesktopsResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopsResponseBody = None,
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
            temp_model = DescribeDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDesktopsInGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        ignore_deleted: bool = None,
        max_results: int = None,
        next_token: str = None,
        pay_type: str = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.ignore_deleted = ignore_deleted
        self.max_results = max_results
        self.next_token = next_token
        self.pay_type = pay_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.ignore_deleted is not None:
            result['IgnoreDeleted'] = self.ignore_deleted
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('IgnoreDeleted') is not None:
            self.ignore_deleted = m.get('IgnoreDeleted')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDesktopsInGroupResponseBodyPaidDesktops(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        disk_type: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        end_user_name: str = None,
        end_user_names: List[str] = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_name: str = None,
        management_flag: str = None,
        management_flags: List[str] = None,
        member_eni_ip: str = None,
        os_type: str = None,
        primary_eni_ip: str = None,
        reset_time: str = None,
        system_disk_size: int = None,
    ):
        self.connection_status = connection_status
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.disk_type = disk_type
        self.end_user_id = end_user_id
        self.end_user_ids = end_user_ids
        self.end_user_name = end_user_name
        self.end_user_names = end_user_names
        self.gpu_driver_version = gpu_driver_version
        self.image_id = image_id
        self.image_name = image_name
        self.management_flag = management_flag
        self.management_flags = management_flags
        self.member_eni_ip = member_eni_ip
        self.os_type = os_type
        self.primary_eni_ip = primary_eni_ip
        self.reset_time = reset_time
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        if self.end_user_names is not None:
            result['EndUserNames'] = self.end_user_names
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags
        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.primary_eni_ip is not None:
            result['PrimaryEniIp'] = self.primary_eni_ip
        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        if m.get('EndUserNames') is not None:
            self.end_user_names = m.get('EndUserNames')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')
        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrimaryEniIp') is not None:
            self.primary_eni_ip = m.get('PrimaryEniIp')
        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeDesktopsInGroupResponseBodyPostPaidDesktops(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        create_duration: str = None,
        create_time: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        desktop_status: str = None,
        disk_type: str = None,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        end_user_name: str = None,
        end_user_names: List[str] = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_name: str = None,
        management_flag: str = None,
        management_flags: List[str] = None,
        member_eni_ip: str = None,
        os_type: str = None,
        primary_eni_ip: str = None,
        release_time: str = None,
        reset_time: str = None,
        system_disk_size: int = None,
    ):
        self.connection_status = connection_status
        self.create_duration = create_duration
        self.create_time = create_time
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.disk_type = disk_type
        self.end_user_id = end_user_id
        self.end_user_ids = end_user_ids
        self.end_user_name = end_user_name
        self.end_user_names = end_user_names
        self.gpu_driver_version = gpu_driver_version
        self.image_id = image_id
        self.image_name = image_name
        self.management_flag = management_flag
        self.management_flags = management_flags
        self.member_eni_ip = member_eni_ip
        self.os_type = os_type
        self.primary_eni_ip = primary_eni_ip
        self.release_time = release_time
        self.reset_time = reset_time
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_duration is not None:
            result['CreateDuration'] = self.create_duration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        if self.end_user_names is not None:
            result['EndUserNames'] = self.end_user_names
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag
        if self.management_flags is not None:
            result['ManagementFlags'] = self.management_flags
        if self.member_eni_ip is not None:
            result['MemberEniIp'] = self.member_eni_ip
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.primary_eni_ip is not None:
            result['PrimaryEniIp'] = self.primary_eni_ip
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.reset_time is not None:
            result['ResetTime'] = self.reset_time
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateDuration') is not None:
            self.create_duration = m.get('CreateDuration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        if m.get('EndUserNames') is not None:
            self.end_user_names = m.get('EndUserNames')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')
        if m.get('ManagementFlags') is not None:
            self.management_flags = m.get('ManagementFlags')
        if m.get('MemberEniIp') is not None:
            self.member_eni_ip = m.get('MemberEniIp')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrimaryEniIp') is not None:
            self.primary_eni_ip = m.get('PrimaryEniIp')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('ResetTime') is not None:
            self.reset_time = m.get('ResetTime')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        return self


class DescribeDesktopsInGroupResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        online_pre_paid_desktops_count: int = None,
        paid_desktops: List[DescribeDesktopsInGroupResponseBodyPaidDesktops] = None,
        paid_desktops_count: int = None,
        post_paid_desktops: List[DescribeDesktopsInGroupResponseBodyPostPaidDesktops] = None,
        post_paid_desktops_count: int = None,
        post_paid_desktops_total_amount: int = None,
        request_id: str = None,
        running_pre_paid_desktops_count: int = None,
        stoped_pre_paid_desktops_count: int = None,
    ):
        self.next_token = next_token
        self.online_pre_paid_desktops_count = online_pre_paid_desktops_count
        self.paid_desktops = paid_desktops
        self.paid_desktops_count = paid_desktops_count
        self.post_paid_desktops = post_paid_desktops
        self.post_paid_desktops_count = post_paid_desktops_count
        self.post_paid_desktops_total_amount = post_paid_desktops_total_amount
        self.request_id = request_id
        self.running_pre_paid_desktops_count = running_pre_paid_desktops_count
        self.stoped_pre_paid_desktops_count = stoped_pre_paid_desktops_count

    def validate(self):
        if self.paid_desktops:
            for k in self.paid_desktops:
                if k:
                    k.validate()
        if self.post_paid_desktops:
            for k in self.post_paid_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.online_pre_paid_desktops_count is not None:
            result['OnlinePrePaidDesktopsCount'] = self.online_pre_paid_desktops_count
        result['PaidDesktops'] = []
        if self.paid_desktops is not None:
            for k in self.paid_desktops:
                result['PaidDesktops'].append(k.to_map() if k else None)
        if self.paid_desktops_count is not None:
            result['PaidDesktopsCount'] = self.paid_desktops_count
        result['PostPaidDesktops'] = []
        if self.post_paid_desktops is not None:
            for k in self.post_paid_desktops:
                result['PostPaidDesktops'].append(k.to_map() if k else None)
        if self.post_paid_desktops_count is not None:
            result['PostPaidDesktopsCount'] = self.post_paid_desktops_count
        if self.post_paid_desktops_total_amount is not None:
            result['PostPaidDesktopsTotalAmount'] = self.post_paid_desktops_total_amount
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_pre_paid_desktops_count is not None:
            result['RunningPrePaidDesktopsCount'] = self.running_pre_paid_desktops_count
        if self.stoped_pre_paid_desktops_count is not None:
            result['StopedPrePaidDesktopsCount'] = self.stoped_pre_paid_desktops_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OnlinePrePaidDesktopsCount') is not None:
            self.online_pre_paid_desktops_count = m.get('OnlinePrePaidDesktopsCount')
        self.paid_desktops = []
        if m.get('PaidDesktops') is not None:
            for k in m.get('PaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPaidDesktops()
                self.paid_desktops.append(temp_model.from_map(k))
        if m.get('PaidDesktopsCount') is not None:
            self.paid_desktops_count = m.get('PaidDesktopsCount')
        self.post_paid_desktops = []
        if m.get('PostPaidDesktops') is not None:
            for k in m.get('PostPaidDesktops'):
                temp_model = DescribeDesktopsInGroupResponseBodyPostPaidDesktops()
                self.post_paid_desktops.append(temp_model.from_map(k))
        if m.get('PostPaidDesktopsCount') is not None:
            self.post_paid_desktops_count = m.get('PostPaidDesktopsCount')
        if m.get('PostPaidDesktopsTotalAmount') is not None:
            self.post_paid_desktops_total_amount = m.get('PostPaidDesktopsTotalAmount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningPrePaidDesktopsCount') is not None:
            self.running_pre_paid_desktops_count = m.get('RunningPrePaidDesktopsCount')
        if m.get('StopedPrePaidDesktopsCount') is not None:
            self.stoped_pre_paid_desktops_count = m.get('StopedPrePaidDesktopsCount')
        return self


class DescribeDesktopsInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDesktopsInGroupResponseBody = None,
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
            temp_model = DescribeDesktopsInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(
        self,
        directory_id: List[str] = None,
        directory_status: str = None,
        directory_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.directory_id = directory_id
        self.directory_status = directory_status
        self.directory_type = directory_type
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_status is not None:
            result['DirectoryStatus'] = self.directory_status
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryStatus') is not None:
            self.directory_status = m.get('DirectoryStatus')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDirectoriesResponseBodyDirectoriesADConnectors(TeaModel):
    def __init__(
        self,
        adconnector_address: str = None,
        connector_status: str = None,
        network_interface_id: str = None,
        specification: str = None,
        trust_key: str = None,
        v_switch_id: str = None,
    ):
        self.adconnector_address = adconnector_address
        self.connector_status = connector_status
        self.network_interface_id = network_interface_id
        self.specification = specification
        self.trust_key = trust_key
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.trust_key is not None:
            result['TrustKey'] = self.trust_key
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('TrustKey') is not None:
            self.trust_key = m.get('TrustKey')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeDirectoriesResponseBodyDirectoriesLogs(TeaModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        step: str = None,
        time_stamp: str = None,
    ):
        self.level = level
        self.message = message
        self.step = step
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.step is not None:
            result['Step'] = self.step
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeDirectoriesResponseBodyDirectories(TeaModel):
    def __init__(
        self,
        adconnectors: List[DescribeDirectoriesResponseBodyDirectoriesADConnectors] = None,
        creation_time: str = None,
        custom_security_group_id: str = None,
        desktop_access_type: str = None,
        desktop_vpc_endpoint: str = None,
        directory_id: str = None,
        directory_type: str = None,
        dns_address: List[str] = None,
        dns_user_name: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_cross_desktop_access: bool = None,
        enable_internet_access: bool = None,
        file_system_ids: List[str] = None,
        logs: List[DescribeDirectoriesResponseBodyDirectoriesLogs] = None,
        mfa_enabled: bool = None,
        name: str = None,
        need_verify_login_risk: bool = None,
        ou_name: str = None,
        sso_enabled: bool = None,
        status: str = None,
        sub_dns_address: List[str] = None,
        sub_domain_name: str = None,
        trust_password: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.adconnectors = adconnectors
        self.creation_time = creation_time
        self.custom_security_group_id = custom_security_group_id
        self.desktop_access_type = desktop_access_type
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.dns_address = dns_address
        self.dns_user_name = dns_user_name
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.enable_admin_access = enable_admin_access
        self.enable_cross_desktop_access = enable_cross_desktop_access
        self.enable_internet_access = enable_internet_access
        self.file_system_ids = file_system_ids
        self.logs = logs
        self.mfa_enabled = mfa_enabled
        self.name = name
        self.need_verify_login_risk = need_verify_login_risk
        self.ou_name = ou_name
        self.sso_enabled = sso_enabled
        self.status = status
        self.sub_dns_address = sub_dns_address
        self.sub_domain_name = sub_domain_name
        self.trust_password = trust_password
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.need_verify_login_risk is not None:
            result['NeedVerifyLoginRisk'] = self.need_verify_login_risk
        if self.ou_name is not None:
            result['OuName'] = self.ou_name
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeDirectoriesResponseBodyDirectoriesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')
        if m.get('OuName') is not None:
            self.ou_name = m.get('OuName')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        ad_hostname: str = None,
        directories: List[DescribeDirectoriesResponseBodyDirectories] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.ad_hostname = ad_hostname
        self.directories = directories
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')
        self.directories = []
        if m.get('Directories') is not None:
            for k in m.get('Directories'):
                temp_model = DescribeDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDirectoriesResponseBody = None,
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
            temp_model = DescribeDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDrivesRequest(TeaModel):
    def __init__(
        self,
        domain_ids: List[str] = None,
        region_id: str = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        self.domain_ids = domain_ids
        self.region_id = region_id
        self.resource_type = resource_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_ids is not None:
            result['DomainIds'] = self.domain_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainIds') is not None:
            self.domain_ids = m.get('DomainIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeDrivesResponseBodyDrivesDesktopGroups(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        return self


class DescribeDrivesResponseBodyDrives(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        desktop_group_count: int = None,
        desktop_groups: List[DescribeDrivesResponseBodyDrivesDesktopGroups] = None,
        domain_id: str = None,
        drive_id: str = None,
        enable_profile_management: bool = None,
        external_domain_id: str = None,
        external_drive_id: str = None,
        external_user_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        name: str = None,
        profile_roaming: bool = None,
        status: str = None,
        total_size: int = None,
        type: str = None,
        used_size: int = None,
        user_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.description = description
        self.desktop_group_count = desktop_group_count
        self.desktop_groups = desktop_groups
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.enable_profile_management = enable_profile_management
        self.external_domain_id = external_domain_id
        self.external_drive_id = external_drive_id
        self.external_user_id = external_user_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.profile_roaming = profile_roaming
        self.status = status
        self.total_size = total_size
        self.type = type
        self.used_size = used_size
        self.user_id = user_id

    def validate(self):
        if self.desktop_groups:
            for k in self.desktop_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count
        result['DesktopGroups'] = []
        if self.desktop_groups is not None:
            for k in self.desktop_groups:
                result['DesktopGroups'].append(k.to_map() if k else None)
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.drive_id is not None:
            result['DriveId'] = self.drive_id
        if self.enable_profile_management is not None:
            result['EnableProfileManagement'] = self.enable_profile_management
        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id
        if self.external_drive_id is not None:
            result['ExternalDriveId'] = self.external_drive_id
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.profile_roaming is not None:
            result['ProfileRoaming'] = self.profile_roaming
        if self.status is not None:
            result['Status'] = self.status
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.type is not None:
            result['Type'] = self.type
        if self.used_size is not None:
            result['UsedSize'] = self.used_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')
        self.desktop_groups = []
        if m.get('DesktopGroups') is not None:
            for k in m.get('DesktopGroups'):
                temp_model = DescribeDrivesResponseBodyDrivesDesktopGroups()
                self.desktop_groups.append(temp_model.from_map(k))
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')
        if m.get('EnableProfileManagement') is not None:
            self.enable_profile_management = m.get('EnableProfileManagement')
        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')
        if m.get('ExternalDriveId') is not None:
            self.external_drive_id = m.get('ExternalDriveId')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProfileRoaming') is not None:
            self.profile_roaming = m.get('ProfileRoaming')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeDrivesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        drives: List[DescribeDrivesResponseBodyDrives] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.drives = drives
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.drives:
            for k in self.drives:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Drives'] = []
        if self.drives is not None:
            for k in self.drives:
                result['Drives'].append(k.to_map() if k else None)
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
        self.drives = []
        if m.get('Drives') is not None:
            for k in m.get('Drives'):
                temp_model = DescribeDrivesResponseBodyDrives()
                self.drives.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDrivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDrivesResponseBody = None,
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
            temp_model = DescribeDrivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowMetricRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        instance_type: str = None,
        metric_type: str = None,
        period: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.metric_type = metric_type
        self.period = period
        self.region_id = region_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeFlowMetricResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowMetricResponseBody = None,
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
            temp_model = DescribeFlowMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowStatisticRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        office_site_id: str = None,
        page_number: int = None,
        page_size: int = None,
        period: int = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.office_site_id = office_site_id
        self.page_number = page_number
        self.page_size = page_size
        self.period = period
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeFlowStatisticResponseBodyDesktopFlowStatistic(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        flow_in: str = None,
        flow_rank: int = None,
    ):
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.flow_in = flow_in
        self.flow_rank = flow_rank

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.flow_in is not None:
            result['FlowIn'] = self.flow_in
        if self.flow_rank is not None:
            result['FlowRank'] = self.flow_rank
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('FlowIn') is not None:
            self.flow_in = m.get('FlowIn')
        if m.get('FlowRank') is not None:
            self.flow_rank = m.get('FlowRank')
        return self


class DescribeFlowStatisticResponseBody(TeaModel):
    def __init__(
        self,
        desktop_count: int = None,
        desktop_flow_statistic: List[DescribeFlowStatisticResponseBodyDesktopFlowStatistic] = None,
        request_id: str = None,
    ):
        self.desktop_count = desktop_count
        self.desktop_flow_statistic = desktop_flow_statistic
        self.request_id = request_id

    def validate(self):
        if self.desktop_flow_statistic:
            for k in self.desktop_flow_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count
        result['DesktopFlowStatistic'] = []
        if self.desktop_flow_statistic is not None:
            for k in self.desktop_flow_statistic:
                result['DesktopFlowStatistic'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')
        self.desktop_flow_statistic = []
        if m.get('DesktopFlowStatistic') is not None:
            for k in m.get('DesktopFlowStatistic'):
                temp_model = DescribeFlowStatisticResponseBodyDesktopFlowStatistic()
                self.desktop_flow_statistic.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFlowStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFlowStatisticResponseBody = None,
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
            temp_model = DescribeFlowStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFotaPendingDesktopsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_uid: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.task_uid = task_uid

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops(TeaModel):
    def __init__(
        self,
        current_app_version: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        fota_project: str = None,
        office_site_id: str = None,
    ):
        self.current_app_version = current_app_version
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.fota_project = fota_project
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.fota_project is not None:
            result['FotaProject'] = self.fota_project
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('FotaProject') is not None:
            self.fota_project = m.get('FotaProject')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class DescribeFotaPendingDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        fota_pending_desktops: List[DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.fota_pending_desktops = fota_pending_desktops
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.fota_pending_desktops:
            for k in self.fota_pending_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FotaPendingDesktops'] = []
        if self.fota_pending_desktops is not None:
            for k in self.fota_pending_desktops:
                result['FotaPendingDesktops'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fota_pending_desktops = []
        if m.get('FotaPendingDesktops') is not None:
            for k in m.get('FotaPendingDesktops'):
                temp_model = DescribeFotaPendingDesktopsResponseBodyFotaPendingDesktops()
                self.fota_pending_desktops.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFotaPendingDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFotaPendingDesktopsResponseBody = None,
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
            temp_model = DescribeFotaPendingDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFotaTasksRequest(TeaModel):
    def __init__(
        self,
        fota_status: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_uid: List[str] = None,
        user_status: str = None,
    ):
        self.fota_status = fota_status
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.task_uid = task_uid
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fota_status is not None:
            result['FotaStatus'] = self.fota_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FotaStatus') is not None:
            self.fota_status = m.get('FotaStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class DescribeFotaTasksResponseBodyFotaTasks(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        fota_project: str = None,
        pending_desktop_count: int = None,
        publish_time: str = None,
        release_note: str = None,
        size: int = None,
        status: str = None,
        task_uid: str = None,
    ):
        self.app_version = app_version
        self.fota_project = fota_project
        self.pending_desktop_count = pending_desktop_count
        self.publish_time = publish_time
        self.release_note = release_note
        self.size = size
        self.status = status
        self.task_uid = task_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.fota_project is not None:
            result['FotaProject'] = self.fota_project
        if self.pending_desktop_count is not None:
            result['PendingDesktopCount'] = self.pending_desktop_count
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('FotaProject') is not None:
            self.fota_project = m.get('FotaProject')
        if m.get('PendingDesktopCount') is not None:
            self.pending_desktop_count = m.get('PendingDesktopCount')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        return self


class DescribeFotaTasksResponseBody(TeaModel):
    def __init__(
        self,
        fota_tasks: List[DescribeFotaTasksResponseBodyFotaTasks] = None,
        request_id: str = None,
    ):
        self.fota_tasks = fota_tasks
        self.request_id = request_id

    def validate(self):
        if self.fota_tasks:
            for k in self.fota_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FotaTasks'] = []
        if self.fota_tasks is not None:
            for k in self.fota_tasks:
                result['FotaTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fota_tasks = []
        if m.get('FotaTasks') is not None:
            for k in m.get('FotaTasks'):
                temp_model = DescribeFotaTasksResponseBodyFotaTasks()
                self.fota_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFotaTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFotaTasksResponseBody = None,
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
            temp_model = DescribeFotaTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFrontVulPatchListRequestVulInfo(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        name: str = None,
        tag: str = None,
    ):
        self.desktop_id = desktop_id
        self.name = name
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeFrontVulPatchListRequest(TeaModel):
    def __init__(
        self,
        operate_type: str = None,
        region_id: str = None,
        type: str = None,
        vul_info: List[DescribeFrontVulPatchListRequestVulInfo] = None,
    ):
        self.operate_type = operate_type
        self.region_id = region_id
        self.type = type
        self.vul_info = vul_info

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = DescribeFrontVulPatchListRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        name: str = None,
    ):
        self.alias_name = alias_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFrontVulPatchListResponseBodyFrontPatchList(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        patch_list: List[DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList] = None,
    ):
        self.desktop_id = desktop_id
        self.patch_list = patch_list

    def validate(self):
        if self.patch_list:
            for k in self.patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        result['PatchList'] = []
        if self.patch_list is not None:
            for k in self.patch_list:
                result['PatchList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        self.patch_list = []
        if m.get('PatchList') is not None:
            for k in m.get('PatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchListPatchList()
                self.patch_list.append(temp_model.from_map(k))
        return self


class DescribeFrontVulPatchListResponseBody(TeaModel):
    def __init__(
        self,
        front_patch_list: List[DescribeFrontVulPatchListResponseBodyFrontPatchList] = None,
        request_id: str = None,
    ):
        self.front_patch_list = front_patch_list
        self.request_id = request_id

    def validate(self):
        if self.front_patch_list:
            for k in self.front_patch_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FrontPatchList'] = []
        if self.front_patch_list is not None:
            for k in self.front_patch_list:
                result['FrontPatchList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.front_patch_list = []
        if m.get('FrontPatchList') is not None:
            for k in m.get('FrontPatchList'):
                temp_model = DescribeFrontVulPatchListResponseBodyFrontPatchList()
                self.front_patch_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFrontVulPatchListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFrontVulPatchListResponseBody = None,
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
            temp_model = DescribeFrontVulPatchListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupedVulRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dealed: str = None,
        lang: str = None,
        necessity: str = None,
        office_site_id: str = None,
        page_size: int = None,
        region_id: str = None,
        type: str = None,
    ):
        self.current_page = current_page
        self.dealed = dealed
        self.lang = lang
        self.necessity = necessity
        self.office_site_id = office_site_id
        self.page_size = page_size
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeGroupedVulResponseBodyGroupedVulItems(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        asap_count: int = None,
        gmt_last: str = None,
        handled_count: int = None,
        later_count: int = None,
        name: str = None,
        nntf_count: int = None,
        tags: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.asap_count = asap_count
        self.gmt_last = gmt_last
        self.handled_count = handled_count
        self.later_count = later_count
        self.name = name
        self.nntf_count = nntf_count
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last
        if self.handled_count is not None:
            result['HandledCount'] = self.handled_count
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.name is not None:
            result['Name'] = self.name
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')
        if m.get('HandledCount') is not None:
            self.handled_count = m.get('HandledCount')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeGroupedVulResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        grouped_vul_items: List[DescribeGroupedVulResponseBodyGroupedVulItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.grouped_vul_items = grouped_vul_items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.grouped_vul_items:
            for k in self.grouped_vul_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['GroupedVulItems'] = []
        if self.grouped_vul_items is not None:
            for k in self.grouped_vul_items:
                result['GroupedVulItems'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.grouped_vul_items = []
        if m.get('GroupedVulItems') is not None:
            for k in m.get('GroupedVulItems'):
                temp_model = DescribeGroupedVulResponseBodyGroupedVulItems()
                self.grouped_vul_items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeGroupedVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGroupedVulResponseBody = None,
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
            temp_model = DescribeGroupedVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageModifiedRecordsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeImageModifiedRecordsResponseBodyImageModifiedRecords(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        new_image_id: str = None,
        new_image_name: str = None,
        status: int = None,
        update_time: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.new_image_id = new_image_id
        self.new_image_name = new_image_name
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.new_image_id is not None:
            result['NewImageId'] = self.new_image_id
        if self.new_image_name is not None:
            result['NewImageName'] = self.new_image_name
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('NewImageId') is not None:
            self.new_image_id = m.get('NewImageId')
        if m.get('NewImageName') is not None:
            self.new_image_name = m.get('NewImageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeImageModifiedRecordsResponseBody(TeaModel):
    def __init__(
        self,
        image_modified_records: List[DescribeImageModifiedRecordsResponseBodyImageModifiedRecords] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.image_modified_records = image_modified_records
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.image_modified_records:
            for k in self.image_modified_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageModifiedRecords'] = []
        if self.image_modified_records is not None:
            for k in self.image_modified_records:
                result['ImageModifiedRecords'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_modified_records = []
        if m.get('ImageModifiedRecords') is not None:
            for k in m.get('ImageModifiedRecords'):
                temp_model = DescribeImageModifiedRecordsResponseBodyImageModifiedRecords()
                self.image_modified_records.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageModifiedRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageModifiedRecordsResponseBody = None,
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
            temp_model = DescribeImageModifiedRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagePermissionRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        region_id: str = None,
    ):
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeImagePermissionResponseBody(TeaModel):
    def __init__(
        self,
        ali_uids: List[str] = None,
        request_id: str = None,
    ):
        self.ali_uids = ali_uids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uids is not None:
            result['AliUids'] = self.ali_uids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUids') is not None:
            self.ali_uids = m.get('AliUids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImagePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImagePermissionResponseBody = None,
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
            temp_model = DescribeImagePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        desktop_instance_type: str = None,
        fota_channel: str = None,
        gpu_category: bool = None,
        gpu_driver_version: str = None,
        image_id: List[str] = None,
        image_status: str = None,
        image_type: str = None,
        language_type: str = None,
        max_results: int = None,
        next_token: str = None,
        os_type: str = None,
        protocol_type: str = None,
        region_id: str = None,
    ):
        self.desktop_instance_type = desktop_instance_type
        self.fota_channel = fota_channel
        self.gpu_category = gpu_category
        self.gpu_driver_version = gpu_driver_version
        self.image_id = image_id
        self.image_status = image_status
        self.image_type = image_type
        self.language_type = language_type
        self.max_results = max_results
        self.next_token = next_token
        self.os_type = os_type
        self.protocol_type = protocol_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_instance_type is not None:
            result['DesktopInstanceType'] = self.desktop_instance_type
        if self.fota_channel is not None:
            result['FotaChannel'] = self.fota_channel
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_status is not None:
            result['ImageStatus'] = self.image_status
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.language_type is not None:
            result['LanguageType'] = self.language_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopInstanceType') is not None:
            self.desktop_instance_type = m.get('DesktopInstanceType')
        if m.get('FotaChannel') is not None:
            self.fota_channel = m.get('FotaChannel')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageStatus') is not None:
            self.image_status = m.get('ImageStatus')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        creation_time: str = None,
        data_disk_size: int = None,
        description: str = None,
        gpu_category: bool = None,
        gpu_driver_version: str = None,
        image_id: str = None,
        image_type: str = None,
        name: str = None,
        os_type: str = None,
        progress: str = None,
        protocol_type: str = None,
        session_type: str = None,
        shared_count: int = None,
        size: int = None,
        status: str = None,
        supported_languages: List[str] = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        self.app_version = app_version
        self.creation_time = creation_time
        self.data_disk_size = data_disk_size
        self.description = description
        self.gpu_category = gpu_category
        self.gpu_driver_version = gpu_driver_version
        self.image_id = image_id
        self.image_type = image_type
        self.name = name
        self.os_type = os_type
        self.progress = progress
        self.protocol_type = protocol_type
        self.session_type = session_type
        self.shared_count = shared_count
        self.size = size
        self.status = status
        self.supported_languages = supported_languages
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.name is not None:
            result['Name'] = self.name
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        if self.shared_count is not None:
            result['SharedCount'] = self.shared_count
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.supported_languages is not None:
            result['SupportedLanguages'] = self.supported_languages
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        if m.get('SharedCount') is not None:
            self.shared_count = m.get('SharedCount')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportedLanguages') is not None:
            self.supported_languages = m.get('SupportedLanguages')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[DescribeImagesResponseBodyImages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.images = images
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = DescribeImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImagesResponseBody = None,
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
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        command_type: str = None,
        content_encoding: str = None,
        desktop_id: str = None,
        include_output: bool = None,
        invoke_id: str = None,
        invoke_status: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.command_type = command_type
        self.content_encoding = content_encoding
        self.desktop_id = desktop_id
        self.include_output = include_output
        self.invoke_id = invoke_id
        self.invoke_status = invoke_status
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInvocationsResponseBodyInvocationsInvokeDesktops(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        desktop_id: str = None,
        dropped: int = None,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        invocation_status: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.desktop_id = desktop_id
        self.dropped = dropped
        self.error_code = error_code
        self.error_info = error_info
        self.exit_code = exit_code
        self.finish_time = finish_time
        self.invocation_status = invocation_status
        self.output = output
        self.repeats = repeats
        self.start_time = start_time
        self.stop_time = stop_time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.output is not None:
            result['Output'] = self.output
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeInvocationsResponseBodyInvocations(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_type: str = None,
        creation_time: str = None,
        end_user_id: str = None,
        invocation_status: str = None,
        invoke_desktops: List[DescribeInvocationsResponseBodyInvocationsInvokeDesktops] = None,
        invoke_id: str = None,
    ):
        self.command_content = command_content
        self.command_type = command_type
        self.creation_time = creation_time
        self.end_user_id = end_user_id
        self.invocation_status = invocation_status
        self.invoke_desktops = invoke_desktops
        self.invoke_id = invoke_id

    def validate(self):
        if self.invoke_desktops:
            for k in self.invoke_desktops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        result['InvokeDesktops'] = []
        if self.invoke_desktops is not None:
            for k in self.invoke_desktops:
                result['InvokeDesktops'].append(k.to_map() if k else None)
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        self.invoke_desktops = []
        if m.get('InvokeDesktops') is not None:
            for k in m.get('InvokeDesktops'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvokeDesktops()
                self.invoke_desktops.append(temp_model.from_map(k))
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: List[DescribeInvocationsResponseBodyInvocations] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.invocations = invocations
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['Invocations'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocations = []
        if m.get('Invocations') is not None:
            for k in m.get('Invocations'):
                temp_model = DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationsResponseBody = None,
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
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKmsKeysRequest(TeaModel):
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


class DescribeKmsKeysResponseBodyKeys(TeaModel):
    def __init__(
        self,
        alias: str = None,
        arn: str = None,
        key_id: str = None,
        type: str = None,
    ):
        self.alias = alias
        self.arn = arn
        self.key_id = key_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeKmsKeysResponseBody(TeaModel):
    def __init__(
        self,
        authorize_status: str = None,
        keys: List[DescribeKmsKeysResponseBodyKeys] = None,
        kms_service_status: str = None,
        request_id: str = None,
    ):
        self.authorize_status = authorize_status
        self.keys = keys
        self.kms_service_status = kms_service_status
        self.request_id = request_id

    def validate(self):
        if self.keys:
            for k in self.keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_status is not None:
            result['AuthorizeStatus'] = self.authorize_status
        result['Keys'] = []
        if self.keys is not None:
            for k in self.keys:
                result['Keys'].append(k.to_map() if k else None)
        if self.kms_service_status is not None:
            result['KmsServiceStatus'] = self.kms_service_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeStatus') is not None:
            self.authorize_status = m.get('AuthorizeStatus')
        self.keys = []
        if m.get('Keys') is not None:
            for k in m.get('Keys'):
                temp_model = DescribeKmsKeysResponseBodyKeys()
                self.keys.append(temp_model.from_map(k))
        if m.get('KmsServiceStatus') is not None:
            self.kms_service_status = m.get('KmsServiceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeKmsKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKmsKeysResponseBody = None,
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
            temp_model = DescribeKmsKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNASFileSystemsRequest(TeaModel):
    def __init__(
        self,
        file_system_id: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNASFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        create_time: str = None,
        description: str = None,
        encryption_enabled: bool = None,
        file_system_id: str = None,
        file_system_name: str = None,
        file_system_status: str = None,
        file_system_type: str = None,
        metered_size: int = None,
        mount_target_domain: str = None,
        mount_target_status: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        storage_type: str = None,
        support_acl: bool = None,
        zone_id: str = None,
    ):
        self.capacity = capacity
        self.create_time = create_time
        self.description = description
        self.encryption_enabled = encryption_enabled
        self.file_system_id = file_system_id
        self.file_system_name = file_system_name
        self.file_system_status = file_system_status
        self.file_system_type = file_system_type
        self.metered_size = metered_size
        self.mount_target_domain = mount_target_domain
        self.mount_target_status = mount_target_status
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.storage_type = storage_type
        self.support_acl = support_acl
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.encryption_enabled is not None:
            result['EncryptionEnabled'] = self.encryption_enabled
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.file_system_status is not None:
            result['FileSystemStatus'] = self.file_system_status
        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.mount_target_status is not None:
            result['MountTargetStatus'] = self.mount_target_status
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.support_acl is not None:
            result['SupportAcl'] = self.support_acl
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EncryptionEnabled') is not None:
            self.encryption_enabled = m.get('EncryptionEnabled')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('FileSystemStatus') is not None:
            self.file_system_status = m.get('FileSystemStatus')
        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('MountTargetStatus') is not None:
            self.mount_target_status = m.get('MountTargetStatus')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('SupportAcl') is not None:
            self.support_acl = m.get('SupportAcl')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeNASFileSystemsResponseBody(TeaModel):
    def __init__(
        self,
        file_systems: List[DescribeNASFileSystemsResponseBodyFileSystems] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.file_systems = file_systems
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = DescribeNASFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNASFileSystemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNASFileSystemsResponseBody = None,
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
            temp_model = DescribeNASFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNetworkPackagesRequest(TeaModel):
    def __init__(
        self,
        internet_charge_type: str = None,
        max_results: int = None,
        network_package_id: List[str] = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.internet_charge_type = internet_charge_type
        self.max_results = max_results
        self.network_package_id = network_package_id
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNetworkPackagesResponseBodyNetworkPackages(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        create_time: str = None,
        eip_addresses: List[str] = None,
        expired_time: str = None,
        internet_charge_type: str = None,
        network_package_id: str = None,
        network_package_status: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_vpc_type: str = None,
    ):
        self.bandwidth = bandwidth
        self.create_time = create_time
        self.eip_addresses = eip_addresses
        self.expired_time = expired_time
        self.internet_charge_type = internet_charge_type
        self.network_package_id = network_package_id
        self.network_package_status = network_package_status
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_vpc_type = office_site_vpc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.network_package_status is not None:
            result['NetworkPackageStatus'] = self.network_package_status
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_vpc_type is not None:
            result['OfficeSiteVpcType'] = self.office_site_vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EipAddresses') is not None:
            self.eip_addresses = m.get('EipAddresses')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('NetworkPackageStatus') is not None:
            self.network_package_status = m.get('NetworkPackageStatus')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteVpcType') is not None:
            self.office_site_vpc_type = m.get('OfficeSiteVpcType')
        return self


class DescribeNetworkPackagesResponseBody(TeaModel):
    def __init__(
        self,
        network_packages: List[DescribeNetworkPackagesResponseBodyNetworkPackages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.network_packages = network_packages
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.network_packages:
            for k in self.network_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkPackages'] = []
        if self.network_packages is not None:
            for k in self.network_packages:
                result['NetworkPackages'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_packages = []
        if m.get('NetworkPackages') is not None:
            for k in m.get('NetworkPackages'):
                temp_model = DescribeNetworkPackagesResponseBodyNetworkPackages()
                self.network_packages.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNetworkPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNetworkPackagesResponseBody = None,
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
            temp_model = DescribeNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOfficeSitesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
        office_site_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.office_site_type = office_site_type
        self.region_id = region_id
        self.status = status

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
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesADConnectors(TeaModel):
    def __init__(
        self,
        adconnector_address: str = None,
        connector_status: str = None,
        network_interface_id: str = None,
        specification: str = None,
        trust_key: str = None,
        v_switch_id: str = None,
    ):
        self.adconnector_address = adconnector_address
        self.connector_status = connector_status
        self.network_interface_id = network_interface_id
        self.specification = specification
        self.trust_key = trust_key
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adconnector_address is not None:
            result['ADConnectorAddress'] = self.adconnector_address
        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.trust_key is not None:
            result['TrustKey'] = self.trust_key
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ADConnectorAddress') is not None:
            self.adconnector_address = m.get('ADConnectorAddress')
        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('TrustKey') is not None:
            self.trust_key = m.get('TrustKey')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeOfficeSitesResponseBodyOfficeSitesLogs(TeaModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        step: str = None,
        time_stamp: str = None,
    ):
        self.level = level
        self.message = message
        self.step = step
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.step is not None:
            result['Step'] = self.step
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class DescribeOfficeSitesResponseBodyOfficeSites(TeaModel):
    def __init__(
        self,
        adconnectors: List[DescribeOfficeSitesResponseBodyOfficeSitesADConnectors] = None,
        ad_hostname: str = None,
        bandwidth: int = None,
        cen_id: str = None,
        cidr_block: str = None,
        cloud_box_office_site: bool = None,
        creation_time: str = None,
        custom_security_group_id: str = None,
        desktop_access_type: str = None,
        desktop_count: int = None,
        desktop_vpc_endpoint: str = None,
        dns_address: List[str] = None,
        dns_user_name: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_cross_desktop_access: bool = None,
        enable_internet_access: bool = None,
        file_system_ids: List[str] = None,
        logs: List[DescribeOfficeSitesResponseBodyOfficeSitesLogs] = None,
        mfa_enabled: bool = None,
        name: str = None,
        need_verify_login_risk: bool = None,
        need_verify_zero_device: bool = None,
        network_package_id: str = None,
        office_site_id: str = None,
        office_site_type: str = None,
        ou_name: str = None,
        protocol_type: str = None,
        sso_enabled: bool = None,
        sso_type: str = None,
        status: str = None,
        sub_dns_address: List[str] = None,
        sub_domain_name: str = None,
        trust_password: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_type: str = None,
    ):
        self.adconnectors = adconnectors
        self.ad_hostname = ad_hostname
        self.bandwidth = bandwidth
        self.cen_id = cen_id
        self.cidr_block = cidr_block
        self.cloud_box_office_site = cloud_box_office_site
        self.creation_time = creation_time
        self.custom_security_group_id = custom_security_group_id
        self.desktop_access_type = desktop_access_type
        self.desktop_count = desktop_count
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.dns_address = dns_address
        self.dns_user_name = dns_user_name
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.enable_admin_access = enable_admin_access
        self.enable_cross_desktop_access = enable_cross_desktop_access
        self.enable_internet_access = enable_internet_access
        self.file_system_ids = file_system_ids
        self.logs = logs
        self.mfa_enabled = mfa_enabled
        self.name = name
        self.need_verify_login_risk = need_verify_login_risk
        self.need_verify_zero_device = need_verify_zero_device
        self.network_package_id = network_package_id
        self.office_site_id = office_site_id
        self.office_site_type = office_site_type
        self.ou_name = ou_name
        self.protocol_type = protocol_type
        self.sso_enabled = sso_enabled
        self.sso_type = sso_type
        self.status = status
        self.sub_dns_address = sub_dns_address
        self.sub_domain_name = sub_domain_name
        self.trust_password = trust_password
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type

    def validate(self):
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.cloud_box_office_site is not None:
            result['CloudBoxOfficeSite'] = self.cloud_box_office_site
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.custom_security_group_id is not None:
            result['CustomSecurityGroupId'] = self.custom_security_group_id
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count
        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.dns_user_name is not None:
            result['DnsUserName'] = self.dns_user_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access
        if self.file_system_ids is not None:
            result['FileSystemIds'] = self.file_system_ids
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.need_verify_login_risk is not None:
            result['NeedVerifyLoginRisk'] = self.need_verify_login_risk
        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.ou_name is not None:
            result['OuName'] = self.ou_name
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.sso_enabled is not None:
            result['SsoEnabled'] = self.sso_enabled
        if self.sso_type is not None:
            result['SsoType'] = self.sso_type
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_dns_address is not None:
            result['SubDnsAddress'] = self.sub_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        if self.trust_password is not None:
            result['TrustPassword'] = self.trust_password
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.adconnectors = []
        if m.get('ADConnectors') is not None:
            for k in m.get('ADConnectors'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CloudBoxOfficeSite') is not None:
            self.cloud_box_office_site = m.get('CloudBoxOfficeSite')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('CustomSecurityGroupId') is not None:
            self.custom_security_group_id = m.get('CustomSecurityGroupId')
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')
        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DnsUserName') is not None:
            self.dns_user_name = m.get('DnsUserName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')
        if m.get('FileSystemIds') is not None:
            self.file_system_ids = m.get('FileSystemIds')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSitesLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')
        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('OuName') is not None:
            self.ou_name = m.get('OuName')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('SsoEnabled') is not None:
            self.sso_enabled = m.get('SsoEnabled')
        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubDnsAddress') is not None:
            self.sub_dns_address = m.get('SubDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        if m.get('TrustPassword') is not None:
            self.trust_password = m.get('TrustPassword')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        return self


class DescribeOfficeSitesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        office_sites: List[DescribeOfficeSitesResponseBodyOfficeSites] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.office_sites = office_sites
        self.request_id = request_id

    def validate(self):
        if self.office_sites:
            for k in self.office_sites:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k in self.office_sites:
                result['OfficeSites'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k in m.get('OfficeSites'):
                temp_model = DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOfficeSitesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOfficeSitesResponseBody = None,
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
            temp_model = DescribeOfficeSitesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_group_id: List[str] = None,
        region_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.policy_group_id = policy_group_id
        self.region_id = region_id

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
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        type: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        self.client_type = client_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_class: str = None,
        device_subclass: str = None,
        product_id: str = None,
        usb_redirect_type: int = None,
        usb_rule_type: int = None,
        vendor_id: str = None,
    ):
        self.description = description
        self.device_class = device_class
        self.device_subclass = device_subclass
        self.product_id = product_id
        self.usb_redirect_type = usb_redirect_type
        self.usb_rule_type = usb_rule_type
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_class is not None:
            result['DeviceClass'] = self.device_class
        if self.device_subclass is not None:
            result['DeviceSubclass'] = self.device_subclass
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.usb_redirect_type is not None:
            result['UsbRedirectType'] = self.usb_redirect_type
        if self.usb_rule_type is not None:
            result['UsbRuleType'] = self.usb_rule_type
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')
        if m.get('DeviceSubclass') is not None:
            self.device_subclass = m.get('DeviceSubclass')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UsbRedirectType') is not None:
            self.usb_redirect_type = m.get('UsbRedirectType')
        if m.get('UsbRuleType') is not None:
            self.usb_rule_type = m.get('UsbRuleType')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class DescribePolicyGroupsResponseBodyDescribePolicyGroups(TeaModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules] = None,
        authorize_security_policy_rules: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules] = None,
        camera_redirect: str = None,
        client_types: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes] = None,
        clipboard: str = None,
        domain_list: str = None,
        eds_count: int = None,
        gpu_acceleration: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        name: str = None,
        net_redirect: str = None,
        policy_group_id: str = None,
        policy_group_type: str = None,
        policy_status: str = None,
        preempt_login: str = None,
        preempt_login_users: List[str] = None,
        printer_redirection: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        recording: str = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: int = None,
        recording_start_time: str = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule] = None,
        visual_quality: str = None,
        watermark: str = None,
        watermark_custom_text: str = None,
        watermark_transparency: str = None,
        watermark_type: str = None,
    ):
        self.app_content_protection = app_content_protection
        self.authorize_access_policy_rules = authorize_access_policy_rules
        self.authorize_security_policy_rules = authorize_security_policy_rules
        self.camera_redirect = camera_redirect
        self.client_types = client_types
        self.clipboard = clipboard
        self.domain_list = domain_list
        self.eds_count = eds_count
        self.gpu_acceleration = gpu_acceleration
        self.html_5access = html_5access
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.name = name
        self.net_redirect = net_redirect
        self.policy_group_id = policy_group_id
        self.policy_group_type = policy_group_type
        self.policy_status = policy_status
        self.preempt_login = preempt_login
        self.preempt_login_users = preempt_login_users
        self.printer_redirection = printer_redirection
        self.record_content = record_content
        self.record_content_expires = record_content_expires
        self.recording = recording
        self.recording_end_time = recording_end_time
        self.recording_expires = recording_expires
        self.recording_fps = recording_fps
        self.recording_start_time = recording_start_time
        self.usb_redirect = usb_redirect
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.visual_quality = visual_quality
        self.watermark = watermark
        self.watermark_custom_text = watermark_custom_text
        self.watermark_transparency = watermark_transparency
        self.watermark_type = watermark_type

    def validate(self):
        if self.authorize_access_policy_rules:
            for k in self.authorize_access_policy_rules:
                if k:
                    k.validate()
        if self.authorize_security_policy_rules:
            for k in self.authorize_security_policy_rules:
                if k:
                    k.validate()
        if self.client_types:
            for k in self.client_types:
                if k:
                    k.validate()
        if self.usb_supply_redirect_rule:
            for k in self.usb_supply_redirect_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection
        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k.to_map() if k else None)
        result['AuthorizeSecurityPolicyRules'] = []
        if self.authorize_security_policy_rules is not None:
            for k in self.authorize_security_policy_rules:
                result['AuthorizeSecurityPolicyRules'].append(k.to_map() if k else None)
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        result['ClientTypes'] = []
        if self.client_types is not None:
            for k in self.client_types:
                result['ClientTypes'].append(k.to_map() if k else None)
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.eds_count is not None:
            result['EdsCount'] = self.eds_count
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.name is not None:
            result['Name'] = self.name
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type
        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.preempt_login_users is not None:
            result['PreemptLoginUsers'] = self.preempt_login_users
        if self.printer_redirection is not None:
            result['PrinterRedirection'] = self.printer_redirection
        if self.record_content is not None:
            result['RecordContent'] = self.record_content
        if self.record_content_expires is not None:
            result['RecordContentExpires'] = self.record_content_expires
        if self.recording is not None:
            result['Recording'] = self.recording
        if self.recording_end_time is not None:
            result['RecordingEndTime'] = self.recording_end_time
        if self.recording_expires is not None:
            result['RecordingExpires'] = self.recording_expires
        if self.recording_fps is not None:
            result['RecordingFps'] = self.recording_fps
        if self.recording_start_time is not None:
            result['RecordingStartTime'] = self.recording_start_time
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        result['UsbSupplyRedirectRule'] = []
        if self.usb_supply_redirect_rule is not None:
            for k in self.usb_supply_redirect_rule:
                result['UsbSupplyRedirectRule'].append(k.to_map() if k else None)
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')
        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k in m.get('AuthorizeAccessPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k))
        self.authorize_security_policy_rules = []
        if m.get('AuthorizeSecurityPolicyRules') is not None:
            for k in m.get('AuthorizeSecurityPolicyRules'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules()
                self.authorize_security_policy_rules.append(temp_model.from_map(k))
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k in m.get('ClientTypes'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes()
                self.client_types.append(temp_model.from_map(k))
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('EdsCount') is not None:
            self.eds_count = m.get('EdsCount')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')
        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('PreemptLoginUsers') is not None:
            self.preempt_login_users = m.get('PreemptLoginUsers')
        if m.get('PrinterRedirection') is not None:
            self.printer_redirection = m.get('PrinterRedirection')
        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')
        if m.get('RecordContentExpires') is not None:
            self.record_content_expires = m.get('RecordContentExpires')
        if m.get('Recording') is not None:
            self.recording = m.get('Recording')
        if m.get('RecordingEndTime') is not None:
            self.recording_end_time = m.get('RecordingEndTime')
        if m.get('RecordingExpires') is not None:
            self.recording_expires = m.get('RecordingExpires')
        if m.get('RecordingFps') is not None:
            self.recording_fps = m.get('RecordingFps')
        if m.get('RecordingStartTime') is not None:
            self.recording_start_time = m.get('RecordingStartTime')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k in m.get('UsbSupplyRedirectRule'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule()
                self.usb_supply_redirect_rule.append(temp_model.from_map(k))
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class DescribePolicyGroupsResponseBody(TeaModel):
    def __init__(
        self,
        describe_policy_groups: List[DescribePolicyGroupsResponseBodyDescribePolicyGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.describe_policy_groups = describe_policy_groups
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_policy_groups = []
        if m.get('DescribePolicyGroups') is not None:
            for k in m.get('DescribePolicyGroups'):
                temp_model = DescribePolicyGroupsResponseBodyDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePolicyGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyGroupsResponseBody = None,
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
            temp_model = DescribePolicyGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
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
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScanTaskProgressRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: int = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeScanTaskProgressResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        request_id: str = None,
        task_status: str = None,
    ):
        self.create_time = create_time
        self.request_id = request_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeScanTaskProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeScanTaskProgressResponseBody = None,
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
            temp_model = DescribeScanTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_event_id: List[str] = None,
        task_id: int = None,
    ):
        self.region_id = region_id
        self.security_event_id = security_event_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        security_event_id: int = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.security_event_id = security_event_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSecurityEventOperationStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operation_statuses: List[DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses] = None,
        task_status: str = None,
    ):
        self.request_id = request_id
        self.security_event_operation_statuses = security_event_operation_statuses
        self.task_status = task_status

    def validate(self):
        if self.security_event_operation_statuses:
            for k in self.security_event_operation_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperationStatuses'] = []
        if self.security_event_operation_statuses is not None:
            for k in self.security_event_operation_statuses:
                result['SecurityEventOperationStatuses'].append(k.to_map() if k else None)
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operation_statuses = []
        if m.get('SecurityEventOperationStatuses') is not None:
            for k in m.get('SecurityEventOperationStatuses'):
                temp_model = DescribeSecurityEventOperationStatusResponseBodySecurityEventOperationStatuses()
                self.security_event_operation_statuses.append(temp_model.from_map(k))
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class DescribeSecurityEventOperationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityEventOperationStatusResponseBody = None,
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
            temp_model = DescribeSecurityEventOperationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityEventOperationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_event_id: int = None,
    ):
        self.region_id = region_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class DescribeSecurityEventOperationsResponseBodySecurityEventOperations(TeaModel):
    def __init__(
        self,
        operation_code: str = None,
        operation_params: str = None,
        user_can_operate: bool = None,
    ):
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.user_can_operate = user_can_operate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.user_can_operate is not None:
            result['UserCanOperate'] = self.user_can_operate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')
        return self


class DescribeSecurityEventOperationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operations: List[DescribeSecurityEventOperationsResponseBodySecurityEventOperations] = None,
    ):
        self.request_id = request_id
        self.security_event_operations = security_event_operations

    def validate(self):
        if self.security_event_operations:
            for k in self.security_event_operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityEventOperations'] = []
        if self.security_event_operations is not None:
            for k in self.security_event_operations:
                result['SecurityEventOperations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_event_operations = []
        if m.get('SecurityEventOperations') is not None:
            for k in m.get('SecurityEventOperations'):
                temp_model = DescribeSecurityEventOperationsResponseBodySecurityEventOperations()
                self.security_event_operations.append(temp_model.from_map(k))
        return self


class DescribeSecurityEventOperationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityEventOperationsResponseBody = None,
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
            temp_model = DescribeSecurityEventOperationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSnapshotsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DescribeSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        desktop_id: str = None,
        progress: str = None,
        protocol_type: str = None,
        remain_time: int = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        snapshot_type: str = None,
        source_disk_size: str = None,
        source_disk_type: str = None,
        status: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.desktop_id = desktop_id
        self.progress = progress
        self.protocol_type = protocol_type
        self.remain_time = remain_time
        self.snapshot_id = snapshot_id
        self.snapshot_name = snapshot_name
        self.snapshot_type = snapshot_type
        self.source_disk_size = source_disk_size
        self.source_disk_type = source_disk_type
        self.status = status
        self.volume_encryption_enabled = volume_encryption_enabled
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.snapshot_type is not None:
            result['SnapshotType'] = self.snapshot_type
        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.status is not None:
            result['Status'] = self.status
        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled
        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SnapshotType') is not None:
            self.snapshot_type = m.get('SnapshotType')
        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')
        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')
        return self


class DescribeSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        snapshots: List[DescribeSnapshotsResponseBodySnapshots] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.snapshots = snapshots

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = DescribeSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        return self


class DescribeSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSnapshotsResponseBody = None,
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
            temp_model = DescribeSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventOverviewRequest(TeaModel):
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


class DescribeSuspEventOverviewResponseBody(TeaModel):
    def __init__(
        self,
        remind_count: int = None,
        request_id: str = None,
        serious_count: int = None,
        suspicious_count: int = None,
    ):
        self.remind_count = remind_count
        self.request_id = request_id
        self.serious_count = serious_count
        self.suspicious_count = suspicious_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remind_count is not None:
            result['RemindCount'] = self.remind_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.serious_count is not None:
            result['SeriousCount'] = self.serious_count
        if self.suspicious_count is not None:
            result['SuspiciousCount'] = self.suspicious_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemindCount') is not None:
            self.remind_count = m.get('RemindCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SeriousCount') is not None:
            self.serious_count = m.get('SeriousCount')
        if m.get('SuspiciousCount') is not None:
            self.suspicious_count = m.get('SuspiciousCount')
        return self


class DescribeSuspEventOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSuspEventOverviewResponseBody = None,
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
            temp_model = DescribeSuspEventOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventQuaraFilesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        office_site_id: str = None,
        page_size: int = None,
        region_id: str = None,
        status: str = None,
    ):
        self.current_page = current_page
        self.office_site_id = office_site_id
        self.page_size = page_size
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSuspEventQuaraFilesResponseBodyQuaraFiles(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        event_name: str = None,
        event_type: str = None,
        id: int = None,
        md_5: str = None,
        modify_time: str = None,
        path: str = None,
        status: str = None,
        tag: str = None,
    ):
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.event_name = event_name
        self.event_type = event_type
        self.id = id
        self.md_5 = md_5
        self.modify_time = modify_time
        self.path = path
        self.status = status
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeSuspEventQuaraFilesResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        quara_files: List[DescribeSuspEventQuaraFilesResponseBodyQuaraFiles] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.quara_files = quara_files
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.quara_files:
            for k in self.quara_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['QuaraFiles'] = []
        if self.quara_files is not None:
            for k in self.quara_files:
                result['QuaraFiles'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.quara_files = []
        if m.get('QuaraFiles') is not None:
            for k in m.get('QuaraFiles'):
                temp_model = DescribeSuspEventQuaraFilesResponseBodyQuaraFiles()
                self.quara_files.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSuspEventQuaraFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSuspEventQuaraFilesResponseBody = None,
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
            temp_model = DescribeSuspEventQuaraFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSuspEventsRequest(TeaModel):
    def __init__(
        self,
        alarm_unique_info: str = None,
        current_page: int = None,
        dealed: str = None,
        lang: str = None,
        levels: str = None,
        office_site_id: str = None,
        page_size: int = None,
        parent_event_type: str = None,
        region_id: str = None,
    ):
        self.alarm_unique_info = alarm_unique_info
        self.current_page = current_page
        self.dealed = dealed
        self.lang = lang
        self.levels = levels
        self.office_site_id = office_site_id
        self.page_size = page_size
        self.parent_event_type = parent_event_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.levels is not None:
            result['Levels'] = self.levels
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_event_type is not None:
            result['ParentEventType'] = self.parent_event_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentEventType') is not None:
            self.parent_event_type = m.get('ParentEventType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSuspEventsResponseBodySuspEventsDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        self.name = name
        self.name_display = name_display
        self.type = type
        self.value = value
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class DescribeSuspEventsResponseBodySuspEvents(TeaModel):
    def __init__(
        self,
        alarm_event_name: str = None,
        alarm_event_name_display: str = None,
        alarm_event_type: str = None,
        alarm_event_type_display: str = None,
        alarm_unique_info: str = None,
        can_be_deal_on_line: str = None,
        can_cancel_fault: bool = None,
        data_source: str = None,
        desc: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        details: List[DescribeSuspEventsResponseBodySuspEventsDetails] = None,
        event_status: int = None,
        event_sub_type: str = None,
        id: int = None,
        last_time: str = None,
        level: str = None,
        name: str = None,
        occurrence_time: str = None,
        operate_error_code: str = None,
        operate_msg: str = None,
        unique_info: str = None,
    ):
        self.alarm_event_name = alarm_event_name
        self.alarm_event_name_display = alarm_event_name_display
        self.alarm_event_type = alarm_event_type
        self.alarm_event_type_display = alarm_event_type_display
        self.alarm_unique_info = alarm_unique_info
        self.can_be_deal_on_line = can_be_deal_on_line
        self.can_cancel_fault = can_cancel_fault
        self.data_source = data_source
        self.desc = desc
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.details = details
        self.event_status = event_status
        self.event_sub_type = event_sub_type
        self.id = id
        self.last_time = last_time
        self.level = level
        self.name = name
        self.occurrence_time = occurrence_time
        self.operate_error_code = operate_error_code
        self.operate_msg = operate_msg
        self.unique_info = unique_info

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_event_name is not None:
            result['AlarmEventName'] = self.alarm_event_name
        if self.alarm_event_name_display is not None:
            result['AlarmEventNameDisplay'] = self.alarm_event_name_display
        if self.alarm_event_type is not None:
            result['AlarmEventType'] = self.alarm_event_type
        if self.alarm_event_type_display is not None:
            result['AlarmEventTypeDisplay'] = self.alarm_event_type_display
        if self.alarm_unique_info is not None:
            result['AlarmUniqueInfo'] = self.alarm_unique_info
        if self.can_be_deal_on_line is not None:
            result['CanBeDealOnLine'] = self.can_be_deal_on_line
        if self.can_cancel_fault is not None:
            result['CanCancelFault'] = self.can_cancel_fault
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.event_status is not None:
            result['EventStatus'] = self.event_status
        if self.event_sub_type is not None:
            result['EventSubType'] = self.event_sub_type
        if self.id is not None:
            result['Id'] = self.id
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.level is not None:
            result['Level'] = self.level
        if self.name is not None:
            result['Name'] = self.name
        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time
        if self.operate_error_code is not None:
            result['OperateErrorCode'] = self.operate_error_code
        if self.operate_msg is not None:
            result['OperateMsg'] = self.operate_msg
        if self.unique_info is not None:
            result['UniqueInfo'] = self.unique_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmEventName') is not None:
            self.alarm_event_name = m.get('AlarmEventName')
        if m.get('AlarmEventNameDisplay') is not None:
            self.alarm_event_name_display = m.get('AlarmEventNameDisplay')
        if m.get('AlarmEventType') is not None:
            self.alarm_event_type = m.get('AlarmEventType')
        if m.get('AlarmEventTypeDisplay') is not None:
            self.alarm_event_type_display = m.get('AlarmEventTypeDisplay')
        if m.get('AlarmUniqueInfo') is not None:
            self.alarm_unique_info = m.get('AlarmUniqueInfo')
        if m.get('CanBeDealOnLine') is not None:
            self.can_be_deal_on_line = m.get('CanBeDealOnLine')
        if m.get('CanCancelFault') is not None:
            self.can_cancel_fault = m.get('CanCancelFault')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeSuspEventsResponseBodySuspEventsDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')
        if m.get('EventSubType') is not None:
            self.event_sub_type = m.get('EventSubType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')
        if m.get('OperateErrorCode') is not None:
            self.operate_error_code = m.get('OperateErrorCode')
        if m.get('OperateMsg') is not None:
            self.operate_msg = m.get('OperateMsg')
        if m.get('UniqueInfo') is not None:
            self.unique_info = m.get('UniqueInfo')
        return self


class DescribeSuspEventsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: str = None,
        request_id: str = None,
        susp_events: List[DescribeSuspEventsResponseBodySuspEvents] = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.susp_events = susp_events
        self.total_count = total_count

    def validate(self):
        if self.susp_events:
            for k in self.susp_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuspEvents'] = []
        if self.susp_events is not None:
            for k in self.susp_events:
                result['SuspEvents'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.susp_events = []
        if m.get('SuspEvents') is not None:
            for k in m.get('SuspEvents'):
                temp_model = DescribeSuspEventsResponseBodySuspEvents()
                self.susp_events.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSuspEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSuspEventsResponseBody = None,
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
            temp_model = DescribeSuspEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserConnectionRecordsRequest(TeaModel):
    def __init__(
        self,
        connect_duration_from: int = None,
        connect_duration_to: int = None,
        connect_end_time_from: int = None,
        connect_end_time_to: int = None,
        connect_start_time_from: int = None,
        connect_start_time_to: int = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        end_user_id: str = None,
        end_user_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.connect_duration_from = connect_duration_from
        self.connect_duration_to = connect_duration_to
        self.connect_end_time_from = connect_end_time_from
        self.connect_end_time_to = connect_end_time_to
        self.connect_start_time_from = connect_start_time_from
        self.connect_start_time_to = connect_start_time_to
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id
        self.end_user_type = end_user_type
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_duration_from is not None:
            result['ConnectDurationFrom'] = self.connect_duration_from
        if self.connect_duration_to is not None:
            result['ConnectDurationTo'] = self.connect_duration_to
        if self.connect_end_time_from is not None:
            result['ConnectEndTimeFrom'] = self.connect_end_time_from
        if self.connect_end_time_to is not None:
            result['ConnectEndTimeTo'] = self.connect_end_time_to
        if self.connect_start_time_from is not None:
            result['ConnectStartTimeFrom'] = self.connect_start_time_from
        if self.connect_start_time_to is not None:
            result['ConnectStartTimeTo'] = self.connect_start_time_to
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDurationFrom') is not None:
            self.connect_duration_from = m.get('ConnectDurationFrom')
        if m.get('ConnectDurationTo') is not None:
            self.connect_duration_to = m.get('ConnectDurationTo')
        if m.get('ConnectEndTimeFrom') is not None:
            self.connect_end_time_from = m.get('ConnectEndTimeFrom')
        if m.get('ConnectEndTimeTo') is not None:
            self.connect_end_time_to = m.get('ConnectEndTimeTo')
        if m.get('ConnectStartTimeFrom') is not None:
            self.connect_start_time_from = m.get('ConnectStartTimeFrom')
        if m.get('ConnectStartTimeTo') is not None:
            self.connect_start_time_to = m.get('ConnectStartTimeTo')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUserConnectionRecordsResponseBodyConnectionRecords(TeaModel):
    def __init__(
        self,
        connect_duration: str = None,
        connect_end_time: str = None,
        connect_start_time: str = None,
        connection_record_id: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
    ):
        self.connect_duration = connect_duration
        self.connect_end_time = connect_end_time
        self.connect_start_time = connect_start_time
        self.connection_record_id = connection_record_id
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.connect_end_time is not None:
            result['ConnectEndTime'] = self.connect_end_time
        if self.connect_start_time is not None:
            result['ConnectStartTime'] = self.connect_start_time
        if self.connection_record_id is not None:
            result['ConnectionRecordId'] = self.connection_record_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('ConnectEndTime') is not None:
            self.connect_end_time = m.get('ConnectEndTime')
        if m.get('ConnectStartTime') is not None:
            self.connect_start_time = m.get('ConnectStartTime')
        if m.get('ConnectionRecordId') is not None:
            self.connection_record_id = m.get('ConnectionRecordId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        return self


class DescribeUserConnectionRecordsResponseBody(TeaModel):
    def __init__(
        self,
        connection_records: List[DescribeUserConnectionRecordsResponseBodyConnectionRecords] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.connection_records = connection_records
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.connection_records:
            for k in self.connection_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionRecords'] = []
        if self.connection_records is not None:
            for k in self.connection_records:
                result['ConnectionRecords'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_records = []
        if m.get('ConnectionRecords') is not None:
            for k in m.get('ConnectionRecords'):
                temp_model = DescribeUserConnectionRecordsResponseBodyConnectionRecords()
                self.connection_records.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserConnectionRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserConnectionRecordsResponseBody = None,
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
            temp_model = DescribeUserConnectionRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersInGroupRequest(TeaModel):
    def __init__(
        self,
        connect_state: int = None,
        desktop_group_id: str = None,
        end_user_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        query_user_detail: bool = None,
        region_id: str = None,
    ):
        self.connect_state = connect_state
        self.desktop_group_id = desktop_group_id
        self.end_user_id = end_user_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.query_user_detail = query_user_detail
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_state is not None:
            result['ConnectState'] = self.connect_state
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_user_detail is not None:
            result['QueryUserDetail'] = self.query_user_detail
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectState') is not None:
            self.connect_state = m.get('ConnectState')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryUserDetail') is not None:
            self.query_user_detail = m.get('QueryUserDetail')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUsersInGroupResponseBodyEndUsersExternalInfo(TeaModel):
    def __init__(
        self,
        external_name: str = None,
        job_number: str = None,
    ):
        self.external_name = external_name
        self.job_number = job_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['ExternalName'] = self.external_name
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        return self


class DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues(TeaModel):
    def __init__(
        self,
        property_value: str = None,
        property_value_id: int = None,
    ):
        self.property_value = property_value
        self.property_value_id = property_value_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels(TeaModel):
    def __init__(
        self,
        property_id: int = None,
        property_key: str = None,
        property_type: int = None,
        property_values: List[DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues] = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.property_id = property_id
        self.property_key = property_key
        self.property_type = property_type
        self.property_values = property_values
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_type is not None:
            result['PropertyType'] = self.property_type
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModelsPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeUsersInGroupResponseBodyEndUsers(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        end_user_email: str = None,
        end_user_id: str = None,
        end_user_name: str = None,
        end_user_phone: str = None,
        end_user_type: str = None,
        external_info: DescribeUsersInGroupResponseBodyEndUsersExternalInfo = None,
        user_desktop_id: str = None,
        user_set_properties_models: List[DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels] = None,
    ):
        self.connection_status = connection_status
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.end_user_email = end_user_email
        self.end_user_id = end_user_id
        self.end_user_name = end_user_name
        self.end_user_phone = end_user_phone
        self.end_user_type = end_user_type
        self.external_info = external_info
        self.user_desktop_id = user_desktop_id
        self.user_set_properties_models = user_set_properties_models

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.user_set_properties_models:
            for k in self.user_set_properties_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.end_user_email is not None:
            result['EndUserEmail'] = self.end_user_email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.end_user_name is not None:
            result['EndUserName'] = self.end_user_name
        if self.end_user_phone is not None:
            result['EndUserPhone'] = self.end_user_phone
        if self.end_user_type is not None:
            result['EndUserType'] = self.end_user_type
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()
        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id
        result['UserSetPropertiesModels'] = []
        if self.user_set_properties_models is not None:
            for k in self.user_set_properties_models:
                result['UserSetPropertiesModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('EndUserEmail') is not None:
            self.end_user_email = m.get('EndUserEmail')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EndUserName') is not None:
            self.end_user_name = m.get('EndUserName')
        if m.get('EndUserPhone') is not None:
            self.end_user_phone = m.get('EndUserPhone')
        if m.get('EndUserType') is not None:
            self.end_user_type = m.get('EndUserType')
        if m.get('ExternalInfo') is not None:
            temp_model = DescribeUsersInGroupResponseBodyEndUsersExternalInfo()
            self.external_info = temp_model.from_map(m['ExternalInfo'])
        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')
        self.user_set_properties_models = []
        if m.get('UserSetPropertiesModels') is not None:
            for k in m.get('UserSetPropertiesModels'):
                temp_model = DescribeUsersInGroupResponseBodyEndUsersUserSetPropertiesModels()
                self.user_set_properties_models.append(temp_model.from_map(k))
        return self


class DescribeUsersInGroupResponseBody(TeaModel):
    def __init__(
        self,
        end_users: List[DescribeUsersInGroupResponseBodyEndUsers] = None,
        next_token: str = None,
        online_users_count: int = None,
        request_id: str = None,
        users_count: int = None,
    ):
        self.end_users = end_users
        self.next_token = next_token
        self.online_users_count = online_users_count
        self.request_id = request_id
        self.users_count = users_count

    def validate(self):
        if self.end_users:
            for k in self.end_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndUsers'] = []
        if self.end_users is not None:
            for k in self.end_users:
                result['EndUsers'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.online_users_count is not None:
            result['OnlineUsersCount'] = self.online_users_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users_count is not None:
            result['UsersCount'] = self.users_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.end_users = []
        if m.get('EndUsers') is not None:
            for k in m.get('EndUsers'):
                temp_model = DescribeUsersInGroupResponseBodyEndUsers()
                self.end_users.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OnlineUsersCount') is not None:
            self.online_users_count = m.get('OnlineUsersCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsersCount') is not None:
            self.users_count = m.get('UsersCount')
        return self


class DescribeUsersInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersInGroupResponseBody = None,
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
            temp_model = DescribeUsersInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersPasswordRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUsersPasswordResponseBodyDesktopUsers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        end_user_id: str = None,
        password: str = None,
    ):
        self.display_name = display_name
        self.end_user_id = end_user_id
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class DescribeUsersPasswordResponseBody(TeaModel):
    def __init__(
        self,
        desktop_users: List[DescribeUsersPasswordResponseBodyDesktopUsers] = None,
        request_id: str = None,
    ):
        self.desktop_users = desktop_users
        self.request_id = request_id

    def validate(self):
        if self.desktop_users:
            for k in self.desktop_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DesktopUsers'] = []
        if self.desktop_users is not None:
            for k in self.desktop_users:
                result['DesktopUsers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_users = []
        if m.get('DesktopUsers') is not None:
            for k in m.get('DesktopUsers'):
                temp_model = DescribeUsersPasswordResponseBodyDesktopUsers()
                self.desktop_users.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUsersPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersPasswordResponseBody = None,
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
            temp_model = DescribeUsersPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVirtualMFADevicesRequest(TeaModel):
    def __init__(
        self,
        end_user_id: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.end_user_id = end_user_id
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeVirtualMFADevicesResponseBodyVirtualMFADevices(TeaModel):
    def __init__(
        self,
        consecutive_fails: int = None,
        directory_id: str = None,
        end_user_id: str = None,
        gmt_enabled: str = None,
        gmt_unlock: str = None,
        office_site_id: str = None,
        serial_number: str = None,
        status: str = None,
    ):
        self.consecutive_fails = consecutive_fails
        self.directory_id = directory_id
        self.end_user_id = end_user_id
        self.gmt_enabled = gmt_enabled
        self.gmt_unlock = gmt_unlock
        self.office_site_id = office_site_id
        self.serial_number = serial_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeVirtualMFADevicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        virtual_mfadevices: List[DescribeVirtualMFADevicesResponseBodyVirtualMFADevices] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.virtual_mfadevices = virtual_mfadevices

    def validate(self):
        if self.virtual_mfadevices:
            for k in self.virtual_mfadevices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VirtualMFADevices'] = []
        if self.virtual_mfadevices is not None:
            for k in self.virtual_mfadevices:
                result['VirtualMFADevices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.virtual_mfadevices = []
        if m.get('VirtualMFADevices') is not None:
            for k in m.get('VirtualMFADevices'):
                temp_model = DescribeVirtualMFADevicesResponseBodyVirtualMFADevices()
                self.virtual_mfadevices.append(temp_model.from_map(k))
        return self


class DescribeVirtualMFADevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVirtualMFADevicesResponseBody = None,
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
            temp_model = DescribeVirtualMFADevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulDetailsRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        lang: str = None,
        name: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.lang = lang
        self.name = name
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVulDetailsResponseBodyCves(TeaModel):
    def __init__(
        self,
        cve_id: str = None,
        cvss_score: str = None,
        summary: str = None,
        title: str = None,
    ):
        self.cve_id = cve_id
        self.cvss_score = cvss_score
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cve_id is not None:
            result['CveId'] = self.cve_id
        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')
        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeVulDetailsResponseBody(TeaModel):
    def __init__(
        self,
        cves: List[DescribeVulDetailsResponseBodyCves] = None,
        request_id: str = None,
    ):
        self.cves = cves
        self.request_id = request_id

    def validate(self):
        if self.cves:
            for k in self.cves:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cves'] = []
        if self.cves is not None:
            for k in self.cves:
                result['Cves'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cves = []
        if m.get('Cves') is not None:
            for k in m.get('Cves'):
                temp_model = DescribeVulDetailsResponseBodyCves()
                self.cves.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVulDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVulDetailsResponseBody = None,
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
            temp_model = DescribeVulDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulListRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        current_page: int = None,
        dealed: str = None,
        lang: str = None,
        name: str = None,
        necessity: str = None,
        office_site_id: str = None,
        page_size: int = None,
        region_id: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.current_page = current_page
        self.dealed = dealed
        self.lang = lang
        self.name = name
        self.necessity = necessity
        self.office_site_id = office_site_id
        self.page_size = page_size
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dealed is not None:
            result['Dealed'] = self.dealed
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.name is not None:
            result['Name'] = self.name
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList(TeaModel):
    def __init__(
        self,
        full_version: str = None,
        match_detail: str = None,
        name: str = None,
        path: str = None,
        update_cmd: str = None,
    ):
        self.full_version = full_version
        self.match_detail = match_detail
        self.name = name
        self.path = path
        self.update_cmd = update_cmd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_version is not None:
            result['FullVersion'] = self.full_version
        if self.match_detail is not None:
            result['MatchDetail'] = self.match_detail
        if self.name is not None:
            result['Name'] = self.name
        if self.path is not None:
            result['Path'] = self.path
        if self.update_cmd is not None:
            result['UpdateCmd'] = self.update_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FullVersion') is not None:
            self.full_version = m.get('FullVersion')
        if m.get('MatchDetail') is not None:
            self.match_detail = m.get('MatchDetail')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('UpdateCmd') is not None:
            self.update_cmd = m.get('UpdateCmd')
        return self


class DescribeVulListResponseBodyVulRecordsExtendContentJson(TeaModel):
    def __init__(
        self,
        rpm_entity_list: List[DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList] = None,
    ):
        self.rpm_entity_list = rpm_entity_list

    def validate(self):
        if self.rpm_entity_list:
            for k in self.rpm_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RpmEntityList'] = []
        if self.rpm_entity_list is not None:
            for k in self.rpm_entity_list:
                result['RpmEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rpm_entity_list = []
        if m.get('RpmEntityList') is not None:
            for k in m.get('RpmEntityList'):
                temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJsonRpmEntityList()
                self.rpm_entity_list.append(temp_model.from_map(k))
        return self


class DescribeVulListResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        extend_content_json: DescribeVulListResponseBodyVulRecordsExtendContentJson = None,
        first_ts: int = None,
        last_ts: int = None,
        modify_ts: int = None,
        name: str = None,
        necessity: str = None,
        online: bool = None,
        os_version: str = None,
        related: str = None,
        repair_ts: int = None,
        result_code: str = None,
        result_message: str = None,
        status: int = None,
        tag: str = None,
        type: str = None,
    ):
        self.alias_name = alias_name
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.extend_content_json = extend_content_json
        self.first_ts = first_ts
        self.last_ts = last_ts
        self.modify_ts = modify_ts
        self.name = name
        self.necessity = necessity
        self.online = online
        self.os_version = os_version
        self.related = related
        self.repair_ts = repair_ts
        self.result_code = result_code
        self.result_message = result_message
        self.status = status
        self.tag = tag
        self.type = type

    def validate(self):
        if self.extend_content_json:
            self.extend_content_json.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.extend_content_json is not None:
            result['ExtendContentJson'] = self.extend_content_json.to_map()
        if self.first_ts is not None:
            result['FirstTs'] = self.first_ts
        if self.last_ts is not None:
            result['LastTs'] = self.last_ts
        if self.modify_ts is not None:
            result['ModifyTs'] = self.modify_ts
        if self.name is not None:
            result['Name'] = self.name
        if self.necessity is not None:
            result['Necessity'] = self.necessity
        if self.online is not None:
            result['Online'] = self.online
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.related is not None:
            result['Related'] = self.related
        if self.repair_ts is not None:
            result['RepairTs'] = self.repair_ts
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.result_message is not None:
            result['ResultMessage'] = self.result_message
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('ExtendContentJson') is not None:
            temp_model = DescribeVulListResponseBodyVulRecordsExtendContentJson()
            self.extend_content_json = temp_model.from_map(m['ExtendContentJson'])
        if m.get('FirstTs') is not None:
            self.first_ts = m.get('FirstTs')
        if m.get('LastTs') is not None:
            self.last_ts = m.get('LastTs')
        if m.get('ModifyTs') is not None:
            self.modify_ts = m.get('ModifyTs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('Related') is not None:
            self.related = m.get('Related')
        if m.get('RepairTs') is not None:
            self.repair_ts = m.get('RepairTs')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeVulListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vul_records: List[DescribeVulListResponseBodyVulRecords] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vul_records = vul_records

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VulRecords'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['VulRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vul_records = []
        if m.get('VulRecords') is not None:
            for k in m.get('VulRecords'):
                temp_model = DescribeVulListResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        return self


class DescribeVulListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVulListResponseBody = None,
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
            temp_model = DescribeVulListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVulOverviewRequest(TeaModel):
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


class DescribeVulOverviewResponseBody(TeaModel):
    def __init__(
        self,
        asap_count: int = None,
        later_count: int = None,
        nntf_count: int = None,
        request_id: str = None,
    ):
        self.asap_count = asap_count
        self.later_count = later_count
        self.nntf_count = nntf_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asap_count is not None:
            result['AsapCount'] = self.asap_count
        if self.later_count is not None:
            result['LaterCount'] = self.later_count
        if self.nntf_count is not None:
            result['NntfCount'] = self.nntf_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsapCount') is not None:
            self.asap_count = m.get('AsapCount')
        if m.get('LaterCount') is not None:
            self.later_count = m.get('LaterCount')
        if m.get('NntfCount') is not None:
            self.nntf_count = m.get('NntfCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeVulOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVulOverviewResponseBody = None,
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
            temp_model = DescribeVulOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_type: str = None,
    ):
        self.region_id = region_id
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCenRequest(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachCenResponseBody(TeaModel):
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


class DetachCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachCenResponseBody = None,
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
            temp_model = DetachCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDesktopsInGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_ids: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.desktop_ids = desktop_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableDesktopsInGroupResponseBody(TeaModel):
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


class DisableDesktopsInGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDesktopsInGroupResponseBody = None,
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
            temp_model = DisableDesktopsInGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateNetworkPackageRequest(TeaModel):
    def __init__(
        self,
        network_package_id: str = None,
        region_id: str = None,
    ):
        self.network_package_id = network_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateNetworkPackageResponseBody(TeaModel):
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


class DissociateNetworkPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateNetworkPackageResponseBody = None,
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
            temp_model = DissociateNetworkPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportClientEventsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_time: str = None,
        end_user_id: str = None,
        event_type: str = None,
        max_results: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.end_time = end_time
        self.end_user_id = end_user_id
        self.event_type = event_type
        self.max_results = max_results
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ExportClientEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportClientEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportClientEventsResponseBody = None,
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
            temp_model = ExportClientEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDesktopGroupInfoRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        desktop_group_id: List[str] = None,
        desktop_group_name: str = None,
        end_user_id: List[str] = None,
        expired_time: str = None,
        lang_type: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        region_id: str = None,
    ):
        self.charge_type = charge_type
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.end_user_id = end_user_id
        self.expired_time = expired_time
        self.lang_type = lang_type
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.lang_type is not None:
            result['LangType'] = self.lang_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ExportDesktopGroupInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportDesktopGroupInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportDesktopGroupInfoResponseBody = None,
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
            temp_model = ExportDesktopGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportDesktopListInfoRequestTag(TeaModel):
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


class ExportDesktopListInfoRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        desktop_id: List[str] = None,
        desktop_name: str = None,
        desktop_status: str = None,
        end_user_id: List[str] = None,
        expired_time: str = None,
        group_id: str = None,
        lang_type: str = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: str = None,
        policy_group_id: str = None,
        region_id: str = None,
        tag: List[ExportDesktopListInfoRequestTag] = None,
        user_name: str = None,
    ):
        self.charge_type = charge_type
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.desktop_status = desktop_status
        self.end_user_id = end_user_id
        self.expired_time = expired_time
        self.group_id = group_id
        self.lang_type = lang_type
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.policy_group_id = policy_group_id
        self.region_id = region_id
        self.tag = tag
        self.user_name = user_name

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
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name
        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.lang_type is not None:
            result['LangType'] = self.lang_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')
        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ExportDesktopListInfoRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ExportDesktopListInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ExportDesktopListInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportDesktopListInfoResponseBody = None,
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
            temp_model = ExportDesktopListInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_user_id: str = None,
        owner_id: int = None,
        password: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
        uuid: str = None,
    ):
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id
        self.owner_id = owner_id
        self.password = password
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.task_id = task_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
        task_status: str = None,
        ticket: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id
        self.task_status = task_status
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConnectionTicketResponseBody = None,
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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDesktopGroupDetailRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetDesktopGroupDetailResponseBodyDesktopsTimerInfos(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        forced: bool = None,
        status: int = None,
        timer_type: int = None,
    ):
        self.cron_expression = cron_expression
        self.forced = forced
        self.status = status
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.forced is not None:
            result['Forced'] = self.forced
        if self.status is not None:
            result['Status'] = self.status
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('Forced') is not None:
            self.forced = m.get('Forced')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class GetDesktopGroupDetailResponseBodyDesktops(TeaModel):
    def __init__(
        self,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        bind_amount: int = None,
        comments: str = None,
        connect_duration: int = None,
        cpu: int = None,
        creation_time: str = None,
        creator: str = None,
        data_disk_category: str = None,
        data_disk_size: str = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        directory_id: str = None,
        directory_type: str = None,
        expired_time: str = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        idle_disconnect_duration: int = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        memory: int = None,
        min_desktops_count: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_type: str = None,
        own_bundle_id: str = None,
        own_bundle_name: str = None,
        own_type: int = None,
        pay_type: str = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        ratio_threshold: float = None,
        res_type: int = None,
        reset_type: int = None,
        status: int = None,
        stop_duration: int = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
        timer_infos: List[GetDesktopGroupDetailResponseBodyDesktopsTimerInfos] = None,
        version: int = None,
    ):
        self.allow_auto_setup = allow_auto_setup
        self.allow_buffer_count = allow_buffer_count
        self.bind_amount = bind_amount
        self.comments = comments
        self.connect_duration = connect_duration
        self.cpu = cpu
        self.creation_time = creation_time
        self.creator = creator
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.directory_id = directory_id
        self.directory_type = directory_type
        self.expired_time = expired_time
        self.gpu_count = gpu_count
        self.gpu_spec = gpu_spec
        self.idle_disconnect_duration = idle_disconnect_duration
        self.keep_duration = keep_duration
        self.load_policy = load_policy
        self.max_desktops_count = max_desktops_count
        self.memory = memory
        self.min_desktops_count = min_desktops_count
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_type = office_site_type
        self.own_bundle_id = own_bundle_id
        self.own_bundle_name = own_bundle_name
        self.own_type = own_type
        self.pay_type = pay_type
        self.policy_group_id = policy_group_id
        self.policy_group_name = policy_group_name
        self.ratio_threshold = ratio_threshold
        self.res_type = res_type
        self.reset_type = reset_type
        self.status = status
        self.stop_duration = stop_duration
        self.system_disk_category = system_disk_category
        self.system_disk_size = system_disk_size
        self.timer_infos = timer_infos
        self.version = version

    def validate(self):
        if self.timer_infos:
            for k in self.timer_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_type is not None:
            result['DirectoryType'] = self.directory_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec
        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.own_bundle_name is not None:
            result['OwnBundleName'] = self.own_bundle_name
        if self.own_type is not None:
            result['OwnType'] = self.own_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name
        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        result['TimerInfos'] = []
        if self.timer_infos is not None:
            for k in self.timer_infos:
                result['TimerInfos'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryType') is not None:
            self.directory_type = m.get('DirectoryType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')
        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('OwnBundleName') is not None:
            self.own_bundle_name = m.get('OwnBundleName')
        if m.get('OwnType') is not None:
            self.own_type = m.get('OwnType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')
        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        self.timer_infos = []
        if m.get('TimerInfos') is not None:
            for k in m.get('TimerInfos'):
                temp_model = GetDesktopGroupDetailResponseBodyDesktopsTimerInfos()
                self.timer_infos.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetDesktopGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        desktops: GetDesktopGroupDetailResponseBodyDesktops = None,
        request_id: str = None,
    ):
        self.desktops = desktops
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            self.desktops.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktops is not None:
            result['Desktops'] = self.desktops.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desktops') is not None:
            temp_model = GetDesktopGroupDetailResponseBodyDesktops()
            self.desktops = temp_model.from_map(m['Desktops'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDesktopGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDesktopGroupDetailResponseBody = None,
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
            temp_model = GetDesktopGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOfficeSiteSsoStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sso_status: bool = None,
    ):
        self.request_id = request_id
        self.sso_status = sso_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')
        return self


class GetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOfficeSiteSsoStatusResponseBody = None,
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
            temp_model = GetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpMetadataRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.directory_id = directory_id
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetSpMetadataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sp_metadata: str = None,
    ):
        self.request_id = request_id
        self.sp_metadata = sp_metadata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sp_metadata is not None:
            result['SpMetadata'] = self.sp_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SpMetadata') is not None:
            self.sp_metadata = m.get('SpMetadata')
        return self


class GetSpMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSpMetadataResponseBody = None,
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
            temp_model = GetSpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HandleSecurityEventsRequestSecurityEvent(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        security_event_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')
        return self


class HandleSecurityEventsRequest(TeaModel):
    def __init__(
        self,
        operation_code: str = None,
        operation_params: str = None,
        region_id: str = None,
        security_event: List[HandleSecurityEventsRequestSecurityEvent] = None,
    ):
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.region_id = region_id
        self.security_event = security_event

    def validate(self):
        if self.security_event:
            for k in self.security_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code
        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['SecurityEvent'] = []
        if self.security_event is not None:
            for k in self.security_event:
                result['SecurityEvent'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')
        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.security_event = []
        if m.get('SecurityEvent') is not None:
            for k in m.get('SecurityEvent'):
                temp_model = HandleSecurityEventsRequestSecurityEvent()
                self.security_event.append(temp_model.from_map(k))
        return self


class HandleSecurityEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: int = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class HandleSecurityEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HandleSecurityEventsResponseBody = None,
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
            temp_model = HandleSecurityEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDirectoryUsersRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        oupath: str = None,
        region_id: str = None,
    ):
        self.directory_id = directory_id
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.oupath = oupath
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oupath is not None:
            result['OUPath'] = self.oupath
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OUPath') is not None:
            self.oupath = m.get('OUPath')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDirectoryUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        end_user: str = None,
    ):
        self.display_name = display_name
        self.end_user = end_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListDirectoryUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[ListDirectoryUsersResponseBodyUsers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListDirectoryUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListDirectoryUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDirectoryUsersResponseBody = None,
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
            temp_model = ListDirectoryUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteOverviewRequest(TeaModel):
    def __init__(
        self,
        force_refresh: bool = None,
        max_results: int = None,
        next_token: str = None,
        office_site_id: List[str] = None,
        query_range: int = None,
        region_id: str = None,
    ):
        self.force_refresh = force_refresh
        self.max_results = max_results
        self.next_token = next_token
        self.office_site_id = office_site_id
        self.query_range = query_range
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_refresh is not None:
            result['ForceRefresh'] = self.force_refresh
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.query_range is not None:
            result['QueryRange'] = self.query_range
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceRefresh') is not None:
            self.force_refresh = m.get('ForceRefresh')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('QueryRange') is not None:
            self.query_range = m.get('QueryRange')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults(TeaModel):
    def __init__(
        self,
        has_expired_eds_count: int = None,
        has_expired_eds_count_for_group: int = None,
        office_site_id: str = None,
        office_site_name: str = None,
        office_site_status: str = None,
        region_id: str = None,
        running_eds_count: int = None,
        running_eds_count_for_group: int = None,
        total_eds_count: int = None,
        total_eds_count_for_group: int = None,
        vpc_type: str = None,
        will_expired_eds_count: int = None,
        will_expired_eds_count_for_group: int = None,
    ):
        self.has_expired_eds_count = has_expired_eds_count
        self.has_expired_eds_count_for_group = has_expired_eds_count_for_group
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.office_site_status = office_site_status
        self.region_id = region_id
        self.running_eds_count = running_eds_count
        self.running_eds_count_for_group = running_eds_count_for_group
        self.total_eds_count = total_eds_count
        self.total_eds_count_for_group = total_eds_count_for_group
        self.vpc_type = vpc_type
        self.will_expired_eds_count = will_expired_eds_count
        self.will_expired_eds_count_for_group = will_expired_eds_count_for_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_expired_eds_count is not None:
            result['HasExpiredEdsCount'] = self.has_expired_eds_count
        if self.has_expired_eds_count_for_group is not None:
            result['HasExpiredEdsCountForGroup'] = self.has_expired_eds_count_for_group
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.office_site_status is not None:
            result['OfficeSiteStatus'] = self.office_site_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_eds_count is not None:
            result['RunningEdsCount'] = self.running_eds_count
        if self.running_eds_count_for_group is not None:
            result['RunningEdsCountForGroup'] = self.running_eds_count_for_group
        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count
        if self.total_eds_count_for_group is not None:
            result['TotalEdsCountForGroup'] = self.total_eds_count_for_group
        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type
        if self.will_expired_eds_count is not None:
            result['WillExpiredEdsCount'] = self.will_expired_eds_count
        if self.will_expired_eds_count_for_group is not None:
            result['WillExpiredEdsCountForGroup'] = self.will_expired_eds_count_for_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasExpiredEdsCount') is not None:
            self.has_expired_eds_count = m.get('HasExpiredEdsCount')
        if m.get('HasExpiredEdsCountForGroup') is not None:
            self.has_expired_eds_count_for_group = m.get('HasExpiredEdsCountForGroup')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('OfficeSiteStatus') is not None:
            self.office_site_status = m.get('OfficeSiteStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningEdsCount') is not None:
            self.running_eds_count = m.get('RunningEdsCount')
        if m.get('RunningEdsCountForGroup') is not None:
            self.running_eds_count_for_group = m.get('RunningEdsCountForGroup')
        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')
        if m.get('TotalEdsCountForGroup') is not None:
            self.total_eds_count_for_group = m.get('TotalEdsCountForGroup')
        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')
        if m.get('WillExpiredEdsCount') is not None:
            self.will_expired_eds_count = m.get('WillExpiredEdsCount')
        if m.get('WillExpiredEdsCountForGroup') is not None:
            self.will_expired_eds_count_for_group = m.get('WillExpiredEdsCountForGroup')
        return self


class ListOfficeSiteOverviewResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        office_site_overview_results: List[ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.office_site_overview_results = office_site_overview_results
        self.request_id = request_id

    def validate(self):
        if self.office_site_overview_results:
            for k in self.office_site_overview_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['OfficeSiteOverviewResults'] = []
        if self.office_site_overview_results is not None:
            for k in self.office_site_overview_results:
                result['OfficeSiteOverviewResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.office_site_overview_results = []
        if m.get('OfficeSiteOverviewResults') is not None:
            for k in m.get('OfficeSiteOverviewResults'):
                temp_model = ListOfficeSiteOverviewResponseBodyOfficeSiteOverviewResults()
                self.office_site_overview_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOfficeSiteOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOfficeSiteOverviewResponseBody = None,
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
            temp_model = ListOfficeSiteOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeSiteUsersRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        max_results: int = None,
        next_token: str = None,
        oupath: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.oupath = oupath
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.oupath is not None:
            result['OUPath'] = self.oupath
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OUPath') is not None:
            self.oupath = m.get('OUPath')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOfficeSiteUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        end_user: str = None,
    ):
        self.display_name = display_name
        self.end_user = end_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.end_user is not None:
            result['EndUser'] = self.end_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EndUser') is not None:
            self.end_user = m.get('EndUser')
        return self


class ListOfficeSiteUsersResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        users: List[ListOfficeSiteUsersResponseBodyUsers] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListOfficeSiteUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListOfficeSiteUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOfficeSiteUsersResponseBody = None,
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
            temp_model = ListOfficeSiteUsersResponseBody()
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
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserAdOrganizationUnitsRequest(TeaModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListUserAdOrganizationUnitsResponseBodyOUNames(TeaModel):
    def __init__(
        self,
        ouname: str = None,
        office_site_id: str = None,
    ):
        self.ouname = ouname
        self.office_site_id = office_site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ouname is not None:
            result['OUName'] = self.ouname
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        return self


class ListUserAdOrganizationUnitsResponseBody(TeaModel):
    def __init__(
        self,
        ounames: List[ListUserAdOrganizationUnitsResponseBodyOUNames] = None,
        request_id: str = None,
    ):
        self.ounames = ounames
        self.request_id = request_id

    def validate(self):
        if self.ounames:
            for k in self.ounames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OUNames'] = []
        if self.ounames is not None:
            for k in self.ounames:
                result['OUNames'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ounames = []
        if m.get('OUNames') is not None:
            for k in m.get('OUNames'):
                temp_model = ListUserAdOrganizationUnitsResponseBodyOUNames()
                self.ounames.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserAdOrganizationUnitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserAdOrganizationUnitsResponseBody = None,
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
            temp_model = ListUserAdOrganizationUnitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class LockVirtualMFADeviceResponseBody(TeaModel):
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


class LockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockVirtualMFADeviceResponseBody = None,
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
            temp_model = LockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorDirectoryRequest(TeaModel):
    def __init__(
        self,
        ad_hostname: str = None,
        directory_id: str = None,
        directory_name: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        mfa_enabled: bool = None,
        ouname: str = None,
        region_id: str = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
    ):
        self.ad_hostname = ad_hostname
        self.directory_id = directory_id
        self.directory_name = directory_name
        self.dns_address = dns_address
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.mfa_enabled = mfa_enabled
        self.ouname = ouname
        self.region_id = region_id
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.ouname is not None:
            result['OUName'] = self.ouname
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        return self


class ModifyADConnectorDirectoryResponseBody(TeaModel):
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


class ModifyADConnectorDirectoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyADConnectorDirectoryResponseBody = None,
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
            temp_model = ModifyADConnectorDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyADConnectorOfficeSiteRequest(TeaModel):
    def __init__(
        self,
        ad_hostname: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        mfa_enabled: bool = None,
        ouname: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
    ):
        self.ad_hostname = ad_hostname
        self.dns_address = dns_address
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_user_name = domain_user_name
        self.mfa_enabled = mfa_enabled
        self.ouname = ouname
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.region_id = region_id
        self.sub_domain_dns_address = sub_domain_dns_address
        self.sub_domain_name = sub_domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname
        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.ouname is not None:
            result['OUName'] = self.ouname
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address
        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')
        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')
        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')
        return self


class ModifyADConnectorOfficeSiteResponseBody(TeaModel):
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


class ModifyADConnectorOfficeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyADConnectorOfficeSiteResponseBody = None,
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
            temp_model = ModifyADConnectorOfficeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBundleRequest(TeaModel):
    def __init__(
        self,
        bundle_id: str = None,
        bundle_name: str = None,
        description: str = None,
        image_id: str = None,
        language: str = None,
        region_id: str = None,
    ):
        self.bundle_id = bundle_id
        self.bundle_name = bundle_name
        self.description = description
        self.image_id = image_id
        self.language = language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.language is not None:
            result['Language'] = self.language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyBundleResponseBody(TeaModel):
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


class ModifyBundleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBundleResponseBody = None,
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
            temp_model = ModifyBundleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCloudDrivePermissionRequest(TeaModel):
    def __init__(
        self,
        cds_id: str = None,
        download_end_user_ids: List[str] = None,
        download_upload_end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        self.cds_id = cds_id
        self.download_end_user_ids = download_end_user_ids
        self.download_upload_end_user_ids = download_upload_end_user_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id
        if self.download_end_user_ids is not None:
            result['DownloadEndUserIds'] = self.download_end_user_ids
        if self.download_upload_end_user_ids is not None:
            result['DownloadUploadEndUserIds'] = self.download_upload_end_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')
        if m.get('DownloadEndUserIds') is not None:
            self.download_end_user_ids = m.get('DownloadEndUserIds')
        if m.get('DownloadUploadEndUserIds') is not None:
            self.download_upload_end_user_ids = m.get('DownloadUploadEndUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyCloudDrivePermissionResponseBody(TeaModel):
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


class ModifyCloudDrivePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyCloudDrivePermissionResponseBody = None,
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
            temp_model = ModifyCloudDrivePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopChargeTypeRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        desktop_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.charge_type = charge_type
        self.desktop_id = desktop_id
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDesktopChargeTypeResponseBody(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopChargeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopChargeTypeResponseBody = None,
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
            temp_model = ModifyDesktopChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        allow_auto_setup: int = None,
        allow_buffer_count: int = None,
        bind_amount: int = None,
        classify: str = None,
        comments: str = None,
        connect_duration: int = None,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
        disable_session_config: bool = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        load_policy: int = None,
        max_desktops_count: int = None,
        min_desktops_count: int = None,
        own_bundle_id: str = None,
        policy_group_id: str = None,
        ratio_threshold: float = None,
        region_id: str = None,
        reset_type: int = None,
        scale_strategy_id: str = None,
        stop_duration: int = None,
    ):
        self.allow_auto_setup = allow_auto_setup
        self.allow_buffer_count = allow_buffer_count
        self.bind_amount = bind_amount
        self.classify = classify
        self.comments = comments
        self.connect_duration = connect_duration
        self.desktop_group_id = desktop_group_id
        self.desktop_group_name = desktop_group_name
        self.disable_session_config = disable_session_config
        self.idle_disconnect_duration = idle_disconnect_duration
        self.image_id = image_id
        self.keep_duration = keep_duration
        self.load_policy = load_policy
        self.max_desktops_count = max_desktops_count
        self.min_desktops_count = min_desktops_count
        self.own_bundle_id = own_bundle_id
        self.policy_group_id = policy_group_id
        self.ratio_threshold = ratio_threshold
        self.region_id = region_id
        self.reset_type = reset_type
        self.scale_strategy_id = scale_strategy_id
        self.stop_duration = stop_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_auto_setup is not None:
            result['AllowAutoSetup'] = self.allow_auto_setup
        if self.allow_buffer_count is not None:
            result['AllowBufferCount'] = self.allow_buffer_count
        if self.bind_amount is not None:
            result['BindAmount'] = self.bind_amount
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.connect_duration is not None:
            result['ConnectDuration'] = self.connect_duration
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name
        if self.disable_session_config is not None:
            result['DisableSessionConfig'] = self.disable_session_config
        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration
        if self.load_policy is not None:
            result['LoadPolicy'] = self.load_policy
        if self.max_desktops_count is not None:
            result['MaxDesktopsCount'] = self.max_desktops_count
        if self.min_desktops_count is not None:
            result['MinDesktopsCount'] = self.min_desktops_count
        if self.own_bundle_id is not None:
            result['OwnBundleId'] = self.own_bundle_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.ratio_threshold is not None:
            result['RatioThreshold'] = self.ratio_threshold
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.scale_strategy_id is not None:
            result['ScaleStrategyId'] = self.scale_strategy_id
        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowAutoSetup') is not None:
            self.allow_auto_setup = m.get('AllowAutoSetup')
        if m.get('AllowBufferCount') is not None:
            self.allow_buffer_count = m.get('AllowBufferCount')
        if m.get('BindAmount') is not None:
            self.bind_amount = m.get('BindAmount')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('ConnectDuration') is not None:
            self.connect_duration = m.get('ConnectDuration')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')
        if m.get('DisableSessionConfig') is not None:
            self.disable_session_config = m.get('DisableSessionConfig')
        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')
        if m.get('LoadPolicy') is not None:
            self.load_policy = m.get('LoadPolicy')
        if m.get('MaxDesktopsCount') is not None:
            self.max_desktops_count = m.get('MaxDesktopsCount')
        if m.get('MinDesktopsCount') is not None:
            self.min_desktops_count = m.get('MinDesktopsCount')
        if m.get('OwnBundleId') is not None:
            self.own_bundle_id = m.get('OwnBundleId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RatioThreshold') is not None:
            self.ratio_threshold = m.get('RatioThreshold')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('ScaleStrategyId') is not None:
            self.scale_strategy_id = m.get('ScaleStrategyId')
        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')
        return self


class ModifyDesktopGroupResponseBody(TeaModel):
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


class ModifyDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopGroupResponseBody = None,
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
            temp_model = ModifyDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopHostNameRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        new_host_name: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.new_host_name = new_host_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.new_host_name is not None:
            result['NewHostName'] = self.new_host_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('NewHostName') is not None:
            self.new_host_name = m.get('NewHostName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDesktopHostNameResponseBody(TeaModel):
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


class ModifyDesktopHostNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopHostNameResponseBody = None,
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
            temp_model = ModifyDesktopHostNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopNameRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        new_desktop_name: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.new_desktop_name = new_desktop_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.new_desktop_name is not None:
            result['NewDesktopName'] = self.new_desktop_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('NewDesktopName') is not None:
            self.new_desktop_name = m.get('NewDesktopName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDesktopNameResponseBody(TeaModel):
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


class ModifyDesktopNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopNameResponseBody = None,
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
            temp_model = ModifyDesktopNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopSpecRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        desktop_id: str = None,
        desktop_type: str = None,
        promotion_id: str = None,
        region_id: str = None,
        root_disk_size_gib: int = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: int = None,
    ):
        self.auto_pay = auto_pay
        self.desktop_id = desktop_id
        self.desktop_type = desktop_type
        self.promotion_id = promotion_id
        self.region_id = region_id
        self.root_disk_size_gib = root_disk_size_gib
        self.user_disk_performance_level = user_disk_performance_level
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib
        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level
        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')
        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')
        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')
        return self


class ModifyDesktopSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopSpecResponseBody = None,
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
            temp_model = ModifyDesktopSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDesktopsPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        policy_group_id: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.policy_group_id = policy_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDesktopsPolicyGroupResponseBodyModifyResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        desktop_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.desktop_id = desktop_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyDesktopsPolicyGroupResponseBody(TeaModel):
    def __init__(
        self,
        modify_results: List[ModifyDesktopsPolicyGroupResponseBodyModifyResults] = None,
        request_id: str = None,
    ):
        self.modify_results = modify_results
        self.request_id = request_id

    def validate(self):
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k in self.modify_results:
                result['ModifyResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modify_results = []
        if m.get('ModifyResults') is not None:
            for k in m.get('ModifyResults'):
                temp_model = ModifyDesktopsPolicyGroupResponseBodyModifyResults()
                self.modify_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDesktopsPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDesktopsPolicyGroupResponseBody = None,
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
            temp_model = ModifyDesktopsPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskSpecRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        desktop_id: str = None,
        promotion_id: str = None,
        region_id: str = None,
        root_disk_performance_level: str = None,
        user_disk_performance_level: str = None,
    ):
        self.auto_pay = auto_pay
        self.desktop_id = desktop_id
        self.promotion_id = promotion_id
        self.region_id = region_id
        self.root_disk_performance_level = root_disk_performance_level
        self.user_disk_performance_level = user_disk_performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level
        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')
        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')
        return self


class ModifyDiskSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDiskSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDiskSpecResponseBody = None,
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
            temp_model = ModifyDiskSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyEntitlementRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        end_user_id: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.end_user_id = end_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyEntitlementResponseBody(TeaModel):
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


class ModifyEntitlementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyEntitlementResponseBody = None,
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
            temp_model = ModifyEntitlementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.description = description
        self.image_id = image_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyImageAttributeResponseBody(TeaModel):
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


class ModifyImageAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyImageAttributeResponseBody = None,
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
            temp_model = ModifyImageAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImagePermissionRequest(TeaModel):
    def __init__(
        self,
        add_account: List[int] = None,
        image_id: str = None,
        region_id: str = None,
        remove_account: List[int] = None,
    ):
        self.add_account = add_account
        self.image_id = image_id
        self.region_id = region_id
        self.remove_account = remove_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_account is not None:
            result['AddAccount'] = self.add_account
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remove_account is not None:
            result['RemoveAccount'] = self.remove_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RemoveAccount') is not None:
            self.remove_account = m.get('RemoveAccount')
        return self


class ModifyImagePermissionResponseBody(TeaModel):
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


class ModifyImagePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyImagePermissionResponseBody = None,
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
            temp_model = ModifyImagePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNASDefaultMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_target_domain: str = None,
        region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_target_domain = mount_target_domain
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyNASDefaultMountTargetResponseBody(TeaModel):
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


class ModifyNASDefaultMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNASDefaultMountTargetResponseBody = None,
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
            temp_model = ModifyNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageBandwidthRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        bandwidth: int = None,
        network_package_id: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.bandwidth = bandwidth
        self.network_package_id = network_package_id
        self.promotion_id = promotion_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyNetworkPackageBandwidthResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNetworkPackageBandwidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNetworkPackageBandwidthResponseBody = None,
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
            temp_model = ModifyNetworkPackageBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNetworkPackageEnabledRequest(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        network_package_id: str = None,
        region_id: str = None,
    ):
        self.enabled = enabled
        self.network_package_id = network_package_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyNetworkPackageEnabledResponseBody(TeaModel):
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


class ModifyNetworkPackageEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNetworkPackageEnabledResponseBody = None,
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
            temp_model = ModifyNetworkPackageEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteAttributeRequest(TeaModel):
    def __init__(
        self,
        desktop_access_type: str = None,
        need_verify_login_risk: bool = None,
        need_verify_zero_device: bool = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
    ):
        self.desktop_access_type = desktop_access_type
        self.need_verify_login_risk = need_verify_login_risk
        self.need_verify_zero_device = need_verify_zero_device
        self.office_site_id = office_site_id
        self.office_site_name = office_site_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type
        if self.need_verify_login_risk is not None:
            result['NeedVerifyLoginRisk'] = self.need_verify_login_risk
        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')
        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')
        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyOfficeSiteAttributeResponseBody(TeaModel):
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


class ModifyOfficeSiteAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOfficeSiteAttributeResponseBody = None,
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
            temp_model = ModifyOfficeSiteAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteCrossDesktopAccessRequest(TeaModel):
    def __init__(
        self,
        enable_cross_desktop_access: bool = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.enable_cross_desktop_access = enable_cross_desktop_access
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_cross_desktop_access is not None:
            result['EnableCrossDesktopAccess'] = self.enable_cross_desktop_access
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCrossDesktopAccess') is not None:
            self.enable_cross_desktop_access = m.get('EnableCrossDesktopAccess')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyOfficeSiteCrossDesktopAccessResponseBody(TeaModel):
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


class ModifyOfficeSiteCrossDesktopAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOfficeSiteCrossDesktopAccessResponseBody = None,
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
            temp_model = ModifyOfficeSiteCrossDesktopAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOfficeSiteMfaEnabledRequest(TeaModel):
    def __init__(
        self,
        mfa_enabled: bool = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.mfa_enabled = mfa_enabled
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyOfficeSiteMfaEnabledResponseBody(TeaModel):
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


class ModifyOfficeSiteMfaEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOfficeSiteMfaEnabledResponseBody = None,
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
            temp_model = ModifyOfficeSiteMfaEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOperateVulRequestVulInfo(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        name: str = None,
        tag: str = None,
    ):
        self.desktop_id = desktop_id
        self.name = name
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ModifyOperateVulRequest(TeaModel):
    def __init__(
        self,
        operate_type: str = None,
        reason: str = None,
        region_id: str = None,
        type: str = None,
        vul_info: List[ModifyOperateVulRequestVulInfo] = None,
    ):
        self.operate_type = operate_type
        self.reason = reason
        self.region_id = region_id
        self.type = type
        self.vul_info = vul_info

    def validate(self):
        if self.vul_info:
            for k in self.vul_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        result['VulInfo'] = []
        if self.vul_info is not None:
            for k in self.vul_info:
                result['VulInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.vul_info = []
        if m.get('VulInfo') is not None:
            for k in m.get('VulInfo'):
                temp_model = ModifyOperateVulRequestVulInfo()
                self.vul_info.append(temp_model.from_map(k))
        return self


class ModifyOperateVulResponseBody(TeaModel):
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


class ModifyOperateVulResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyOperateVulResponseBody = None,
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
            temp_model = ModifyOperateVulResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyGroupRequestAuthorizeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        type: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyPolicyGroupRequestClientType(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        self.client_type = client_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyPolicyGroupRequestRevokeAccessPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ModifyPolicyGroupRequestRevokeSecurityPolicyRule(TeaModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        type: str = None,
    ):
        self.cidr_ip = cidr_ip
        self.description = description
        self.ip_protocol = ip_protocol
        self.policy = policy
        self.port_range = port_range
        self.priority = priority
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip
        if self.description is not None:
            result['Description'] = self.description
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port_range is not None:
            result['PortRange'] = self.port_range
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ModifyPolicyGroupRequestUsbSupplyRedirectRule(TeaModel):
    def __init__(
        self,
        description: str = None,
        device_class: str = None,
        device_subclass: str = None,
        product_id: str = None,
        usb_redirect_type: int = None,
        usb_rule_type: int = None,
        vendor_id: str = None,
    ):
        self.description = description
        self.device_class = device_class
        self.device_subclass = device_subclass
        self.product_id = product_id
        self.usb_redirect_type = usb_redirect_type
        self.usb_rule_type = usb_rule_type
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_class is not None:
            result['DeviceClass'] = self.device_class
        if self.device_subclass is not None:
            result['DeviceSubclass'] = self.device_subclass
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.usb_redirect_type is not None:
            result['UsbRedirectType'] = self.usb_redirect_type
        if self.usb_rule_type is not None:
            result['UsbRuleType'] = self.usb_rule_type
        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')
        if m.get('DeviceSubclass') is not None:
            self.device_subclass = m.get('DeviceSubclass')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('UsbRedirectType') is not None:
            self.usb_redirect_type = m.get('UsbRedirectType')
        if m.get('UsbRuleType') is not None:
            self.usb_rule_type = m.get('UsbRuleType')
        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')
        return self


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(
        self,
        app_content_protection: str = None,
        authorize_access_policy_rule: List[ModifyPolicyGroupRequestAuthorizeAccessPolicyRule] = None,
        authorize_security_policy_rule: List[ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule] = None,
        camera_redirect: str = None,
        client_type: List[ModifyPolicyGroupRequestClientType] = None,
        clipboard: str = None,
        domain_list: str = None,
        gpu_acceleration: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        name: str = None,
        net_redirect: str = None,
        policy_group_id: str = None,
        preempt_login: str = None,
        preempt_login_user: List[str] = None,
        printer_redirection: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        recording: str = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: int = None,
        recording_start_time: str = None,
        region_id: str = None,
        revoke_access_policy_rule: List[ModifyPolicyGroupRequestRevokeAccessPolicyRule] = None,
        revoke_security_policy_rule: List[ModifyPolicyGroupRequestRevokeSecurityPolicyRule] = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[ModifyPolicyGroupRequestUsbSupplyRedirectRule] = None,
        visual_quality: str = None,
        watermark: str = None,
        watermark_transparency: str = None,
        watermark_type: str = None,
    ):
        self.app_content_protection = app_content_protection
        self.authorize_access_policy_rule = authorize_access_policy_rule
        self.authorize_security_policy_rule = authorize_security_policy_rule
        self.camera_redirect = camera_redirect
        self.client_type = client_type
        self.clipboard = clipboard
        self.domain_list = domain_list
        self.gpu_acceleration = gpu_acceleration
        self.html_5access = html_5access
        self.html_5file_transfer = html_5file_transfer
        self.local_drive = local_drive
        self.name = name
        self.net_redirect = net_redirect
        self.policy_group_id = policy_group_id
        self.preempt_login = preempt_login
        self.preempt_login_user = preempt_login_user
        self.printer_redirection = printer_redirection
        self.record_content = record_content
        self.record_content_expires = record_content_expires
        self.recording = recording
        self.recording_end_time = recording_end_time
        self.recording_expires = recording_expires
        self.recording_fps = recording_fps
        self.recording_start_time = recording_start_time
        self.region_id = region_id
        self.revoke_access_policy_rule = revoke_access_policy_rule
        self.revoke_security_policy_rule = revoke_security_policy_rule
        self.usb_redirect = usb_redirect
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.visual_quality = visual_quality
        self.watermark = watermark
        self.watermark_transparency = watermark_transparency
        self.watermark_type = watermark_type

    def validate(self):
        if self.authorize_access_policy_rule:
            for k in self.authorize_access_policy_rule:
                if k:
                    k.validate()
        if self.authorize_security_policy_rule:
            for k in self.authorize_security_policy_rule:
                if k:
                    k.validate()
        if self.client_type:
            for k in self.client_type:
                if k:
                    k.validate()
        if self.revoke_access_policy_rule:
            for k in self.revoke_access_policy_rule:
                if k:
                    k.validate()
        if self.revoke_security_policy_rule:
            for k in self.revoke_security_policy_rule:
                if k:
                    k.validate()
        if self.usb_supply_redirect_rule:
            for k in self.usb_supply_redirect_rule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection
        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k.to_map() if k else None)
        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k.to_map() if k else None)
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect
        result['ClientType'] = []
        if self.client_type is not None:
            for k in self.client_type:
                result['ClientType'].append(k.to_map() if k else None)
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration
        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access
        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.name is not None:
            result['Name'] = self.name
        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect
        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id
        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login
        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user
        if self.printer_redirection is not None:
            result['PrinterRedirection'] = self.printer_redirection
        if self.record_content is not None:
            result['RecordContent'] = self.record_content
        if self.record_content_expires is not None:
            result['RecordContentExpires'] = self.record_content_expires
        if self.recording is not None:
            result['Recording'] = self.recording
        if self.recording_end_time is not None:
            result['RecordingEndTime'] = self.recording_end_time
        if self.recording_expires is not None:
            result['RecordingExpires'] = self.recording_expires
        if self.recording_fps is not None:
            result['RecordingFps'] = self.recording_fps
        if self.recording_start_time is not None:
            result['RecordingStartTime'] = self.recording_start_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RevokeAccessPolicyRule'] = []
        if self.revoke_access_policy_rule is not None:
            for k in self.revoke_access_policy_rule:
                result['RevokeAccessPolicyRule'].append(k.to_map() if k else None)
        result['RevokeSecurityPolicyRule'] = []
        if self.revoke_security_policy_rule is not None:
            for k in self.revoke_security_policy_rule:
                result['RevokeSecurityPolicyRule'].append(k.to_map() if k else None)
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        result['UsbSupplyRedirectRule'] = []
        if self.usb_supply_redirect_rule is not None:
            for k in self.usb_supply_redirect_rule:
                result['UsbSupplyRedirectRule'].append(k.to_map() if k else None)
        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')
        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k in m.get('AuthorizeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k))
        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k))
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')
        self.client_type = []
        if m.get('ClientType') is not None:
            for k in m.get('ClientType'):
                temp_model = ModifyPolicyGroupRequestClientType()
                self.client_type.append(temp_model.from_map(k))
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')
        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')
        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')
        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')
        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')
        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')
        if m.get('PrinterRedirection') is not None:
            self.printer_redirection = m.get('PrinterRedirection')
        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')
        if m.get('RecordContentExpires') is not None:
            self.record_content_expires = m.get('RecordContentExpires')
        if m.get('Recording') is not None:
            self.recording = m.get('Recording')
        if m.get('RecordingEndTime') is not None:
            self.recording_end_time = m.get('RecordingEndTime')
        if m.get('RecordingExpires') is not None:
            self.recording_expires = m.get('RecordingExpires')
        if m.get('RecordingFps') is not None:
            self.recording_fps = m.get('RecordingFps')
        if m.get('RecordingStartTime') is not None:
            self.recording_start_time = m.get('RecordingStartTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.revoke_access_policy_rule = []
        if m.get('RevokeAccessPolicyRule') is not None:
            for k in m.get('RevokeAccessPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeAccessPolicyRule()
                self.revoke_access_policy_rule.append(temp_model.from_map(k))
        self.revoke_security_policy_rule = []
        if m.get('RevokeSecurityPolicyRule') is not None:
            for k in m.get('RevokeSecurityPolicyRule'):
                temp_model = ModifyPolicyGroupRequestRevokeSecurityPolicyRule()
                self.revoke_security_policy_rule.append(temp_model.from_map(k))
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k in m.get('UsbSupplyRedirectRule'):
                temp_model = ModifyPolicyGroupRequestUsbSupplyRedirectRule()
                self.usb_supply_redirect_rule.append(temp_model.from_map(k))
        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        return self


class ModifyPolicyGroupResponseBody(TeaModel):
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


class ModifyPolicyGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyGroupResponseBody = None,
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
            temp_model = ModifyPolicyGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserEntitlementRequest(TeaModel):
    def __init__(
        self,
        authorize_desktop_id: List[str] = None,
        end_user_id: List[str] = None,
        region_id: str = None,
        revoke_desktop_id: List[str] = None,
    ):
        self.authorize_desktop_id = authorize_desktop_id
        self.end_user_id = end_user_id
        self.region_id = region_id
        self.revoke_desktop_id = revoke_desktop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorize_desktop_id is not None:
            result['AuthorizeDesktopId'] = self.authorize_desktop_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.revoke_desktop_id is not None:
            result['RevokeDesktopId'] = self.revoke_desktop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeDesktopId') is not None:
            self.authorize_desktop_id = m.get('AuthorizeDesktopId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RevokeDesktopId') is not None:
            self.revoke_desktop_id = m.get('RevokeDesktopId')
        return self


class ModifyUserEntitlementResponseBody(TeaModel):
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


class ModifyUserEntitlementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserEntitlementResponseBody = None,
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
            temp_model = ModifyUserEntitlementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserToDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        new_end_user_ids: List[str] = None,
        old_end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.new_end_user_ids = new_end_user_ids
        self.old_end_user_ids = old_end_user_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.new_end_user_ids is not None:
            result['NewEndUserIds'] = self.new_end_user_ids
        if self.old_end_user_ids is not None:
            result['OldEndUserIds'] = self.old_end_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('NewEndUserIds') is not None:
            self.new_end_user_ids = m.get('NewEndUserIds')
        if m.get('OldEndUserIds') is not None:
            self.old_end_user_ids = m.get('OldEndUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyUserToDesktopGroupResponseBody(TeaModel):
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


class ModifyUserToDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUserToDesktopGroupResponseBody = None,
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
            temp_model = ModifyUserToDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateVulsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        operate_type: str = None,
        precondition: int = None,
        reason: str = None,
        region_id: str = None,
        type: str = None,
        vul_name: List[str] = None,
    ):
        self.desktop_id = desktop_id
        self.operate_type = operate_type
        self.precondition = precondition
        self.reason = reason
        self.region_id = region_id
        self.type = type
        self.vul_name = vul_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.precondition is not None:
            result['Precondition'] = self.precondition
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.vul_name is not None:
            result['VulName'] = self.vul_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Precondition') is not None:
            self.precondition = m.get('Precondition')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VulName') is not None:
            self.vul_name = m.get('VulName')
        return self


class OperateVulsResponseBody(TeaModel):
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


class OperateVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateVulsResponseBody = None,
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
            temp_model = OperateVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RebootDesktopsResponseBody(TeaModel):
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


class RebootDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootDesktopsResponseBody = None,
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
            temp_model = RebootDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebuildDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        image_id: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.image_id = image_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RebuildDesktopsResponseBodyRebuildResults(TeaModel):
    def __init__(
        self,
        code: str = None,
        desktop_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.desktop_id = desktop_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RebuildDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        rebuild_results: List[RebuildDesktopsResponseBodyRebuildResults] = None,
        request_id: str = None,
    ):
        self.rebuild_results = rebuild_results
        self.request_id = request_id

    def validate(self):
        if self.rebuild_results:
            for k in self.rebuild_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RebuildResults'] = []
        if self.rebuild_results is not None:
            for k in self.rebuild_results:
                result['RebuildResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rebuild_results = []
        if m.get('RebuildResults') is not None:
            for k in m.get('RebuildResults'):
                temp_model = RebuildDesktopsResponseBodyRebuildResults()
                self.rebuild_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebuildDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebuildDesktopsResponseBody = None,
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
            temp_model = RebuildDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromDesktopGroupRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_ids: List[str] = None,
        end_user_ids: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.desktop_group_ids = desktop_group_ids
        self.end_user_ids = end_user_ids
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_group_ids is not None:
            result['DesktopGroupIds'] = self.desktop_group_ids
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopGroupIds') is not None:
            self.desktop_group_ids = m.get('DesktopGroupIds')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveUserFromDesktopGroupResponseBody(TeaModel):
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


class RemoveUserFromDesktopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserFromDesktopGroupResponseBody = None,
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
            temp_model = RemoveUserFromDesktopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewDesktopsRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        desktop_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.desktop_id = desktop_id
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenewDesktopsResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewDesktopsResponseBody = None,
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
            temp_model = RenewDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewNetworkPackagesRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        network_package_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        self.auto_pay = auto_pay
        self.network_package_id = network_package_id
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenewNetworkPackagesResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewNetworkPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewNetworkPackagesResponseBody = None,
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
            temp_model = RenewNetworkPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_id: List[str] = None,
        image_id: str = None,
        pay_type: str = None,
        region_id: str = None,
        reset_type: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.desktop_id = desktop_id
        self.image_id = image_id
        self.pay_type = pay_type
        self.region_id = region_id
        self.reset_type = reset_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        return self


class ResetDesktopsResponseBody(TeaModel):
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


class ResetDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetDesktopsResponseBody = None,
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
            temp_model = ResetDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetNASDefaultMountTargetRequest(TeaModel):
    def __init__(
        self,
        file_system_id: str = None,
        region_id: str = None,
    ):
        self.file_system_id = file_system_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetNASDefaultMountTargetResponseBody(TeaModel):
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


class ResetNASDefaultMountTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetNASDefaultMountTargetResponseBody = None,
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
            temp_model = ResetNASDefaultMountTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSnapshotRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        self.region_id = region_id
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetSnapshotResponseBody(TeaModel):
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


class ResetSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetSnapshotResponseBody = None,
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
            temp_model = ResetSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSuspEventQuaraFileRequest(TeaModel):
    def __init__(
        self,
        desktop_id: str = None,
        quara_field_id: int = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.quara_field_id = quara_field_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.quara_field_id is not None:
            result['QuaraFieldId'] = self.quara_field_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('QuaraFieldId') is not None:
            self.quara_field_id = m.get('QuaraFieldId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RollbackSuspEventQuaraFileResponseBody(TeaModel):
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


class RollbackSuspEventQuaraFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackSuspEventQuaraFileResponseBody = None,
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
            temp_model = RollbackSuspEventQuaraFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        content_encoding: str = None,
        desktop_id: List[str] = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
    ):
        self.command_content = command_content
        self.content_encoding = content_encoding
        self.desktop_id = desktop_id
        self.region_id = region_id
        self.timeout = timeout
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
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
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        extra_info: str = None,
        region_id: str = None,
        verify_code_action: str = None,
    ):
        self.extra_info = extra_info
        self.region_id = region_id
        self.verify_code_action = verify_code_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.verify_code_action is not None:
            result['VerifyCodeAction'] = self.verify_code_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VerifyCodeAction') is not None:
            self.verify_code_action = m.get('VerifyCodeAction')
        return self


class SendVerifyCodeResponseBody(TeaModel):
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


class SendVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerifyCodeResponseBody = None,
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
            temp_model = SendVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDesktopGroupTimerRequest(TeaModel):
    def __init__(
        self,
        cron_expression: str = None,
        desktop_group_id: str = None,
        force: bool = None,
        region_id: str = None,
        reset_type: int = None,
        timer_type: int = None,
    ):
        self.cron_expression = cron_expression
        self.desktop_group_id = desktop_group_id
        self.force = force
        self.region_id = region_id
        self.reset_type = reset_type
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.force is not None:
            result['Force'] = self.force
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reset_type is not None:
            result['ResetType'] = self.reset_type
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResetType') is not None:
            self.reset_type = m.get('ResetType')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class SetDesktopGroupTimerResponseBody(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        order_ids: List[str] = None,
        request_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.order_ids = order_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDesktopGroupTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDesktopGroupTimerResponseBody = None,
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
            temp_model = SetDesktopGroupTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDesktopGroupTimerStatusRequest(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
        status: int = None,
        timer_type: int = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.region_id = region_id
        self.status = status
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.timer_type is not None:
            result['TimerType'] = self.timer_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')
        return self


class SetDesktopGroupTimerStatusResponseBody(TeaModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        order_ids: List[str] = None,
        request_id: str = None,
    ):
        self.desktop_group_id = desktop_group_id
        self.order_ids = order_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetDesktopGroupTimerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDesktopGroupTimerStatusResponseBody = None,
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
            temp_model = SetDesktopGroupTimerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetIdpMetadataRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        idp_metadata: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.directory_id = directory_id
        self.idp_metadata = idp_metadata
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id
        if self.idp_metadata is not None:
            result['IdpMetadata'] = self.idp_metadata
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')
        if m.get('IdpMetadata') is not None:
            self.idp_metadata = m.get('IdpMetadata')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetIdpMetadataResponseBody(TeaModel):
    def __init__(
        self,
        idp_entity_id: str = None,
        request_id: str = None,
    ):
        self.idp_entity_id = idp_entity_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.idp_entity_id is not None:
            result['IdpEntityId'] = self.idp_entity_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpEntityId') is not None:
            self.idp_entity_id = m.get('IdpEntityId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetIdpMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetIdpMetadataResponseBody = None,
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
            temp_model = SetIdpMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetOfficeSiteSsoStatusRequest(TeaModel):
    def __init__(
        self,
        enable_sso: bool = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        self.enable_sso = enable_sso
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sso is not None:
            result['EnableSso'] = self.enable_sso
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSso') is not None:
            self.enable_sso = m.get('EnableSso')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetOfficeSiteSsoStatusResponseBody(TeaModel):
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


class SetOfficeSiteSsoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetOfficeSiteSsoStatusResponseBody = None,
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
            temp_model = SetOfficeSiteSsoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDesktopsResponseBody(TeaModel):
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


class StartDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDesktopsResponseBody = None,
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
            temp_model = StartDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartVirusScanTaskRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        office_site_id: List[str] = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.office_site_id = office_site_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartVirusScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scan_task_id: int = None,
    ):
        self.request_id = request_id
        self.scan_task_id = scan_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        return self


class StartVirusScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartVirusScanTaskResponseBody = None,
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
            temp_model = StartVirusScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDesktopsRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        region_id: str = None,
        stopped_mode: str = None,
    ):
        self.desktop_id = desktop_id
        self.region_id = region_id
        self.stopped_mode = stopped_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        return self


class StopDesktopsResponseBody(TeaModel):
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


class StopDesktopsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDesktopsResponseBody = None,
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
            temp_model = StopDesktopsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        invoke_id: str = None,
        region_id: str = None,
    ):
        self.desktop_id = desktop_id
        self.invoke_id = invoke_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInvocationResponseBody(TeaModel):
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


class StopInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInvocationResponseBody = None,
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
            temp_model = StopInvocationResponseBody()
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
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockVirtualMFADeviceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        serial_number: str = None,
    ):
        self.region_id = region_id
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnlockVirtualMFADeviceResponseBody(TeaModel):
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


class UnlockVirtualMFADeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnlockVirtualMFADeviceResponseBody = None,
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
            temp_model = UnlockVirtualMFADeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFotaTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_uid: str = None,
        user_status: str = None,
    ):
        self.region_id = region_id
        self.task_uid = task_uid
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_uid is not None:
            result['TaskUid'] = self.task_uid
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskUid') is not None:
            self.task_uid = m.get('TaskUid')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class UpdateFotaTaskResponseBody(TeaModel):
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


class UpdateFotaTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFotaTaskResponseBody = None,
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
            temp_model = UpdateFotaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadImageRequest(TeaModel):
    def __init__(
        self,
        data_disk_size: int = None,
        description: str = None,
        enable_security_check: bool = None,
        gpu_category: bool = None,
        gpu_driver_type: str = None,
        image_name: str = None,
        license_type: str = None,
        os_type: str = None,
        oss_object_path: str = None,
        protocol_type: str = None,
        region_id: str = None,
    ):
        self.data_disk_size = data_disk_size
        self.description = description
        self.enable_security_check = enable_security_check
        self.gpu_category = gpu_category
        self.gpu_driver_type = gpu_driver_type
        self.image_name = image_name
        self.license_type = license_type
        self.os_type = os_type
        self.oss_object_path = oss_object_path
        self.protocol_type = protocol_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_security_check is not None:
            result['EnableSecurityCheck'] = self.enable_security_check
        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category
        if self.gpu_driver_type is not None:
            result['GpuDriverType'] = self.gpu_driver_type
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.license_type is not None:
            result['LicenseType'] = self.license_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.oss_object_path is not None:
            result['OssObjectPath'] = self.oss_object_path
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableSecurityCheck') is not None:
            self.enable_security_check = m.get('EnableSecurityCheck')
        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')
        if m.get('GpuDriverType') is not None:
            self.gpu_driver_type = m.get('GpuDriverType')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OssObjectPath') is not None:
            self.oss_object_path = m.get('OssObjectPath')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UploadImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        self.image_id = image_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadImageResponseBody = None,
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
            temp_model = UploadImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCenRequest(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        region_id: str = None,
        verify_code: str = None,
    ):
        self.cen_id = cen_id
        self.cen_owner_id = cen_owner_id
        self.cidr_block = cidr_block
        self.region_id = region_id
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cen_id is not None:
            result['CenId'] = self.cen_id
        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')
        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyCenResponseBodyRouteEntries(TeaModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        next_hop_instance_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        self.destination_cidr_block = destination_cidr_block
        self.next_hop_instance_id = next_hop_instance_id
        self.region_id = region_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block
        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')
        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class VerifyCenResponseBody(TeaModel):
    def __init__(
        self,
        cidr_blocks: List[str] = None,
        request_id: str = None,
        route_entries: List[VerifyCenResponseBodyRouteEntries] = None,
        status: str = None,
    ):
        self.cidr_blocks = cidr_blocks
        self.request_id = request_id
        self.route_entries = route_entries
        self.status = status

    def validate(self):
        if self.route_entries:
            for k in self.route_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_blocks is not None:
            result['CidrBlocks'] = self.cidr_blocks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RouteEntries'] = []
        if self.route_entries is not None:
            for k in self.route_entries:
                result['RouteEntries'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlocks') is not None:
            self.cidr_blocks = m.get('CidrBlocks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.route_entries = []
        if m.get('RouteEntries') is not None:
            for k in m.get('RouteEntries'):
                temp_model = VerifyCenResponseBodyRouteEntries()
                self.route_entries.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class VerifyCenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyCenResponseBody = None,
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
            temp_model = VerifyCenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


