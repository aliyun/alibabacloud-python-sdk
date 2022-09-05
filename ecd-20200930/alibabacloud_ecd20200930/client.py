# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecd20200930 import models as ecd_20200930_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_office_site_with_options(
        self,
        request: ecd_20200930_models.ActivateOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ActivateOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ActivateOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_office_site_with_options_async(
        self,
        request: ecd_20200930_models.ActivateOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ActivateOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ActivateOfficeSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_office_site(
        self,
        request: ecd_20200930_models.ActivateOfficeSiteRequest,
    ) -> ecd_20200930_models.ActivateOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_office_site_with_options(request, runtime)

    async def activate_office_site_async(
        self,
        request: ecd_20200930_models.ActivateOfficeSiteRequest,
    ) -> ecd_20200930_models.ActivateOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_office_site_with_options_async(request, runtime)

    def add_user_to_desktop_group_with_options(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AddUserToDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_desktop_group(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_user_to_desktop_group_with_options(request, runtime)

    async def add_user_to_desktop_group_async(
        self,
        request: ecd_20200930_models.AddUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.AddUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_user_to_desktop_group_with_options_async(request, runtime)

    def apply_coordination_for_monitoring_with_options(
        self,
        request: ecd_20200930_models.ApplyCoordinationForMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ApplyCoordinationForMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coordinate_policy_type):
            query['CoordinatePolicyType'] = request.coordinate_policy_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.initiator_type):
            query['InitiatorType'] = request.initiator_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_candidates):
            query['ResourceCandidates'] = request.resource_candidates
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApplyCoordinationForMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_coordination_for_monitoring_with_options_async(
        self,
        request: ecd_20200930_models.ApplyCoordinationForMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ApplyCoordinationForMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coordinate_policy_type):
            query['CoordinatePolicyType'] = request.coordinate_policy_type
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.initiator_type):
            query['InitiatorType'] = request.initiator_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_candidates):
            query['ResourceCandidates'] = request.resource_candidates
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApplyCoordinationForMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_coordination_for_monitoring(
        self,
        request: ecd_20200930_models.ApplyCoordinationForMonitoringRequest,
    ) -> ecd_20200930_models.ApplyCoordinationForMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_coordination_for_monitoring_with_options(request, runtime)

    async def apply_coordination_for_monitoring_async(
        self,
        request: ecd_20200930_models.ApplyCoordinationForMonitoringRequest,
    ) -> ecd_20200930_models.ApplyCoordinationForMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_coordination_for_monitoring_with_options_async(request, runtime)

    def approve_fota_update_with_options(
        self,
        request: ecd_20200930_models.ApproveFotaUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ApproveFotaUpdateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveFotaUpdate',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApproveFotaUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_fota_update_with_options_async(
        self,
        request: ecd_20200930_models.ApproveFotaUpdateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ApproveFotaUpdateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveFotaUpdate',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ApproveFotaUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_fota_update(
        self,
        request: ecd_20200930_models.ApproveFotaUpdateRequest,
    ) -> ecd_20200930_models.ApproveFotaUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_fota_update_with_options(request, runtime)

    async def approve_fota_update_async(
        self,
        request: ecd_20200930_models.ApproveFotaUpdateRequest,
    ) -> ecd_20200930_models.ApproveFotaUpdateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_fota_update_with_options_async(request, runtime)

    def associate_network_package_with_options(
        self,
        request: ecd_20200930_models.AssociateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AssociateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AssociateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_network_package_with_options_async(
        self,
        request: ecd_20200930_models.AssociateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AssociateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AssociateNetworkPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_network_package(
        self,
        request: ecd_20200930_models.AssociateNetworkPackageRequest,
    ) -> ecd_20200930_models.AssociateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_network_package_with_options(request, runtime)

    async def associate_network_package_async(
        self,
        request: ecd_20200930_models.AssociateNetworkPackageRequest,
    ) -> ecd_20200930_models.AssociateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_network_package_with_options_async(request, runtime)

    def attach_cen_with_options(
        self,
        request: ecd_20200930_models.AttachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AttachCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_cen_with_options_async(
        self,
        request: ecd_20200930_models.AttachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.AttachCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.AttachCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_cen(
        self,
        request: ecd_20200930_models.AttachCenRequest,
    ) -> ecd_20200930_models.AttachCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_cen_with_options(request, runtime)

    async def attach_cen_async(
        self,
        request: ecd_20200930_models.AttachCenRequest,
    ) -> ecd_20200930_models.AttachCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_cen_with_options_async(request, runtime)

    def cancel_coordination_for_monitoring_with_options(
        self,
        request: ecd_20200930_models.CancelCoordinationForMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CancelCoordinationForMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_ids):
            query['CoIds'] = request.co_ids
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCoordinationForMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_coordination_for_monitoring_with_options_async(
        self,
        request: ecd_20200930_models.CancelCoordinationForMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CancelCoordinationForMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.co_ids):
            query['CoIds'] = request.co_ids
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCoordinationForMonitoring',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCoordinationForMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_coordination_for_monitoring(
        self,
        request: ecd_20200930_models.CancelCoordinationForMonitoringRequest,
    ) -> ecd_20200930_models.CancelCoordinationForMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_coordination_for_monitoring_with_options(request, runtime)

    async def cancel_coordination_for_monitoring_async(
        self,
        request: ecd_20200930_models.CancelCoordinationForMonitoringRequest,
    ) -> ecd_20200930_models.CancelCoordinationForMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_coordination_for_monitoring_with_options_async(request, runtime)

    def cancel_copy_image_with_options(
        self,
        request: ecd_20200930_models.CancelCopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CancelCopyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_copy_image_with_options_async(
        self,
        request: ecd_20200930_models.CancelCopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CancelCopyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CancelCopyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_copy_image(
        self,
        request: ecd_20200930_models.CancelCopyImageRequest,
    ) -> ecd_20200930_models.CancelCopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_copy_image_with_options(request, runtime)

    async def cancel_copy_image_async(
        self,
        request: ecd_20200930_models.CancelCopyImageRequest,
    ) -> ecd_20200930_models.CancelCopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_copy_image_with_options_async(request, runtime)

    def clone_policy_group_with_options(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClonePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClonePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ClonePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_policy_group(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_policy_group_with_options(request, runtime)

    async def clone_policy_group_async(
        self,
        request: ecd_20200930_models.ClonePolicyGroupRequest,
    ) -> ecd_20200930_models.ClonePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_policy_group_with_options_async(request, runtime)

    def config_adconnector_trust_with_options(
        self,
        request: ecd_20200930_models.ConfigADConnectorTrustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ConfigADConnectorTrustResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trust_key):
            query['TrustKey'] = request.trust_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorTrust',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorTrustResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_adconnector_trust_with_options_async(
        self,
        request: ecd_20200930_models.ConfigADConnectorTrustRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ConfigADConnectorTrustResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trust_key):
            query['TrustKey'] = request.trust_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorTrust',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorTrustResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_adconnector_trust(
        self,
        request: ecd_20200930_models.ConfigADConnectorTrustRequest,
    ) -> ecd_20200930_models.ConfigADConnectorTrustResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_adconnector_trust_with_options(request, runtime)

    async def config_adconnector_trust_async(
        self,
        request: ecd_20200930_models.ConfigADConnectorTrustRequest,
    ) -> ecd_20200930_models.ConfigADConnectorTrustResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_adconnector_trust_with_options_async(request, runtime)

    def config_adconnector_user_with_options(
        self,
        request: ecd_20200930_models.ConfigADConnectorUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ConfigADConnectorUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorUser',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_adconnector_user_with_options_async(
        self,
        request: ecd_20200930_models.ConfigADConnectorUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ConfigADConnectorUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigADConnectorUser',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ConfigADConnectorUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_adconnector_user(
        self,
        request: ecd_20200930_models.ConfigADConnectorUserRequest,
    ) -> ecd_20200930_models.ConfigADConnectorUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_adconnector_user_with_options(request, runtime)

    async def config_adconnector_user_async(
        self,
        request: ecd_20200930_models.ConfigADConnectorUserRequest,
    ) -> ecd_20200930_models.ConfigADConnectorUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_adconnector_user_with_options_async(request, runtime)

    def copy_image_with_options(
        self,
        request: ecd_20200930_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CopyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_description):
            query['DestinationDescription'] = request.destination_description
        if not UtilClient.is_unset(request.destination_image_name):
            query['DestinationImageName'] = request.destination_image_name
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CopyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_image_with_options_async(
        self,
        request: ecd_20200930_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CopyImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_description):
            query['DestinationDescription'] = request.destination_description
        if not UtilClient.is_unset(request.destination_image_name):
            query['DestinationImageName'] = request.destination_image_name
        if not UtilClient.is_unset(request.destination_region_id):
            query['DestinationRegionId'] = request.destination_region_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CopyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_image(
        self,
        request: ecd_20200930_models.CopyImageRequest,
    ) -> ecd_20200930_models.CopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    async def copy_image_async(
        self,
        request: ecd_20200930_models.CopyImageRequest,
    ) -> ecd_20200930_models.CopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_image_with_options_async(request, runtime)

    def create_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_adconnector_directory(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    async def create_adconnector_directory_async(
        self,
        request: ecd_20200930_models.CreateADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.CreateADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adconnector_directory_with_options_async(request, runtime)

    def create_adconnector_office_site_with_options(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_adconnector_office_site_with_options_async(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateADConnectorOfficeSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_adconnector_office_site(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_office_site_with_options(request, runtime)

    async def create_adconnector_office_site_async(
        self,
        request: ecd_20200930_models.CreateADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_adconnector_office_site_with_options_async(request, runtime)

    def create_bundle_with_options(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_bundle_with_options_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_bundle(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    async def create_bundle_async(
        self,
        request: ecd_20200930_models.CreateBundleRequest,
    ) -> ecd_20200930_models.CreateBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bundle_with_options_async(request, runtime)

    def create_desktop_group_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_classify_users):
            query['AllClassifyUsers'] = request.all_classify_users
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.default_init_desktop_count):
            query['DefaultInitDesktopCount'] = request.default_init_desktop_count
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_classify_users):
            query['AllClassifyUsers'] = request.all_classify_users
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.default_init_desktop_count):
            query['DefaultInitDesktopCount'] = request.default_init_desktop_count
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_desktop_group(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktop_group_with_options(request, runtime)

    async def create_desktop_group_async(
        self,
        request: ecd_20200930_models.CreateDesktopGroupRequest,
    ) -> ecd_20200930_models.CreateDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktop_group_with_options_async(request, runtime)

    def create_desktops_with_options(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_name_suffix):
            query['DesktopNameSuffix'] = request.desktop_name_suffix
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_assign_mode):
            query['UserAssignMode'] = request.user_assign_mode
        if not UtilClient.is_unset(request.user_commands):
            query['UserCommands'] = request.user_commands
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_desktops_with_options_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_name_suffix):
            query['DesktopNameSuffix'] = request.desktop_name_suffix
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_assign_mode):
            query['UserAssignMode'] = request.user_assign_mode
        if not UtilClient.is_unset(request.user_commands):
            query['UserCommands'] = request.user_commands
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        if not UtilClient.is_unset(request.volume_encryption_key):
            query['VolumeEncryptionKey'] = request.volume_encryption_key
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_desktops(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    async def create_desktops_async(
        self,
        request: ecd_20200930_models.CreateDesktopsRequest,
    ) -> ecd_20200930_models.CreateDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_desktops_with_options_async(request, runtime)

    def create_disk_encryption_service_with_options(
        self,
        request: ecd_20200930_models.CreateDiskEncryptionServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDiskEncryptionServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskEncryptionService',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDiskEncryptionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_disk_encryption_service_with_options_async(
        self,
        request: ecd_20200930_models.CreateDiskEncryptionServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDiskEncryptionServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDiskEncryptionService',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDiskEncryptionServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_disk_encryption_service(
        self,
        request: ecd_20200930_models.CreateDiskEncryptionServiceRequest,
    ) -> ecd_20200930_models.CreateDiskEncryptionServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disk_encryption_service_with_options(request, runtime)

    async def create_disk_encryption_service_async(
        self,
        request: ecd_20200930_models.CreateDiskEncryptionServiceRequest,
    ) -> ecd_20200930_models.CreateDiskEncryptionServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_encryption_service_with_options_async(request, runtime)

    def create_drive_with_options(
        self,
        request: ecd_20200930_models.CreateDriveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDriveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.drive_name):
            query['DriveName'] = request.drive_name
        if not UtilClient.is_unset(request.external_domain_id):
            query['ExternalDomainId'] = request.external_domain_id
        if not UtilClient.is_unset(request.profile_roaming):
            query['ProfileRoaming'] = request.profile_roaming
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.total_size):
            query['TotalSize'] = request.total_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_size):
            query['UsedSize'] = request.used_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDriveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_drive_with_options_async(
        self,
        request: ecd_20200930_models.CreateDriveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateDriveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_uid):
            query['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain_id):
            query['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.drive_name):
            query['DriveName'] = request.drive_name
        if not UtilClient.is_unset(request.external_domain_id):
            query['ExternalDomainId'] = request.external_domain_id
        if not UtilClient.is_unset(request.profile_roaming):
            query['ProfileRoaming'] = request.profile_roaming
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.total_size):
            query['TotalSize'] = request.total_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_size):
            query['UsedSize'] = request.used_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDrive',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateDriveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_drive(
        self,
        request: ecd_20200930_models.CreateDriveRequest,
    ) -> ecd_20200930_models.CreateDriveResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drive_with_options(request, runtime)

    async def create_drive_async(
        self,
        request: ecd_20200930_models.CreateDriveRequest,
    ) -> ecd_20200930_models.CreateDriveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drive_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_clean_userdata):
            query['AutoCleanUserdata'] = request.auto_clean_userdata
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_resource_type):
            query['ImageResourceType'] = request.image_resource_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_clean_userdata):
            query['AutoCleanUserdata'] = request.auto_clean_userdata
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.image_resource_type):
            query['ImageResourceType'] = request.image_resource_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: ecd_20200930_models.CreateImageRequest,
    ) -> ecd_20200930_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_nasfile_system_with_options(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNASFileSystem',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nasfile_system_with_options_async(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNASFileSystem',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNASFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nasfile_system(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nasfile_system_with_options(request, runtime)

    async def create_nasfile_system_async(
        self,
        request: ecd_20200930_models.CreateNASFileSystemRequest,
    ) -> ecd_20200930_models.CreateNASFileSystemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nasfile_system_with_options_async(request, runtime)

    def create_network_package_with_options(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_package_with_options_async(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateNetworkPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_package(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_package_with_options(request, runtime)

    async def create_network_package_async(
        self,
        request: ecd_20200930_models.CreateNetworkPackageRequest,
    ) -> ecd_20200930_models.CreateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_package_with_options_async(request, runtime)

    def create_policy_group_with_options(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreatePolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_group(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    async def create_policy_group_async(
        self,
        request: ecd_20200930_models.CreatePolicyGroupRequest,
    ) -> ecd_20200930_models.CreatePolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_group_with_options_async(request, runtime)

    def create_ramdirectory_with_options(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRAMDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ramdirectory_with_options_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRAMDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateRAMDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ramdirectory(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    async def create_ramdirectory_async(
        self,
        request: ecd_20200930_models.CreateRAMDirectoryRequest,
    ) -> ecd_20200930_models.CreateRAMDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ramdirectory_with_options_async(request, runtime)

    def create_simple_office_site_with_options(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.cloud_box_office_site):
            query['CloudBoxOfficeSite'] = request.cloud_box_office_site
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimpleOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_simple_office_site_with_options_async(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.cloud_box_office_site):
            query['CloudBoxOfficeSite'] = request.cloud_box_office_site
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.enable_admin_access):
            query['EnableAdminAccess'] = request.enable_admin_access
        if not UtilClient.is_unset(request.enable_internet_access):
            query['EnableInternetAccess'] = request.enable_internet_access
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimpleOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSimpleOfficeSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_simple_office_site(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_simple_office_site_with_options(request, runtime)

    async def create_simple_office_site_async(
        self,
        request: ecd_20200930_models.CreateSimpleOfficeSiteRequest,
    ) -> ecd_20200930_models.CreateSimpleOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_simple_office_site_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.source_disk_type):
            query['SourceDiskType'] = request.source_disk_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: ecd_20200930_models.CreateSnapshotRequest,
    ) -> ecd_20200930_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_bundles_with_options(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteBundlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_bundles(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    async def delete_bundles_async(
        self,
        request: ecd_20200930_models.DeleteBundlesRequest,
    ) -> ecd_20200930_models.DeleteBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bundles_with_options_async(request, runtime)

    def delete_cloud_drive_users_with_options(
        self,
        request: ecd_20200930_models.DeleteCloudDriveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteCloudDriveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudDriveUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteCloudDriveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cloud_drive_users_with_options_async(
        self,
        request: ecd_20200930_models.DeleteCloudDriveUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteCloudDriveUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCloudDriveUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteCloudDriveUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cloud_drive_users(
        self,
        request: ecd_20200930_models.DeleteCloudDriveUsersRequest,
    ) -> ecd_20200930_models.DeleteCloudDriveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cloud_drive_users_with_options(request, runtime)

    async def delete_cloud_drive_users_async(
        self,
        request: ecd_20200930_models.DeleteCloudDriveUsersRequest,
    ) -> ecd_20200930_models.DeleteCloudDriveUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cloud_drive_users_with_options_async(request, runtime)

    def delete_desktop_group_with_options(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_desktop_group(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_desktop_group_with_options(request, runtime)

    async def delete_desktop_group_async(
        self,
        request: ecd_20200930_models.DeleteDesktopGroupRequest,
    ) -> ecd_20200930_models.DeleteDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktop_group_with_options_async(request, runtime)

    def delete_desktops_with_options(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_desktops(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    async def delete_desktops_async(
        self,
        request: ecd_20200930_models.DeleteDesktopsRequest,
    ) -> ecd_20200930_models.DeleteDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_desktops_with_options_async(request, runtime)

    def delete_directories_with_options(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_directories_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_directories(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    async def delete_directories_async(
        self,
        request: ecd_20200930_models.DeleteDirectoriesRequest,
    ) -> ecd_20200930_models.DeleteDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_directories_with_options_async(request, runtime)

    def delete_drive_with_options(
        self,
        request: ecd_20200930_models.DeleteDriveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDriveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drive_id):
            query['DriveId'] = request.drive_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDriveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_drive_with_options_async(
        self,
        request: ecd_20200930_models.DeleteDriveRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteDriveResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drive_id):
            query['DriveId'] = request.drive_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDrive',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteDriveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_drive(
        self,
        request: ecd_20200930_models.DeleteDriveRequest,
    ) -> ecd_20200930_models.DeleteDriveResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_drive_with_options(request, runtime)

    async def delete_drive_async(
        self,
        request: ecd_20200930_models.DeleteDriveRequest,
    ) -> ecd_20200930_models.DeleteDriveResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_drive_with_options_async(request, runtime)

    def delete_images_with_options(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_with_options_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    async def delete_images_async(
        self,
        request: ecd_20200930_models.DeleteImagesRequest,
    ) -> ecd_20200930_models.DeleteImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_with_options_async(request, runtime)

    def delete_nasfile_systems_with_options(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nasfile_systems_with_options_async(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNASFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nasfile_systems(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nasfile_systems_with_options(request, runtime)

    async def delete_nasfile_systems_async(
        self,
        request: ecd_20200930_models.DeleteNASFileSystemsRequest,
    ) -> ecd_20200930_models.DeleteNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nasfile_systems_with_options_async(request, runtime)

    def delete_network_packages_with_options(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_packages_with_options_async(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteNetworkPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_packages(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_packages_with_options(request, runtime)

    async def delete_network_packages_async(
        self,
        request: ecd_20200930_models.DeleteNetworkPackagesRequest,
    ) -> ecd_20200930_models.DeleteNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_packages_with_options_async(request, runtime)

    def delete_office_sites_with_options(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_office_sites_with_options_async(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteOfficeSitesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_office_sites(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_office_sites_with_options(request, runtime)

    async def delete_office_sites_async(
        self,
        request: ecd_20200930_models.DeleteOfficeSitesRequest,
    ) -> ecd_20200930_models.DeleteOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_office_sites_with_options_async(request, runtime)

    def delete_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeletePolicyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_groups(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    async def delete_policy_groups_async(
        self,
        request: ecd_20200930_models.DeletePolicyGroupsRequest,
    ) -> ecd_20200930_models.DeletePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_groups_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: ecd_20200930_models.DeleteSnapshotRequest,
    ) -> ecd_20200930_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DeleteVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_mfadevice(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_mfadevice_with_options(request, runtime)

    async def delete_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.DeleteVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.DeleteVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_mfadevice_with_options_async(request, runtime)

    def describe_alarm_event_stack_info_with_options(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventStackInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarm_event_stack_info_with_options_async(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarmEventStackInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeAlarmEventStackInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarm_event_stack_info(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alarm_event_stack_info_with_options(request, runtime)

    async def describe_alarm_event_stack_info_async(
        self,
        request: ecd_20200930_models.DescribeAlarmEventStackInfoRequest,
    ) -> ecd_20200930_models.DescribeAlarmEventStackInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarm_event_stack_info_with_options_async(request, runtime)

    def describe_bundles_with_options(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_type):
            query['BundleType'] = request.bundle_type
        if not UtilClient.is_unset(request.check_stock):
            query['CheckStock'] = request.check_stock
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_type_family):
            query['DesktopTypeFamily'] = request.desktop_type_family
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
        if not UtilClient.is_unset(request.from_desktop_group):
            query['FromDesktopGroup'] = request.from_desktop_group
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.support_multi_session):
            query['SupportMultiSession'] = request.support_multi_session
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bundles_with_options_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_type):
            query['BundleType'] = request.bundle_type
        if not UtilClient.is_unset(request.check_stock):
            query['CheckStock'] = request.check_stock
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_type_family):
            query['DesktopTypeFamily'] = request.desktop_type_family
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
        if not UtilClient.is_unset(request.from_desktop_group):
            query['FromDesktopGroup'] = request.from_desktop_group
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.support_multi_session):
            query['SupportMultiSession'] = request.support_multi_session
        if not UtilClient.is_unset(request.volume_encryption_enabled):
            query['VolumeEncryptionEnabled'] = request.volume_encryption_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBundles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeBundlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bundles(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    async def describe_bundles_async(
        self,
        request: ecd_20200930_models.DescribeBundlesRequest,
    ) -> ecd_20200930_models.DescribeBundlesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bundles_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCensResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
    ) -> ecd_20200930_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: ecd_20200930_models.DescribeCensRequest,
    ) -> ecd_20200930_models.DescribeCensResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_client_events_with_options(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_ip):
            query['DesktopIp'] = request.desktop_ip
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_events_with_options_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_ip):
            query['DesktopIp'] = request.desktop_ip
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeClientEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_events(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_events_with_options(request, runtime)

    async def describe_client_events_async(
        self,
        request: ecd_20200930_models.DescribeClientEventsRequest,
    ) -> ecd_20200930_models.DescribeClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_events_with_options_async(request, runtime)

    def describe_cloud_drive_permissions_with_options(
        self,
        request: ecd_20200930_models.DescribeCloudDrivePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCloudDrivePermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDrivePermissions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCloudDrivePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_drive_permissions_with_options_async(
        self,
        request: ecd_20200930_models.DescribeCloudDrivePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeCloudDrivePermissionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudDrivePermissions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeCloudDrivePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_drive_permissions(
        self,
        request: ecd_20200930_models.DescribeCloudDrivePermissionsRequest,
    ) -> ecd_20200930_models.DescribeCloudDrivePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_drive_permissions_with_options(request, runtime)

    async def describe_cloud_drive_permissions_async(
        self,
        request: ecd_20200930_models.DescribeCloudDrivePermissionsRequest,
    ) -> ecd_20200930_models.DescribeCloudDrivePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_drive_permissions_with_options_async(request, runtime)

    def describe_desktop_groups_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.excluded_end_user_ids):
            query['ExcludedEndUserIds'] = request.excluded_end_user_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktop_groups_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.excluded_end_user_ids):
            query['ExcludedEndUserIds'] = request.excluded_end_user_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.own_type):
            query['OwnType'] = request.own_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktop_groups(
        self,
        request: ecd_20200930_models.DescribeDesktopGroupsRequest,
    ) -> ecd_20200930_models.DescribeDesktopGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_groups_with_options(request, runtime)

    async def describe_desktop_groups_async(
        self,
        request: ecd_20200930_models.DescribeDesktopGroupsRequest,
    ) -> ecd_20200930_models.DescribeDesktopGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_groups_with_options_async(request, runtime)

    def describe_desktop_ids_by_vul_names_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopIdsByVulNames',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktop_ids_by_vul_names_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopIdsByVulNames',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktop_ids_by_vul_names(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_ids_by_vul_names_with_options(request, runtime)

    async def describe_desktop_ids_by_vul_names_async(
        self,
        request: ecd_20200930_models.DescribeDesktopIdsByVulNamesRequest,
    ) -> ecd_20200930_models.DescribeDesktopIdsByVulNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_ids_by_vul_names_with_options_async(request, runtime)

    def describe_desktop_types_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applied_scope):
            query['AppliedScope'] = request.applied_scope
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_id_for_modify):
            query['DesktopIdForModify'] = request.desktop_id_for_modify
        if not UtilClient.is_unset(request.desktop_type_id):
            query['DesktopTypeId'] = request.desktop_type_id
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopTypes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktop_types_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.applied_scope):
            query['AppliedScope'] = request.applied_scope
        if not UtilClient.is_unset(request.cpu_count):
            query['CpuCount'] = request.cpu_count
        if not UtilClient.is_unset(request.desktop_id_for_modify):
            query['DesktopIdForModify'] = request.desktop_id_for_modify
        if not UtilClient.is_unset(request.desktop_type_id):
            query['DesktopTypeId'] = request.desktop_type_id
        if not UtilClient.is_unset(request.gpu_count):
            query['GpuCount'] = request.gpu_count
        if not UtilClient.is_unset(request.instance_type_family):
            query['InstanceTypeFamily'] = request.instance_type_family
        if not UtilClient.is_unset(request.memory_size):
            query['MemorySize'] = request.memory_size
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopTypes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktop_types(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    async def describe_desktop_types_async(
        self,
        request: ecd_20200930_models.DescribeDesktopTypesRequest,
    ) -> ecd_20200930_models.DescribeDesktopTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktop_types_with_options_async(request, runtime)

    def describe_desktops_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.excluded_end_user_id):
            query['ExcludedEndUserId'] = request.excluded_end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.filter_desktop_group):
            query['FilterDesktopGroup'] = request.filter_desktop_group
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.management_flag):
            query['ManagementFlag'] = request.management_flag
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.excluded_end_user_id):
            query['ExcludedEndUserId'] = request.excluded_end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.filter_desktop_group):
            query['FilterDesktopGroup'] = request.filter_desktop_group
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.management_flag):
            query['ManagementFlag'] = request.management_flag
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.query_fota_update):
            query['QueryFotaUpdate'] = request.query_fota_update
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktops(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    async def describe_desktops_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsRequest,
    ) -> ecd_20200930_models.DescribeDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_with_options_async(request, runtime)

    def describe_desktops_in_group_with_options(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.ignore_deleted):
            query['IgnoreDeleted'] = request.ignore_deleted
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_desktops_in_group_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.ignore_deleted):
            query['IgnoreDeleted'] = request.ignore_deleted
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDesktopsInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_desktops_in_group(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_in_group_with_options(request, runtime)

    async def describe_desktops_in_group_async(
        self,
        request: ecd_20200930_models.DescribeDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DescribeDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_desktops_in_group_with_options_async(request, runtime)

    def describe_directories_with_options(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_status):
            query['DirectoryStatus'] = request.directory_status
        if not UtilClient.is_unset(request.directory_type):
            query['DirectoryType'] = request.directory_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_directories_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_status):
            query['DirectoryStatus'] = request.directory_status
        if not UtilClient.is_unset(request.directory_type):
            query['DirectoryType'] = request.directory_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_directories(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    async def describe_directories_async(
        self,
        request: ecd_20200930_models.DescribeDirectoriesRequest,
    ) -> ecd_20200930_models.DescribeDirectoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_directories_with_options_async(request, runtime)

    def describe_drives_with_options(
        self,
        request: ecd_20200930_models.DescribeDrivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDrivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_ids):
            query['DomainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrives',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDrivesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_drives_with_options_async(
        self,
        request: ecd_20200930_models.DescribeDrivesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeDrivesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_ids):
            query['DomainIds'] = request.domain_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDrives',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeDrivesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_drives(
        self,
        request: ecd_20200930_models.DescribeDrivesRequest,
    ) -> ecd_20200930_models.DescribeDrivesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drives_with_options(request, runtime)

    async def describe_drives_async(
        self,
        request: ecd_20200930_models.DescribeDrivesRequest,
    ) -> ecd_20200930_models.DescribeDrivesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drives_with_options_async(request, runtime)

    def describe_flow_metric_with_options(
        self,
        request: ecd_20200930_models.DescribeFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFlowMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowMetric',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_metric_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFlowMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowMetric',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_metric(
        self,
        request: ecd_20200930_models.DescribeFlowMetricRequest,
    ) -> ecd_20200930_models.DescribeFlowMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_metric_with_options(request, runtime)

    async def describe_flow_metric_async(
        self,
        request: ecd_20200930_models.DescribeFlowMetricRequest,
    ) -> ecd_20200930_models.DescribeFlowMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_metric_with_options_async(request, runtime)

    def describe_flow_statistic_with_options(
        self,
        request: ecd_20200930_models.DescribeFlowStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFlowStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowStatistic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_statistic_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFlowStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFlowStatisticResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowStatistic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFlowStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_statistic(
        self,
        request: ecd_20200930_models.DescribeFlowStatisticRequest,
    ) -> ecd_20200930_models.DescribeFlowStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_statistic_with_options(request, runtime)

    async def describe_flow_statistic_async(
        self,
        request: ecd_20200930_models.DescribeFlowStatisticRequest,
    ) -> ecd_20200930_models.DescribeFlowStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_statistic_with_options_async(request, runtime)

    def describe_fota_pending_desktops_with_options(
        self,
        request: ecd_20200930_models.DescribeFotaPendingDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFotaPendingDesktopsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaPendingDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaPendingDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fota_pending_desktops_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFotaPendingDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFotaPendingDesktopsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaPendingDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaPendingDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fota_pending_desktops(
        self,
        request: ecd_20200930_models.DescribeFotaPendingDesktopsRequest,
    ) -> ecd_20200930_models.DescribeFotaPendingDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fota_pending_desktops_with_options(request, runtime)

    async def describe_fota_pending_desktops_async(
        self,
        request: ecd_20200930_models.DescribeFotaPendingDesktopsRequest,
    ) -> ecd_20200930_models.DescribeFotaPendingDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fota_pending_desktops_with_options_async(request, runtime)

    def describe_fota_tasks_with_options(
        self,
        request: ecd_20200930_models.DescribeFotaTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFotaTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fota_status):
            query['FotaStatus'] = request.fota_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_fota_tasks_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFotaTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFotaTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fota_status):
            query['FotaStatus'] = request.fota_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFotaTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFotaTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_fota_tasks(
        self,
        request: ecd_20200930_models.DescribeFotaTasksRequest,
    ) -> ecd_20200930_models.DescribeFotaTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_fota_tasks_with_options(request, runtime)

    async def describe_fota_tasks_async(
        self,
        request: ecd_20200930_models.DescribeFotaTasksRequest,
    ) -> ecd_20200930_models.DescribeFotaTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_fota_tasks_with_options_async(request, runtime)

    def describe_front_vul_patch_list_with_options(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFrontVulPatchList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_front_vul_patch_list_with_options_async(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFrontVulPatchList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeFrontVulPatchListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_front_vul_patch_list(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_front_vul_patch_list_with_options(request, runtime)

    async def describe_front_vul_patch_list_async(
        self,
        request: ecd_20200930_models.DescribeFrontVulPatchListRequest,
    ) -> ecd_20200930_models.DescribeFrontVulPatchListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_front_vul_patch_list_with_options_async(request, runtime)

    def describe_grouped_vul_with_options(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_grouped_vul_with_options_async(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroupedVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeGroupedVulResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_grouped_vul(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grouped_vul_with_options(request, runtime)

    async def describe_grouped_vul_async(
        self,
        request: ecd_20200930_models.DescribeGroupedVulRequest,
    ) -> ecd_20200930_models.DescribeGroupedVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grouped_vul_with_options_async(request, runtime)

    def describe_image_modified_records_with_options(
        self,
        request: ecd_20200930_models.DescribeImageModifiedRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImageModifiedRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModifiedRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImageModifiedRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_modified_records_with_options_async(
        self,
        request: ecd_20200930_models.DescribeImageModifiedRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImageModifiedRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImageModifiedRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImageModifiedRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_modified_records(
        self,
        request: ecd_20200930_models.DescribeImageModifiedRecordsRequest,
    ) -> ecd_20200930_models.DescribeImageModifiedRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_modified_records_with_options(request, runtime)

    async def describe_image_modified_records_async(
        self,
        request: ecd_20200930_models.DescribeImageModifiedRecordsRequest,
    ) -> ecd_20200930_models.DescribeImageModifiedRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_modified_records_with_options_async(request, runtime)

    def describe_image_permission_with_options(
        self,
        request: ecd_20200930_models.DescribeImagePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_permission_with_options_async(
        self,
        request: ecd_20200930_models.DescribeImagePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_permission(
        self,
        request: ecd_20200930_models.DescribeImagePermissionRequest,
    ) -> ecd_20200930_models.DescribeImagePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_permission_with_options(request, runtime)

    async def describe_image_permission_async(
        self,
        request: ecd_20200930_models.DescribeImagePermissionRequest,
    ) -> ecd_20200930_models.DescribeImagePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_permission_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_instance_type):
            query['DesktopInstanceType'] = request.desktop_instance_type
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_status):
            query['ImageStatus'] = request.image_status
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.language_type):
            query['LanguageType'] = request.language_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_instance_type):
            query['DesktopInstanceType'] = request.desktop_instance_type
        if not UtilClient.is_unset(request.fota_channel):
            query['FotaChannel'] = request.fota_channel
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_version):
            query['GpuDriverVersion'] = request.gpu_driver_version
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_status):
            query['ImageStatus'] = request.image_status
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.language_type):
            query['LanguageType'] = request.language_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeImages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_images(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: ecd_20200930_models.DescribeImagesRequest,
    ) -> ecd_20200930_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.include_output):
            query['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_type):
            query['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.include_output):
            query['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.invoke_status):
            query['InvokeStatus'] = request.invoke_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: ecd_20200930_models.DescribeInvocationsRequest,
    ) -> ecd_20200930_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_kms_keys_with_options(
        self,
        request: ecd_20200930_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeKmsKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_keys_with_options_async(
        self,
        request: ecd_20200930_models.DescribeKmsKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeKmsKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKmsKeys',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_keys(
        self,
        request: ecd_20200930_models.DescribeKmsKeysRequest,
    ) -> ecd_20200930_models.DescribeKmsKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    async def describe_kms_keys_async(
        self,
        request: ecd_20200930_models.DescribeKmsKeysRequest,
    ) -> ecd_20200930_models.DescribeKmsKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_kms_keys_with_options_async(request, runtime)

    def describe_nasfile_systems_with_options(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nasfile_systems_with_options_async(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNASFileSystems',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNASFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nasfile_systems(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nasfile_systems_with_options(request, runtime)

    async def describe_nasfile_systems_async(
        self,
        request: ecd_20200930_models.DescribeNASFileSystemsRequest,
    ) -> ecd_20200930_models.DescribeNASFileSystemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nasfile_systems_with_options_async(request, runtime)

    def describe_network_packages_with_options(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_network_packages_with_options_async(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeNetworkPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_network_packages(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_packages_with_options(request, runtime)

    async def describe_network_packages_async(
        self,
        request: ecd_20200930_models.DescribeNetworkPackagesRequest,
    ) -> ecd_20200930_models.DescribeNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_packages_with_options_async(request, runtime)

    def describe_office_sites_with_options(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_type):
            query['OfficeSiteType'] = request.office_site_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_office_sites_with_options_async(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_type):
            query['OfficeSiteType'] = request.office_site_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeOfficeSites',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeOfficeSitesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_office_sites(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_office_sites_with_options(request, runtime)

    async def describe_office_sites_async(
        self,
        request: ecd_20200930_models.DescribeOfficeSitesRequest,
    ) -> ecd_20200930_models.DescribeOfficeSitesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_office_sites_with_options_async(request, runtime)

    def describe_policy_groups_with_options(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_groups_with_options_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyGroups',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribePolicyGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_groups(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    async def describe_policy_groups_async(
        self,
        request: ecd_20200930_models.DescribePolicyGroupsRequest,
    ) -> ecd_20200930_models.DescribePolicyGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_groups_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ecd_20200930_models.DescribeRegionsRequest,
    ) -> ecd_20200930_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scan_task_progress_with_options(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scan_task_progress_with_options_async(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScanTaskProgress',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeScanTaskProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scan_task_progress(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scan_task_progress_with_options(request, runtime)

    async def describe_scan_task_progress_async(
        self,
        request: ecd_20200930_models.DescribeScanTaskProgressRequest,
    ) -> ecd_20200930_models.DescribeScanTaskProgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scan_task_progress_with_options_async(request, runtime)

    def describe_security_event_operation_status_with_options(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operation_status_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperationStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operation_status(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operation_status_with_options(request, runtime)

    async def describe_security_event_operation_status_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationStatusRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operation_status_with_options_async(request, runtime)

    def describe_security_event_operations_with_options(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityEventOperations',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSecurityEventOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operations(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    async def describe_security_event_operations_async(
        self,
        request: ecd_20200930_models.DescribeSecurityEventOperationsRequest,
    ) -> ecd_20200930_models.DescribeSecurityEventOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_event_operations_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshots(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ecd_20200930_models.DescribeSnapshotsRequest,
    ) -> ecd_20200930_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_susp_event_overview_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_event_overview_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_event_overview(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_overview_with_options(request, runtime)

    async def describe_susp_event_overview_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventOverviewRequest,
    ) -> ecd_20200930_models.DescribeSuspEventOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_overview_with_options_async(request, runtime)

    def describe_susp_event_quara_files_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_event_quara_files_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEventQuaraFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventQuaraFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_event_quara_files(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_event_quara_files_with_options(request, runtime)

    async def describe_susp_event_quara_files_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventQuaraFilesRequest,
    ) -> ecd_20200930_models.DescribeSuspEventQuaraFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_event_quara_files_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_type):
            query['ParentEventType'] = request.parent_event_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.levels):
            query['Levels'] = request.levels
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_event_type):
            query['ParentEventType'] = request.parent_event_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSuspEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeSuspEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_events(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    async def describe_susp_events_async(
        self,
        request: ecd_20200930_models.DescribeSuspEventsRequest,
    ) -> ecd_20200930_models.DescribeSuspEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_susp_events_with_options_async(request, runtime)

    def describe_user_connection_records_with_options(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_duration_from):
            query['ConnectDurationFrom'] = request.connect_duration_from
        if not UtilClient.is_unset(request.connect_duration_to):
            query['ConnectDurationTo'] = request.connect_duration_to
        if not UtilClient.is_unset(request.connect_end_time_from):
            query['ConnectEndTimeFrom'] = request.connect_end_time_from
        if not UtilClient.is_unset(request.connect_end_time_to):
            query['ConnectEndTimeTo'] = request.connect_end_time_to
        if not UtilClient.is_unset(request.connect_start_time_from):
            query['ConnectStartTimeFrom'] = request.connect_start_time_from
        if not UtilClient.is_unset(request.connect_start_time_to):
            query['ConnectStartTimeTo'] = request.connect_start_time_to
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.end_user_type):
            query['EndUserType'] = request.end_user_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConnectionRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_connection_records_with_options_async(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_duration_from):
            query['ConnectDurationFrom'] = request.connect_duration_from
        if not UtilClient.is_unset(request.connect_duration_to):
            query['ConnectDurationTo'] = request.connect_duration_to
        if not UtilClient.is_unset(request.connect_end_time_from):
            query['ConnectEndTimeFrom'] = request.connect_end_time_from
        if not UtilClient.is_unset(request.connect_end_time_to):
            query['ConnectEndTimeTo'] = request.connect_end_time_to
        if not UtilClient.is_unset(request.connect_start_time_from):
            query['ConnectStartTimeFrom'] = request.connect_start_time_from
        if not UtilClient.is_unset(request.connect_start_time_to):
            query['ConnectStartTimeTo'] = request.connect_start_time_to
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.end_user_type):
            query['EndUserType'] = request.end_user_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserConnectionRecords',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUserConnectionRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_connection_records(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_connection_records_with_options(request, runtime)

    async def describe_user_connection_records_async(
        self,
        request: ecd_20200930_models.DescribeUserConnectionRecordsRequest,
    ) -> ecd_20200930_models.DescribeUserConnectionRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_connection_records_with_options_async(request, runtime)

    def describe_users_in_group_with_options(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_state):
            query['ConnectState'] = request.connect_state
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_user_detail):
            query['QueryUserDetail'] = request.query_user_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_in_group_with_options_async(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connect_state):
            query['ConnectState'] = request.connect_state
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.query_user_detail):
            query['QueryUserDetail'] = request.query_user_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users_in_group(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_users_in_group_with_options(request, runtime)

    async def describe_users_in_group_async(
        self,
        request: ecd_20200930_models.DescribeUsersInGroupRequest,
    ) -> ecd_20200930_models.DescribeUsersInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_in_group_with_options_async(request, runtime)

    def describe_users_password_with_options(
        self,
        request: ecd_20200930_models.DescribeUsersPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersPassword',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_password_with_options_async(
        self,
        request: ecd_20200930_models.DescribeUsersPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeUsersPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsersPassword',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeUsersPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users_password(
        self,
        request: ecd_20200930_models.DescribeUsersPasswordRequest,
    ) -> ecd_20200930_models.DescribeUsersPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_users_password_with_options(request, runtime)

    async def describe_users_password_async(
        self,
        request: ecd_20200930_models.DescribeUsersPasswordRequest,
    ) -> ecd_20200930_models.DescribeUsersPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_password_with_options_async(request, runtime)

    def describe_virtual_mfadevices_with_options(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualMFADevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_virtual_mfadevices_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVirtualMFADevices',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVirtualMFADevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_virtual_mfadevices(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_mfadevices_with_options(request, runtime)

    async def describe_virtual_mfadevices_async(
        self,
        request: ecd_20200930_models.DescribeVirtualMFADevicesRequest,
    ) -> ecd_20200930_models.DescribeVirtualMFADevicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_mfadevices_with_options_async(request, runtime)

    def describe_vul_details_with_options(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_details_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulDetails',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_details(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_details_with_options(request, runtime)

    async def describe_vul_details_async(
        self,
        request: ecd_20200930_models.DescribeVulDetailsRequest,
    ) -> ecd_20200930_models.DescribeVulDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_details_with_options_async(request, runtime)

    def describe_vul_list_with_options(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_list_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dealed):
            query['Dealed'] = request.dealed
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.necessity):
            query['Necessity'] = request.necessity
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulList',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_list(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_list_with_options(request, runtime)

    async def describe_vul_list_async(
        self,
        request: ecd_20200930_models.DescribeVulListRequest,
    ) -> ecd_20200930_models.DescribeVulListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_list_with_options_async(request, runtime)

    def describe_vul_overview_with_options(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vul_overview_with_options_async(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVulOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeVulOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vul_overview(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_overview_with_options(request, runtime)

    async def describe_vul_overview_async(
        self,
        request: ecd_20200930_models.DescribeVulOverviewRequest,
    ) -> ecd_20200930_models.DescribeVulOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_overview_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.zone_type):
            query['ZoneType'] = request.zone_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ecd_20200930_models.DescribeZonesRequest,
    ) -> ecd_20200930_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_cen_with_options(
        self,
        request: ecd_20200930_models.DetachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DetachCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_cen_with_options_async(
        self,
        request: ecd_20200930_models.DetachCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DetachCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DetachCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_cen(
        self,
        request: ecd_20200930_models.DetachCenRequest,
    ) -> ecd_20200930_models.DetachCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_cen_with_options(request, runtime)

    async def detach_cen_async(
        self,
        request: ecd_20200930_models.DetachCenRequest,
    ) -> ecd_20200930_models.DetachCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_cen_with_options_async(request, runtime)

    def disable_desktops_in_group_with_options(
        self,
        request: ecd_20200930_models.DisableDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DisableDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_ids):
            query['DesktopIds'] = request.desktop_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DisableDesktopsInGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_desktops_in_group_with_options_async(
        self,
        request: ecd_20200930_models.DisableDesktopsInGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DisableDesktopsInGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_ids):
            query['DesktopIds'] = request.desktop_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDesktopsInGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DisableDesktopsInGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_desktops_in_group(
        self,
        request: ecd_20200930_models.DisableDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DisableDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_desktops_in_group_with_options(request, runtime)

    async def disable_desktops_in_group_async(
        self,
        request: ecd_20200930_models.DisableDesktopsInGroupRequest,
    ) -> ecd_20200930_models.DisableDesktopsInGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_desktops_in_group_with_options_async(request, runtime)

    def dissociate_network_package_with_options(
        self,
        request: ecd_20200930_models.DissociateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DissociateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DissociateNetworkPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_network_package_with_options_async(
        self,
        request: ecd_20200930_models.DissociateNetworkPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.DissociateNetworkPackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DissociateNetworkPackage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.DissociateNetworkPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_network_package(
        self,
        request: ecd_20200930_models.DissociateNetworkPackageRequest,
    ) -> ecd_20200930_models.DissociateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_network_package_with_options(request, runtime)

    async def dissociate_network_package_async(
        self,
        request: ecd_20200930_models.DissociateNetworkPackageRequest,
    ) -> ecd_20200930_models.DissociateNetworkPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_network_package_with_options_async(request, runtime)

    def export_client_events_with_options(
        self,
        request: ecd_20200930_models.ExportClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportClientEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportClientEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_client_events_with_options_async(
        self,
        request: ecd_20200930_models.ExportClientEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportClientEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportClientEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportClientEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_client_events(
        self,
        request: ecd_20200930_models.ExportClientEventsRequest,
    ) -> ecd_20200930_models.ExportClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_client_events_with_options(request, runtime)

    async def export_client_events_async(
        self,
        request: ecd_20200930_models.ExportClientEventsRequest,
    ) -> ecd_20200930_models.ExportClientEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_client_events_with_options_async(request, runtime)

    def export_desktop_group_info_with_options(
        self,
        request: ecd_20200930_models.ExportDesktopGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportDesktopGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopGroupInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_desktop_group_info_with_options_async(
        self,
        request: ecd_20200930_models.ExportDesktopGroupInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportDesktopGroupInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopGroupInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_desktop_group_info(
        self,
        request: ecd_20200930_models.ExportDesktopGroupInfoRequest,
    ) -> ecd_20200930_models.ExportDesktopGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_group_info_with_options(request, runtime)

    async def export_desktop_group_info_async(
        self,
        request: ecd_20200930_models.ExportDesktopGroupInfoRequest,
    ) -> ecd_20200930_models.ExportDesktopGroupInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_desktop_group_info_with_options_async(request, runtime)

    def export_desktop_list_info_with_options(
        self,
        request: ecd_20200930_models.ExportDesktopListInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportDesktopListInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopListInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopListInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_desktop_list_info_with_options_async(
        self,
        request: ecd_20200930_models.ExportDesktopListInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ExportDesktopListInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_name):
            query['DesktopName'] = request.desktop_name
        if not UtilClient.is_unset(request.desktop_status):
            query['DesktopStatus'] = request.desktop_status
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.expired_time):
            query['ExpiredTime'] = request.expired_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.lang_type):
            query['LangType'] = request.lang_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportDesktopListInfo',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ExportDesktopListInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_desktop_list_info(
        self,
        request: ecd_20200930_models.ExportDesktopListInfoRequest,
    ) -> ecd_20200930_models.ExportDesktopListInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_desktop_list_info_with_options(request, runtime)

    async def export_desktop_list_info_async(
        self,
        request: ecd_20200930_models.ExportDesktopListInfoRequest,
    ) -> ecd_20200930_models.ExportDesktopListInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_desktop_list_info_with_options_async(request, runtime)

    def get_connection_ticket_with_options(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetConnectionTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: ecd_20200930_models.GetConnectionTicketRequest,
    ) -> ecd_20200930_models.GetConnectionTicketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def get_desktop_group_detail_with_options(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDesktopGroupDetail',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_desktop_group_detail_with_options_async(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDesktopGroupDetail',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetDesktopGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_desktop_group_detail(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_desktop_group_detail_with_options(request, runtime)

    async def get_desktop_group_detail_async(
        self,
        request: ecd_20200930_models.GetDesktopGroupDetailRequest,
    ) -> ecd_20200930_models.GetDesktopGroupDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_desktop_group_detail_with_options_async(request, runtime)

    def get_office_site_sso_status_with_options(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_office_site_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetOfficeSiteSsoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_office_site_sso_status(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_site_sso_status_with_options(request, runtime)

    async def get_office_site_sso_status_async(
        self,
        request: ecd_20200930_models.GetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.GetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_site_sso_status_with_options_async(request, runtime)

    def get_sp_metadata_with_options(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.GetSpMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sp_metadata(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sp_metadata_with_options(request, runtime)

    async def get_sp_metadata_async(
        self,
        request: ecd_20200930_models.GetSpMetadataRequest,
    ) -> ecd_20200930_models.GetSpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sp_metadata_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event):
            query['SecurityEvent'] = request.security_event
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not UtilClient.is_unset(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_event):
            query['SecurityEvent'] = request.security_event
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleSecurityEvents',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.HandleSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_security_events(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    async def handle_security_events_async(
        self,
        request: ecd_20200930_models.HandleSecurityEventsRequest,
    ) -> ecd_20200930_models.HandleSecurityEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_security_events_with_options_async(request, runtime)

    def list_directory_users_with_options(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoryUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directory_users_with_options_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoryUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListDirectoryUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directory_users(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    async def list_directory_users_async(
        self,
        request: ecd_20200930_models.ListDirectoryUsersRequest,
    ) -> ecd_20200930_models.ListDirectoryUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_directory_users_with_options_async(request, runtime)

    def list_office_site_overview_with_options(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_refresh):
            query['ForceRefresh'] = request.force_refresh
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.query_range):
            query['QueryRange'] = request.query_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_office_site_overview_with_options_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_refresh):
            query['ForceRefresh'] = request.force_refresh
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.query_range):
            query['QueryRange'] = request.query_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteOverview',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_office_site_overview(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_overview_with_options(request, runtime)

    async def list_office_site_overview_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteOverviewRequest,
    ) -> ecd_20200930_models.ListOfficeSiteOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_site_overview_with_options_async(request, runtime)

    def list_office_site_users_with_options(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_office_site_users_with_options_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oupath):
            query['OUPath'] = request.oupath
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeSiteUsers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListOfficeSiteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_office_site_users(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_site_users_with_options(request, runtime)

    async def list_office_site_users_async(
        self,
        request: ecd_20200930_models.ListOfficeSiteUsersRequest,
    ) -> ecd_20200930_models.ListOfficeSiteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_site_users_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ecd_20200930_models.ListTagResourcesRequest,
    ) -> ecd_20200930_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_ad_organization_units_with_options(
        self,
        request: ecd_20200930_models.ListUserAdOrganizationUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListUserAdOrganizationUnitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAdOrganizationUnits',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListUserAdOrganizationUnitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_ad_organization_units_with_options_async(
        self,
        request: ecd_20200930_models.ListUserAdOrganizationUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ListUserAdOrganizationUnitsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserAdOrganizationUnits',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ListUserAdOrganizationUnitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_ad_organization_units(
        self,
        request: ecd_20200930_models.ListUserAdOrganizationUnitsRequest,
    ) -> ecd_20200930_models.ListUserAdOrganizationUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_ad_organization_units_with_options(request, runtime)

    async def list_user_ad_organization_units_async(
        self,
        request: ecd_20200930_models.ListUserAdOrganizationUnitsRequest,
    ) -> ecd_20200930_models.ListUserAdOrganizationUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_ad_organization_units_with_options_async(request, runtime)

    def lock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def lock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.LockVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_virtual_mfadevice_with_options(request, runtime)

    async def lock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.LockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.LockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_virtual_mfadevice_with_options_async(request, runtime)

    def modify_adconnector_directory_with_options(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_adconnector_directory_with_options_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.directory_name):
            query['DirectoryName'] = request.directory_name
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorDirectory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_adconnector_directory(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_directory_with_options(request, runtime)

    async def modify_adconnector_directory_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorDirectoryRequest,
    ) -> ecd_20200930_models.ModifyADConnectorDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_adconnector_directory_with_options_async(request, runtime)

    def modify_adconnector_office_site_with_options(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_adconnector_office_site_with_options_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_hostname):
            query['AdHostname'] = request.ad_hostname
        if not UtilClient.is_unset(request.dns_address):
            query['DnsAddress'] = request.dns_address
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_password):
            query['DomainPassword'] = request.domain_password
        if not UtilClient.is_unset(request.domain_user_name):
            query['DomainUserName'] = request.domain_user_name
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.ouname):
            query['OUName'] = request.ouname
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sub_domain_dns_address):
            query['SubDomainDnsAddress'] = request.sub_domain_dns_address
        if not UtilClient.is_unset(request.sub_domain_name):
            query['SubDomainName'] = request.sub_domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyADConnectorOfficeSite',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyADConnectorOfficeSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_adconnector_office_site(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_adconnector_office_site_with_options(request, runtime)

    async def modify_adconnector_office_site_async(
        self,
        request: ecd_20200930_models.ModifyADConnectorOfficeSiteRequest,
    ) -> ecd_20200930_models.ModifyADConnectorOfficeSiteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_adconnector_office_site_with_options_async(request, runtime)

    def modify_bundle_with_options(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_bundle_with_options_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bundle_id):
            query['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.bundle_name):
            query['BundleName'] = request.bundle_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBundle',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyBundleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_bundle(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bundle_with_options(request, runtime)

    async def modify_bundle_async(
        self,
        request: ecd_20200930_models.ModifyBundleRequest,
    ) -> ecd_20200930_models.ModifyBundleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bundle_with_options_async(request, runtime)

    def modify_cloud_drive_permission_with_options(
        self,
        request: ecd_20200930_models.ModifyCloudDrivePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyCloudDrivePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.download_end_user_ids):
            query['DownloadEndUserIds'] = request.download_end_user_ids
        if not UtilClient.is_unset(request.download_upload_end_user_ids):
            query['DownloadUploadEndUserIds'] = request.download_upload_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudDrivePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCloudDrivePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cloud_drive_permission_with_options_async(
        self,
        request: ecd_20200930_models.ModifyCloudDrivePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyCloudDrivePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cds_id):
            query['CdsId'] = request.cds_id
        if not UtilClient.is_unset(request.download_end_user_ids):
            query['DownloadEndUserIds'] = request.download_end_user_ids
        if not UtilClient.is_unset(request.download_upload_end_user_ids):
            query['DownloadUploadEndUserIds'] = request.download_upload_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCloudDrivePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyCloudDrivePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cloud_drive_permission(
        self,
        request: ecd_20200930_models.ModifyCloudDrivePermissionRequest,
    ) -> ecd_20200930_models.ModifyCloudDrivePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cloud_drive_permission_with_options(request, runtime)

    async def modify_cloud_drive_permission_async(
        self,
        request: ecd_20200930_models.ModifyCloudDrivePermissionRequest,
    ) -> ecd_20200930_models.ModifyCloudDrivePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cloud_drive_permission_with_options_async(request, runtime)

    def modify_desktop_charge_type_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopChargeType',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktop_charge_type_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopChargeType',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktop_charge_type(
        self,
        request: ecd_20200930_models.ModifyDesktopChargeTypeRequest,
    ) -> ecd_20200930_models.ModifyDesktopChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_charge_type_with_options(request, runtime)

    async def modify_desktop_charge_type_async(
        self,
        request: ecd_20200930_models.ModifyDesktopChargeTypeRequest,
    ) -> ecd_20200930_models.ModifyDesktopChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_charge_type_with_options_async(request, runtime)

    def modify_desktop_group_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.disable_session_config):
            query['DisableSessionConfig'] = request.disable_session_config
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.own_bundle_id):
            query['OwnBundleId'] = request.own_bundle_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_auto_setup):
            query['AllowAutoSetup'] = request.allow_auto_setup
        if not UtilClient.is_unset(request.allow_buffer_count):
            query['AllowBufferCount'] = request.allow_buffer_count
        if not UtilClient.is_unset(request.bind_amount):
            query['BindAmount'] = request.bind_amount
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.connect_duration):
            query['ConnectDuration'] = request.connect_duration
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_name):
            query['DesktopGroupName'] = request.desktop_group_name
        if not UtilClient.is_unset(request.disable_session_config):
            query['DisableSessionConfig'] = request.disable_session_config
        if not UtilClient.is_unset(request.idle_disconnect_duration):
            query['IdleDisconnectDuration'] = request.idle_disconnect_duration
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.keep_duration):
            query['KeepDuration'] = request.keep_duration
        if not UtilClient.is_unset(request.load_policy):
            query['LoadPolicy'] = request.load_policy
        if not UtilClient.is_unset(request.max_desktops_count):
            query['MaxDesktopsCount'] = request.max_desktops_count
        if not UtilClient.is_unset(request.min_desktops_count):
            query['MinDesktopsCount'] = request.min_desktops_count
        if not UtilClient.is_unset(request.own_bundle_id):
            query['OwnBundleId'] = request.own_bundle_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.ratio_threshold):
            query['RatioThreshold'] = request.ratio_threshold
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.scale_strategy_id):
            query['ScaleStrategyId'] = request.scale_strategy_id
        if not UtilClient.is_unset(request.stop_duration):
            query['StopDuration'] = request.stop_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktop_group(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_group_with_options(request, runtime)

    async def modify_desktop_group_async(
        self,
        request: ecd_20200930_models.ModifyDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_group_with_options_async(request, runtime)

    def modify_desktop_host_name_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopHostNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopHostNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_host_name):
            query['NewHostName'] = request.new_host_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopHostName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopHostNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktop_host_name_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopHostNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopHostNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_host_name):
            query['NewHostName'] = request.new_host_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopHostName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopHostNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktop_host_name(
        self,
        request: ecd_20200930_models.ModifyDesktopHostNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopHostNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_host_name_with_options(request, runtime)

    async def modify_desktop_host_name_async(
        self,
        request: ecd_20200930_models.ModifyDesktopHostNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopHostNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_host_name_with_options_async(request, runtime)

    def modify_desktop_name_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_desktop_name):
            query['NewDesktopName'] = request.new_desktop_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktop_name_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.new_desktop_name):
            query['NewDesktopName'] = request.new_desktop_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopName',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktop_name(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_name_with_options(request, runtime)

    async def modify_desktop_name_async(
        self,
        request: ecd_20200930_models.ModifyDesktopNameRequest,
    ) -> ecd_20200930_models.ModifyDesktopNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_name_with_options_async(request, runtime)

    def modify_desktop_spec_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktop_spec_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.desktop_type):
            query['DesktopType'] = request.desktop_type
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_size_gib):
            query['RootDiskSizeGib'] = request.root_disk_size_gib
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_size_gib):
            query['UserDiskSizeGib'] = request.user_disk_size_gib
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktop_spec(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_spec_with_options(request, runtime)

    async def modify_desktop_spec_async(
        self,
        request: ecd_20200930_models.ModifyDesktopSpecRequest,
    ) -> ecd_20200930_models.ModifyDesktopSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktop_spec_with_options_async(request, runtime)

    def modify_desktops_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopsPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_desktops_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDesktopsPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDesktopsPolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_desktops_policy_group(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    async def modify_desktops_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyDesktopsPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyDesktopsPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_desktops_policy_group_with_options_async(request, runtime)

    def modify_disk_spec_with_options(
        self,
        request: ecd_20200930_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDiskSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_spec_with_options_async(
        self,
        request: ecd_20200930_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.root_disk_performance_level):
            query['RootDiskPerformanceLevel'] = request.root_disk_performance_level
        if not UtilClient.is_unset(request.user_disk_performance_level):
            query['UserDiskPerformanceLevel'] = request.user_disk_performance_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDiskSpec',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyDiskSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_spec(
        self,
        request: ecd_20200930_models.ModifyDiskSpecRequest,
    ) -> ecd_20200930_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    async def modify_disk_spec_async(
        self,
        request: ecd_20200930_models.ModifyDiskSpecRequest,
    ) -> ecd_20200930_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_spec_with_options_async(request, runtime)

    def modify_entitlement_with_options(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_entitlement_with_options_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyEntitlementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_entitlement(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    async def modify_entitlement_async(
        self,
        request: ecd_20200930_models.ModifyEntitlementRequest,
    ) -> ecd_20200930_models.ModifyEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_entitlement_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImageAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImageAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_attribute(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ecd_20200930_models.ModifyImageAttributeRequest,
    ) -> ecd_20200930_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_image_permission_with_options(
        self,
        request: ecd_20200930_models.ModifyImagePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImagePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImagePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_image_permission_with_options_async(
        self,
        request: ecd_20200930_models.ModifyImagePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyImagePermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_account):
            query['AddAccount'] = request.add_account
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_account):
            query['RemoveAccount'] = request.remove_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyImagePermission',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyImagePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_image_permission(
        self,
        request: ecd_20200930_models.ModifyImagePermissionRequest,
    ) -> ecd_20200930_models.ModifyImagePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_permission_with_options(request, runtime)

    async def modify_image_permission_async(
        self,
        request: ecd_20200930_models.ModifyImagePermissionRequest,
    ) -> ecd_20200930_models.ModifyImagePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_permission_with_options_async(request, runtime)

    def modify_nasdefault_mount_target_with_options(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_nasdefault_mount_target_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNASDefaultMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_nasdefault_mount_target(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nasdefault_mount_target_with_options(request, runtime)

    async def modify_nasdefault_mount_target_async(
        self,
        request: ecd_20200930_models.ModifyNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ModifyNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nasdefault_mount_target_with_options_async(request, runtime)

    def modify_network_package_bandwidth_with_options(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageBandwidth',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageBandwidthResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_package_bandwidth_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageBandwidthResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageBandwidth',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageBandwidthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_package_bandwidth(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageBandwidthRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_bandwidth_with_options(request, runtime)

    async def modify_network_package_bandwidth_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageBandwidthRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_package_bandwidth_with_options_async(request, runtime)

    def modify_network_package_enabled_with_options(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_network_package_enabled_with_options_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNetworkPackageEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyNetworkPackageEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_network_package_enabled(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_package_enabled_with_options(request, runtime)

    async def modify_network_package_enabled_async(
        self,
        request: ecd_20200930_models.ModifyNetworkPackageEnabledRequest,
    ) -> ecd_20200930_models.ModifyNetworkPackageEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_package_enabled_with_options_async(request, runtime)

    def modify_office_site_attribute_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.need_verify_login_risk):
            query['NeedVerifyLoginRisk'] = request.need_verify_login_risk
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_office_site_attribute_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_access_type):
            query['DesktopAccessType'] = request.desktop_access_type
        if not UtilClient.is_unset(request.need_verify_login_risk):
            query['NeedVerifyLoginRisk'] = request.need_verify_login_risk
        if not UtilClient.is_unset(request.need_verify_zero_device):
            query['NeedVerifyZeroDevice'] = request.need_verify_zero_device
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.office_site_name):
            query['OfficeSiteName'] = request.office_site_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteAttribute',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_office_site_attribute(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_attribute_with_options(request, runtime)

    async def modify_office_site_attribute_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteAttributeRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_attribute_with_options_async(request, runtime)

    def modify_office_site_cross_desktop_access_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_cross_desktop_access):
            query['EnableCrossDesktopAccess'] = request.enable_cross_desktop_access
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteCrossDesktopAccess',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_office_site_cross_desktop_access_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_cross_desktop_access):
            query['EnableCrossDesktopAccess'] = request.enable_cross_desktop_access
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteCrossDesktopAccess',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_office_site_cross_desktop_access(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_cross_desktop_access_with_options(request, runtime)

    async def modify_office_site_cross_desktop_access_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteCrossDesktopAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_cross_desktop_access_with_options_async(request, runtime)

    def modify_office_site_mfa_enabled_with_options(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteMfaEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_office_site_mfa_enabled_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mfa_enabled):
            query['MfaEnabled'] = request.mfa_enabled
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOfficeSiteMfaEnabled',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_office_site_mfa_enabled(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_office_site_mfa_enabled_with_options(request, runtime)

    async def modify_office_site_mfa_enabled_async(
        self,
        request: ecd_20200930_models.ModifyOfficeSiteMfaEnabledRequest,
    ) -> ecd_20200930_models.ModifyOfficeSiteMfaEnabledResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_office_site_mfa_enabled_with_options_async(request, runtime)

    def modify_operate_vul_with_options(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_operate_vul_with_options_async(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_info):
            query['VulInfo'] = request.vul_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOperateVul',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyOperateVulResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_operate_vul(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_operate_vul_with_options(request, runtime)

    async def modify_operate_vul_async(
        self,
        request: ecd_20200930_models.ModifyOperateVulRequest,
    ) -> ecd_20200930_models.ModifyOperateVulResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_operate_vul_with_options_async(request, runtime)

    def modify_policy_group_with_options(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.revoke_access_policy_rule):
            query['RevokeAccessPolicyRule'] = request.revoke_access_policy_rule
        if not UtilClient.is_unset(request.revoke_security_policy_rule):
            query['RevokeSecurityPolicyRule'] = request.revoke_security_policy_rule
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_policy_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_content_protection):
            query['AppContentProtection'] = request.app_content_protection
        if not UtilClient.is_unset(request.authorize_access_policy_rule):
            query['AuthorizeAccessPolicyRule'] = request.authorize_access_policy_rule
        if not UtilClient.is_unset(request.authorize_security_policy_rule):
            query['AuthorizeSecurityPolicyRule'] = request.authorize_security_policy_rule
        if not UtilClient.is_unset(request.camera_redirect):
            query['CameraRedirect'] = request.camera_redirect
        if not UtilClient.is_unset(request.client_type):
            query['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.clipboard):
            query['Clipboard'] = request.clipboard
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.gpu_acceleration):
            query['GpuAcceleration'] = request.gpu_acceleration
        if not UtilClient.is_unset(request.html_5access):
            query['Html5Access'] = request.html_5access
        if not UtilClient.is_unset(request.html_5file_transfer):
            query['Html5FileTransfer'] = request.html_5file_transfer
        if not UtilClient.is_unset(request.local_drive):
            query['LocalDrive'] = request.local_drive
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_redirect):
            query['NetRedirect'] = request.net_redirect
        if not UtilClient.is_unset(request.policy_group_id):
            query['PolicyGroupId'] = request.policy_group_id
        if not UtilClient.is_unset(request.preempt_login):
            query['PreemptLogin'] = request.preempt_login
        if not UtilClient.is_unset(request.preempt_login_user):
            query['PreemptLoginUser'] = request.preempt_login_user
        if not UtilClient.is_unset(request.printer_redirection):
            query['PrinterRedirection'] = request.printer_redirection
        if not UtilClient.is_unset(request.record_content):
            query['RecordContent'] = request.record_content
        if not UtilClient.is_unset(request.record_content_expires):
            query['RecordContentExpires'] = request.record_content_expires
        if not UtilClient.is_unset(request.recording):
            query['Recording'] = request.recording
        if not UtilClient.is_unset(request.recording_end_time):
            query['RecordingEndTime'] = request.recording_end_time
        if not UtilClient.is_unset(request.recording_expires):
            query['RecordingExpires'] = request.recording_expires
        if not UtilClient.is_unset(request.recording_fps):
            query['RecordingFps'] = request.recording_fps
        if not UtilClient.is_unset(request.recording_start_time):
            query['RecordingStartTime'] = request.recording_start_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.revoke_access_policy_rule):
            query['RevokeAccessPolicyRule'] = request.revoke_access_policy_rule
        if not UtilClient.is_unset(request.revoke_security_policy_rule):
            query['RevokeSecurityPolicyRule'] = request.revoke_security_policy_rule
        if not UtilClient.is_unset(request.usb_redirect):
            query['UsbRedirect'] = request.usb_redirect
        if not UtilClient.is_unset(request.usb_supply_redirect_rule):
            query['UsbSupplyRedirectRule'] = request.usb_supply_redirect_rule
        if not UtilClient.is_unset(request.visual_quality):
            query['VisualQuality'] = request.visual_quality
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        if not UtilClient.is_unset(request.watermark_transparency):
            query['WatermarkTransparency'] = request.watermark_transparency
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPolicyGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyPolicyGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_policy_group(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    async def modify_policy_group_async(
        self,
        request: ecd_20200930_models.ModifyPolicyGroupRequest,
    ) -> ecd_20200930_models.ModifyPolicyGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_policy_group_with_options_async(request, runtime)

    def modify_user_entitlement_with_options(
        self,
        request: ecd_20200930_models.ModifyUserEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserEntitlementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_desktop_id):
            query['AuthorizeDesktopId'] = request.authorize_desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.revoke_desktop_id):
            query['RevokeDesktopId'] = request.revoke_desktop_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserEntitlementResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_entitlement_with_options_async(
        self,
        request: ecd_20200930_models.ModifyUserEntitlementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserEntitlementResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_desktop_id):
            query['AuthorizeDesktopId'] = request.authorize_desktop_id
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.revoke_desktop_id):
            query['RevokeDesktopId'] = request.revoke_desktop_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserEntitlement',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserEntitlementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_entitlement(
        self,
        request: ecd_20200930_models.ModifyUserEntitlementRequest,
    ) -> ecd_20200930_models.ModifyUserEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_entitlement_with_options(request, runtime)

    async def modify_user_entitlement_async(
        self,
        request: ecd_20200930_models.ModifyUserEntitlementRequest,
    ) -> ecd_20200930_models.ModifyUserEntitlementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_entitlement_with_options_async(request, runtime)

    def modify_user_to_desktop_group_with_options(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.new_end_user_ids):
            query['NewEndUserIds'] = request.new_end_user_ids
        if not UtilClient.is_unset(request.old_end_user_ids):
            query['OldEndUserIds'] = request.old_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_to_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.new_end_user_ids):
            query['NewEndUserIds'] = request.new_end_user_ids
        if not UtilClient.is_unset(request.old_end_user_ids):
            query['OldEndUserIds'] = request.old_end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserToDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ModifyUserToDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_to_desktop_group(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_to_desktop_group_with_options(request, runtime)

    async def modify_user_to_desktop_group_async(
        self,
        request: ecd_20200930_models.ModifyUserToDesktopGroupRequest,
    ) -> ecd_20200930_models.ModifyUserToDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_to_desktop_group_with_options_async(request, runtime)

    def operate_vuls_with_options(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.precondition):
            query['Precondition'] = request.precondition
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_vuls_with_options_async(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.OperateVulsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        if not UtilClient.is_unset(request.precondition):
            query['Precondition'] = request.precondition
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vul_name):
            query['VulName'] = request.vul_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateVuls',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.OperateVulsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_vuls(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
    ) -> ecd_20200930_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_vuls_with_options(request, runtime)

    async def operate_vuls_async(
        self,
        request: ecd_20200930_models.OperateVulsRequest,
    ) -> ecd_20200930_models.OperateVulsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_vuls_with_options_async(request, runtime)

    def reboot_desktops_with_options(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebootDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebootDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_desktops(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    async def reboot_desktops_async(
        self,
        request: ecd_20200930_models.RebootDesktopsRequest,
    ) -> ecd_20200930_models.RebootDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_desktops_with_options_async(request, runtime)

    def rebuild_desktops_with_options(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RebuildDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_desktops(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_desktops_with_options(request, runtime)

    async def rebuild_desktops_async(
        self,
        request: ecd_20200930_models.RebuildDesktopsRequest,
    ) -> ecd_20200930_models.RebuildDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_desktops_with_options_async(request, runtime)

    def remove_user_from_desktop_group_with_options(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_from_desktop_group_with_options_async(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_group_ids):
            query['DesktopGroupIds'] = request.desktop_group_ids
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUserFromDesktopGroup',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RemoveUserFromDesktopGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_from_desktop_group(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_user_from_desktop_group_with_options(request, runtime)

    async def remove_user_from_desktop_group_async(
        self,
        request: ecd_20200930_models.RemoveUserFromDesktopGroupRequest,
    ) -> ecd_20200930_models.RemoveUserFromDesktopGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_user_from_desktop_group_with_options_async(request, runtime)

    def renew_desktops_with_options(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_desktops_with_options_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_desktops(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_desktops_with_options(request, runtime)

    async def renew_desktops_async(
        self,
        request: ecd_20200930_models.RenewDesktopsRequest,
    ) -> ecd_20200930_models.RenewDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_desktops_with_options_async(request, runtime)

    def renew_network_packages_with_options(
        self,
        request: ecd_20200930_models.RenewNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewNetworkPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_network_packages_with_options_async(
        self,
        request: ecd_20200930_models.RenewNetworkPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RenewNetworkPackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.network_package_id):
            query['NetworkPackageId'] = request.network_package_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewNetworkPackages',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RenewNetworkPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_network_packages(
        self,
        request: ecd_20200930_models.RenewNetworkPackagesRequest,
    ) -> ecd_20200930_models.RenewNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_network_packages_with_options(request, runtime)

    async def renew_network_packages_async(
        self,
        request: ecd_20200930_models.RenewNetworkPackagesRequest,
    ) -> ecd_20200930_models.RenewNetworkPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_network_packages_with_options_async(request, runtime)

    def reset_desktops_with_options(
        self,
        request: ecd_20200930_models.ResetDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_desktops_with_options_async(
        self,
        request: ecd_20200930_models.ResetDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_desktops(
        self,
        request: ecd_20200930_models.ResetDesktopsRequest,
    ) -> ecd_20200930_models.ResetDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_desktops_with_options(request, runtime)

    async def reset_desktops_async(
        self,
        request: ecd_20200930_models.ResetDesktopsRequest,
    ) -> ecd_20200930_models.ResetDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_desktops_with_options_async(request, runtime)

    def reset_nasdefault_mount_target_with_options(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_nasdefault_mount_target_with_options_async(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNASDefaultMountTarget',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetNASDefaultMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_nasdefault_mount_target(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_nasdefault_mount_target_with_options(request, runtime)

    async def reset_nasdefault_mount_target_async(
        self,
        request: ecd_20200930_models.ResetNASDefaultMountTargetRequest,
    ) -> ecd_20200930_models.ResetNASDefaultMountTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_nasdefault_mount_target_with_options_async(request, runtime)

    def reset_snapshot_with_options(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_snapshot_with_options_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSnapshot',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.ResetSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_snapshot(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_snapshot_with_options(request, runtime)

    async def reset_snapshot_async(
        self,
        request: ecd_20200930_models.ResetSnapshotRequest,
    ) -> ecd_20200930_models.ResetSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_snapshot_with_options_async(request, runtime)

    def rollback_susp_event_quara_file_with_options(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.quara_field_id):
            query['QuaraFieldId'] = request.quara_field_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_susp_event_quara_file_with_options_async(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.quara_field_id):
            query['QuaraFieldId'] = request.quara_field_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackSuspEventQuaraFile',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RollbackSuspEventQuaraFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_susp_event_quara_file(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_susp_event_quara_file_with_options(request, runtime)

    async def rollback_susp_event_quara_file_async(
        self,
        request: ecd_20200930_models.RollbackSuspEventQuaraFileRequest,
    ) -> ecd_20200930_models.RollbackSuspEventQuaraFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_susp_event_quara_file_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.RunCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command_content):
            query['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.content_encoding):
            query['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: ecd_20200930_models.RunCommandRequest,
    ) -> ecd_20200930_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_verify_code_with_options(
        self,
        request: ecd_20200930_models.SendVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SendVerifyCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code_action):
            query['VerifyCodeAction'] = request.verify_code_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCode',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SendVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verify_code_with_options_async(
        self,
        request: ecd_20200930_models.SendVerifyCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SendVerifyCodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code_action):
            query['VerifyCodeAction'] = request.verify_code_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerifyCode',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SendVerifyCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verify_code(
        self,
        request: ecd_20200930_models.SendVerifyCodeRequest,
    ) -> ecd_20200930_models.SendVerifyCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verify_code_with_options(request, runtime)

    async def send_verify_code_async(
        self,
        request: ecd_20200930_models.SendVerifyCodeRequest,
    ) -> ecd_20200930_models.SendVerifyCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verify_code_with_options_async(request, runtime)

    def set_desktop_group_timer_with_options(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDesktopGroupTimerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_desktop_group_timer_with_options_async(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDesktopGroupTimerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reset_type):
            query['ResetType'] = request.reset_type
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimer',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_desktop_group_timer(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerRequest,
    ) -> ecd_20200930_models.SetDesktopGroupTimerResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_desktop_group_timer_with_options(request, runtime)

    async def set_desktop_group_timer_async(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerRequest,
    ) -> ecd_20200930_models.SetDesktopGroupTimerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_desktop_group_timer_with_options_async(request, runtime)

    def set_desktop_group_timer_status_with_options(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDesktopGroupTimerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimerStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_desktop_group_timer_status_with_options_async(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetDesktopGroupTimerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_group_id):
            query['DesktopGroupId'] = request.desktop_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.timer_type):
            query['TimerType'] = request.timer_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDesktopGroupTimerStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetDesktopGroupTimerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_desktop_group_timer_status(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerStatusRequest,
    ) -> ecd_20200930_models.SetDesktopGroupTimerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_desktop_group_timer_status_with_options(request, runtime)

    async def set_desktop_group_timer_status_async(
        self,
        request: ecd_20200930_models.SetDesktopGroupTimerStatusRequest,
    ) -> ecd_20200930_models.SetDesktopGroupTimerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_desktop_group_timer_status_with_options_async(request, runtime)

    def set_idp_metadata_with_options(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIdpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_idp_metadata_with_options_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.idp_metadata):
            query['IdpMetadata'] = request.idp_metadata
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetIdpMetadata',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetIdpMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_idp_metadata(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_idp_metadata_with_options(request, runtime)

    async def set_idp_metadata_async(
        self,
        request: ecd_20200930_models.SetIdpMetadataRequest,
    ) -> ecd_20200930_models.SetIdpMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_idp_metadata_with_options_async(request, runtime)

    def set_office_site_sso_status_with_options(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_sso):
            query['EnableSso'] = request.enable_sso
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_office_site_sso_status_with_options_async(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_sso):
            query['EnableSso'] = request.enable_sso
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetOfficeSiteSsoStatus',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.SetOfficeSiteSsoStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_office_site_sso_status(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_office_site_sso_status_with_options(request, runtime)

    async def set_office_site_sso_status_async(
        self,
        request: ecd_20200930_models.SetOfficeSiteSsoStatusRequest,
    ) -> ecd_20200930_models.SetOfficeSiteSsoStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_office_site_sso_status_with_options_async(request, runtime)

    def start_desktops_with_options(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_desktops(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_desktops_with_options(request, runtime)

    async def start_desktops_async(
        self,
        request: ecd_20200930_models.StartDesktopsRequest,
    ) -> ecd_20200930_models.StartDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_desktops_with_options_async(request, runtime)

    def start_virus_scan_task_with_options(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_virus_scan_task_with_options_async(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.office_site_id):
            query['OfficeSiteId'] = request.office_site_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartVirusScanTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StartVirusScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_virus_scan_task(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_virus_scan_task_with_options(request, runtime)

    async def start_virus_scan_task_async(
        self,
        request: ecd_20200930_models.StartVirusScanTaskRequest,
    ) -> ecd_20200930_models.StartVirusScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_virus_scan_task_with_options_async(request, runtime)

    def stop_desktops_with_options(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stopped_mode):
            query['StoppedMode'] = request.stopped_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_desktops_with_options_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stopped_mode):
            query['StoppedMode'] = request.stopped_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDesktops',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopDesktopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_desktops(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_desktops_with_options(request, runtime)

    async def stop_desktops_async(
        self,
        request: ecd_20200930_models.StopDesktopsRequest,
    ) -> ecd_20200930_models.StopDesktopsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_desktops_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInvocation',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desktop_id):
            query['DesktopId'] = request.desktop_id
        if not UtilClient.is_unset(request.invoke_id):
            query['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInvocation',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.StopInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_invocation(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: ecd_20200930_models.StopInvocationRequest,
    ) -> ecd_20200930_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ecd_20200930_models.TagResourcesRequest,
    ) -> ecd_20200930_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unlock_virtual_mfadevice_with_options(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def unlock_virtual_mfadevice_with_options_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockVirtualMFADevice',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UnlockVirtualMFADeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unlock_virtual_mfadevice(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_virtual_mfadevice_with_options(request, runtime)

    async def unlock_virtual_mfadevice_async(
        self,
        request: ecd_20200930_models.UnlockVirtualMFADeviceRequest,
    ) -> ecd_20200930_models.UnlockVirtualMFADeviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_virtual_mfadevice_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ecd_20200930_models.UntagResourcesRequest,
    ) -> ecd_20200930_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_fota_task_with_options(
        self,
        request: ecd_20200930_models.UpdateFotaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UpdateFotaTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFotaTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UpdateFotaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_fota_task_with_options_async(
        self,
        request: ecd_20200930_models.UpdateFotaTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UpdateFotaTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_uid):
            query['TaskUid'] = request.task_uid
        if not UtilClient.is_unset(request.user_status):
            query['UserStatus'] = request.user_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFotaTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UpdateFotaTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_fota_task(
        self,
        request: ecd_20200930_models.UpdateFotaTaskRequest,
    ) -> ecd_20200930_models.UpdateFotaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_fota_task_with_options(request, runtime)

    async def update_fota_task_async(
        self,
        request: ecd_20200930_models.UpdateFotaTaskRequest,
    ) -> ecd_20200930_models.UpdateFotaTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_fota_task_with_options_async(request, runtime)

    def upload_image_with_options(
        self,
        request: ecd_20200930_models.UploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UploadImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_security_check):
            query['EnableSecurityCheck'] = request.enable_security_check
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_type):
            query['GpuDriverType'] = request.gpu_driver_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.oss_object_path):
            query['OssObjectPath'] = request.oss_object_path
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UploadImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_image_with_options_async(
        self,
        request: ecd_20200930_models.UploadImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.UploadImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_disk_size):
            query['DataDiskSize'] = request.data_disk_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_security_check):
            query['EnableSecurityCheck'] = request.enable_security_check
        if not UtilClient.is_unset(request.gpu_category):
            query['GpuCategory'] = request.gpu_category
        if not UtilClient.is_unset(request.gpu_driver_type):
            query['GpuDriverType'] = request.gpu_driver_type
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.license_type):
            query['LicenseType'] = request.license_type
        if not UtilClient.is_unset(request.os_type):
            query['OsType'] = request.os_type
        if not UtilClient.is_unset(request.oss_object_path):
            query['OssObjectPath'] = request.oss_object_path
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadImage',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.UploadImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_image(
        self,
        request: ecd_20200930_models.UploadImageRequest,
    ) -> ecd_20200930_models.UploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_image_with_options(request, runtime)

    async def upload_image_async(
        self,
        request: ecd_20200930_models.UploadImageRequest,
    ) -> ecd_20200930_models.UploadImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_image_with_options_async(request, runtime)

    def verify_cen_with_options(
        self,
        request: ecd_20200930_models.VerifyCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.VerifyCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.VerifyCenResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_cen_with_options_async(
        self,
        request: ecd_20200930_models.VerifyCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecd_20200930_models.VerifyCenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cen_owner_id):
            query['CenOwnerId'] = request.cen_owner_id
        if not UtilClient.is_unset(request.cidr_block):
            query['CidrBlock'] = request.cidr_block
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyCen',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ecd_20200930_models.VerifyCenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_cen(
        self,
        request: ecd_20200930_models.VerifyCenRequest,
    ) -> ecd_20200930_models.VerifyCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_cen_with_options(request, runtime)

    async def verify_cen_async(
        self,
        request: ecd_20200930_models.VerifyCenRequest,
    ) -> ecd_20200930_models.VerifyCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_cen_with_options_async(request, runtime)
