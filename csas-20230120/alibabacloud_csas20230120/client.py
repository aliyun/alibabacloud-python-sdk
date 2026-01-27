# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_csas20230120 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('csas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_application_2connector_with_options(
        self,
        tmp_req: main_models.AttachApplication2ConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachApplication2ConnectorResponse:
        tmp_req.validate()
        request = main_models.AttachApplication2ConnectorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_ids):
            request.application_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not DaraCore.is_null(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not DaraCore.is_null(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachApplication2Connector',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_application_2connector_with_options_async(
        self,
        tmp_req: main_models.AttachApplication2ConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachApplication2ConnectorResponse:
        tmp_req.validate()
        request = main_models.AttachApplication2ConnectorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_ids):
            request.application_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not DaraCore.is_null(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not DaraCore.is_null(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachApplication2Connector',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_application_2connector(
        self,
        request: main_models.AttachApplication2ConnectorRequest,
    ) -> main_models.AttachApplication2ConnectorResponse:
        runtime = RuntimeOptions()
        return self.attach_application_2connector_with_options(request, runtime)

    async def attach_application_2connector_async(
        self,
        request: main_models.AttachApplication2ConnectorRequest,
    ) -> main_models.AttachApplication2ConnectorResponse:
        runtime = RuntimeOptions()
        return await self.attach_application_2connector_with_options_async(request, runtime)

    def attach_policy_2approval_process_with_options(
        self,
        request: main_models.AttachPolicy2ApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicy2ApprovalProcessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy2ApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicy2ApprovalProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_2approval_process_with_options_async(
        self,
        request: main_models.AttachPolicy2ApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachPolicy2ApprovalProcessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AttachPolicy2ApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachPolicy2ApprovalProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy_2approval_process(
        self,
        request: main_models.AttachPolicy2ApprovalProcessRequest,
    ) -> main_models.AttachPolicy2ApprovalProcessResponse:
        runtime = RuntimeOptions()
        return self.attach_policy_2approval_process_with_options(request, runtime)

    async def attach_policy_2approval_process_async(
        self,
        request: main_models.AttachPolicy2ApprovalProcessRequest,
    ) -> main_models.AttachPolicy2ApprovalProcessResponse:
        runtime = RuntimeOptions()
        return await self.attach_policy_2approval_process_with_options_async(request, runtime)

    def create_approval_process_with_options(
        self,
        tmp_req: main_models.CreateApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApprovalProcessResponse:
        tmp_req.validate()
        request = main_models.CreateApprovalProcessShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.match_schemas):
            request.match_schemas_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schemas, 'MatchSchemas', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_schemas_shrink):
            body['MatchSchemas'] = request.match_schemas_shrink
        if not DaraCore.is_null(request.process_name):
            body['ProcessName'] = request.process_name
        body_flat = {}
        if not DaraCore.is_null(request.process_nodes):
            body_flat['ProcessNodes'] = request.process_nodes
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApprovalProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_approval_process_with_options_async(
        self,
        tmp_req: main_models.CreateApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApprovalProcessResponse:
        tmp_req.validate()
        request = main_models.CreateApprovalProcessShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.match_schemas):
            request.match_schemas_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schemas, 'MatchSchemas', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_schemas_shrink):
            body['MatchSchemas'] = request.match_schemas_shrink
        if not DaraCore.is_null(request.process_name):
            body['ProcessName'] = request.process_name
        body_flat = {}
        if not DaraCore.is_null(request.process_nodes):
            body_flat['ProcessNodes'] = request.process_nodes
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApprovalProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_approval_process(
        self,
        request: main_models.CreateApprovalProcessRequest,
    ) -> main_models.CreateApprovalProcessResponse:
        runtime = RuntimeOptions()
        return self.create_approval_process_with_options(request, runtime)

    async def create_approval_process_async(
        self,
        request: main_models.CreateApprovalProcessRequest,
    ) -> main_models.CreateApprovalProcessResponse:
        runtime = RuntimeOptions()
        return await self.create_approval_process_with_options_async(request, runtime)

    def create_client_user_with_options(
        self,
        request: main_models.CreateClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_user_with_options_async(
        self,
        request: main_models.CreateClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_user(
        self,
        request: main_models.CreateClientUserRequest,
    ) -> main_models.CreateClientUserResponse:
        runtime = RuntimeOptions()
        return self.create_client_user_with_options(request, runtime)

    async def create_client_user_async(
        self,
        request: main_models.CreateClientUserRequest,
    ) -> main_models.CreateClientUserResponse:
        runtime = RuntimeOptions()
        return await self.create_client_user_with_options_async(request, runtime)

    def create_dynamic_route_with_options(
        self,
        request: main_models.CreateDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDynamicRouteResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_hop):
            body['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dynamic_route_with_options_async(
        self,
        request: main_models.CreateDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDynamicRouteResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_hop):
            body['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dynamic_route(
        self,
        request: main_models.CreateDynamicRouteRequest,
    ) -> main_models.CreateDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.create_dynamic_route_with_options(request, runtime)

    async def create_dynamic_route_async(
        self,
        request: main_models.CreateDynamicRouteRequest,
    ) -> main_models.CreateDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.create_dynamic_route_with_options_async(request, runtime)

    def create_enterprise_accelerate_policy_with_options(
        self,
        request: main_models.CreateEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acceleration_type):
            body['AccelerationType'] = request.acceleration_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.show_in_client):
            body['ShowInClient'] = request.show_in_client
        if not DaraCore.is_null(request.upstream_host):
            body['UpstreamHost'] = request.upstream_host
        if not DaraCore.is_null(request.upstream_port):
            body['UpstreamPort'] = request.upstream_port
        if not DaraCore.is_null(request.upstream_type):
            body['UpstreamType'] = request.upstream_type
        if not DaraCore.is_null(request.user_attribute_group):
            body['UserAttributeGroup'] = request.user_attribute_group
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseAcceleratePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_accelerate_policy_with_options_async(
        self,
        request: main_models.CreateEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acceleration_type):
            body['AccelerationType'] = request.acceleration_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.show_in_client):
            body['ShowInClient'] = request.show_in_client
        if not DaraCore.is_null(request.upstream_host):
            body['UpstreamHost'] = request.upstream_host
        if not DaraCore.is_null(request.upstream_port):
            body['UpstreamPort'] = request.upstream_port
        if not DaraCore.is_null(request.upstream_type):
            body['UpstreamType'] = request.upstream_type
        if not DaraCore.is_null(request.user_attribute_group):
            body['UserAttributeGroup'] = request.user_attribute_group
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseAcceleratePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise_accelerate_policy(
        self,
        request: main_models.CreateEnterpriseAcceleratePolicyRequest,
    ) -> main_models.CreateEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_enterprise_accelerate_policy_with_options(request, runtime)

    async def create_enterprise_accelerate_policy_async(
        self,
        request: main_models.CreateEnterpriseAcceleratePolicyRequest,
    ) -> main_models.CreateEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_enterprise_accelerate_policy_with_options_async(request, runtime)

    def create_enterprise_accelerate_target_with_options(
        self,
        request: main_models.CreateEnterpriseAccelerateTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseAccelerateTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        body_flat = {}
        if not DaraCore.is_null(request.target):
            body_flat['Target'] = request.target
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseAccelerateTarget',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseAccelerateTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_accelerate_target_with_options_async(
        self,
        request: main_models.CreateEnterpriseAccelerateTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseAccelerateTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        body_flat = {}
        if not DaraCore.is_null(request.target):
            body_flat['Target'] = request.target
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterpriseAccelerateTarget',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseAccelerateTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise_accelerate_target(
        self,
        request: main_models.CreateEnterpriseAccelerateTargetRequest,
    ) -> main_models.CreateEnterpriseAccelerateTargetResponse:
        runtime = RuntimeOptions()
        return self.create_enterprise_accelerate_target_with_options(request, runtime)

    async def create_enterprise_accelerate_target_async(
        self,
        request: main_models.CreateEnterpriseAccelerateTargetRequest,
    ) -> main_models.CreateEnterpriseAccelerateTargetResponse:
        runtime = RuntimeOptions()
        return await self.create_enterprise_accelerate_target_with_options_async(request, runtime)

    def create_idp_department_with_options(
        self,
        request: main_models.CreateIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idp_department_with_options_async(
        self,
        request: main_models.CreateIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idp_department(
        self,
        request: main_models.CreateIdpDepartmentRequest,
    ) -> main_models.CreateIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return self.create_idp_department_with_options(request, runtime)

    async def create_idp_department_async(
        self,
        request: main_models.CreateIdpDepartmentRequest,
    ) -> main_models.CreateIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.create_idp_department_with_options_async(request, runtime)

    def create_private_access_application_with_options(
        self,
        tmp_req: main_models.CreatePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessApplicationResponse:
        tmp_req.validate()
        request = main_models.CreatePrivateAccessApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.l_7config):
            request.l_7config_shrink = Utils.array_to_string_with_specified_style(tmp_req.l_7config, 'L7Config', 'json')
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.address_groups):
            body_flat['AddressGroups'] = request.address_groups
        if not DaraCore.is_null(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not DaraCore.is_null(request.browser_access_status):
            body['BrowserAccessStatus'] = request.browser_access_status
        if not DaraCore.is_null(request.config_mode):
            body['ConfigMode'] = request.config_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.l_7config_shrink):
            body['L7Config'] = request.l_7config_shrink
        if not DaraCore.is_null(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not DaraCore.is_null(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_application_with_options_async(
        self,
        tmp_req: main_models.CreatePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessApplicationResponse:
        tmp_req.validate()
        request = main_models.CreatePrivateAccessApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.l_7config):
            request.l_7config_shrink = Utils.array_to_string_with_specified_style(tmp_req.l_7config, 'L7Config', 'json')
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.address_groups):
            body_flat['AddressGroups'] = request.address_groups
        if not DaraCore.is_null(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not DaraCore.is_null(request.browser_access_status):
            body['BrowserAccessStatus'] = request.browser_access_status
        if not DaraCore.is_null(request.config_mode):
            body['ConfigMode'] = request.config_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.l_7config_shrink):
            body['L7Config'] = request.l_7config_shrink
        if not DaraCore.is_null(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not DaraCore.is_null(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_application(
        self,
        request: main_models.CreatePrivateAccessApplicationRequest,
    ) -> main_models.CreatePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_private_access_application_with_options(request, runtime)

    async def create_private_access_application_async(
        self,
        request: main_models.CreatePrivateAccessApplicationRequest,
    ) -> main_models.CreatePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_private_access_application_with_options_async(request, runtime)

    def create_private_access_policy_with_options(
        self,
        request: main_models.CreatePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not DaraCore.is_null(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not DaraCore.is_null(request.trigger_template_id):
            body['TriggerTemplateId'] = request.trigger_template_id
        if not DaraCore.is_null(request.trusted_process_group_ids):
            body_flat['TrustedProcessGroupIds'] = request.trusted_process_group_ids
        if not DaraCore.is_null(request.trusted_process_status):
            body['TrustedProcessStatus'] = request.trusted_process_status
        if not DaraCore.is_null(request.trusted_software_ids):
            body_flat['TrustedSoftwareIds'] = request.trusted_software_ids
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        if not DaraCore.is_null(request.valid_from):
            body['ValidFrom'] = request.valid_from
        if not DaraCore.is_null(request.valid_time_status):
            body['ValidTimeStatus'] = request.valid_time_status
        if not DaraCore.is_null(request.valid_until):
            body['ValidUntil'] = request.valid_until
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_policy_with_options_async(
        self,
        request: main_models.CreatePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not DaraCore.is_null(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not DaraCore.is_null(request.trigger_template_id):
            body['TriggerTemplateId'] = request.trigger_template_id
        if not DaraCore.is_null(request.trusted_process_group_ids):
            body_flat['TrustedProcessGroupIds'] = request.trusted_process_group_ids
        if not DaraCore.is_null(request.trusted_process_status):
            body['TrustedProcessStatus'] = request.trusted_process_status
        if not DaraCore.is_null(request.trusted_software_ids):
            body_flat['TrustedSoftwareIds'] = request.trusted_software_ids
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        if not DaraCore.is_null(request.valid_from):
            body['ValidFrom'] = request.valid_from
        if not DaraCore.is_null(request.valid_time_status):
            body['ValidTimeStatus'] = request.valid_time_status
        if not DaraCore.is_null(request.valid_until):
            body['ValidUntil'] = request.valid_until
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_policy(
        self,
        request: main_models.CreatePrivateAccessPolicyRequest,
    ) -> main_models.CreatePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_private_access_policy_with_options(request, runtime)

    async def create_private_access_policy_async(
        self,
        request: main_models.CreatePrivateAccessPolicyRequest,
    ) -> main_models.CreatePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_private_access_policy_with_options_async(request, runtime)

    def create_private_access_tag_with_options(
        self,
        request: main_models.CreatePrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_tag_with_options_async(
        self,
        request: main_models.CreatePrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivateAccessTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_tag(
        self,
        request: main_models.CreatePrivateAccessTagRequest,
    ) -> main_models.CreatePrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return self.create_private_access_tag_with_options(request, runtime)

    async def create_private_access_tag_async(
        self,
        request: main_models.CreatePrivateAccessTagRequest,
    ) -> main_models.CreatePrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return await self.create_private_access_tag_with_options_async(request, runtime)

    def create_registration_policy_with_options(
        self,
        tmp_req: main_models.CreateRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistrationPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateRegistrationPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.company_limit_count):
            request.company_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not DaraCore.is_null(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not DaraCore.is_null(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not DaraCore.is_null(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not DaraCore.is_null(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registration_policy_with_options_async(
        self,
        tmp_req: main_models.CreateRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistrationPolicyResponse:
        tmp_req.validate()
        request = main_models.CreateRegistrationPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.company_limit_count):
            request.company_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not DaraCore.is_null(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not DaraCore.is_null(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not DaraCore.is_null(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not DaraCore.is_null(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registration_policy(
        self,
        request: main_models.CreateRegistrationPolicyRequest,
    ) -> main_models.CreateRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_registration_policy_with_options(request, runtime)

    async def create_registration_policy_async(
        self,
        request: main_models.CreateRegistrationPolicyRequest,
    ) -> main_models.CreateRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_registration_policy_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: main_models.CreateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserGroupResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: main_models.CreateUserGroupRequest,
    ) -> main_models.CreateUserGroupResponse:
        runtime = RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: main_models.CreateUserGroupRequest,
    ) -> main_models.CreateUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def create_wm_base_image_with_options(
        self,
        tmp_req: main_models.CreateWmBaseImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmBaseImageResponse:
        tmp_req.validate()
        request = main_models.CreateWmBaseImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_control):
            request.image_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_control, 'ImageControl', 'json')
        query = {}
        if not DaraCore.is_null(request.comment):
            query['comment'] = request.comment
        body = {}
        if not DaraCore.is_null(request.height):
            body['Height'] = request.height
        if not DaraCore.is_null(request.image_control_shrink):
            body['ImageControl'] = request.image_control_shrink
        if not DaraCore.is_null(request.opacity):
            body['Opacity'] = request.opacity
        if not DaraCore.is_null(request.scale):
            body['Scale'] = request.scale
        if not DaraCore.is_null(request.width):
            body['Width'] = request.width
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmBaseImage',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmBaseImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_base_image_with_options_async(
        self,
        tmp_req: main_models.CreateWmBaseImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmBaseImageResponse:
        tmp_req.validate()
        request = main_models.CreateWmBaseImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.image_control):
            request.image_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_control, 'ImageControl', 'json')
        query = {}
        if not DaraCore.is_null(request.comment):
            query['comment'] = request.comment
        body = {}
        if not DaraCore.is_null(request.height):
            body['Height'] = request.height
        if not DaraCore.is_null(request.image_control_shrink):
            body['ImageControl'] = request.image_control_shrink
        if not DaraCore.is_null(request.opacity):
            body['Opacity'] = request.opacity
        if not DaraCore.is_null(request.scale):
            body['Scale'] = request.scale
        if not DaraCore.is_null(request.width):
            body['Width'] = request.width
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmBaseImage',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmBaseImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_base_image(
        self,
        request: main_models.CreateWmBaseImageRequest,
    ) -> main_models.CreateWmBaseImageResponse:
        runtime = RuntimeOptions()
        return self.create_wm_base_image_with_options(request, runtime)

    async def create_wm_base_image_async(
        self,
        request: main_models.CreateWmBaseImageRequest,
    ) -> main_models.CreateWmBaseImageResponse:
        runtime = RuntimeOptions()
        return await self.create_wm_base_image_with_options_async(request, runtime)

    def create_wm_embed_task_with_options(
        self,
        tmp_req: main_models.CreateWmEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmEmbedTaskResponse:
        tmp_req.validate()
        request = main_models.CreateWmEmbedTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audio_control):
            request.audio_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.audio_control, 'AudioControl', 'json')
        if not DaraCore.is_null(tmp_req.csv_control):
            request.csv_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not DaraCore.is_null(tmp_req.document_control):
            request.document_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_control, 'DocumentControl', 'json')
        if not DaraCore.is_null(tmp_req.image_control):
            request.image_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_control, 'ImageControl', 'json')
        if not DaraCore.is_null(tmp_req.video_control):
            request.video_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_control, 'VideoControl', 'json')
        body = {}
        if not DaraCore.is_null(request.audio_control_shrink):
            body['AudioControl'] = request.audio_control_shrink
        if not DaraCore.is_null(request.csv_control_shrink):
            body['CsvControl'] = request.csv_control_shrink
        if not DaraCore.is_null(request.document_control_shrink):
            body['DocumentControl'] = request.document_control_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filename):
            body['Filename'] = request.filename
        if not DaraCore.is_null(request.image_control_shrink):
            body['ImageControl'] = request.image_control_shrink
        if not DaraCore.is_null(request.image_embed_jpeg_quality):
            body['ImageEmbedJpegQuality'] = request.image_embed_jpeg_quality
        if not DaraCore.is_null(request.image_embed_level):
            body['ImageEmbedLevel'] = request.image_embed_level
        if not DaraCore.is_null(request.invisible_enable):
            body['InvisibleEnable'] = request.invisible_enable
        if not DaraCore.is_null(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not DaraCore.is_null(request.video_control_shrink):
            body['VideoControl'] = request.video_control_shrink
        if not DaraCore.is_null(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmEmbedTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmEmbedTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_embed_task_with_options_async(
        self,
        tmp_req: main_models.CreateWmEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmEmbedTaskResponse:
        tmp_req.validate()
        request = main_models.CreateWmEmbedTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.audio_control):
            request.audio_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.audio_control, 'AudioControl', 'json')
        if not DaraCore.is_null(tmp_req.csv_control):
            request.csv_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not DaraCore.is_null(tmp_req.document_control):
            request.document_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.document_control, 'DocumentControl', 'json')
        if not DaraCore.is_null(tmp_req.image_control):
            request.image_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_control, 'ImageControl', 'json')
        if not DaraCore.is_null(tmp_req.video_control):
            request.video_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.video_control, 'VideoControl', 'json')
        body = {}
        if not DaraCore.is_null(request.audio_control_shrink):
            body['AudioControl'] = request.audio_control_shrink
        if not DaraCore.is_null(request.csv_control_shrink):
            body['CsvControl'] = request.csv_control_shrink
        if not DaraCore.is_null(request.document_control_shrink):
            body['DocumentControl'] = request.document_control_shrink
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filename):
            body['Filename'] = request.filename
        if not DaraCore.is_null(request.image_control_shrink):
            body['ImageControl'] = request.image_control_shrink
        if not DaraCore.is_null(request.image_embed_jpeg_quality):
            body['ImageEmbedJpegQuality'] = request.image_embed_jpeg_quality
        if not DaraCore.is_null(request.image_embed_level):
            body['ImageEmbedLevel'] = request.image_embed_level
        if not DaraCore.is_null(request.invisible_enable):
            body['InvisibleEnable'] = request.invisible_enable
        if not DaraCore.is_null(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not DaraCore.is_null(request.video_control_shrink):
            body['VideoControl'] = request.video_control_shrink
        if not DaraCore.is_null(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmEmbedTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmEmbedTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_embed_task(
        self,
        request: main_models.CreateWmEmbedTaskRequest,
    ) -> main_models.CreateWmEmbedTaskResponse:
        runtime = RuntimeOptions()
        return self.create_wm_embed_task_with_options(request, runtime)

    async def create_wm_embed_task_async(
        self,
        request: main_models.CreateWmEmbedTaskRequest,
    ) -> main_models.CreateWmEmbedTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_wm_embed_task_with_options_async(request, runtime)

    def create_wm_extract_task_with_options(
        self,
        tmp_req: main_models.CreateWmExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmExtractTaskResponse:
        tmp_req.validate()
        request = main_models.CreateWmExtractTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.csv_control):
            request.csv_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not DaraCore.is_null(tmp_req.image_extract_params_open_api):
            request.image_extract_params_open_api_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_extract_params_open_api, 'ImageExtractParamsOpenApi', 'json')
        query = {}
        if not DaraCore.is_null(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        if not DaraCore.is_null(request.image_extract_params_open_api_shrink):
            query['ImageExtractParamsOpenApi'] = request.image_extract_params_open_api_shrink
        if not DaraCore.is_null(request.is_client_embed):
            query['IsClientEmbed'] = request.is_client_embed
        body = {}
        if not DaraCore.is_null(request.document_is_capture):
            body['DocumentIsCapture'] = request.document_is_capture
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filename):
            body['Filename'] = request.filename
        if not DaraCore.is_null(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not DaraCore.is_null(request.video_speed):
            body['VideoSpeed'] = request.video_speed
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmExtractTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmExtractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_extract_task_with_options_async(
        self,
        tmp_req: main_models.CreateWmExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmExtractTaskResponse:
        tmp_req.validate()
        request = main_models.CreateWmExtractTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.csv_control):
            request.csv_control_shrink = Utils.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not DaraCore.is_null(tmp_req.image_extract_params_open_api):
            request.image_extract_params_open_api_shrink = Utils.array_to_string_with_specified_style(tmp_req.image_extract_params_open_api, 'ImageExtractParamsOpenApi', 'json')
        query = {}
        if not DaraCore.is_null(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        if not DaraCore.is_null(request.image_extract_params_open_api_shrink):
            query['ImageExtractParamsOpenApi'] = request.image_extract_params_open_api_shrink
        if not DaraCore.is_null(request.is_client_embed):
            query['IsClientEmbed'] = request.is_client_embed
        body = {}
        if not DaraCore.is_null(request.document_is_capture):
            body['DocumentIsCapture'] = request.document_is_capture
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        if not DaraCore.is_null(request.filename):
            body['Filename'] = request.filename
        if not DaraCore.is_null(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not DaraCore.is_null(request.video_speed):
            body['VideoSpeed'] = request.video_speed
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmExtractTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmExtractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_extract_task(
        self,
        request: main_models.CreateWmExtractTaskRequest,
    ) -> main_models.CreateWmExtractTaskResponse:
        runtime = RuntimeOptions()
        return self.create_wm_extract_task_with_options(request, runtime)

    async def create_wm_extract_task_async(
        self,
        request: main_models.CreateWmExtractTaskRequest,
    ) -> main_models.CreateWmExtractTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_wm_extract_task_with_options_async(request, runtime)

    def create_wm_info_mapping_with_options(
        self,
        request: main_models.CreateWmInfoMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmInfoMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmInfoMapping',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmInfoMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_info_mapping_with_options_async(
        self,
        request: main_models.CreateWmInfoMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWmInfoMappingResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not DaraCore.is_null(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not DaraCore.is_null(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateWmInfoMapping',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWmInfoMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_info_mapping(
        self,
        request: main_models.CreateWmInfoMappingRequest,
    ) -> main_models.CreateWmInfoMappingResponse:
        runtime = RuntimeOptions()
        return self.create_wm_info_mapping_with_options(request, runtime)

    async def create_wm_info_mapping_async(
        self,
        request: main_models.CreateWmInfoMappingRequest,
    ) -> main_models.CreateWmInfoMappingResponse:
        runtime = RuntimeOptions()
        return await self.create_wm_info_mapping_with_options_async(request, runtime)

    def delete_approval_processes_with_options(
        self,
        request: main_models.DeleteApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApprovalProcessesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.process_ids):
            body_flat['ProcessIds'] = request.process_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApprovalProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_approval_processes_with_options_async(
        self,
        request: main_models.DeleteApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApprovalProcessesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.process_ids):
            body_flat['ProcessIds'] = request.process_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApprovalProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_approval_processes(
        self,
        request: main_models.DeleteApprovalProcessesRequest,
    ) -> main_models.DeleteApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return self.delete_approval_processes_with_options(request, runtime)

    async def delete_approval_processes_async(
        self,
        request: main_models.DeleteApprovalProcessesRequest,
    ) -> main_models.DeleteApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return await self.delete_approval_processes_with_options_async(request, runtime)

    def delete_client_user_with_options(
        self,
        request: main_models.DeleteClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_user_with_options_async(
        self,
        request: main_models.DeleteClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_user(
        self,
        request: main_models.DeleteClientUserRequest,
    ) -> main_models.DeleteClientUserResponse:
        runtime = RuntimeOptions()
        return self.delete_client_user_with_options(request, runtime)

    async def delete_client_user_async(
        self,
        request: main_models.DeleteClientUserRequest,
    ) -> main_models.DeleteClientUserResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_user_with_options_async(request, runtime)

    def delete_dynamic_route_with_options(
        self,
        request: main_models.DeleteDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_route_with_options_async(
        self,
        request: main_models.DeleteDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicRouteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_route(
        self,
        request: main_models.DeleteDynamicRouteRequest,
    ) -> main_models.DeleteDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.delete_dynamic_route_with_options(request, runtime)

    async def delete_dynamic_route_async(
        self,
        request: main_models.DeleteDynamicRouteRequest,
    ) -> main_models.DeleteDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.delete_dynamic_route_with_options_async(request, runtime)

    def delete_enterprise_accelerate_policy_with_options(
        self,
        request: main_models.DeleteEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseAcceleratePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_accelerate_policy_with_options_async(
        self,
        request: main_models.DeleteEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseAcceleratePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_accelerate_policy(
        self,
        request: main_models.DeleteEnterpriseAcceleratePolicyRequest,
    ) -> main_models.DeleteEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_enterprise_accelerate_policy_with_options(request, runtime)

    async def delete_enterprise_accelerate_policy_async(
        self,
        request: main_models.DeleteEnterpriseAcceleratePolicyRequest,
    ) -> main_models.DeleteEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_enterprise_accelerate_policy_with_options_async(request, runtime)

    def delete_enterprise_accelerate_target_with_options(
        self,
        request: main_models.DeleteEnterpriseAccelerateTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseAccelerateTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        body_flat = {}
        if not DaraCore.is_null(request.target):
            body_flat['Target'] = request.target
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseAccelerateTarget',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseAccelerateTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_accelerate_target_with_options_async(
        self,
        request: main_models.DeleteEnterpriseAccelerateTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseAccelerateTargetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        body_flat = {}
        if not DaraCore.is_null(request.target):
            body_flat['Target'] = request.target
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterpriseAccelerateTarget',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseAccelerateTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise_accelerate_target(
        self,
        request: main_models.DeleteEnterpriseAccelerateTargetRequest,
    ) -> main_models.DeleteEnterpriseAccelerateTargetResponse:
        runtime = RuntimeOptions()
        return self.delete_enterprise_accelerate_target_with_options(request, runtime)

    async def delete_enterprise_accelerate_target_async(
        self,
        request: main_models.DeleteEnterpriseAccelerateTargetRequest,
    ) -> main_models.DeleteEnterpriseAccelerateTargetResponse:
        runtime = RuntimeOptions()
        return await self.delete_enterprise_accelerate_target_with_options_async(request, runtime)

    def delete_idp_department_with_options(
        self,
        request: main_models.DeleteIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_idp_department_with_options_async(
        self,
        request: main_models.DeleteIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_idp_department(
        self,
        request: main_models.DeleteIdpDepartmentRequest,
    ) -> main_models.DeleteIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return self.delete_idp_department_with_options(request, runtime)

    async def delete_idp_department_async(
        self,
        request: main_models.DeleteIdpDepartmentRequest,
    ) -> main_models.DeleteIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_idp_department_with_options_async(request, runtime)

    def delete_otp_config_with_options(
        self,
        request: main_models.DeleteOtpConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOtpConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOtpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOtpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_otp_config_with_options_async(
        self,
        request: main_models.DeleteOtpConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOtpConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOtpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOtpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_otp_config(
        self,
        request: main_models.DeleteOtpConfigRequest,
    ) -> main_models.DeleteOtpConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_otp_config_with_options(request, runtime)

    async def delete_otp_config_async(
        self,
        request: main_models.DeleteOtpConfigRequest,
    ) -> main_models.DeleteOtpConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_otp_config_with_options_async(request, runtime)

    def delete_private_access_application_with_options(
        self,
        request: main_models.DeletePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_application_with_options_async(
        self,
        request: main_models.DeletePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessApplicationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_application(
        self,
        request: main_models.DeletePrivateAccessApplicationRequest,
    ) -> main_models.DeletePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_private_access_application_with_options(request, runtime)

    async def delete_private_access_application_async(
        self,
        request: main_models.DeletePrivateAccessApplicationRequest,
    ) -> main_models.DeletePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_access_application_with_options_async(request, runtime)

    def delete_private_access_policy_with_options(
        self,
        request: main_models.DeletePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_policy_with_options_async(
        self,
        request: main_models.DeletePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_policy(
        self,
        request: main_models.DeletePrivateAccessPolicyRequest,
    ) -> main_models.DeletePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_private_access_policy_with_options(request, runtime)

    async def delete_private_access_policy_async(
        self,
        request: main_models.DeletePrivateAccessPolicyRequest,
    ) -> main_models.DeletePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_access_policy_with_options_async(request, runtime)

    def delete_private_access_tag_with_options(
        self,
        request: main_models.DeletePrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_tag_with_options_async(
        self,
        request: main_models.DeletePrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivateAccessTagResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_tag(
        self,
        request: main_models.DeletePrivateAccessTagRequest,
    ) -> main_models.DeletePrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return self.delete_private_access_tag_with_options(request, runtime)

    async def delete_private_access_tag_async(
        self,
        request: main_models.DeletePrivateAccessTagRequest,
    ) -> main_models.DeletePrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_private_access_tag_with_options_async(request, runtime)

    def delete_registration_policies_with_options(
        self,
        request: main_models.DeleteRegistrationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistrationPoliciesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.policy_ids):
            body_flat['PolicyIds'] = request.policy_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistrationPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registration_policies_with_options_async(
        self,
        request: main_models.DeleteRegistrationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistrationPoliciesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.policy_ids):
            body_flat['PolicyIds'] = request.policy_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistrationPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registration_policies(
        self,
        request: main_models.DeleteRegistrationPoliciesRequest,
    ) -> main_models.DeleteRegistrationPoliciesResponse:
        runtime = RuntimeOptions()
        return self.delete_registration_policies_with_options(request, runtime)

    async def delete_registration_policies_async(
        self,
        request: main_models.DeleteRegistrationPoliciesRequest,
    ) -> main_models.DeleteRegistrationPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.delete_registration_policies_with_options_async(request, runtime)

    def delete_user_devices_with_options(
        self,
        request: main_models.DeleteUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDevicesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_devices_with_options_async(
        self,
        request: main_models.DeleteUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserDevicesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_devices(
        self,
        request: main_models.DeleteUserDevicesRequest,
    ) -> main_models.DeleteUserDevicesResponse:
        runtime = RuntimeOptions()
        return self.delete_user_devices_with_options(request, runtime)

    async def delete_user_devices_async(
        self,
        request: main_models.DeleteUserDevicesRequest,
    ) -> main_models.DeleteUserDevicesResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_devices_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: main_models.DeleteUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: main_models.DeleteUserGroupRequest,
    ) -> main_models.DeleteUserGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: main_models.DeleteUserGroupRequest,
    ) -> main_models.DeleteUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def detach_application_2connector_with_options(
        self,
        tmp_req: main_models.DetachApplication2ConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachApplication2ConnectorResponse:
        tmp_req.validate()
        request = main_models.DetachApplication2ConnectorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_ids):
            request.application_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not DaraCore.is_null(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not DaraCore.is_null(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachApplication2Connector',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_application_2connector_with_options_async(
        self,
        tmp_req: main_models.DetachApplication2ConnectorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachApplication2ConnectorResponse:
        tmp_req.validate()
        request = main_models.DetachApplication2ConnectorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_ids):
            request.application_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not DaraCore.is_null(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not DaraCore.is_null(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachApplication2Connector',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_application_2connector(
        self,
        request: main_models.DetachApplication2ConnectorRequest,
    ) -> main_models.DetachApplication2ConnectorResponse:
        runtime = RuntimeOptions()
        return self.detach_application_2connector_with_options(request, runtime)

    async def detach_application_2connector_async(
        self,
        request: main_models.DetachApplication2ConnectorRequest,
    ) -> main_models.DetachApplication2ConnectorResponse:
        runtime = RuntimeOptions()
        return await self.detach_application_2connector_with_options_async(request, runtime)

    def detach_policy_2approval_process_with_options(
        self,
        request: main_models.DetachPolicy2ApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicy2ApprovalProcessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy2ApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicy2ApprovalProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_2approval_process_with_options_async(
        self,
        request: main_models.DetachPolicy2ApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachPolicy2ApprovalProcessResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DetachPolicy2ApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachPolicy2ApprovalProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy_2approval_process(
        self,
        request: main_models.DetachPolicy2ApprovalProcessRequest,
    ) -> main_models.DetachPolicy2ApprovalProcessResponse:
        runtime = RuntimeOptions()
        return self.detach_policy_2approval_process_with_options(request, runtime)

    async def detach_policy_2approval_process_async(
        self,
        request: main_models.DetachPolicy2ApprovalProcessRequest,
    ) -> main_models.DetachPolicy2ApprovalProcessResponse:
        runtime = RuntimeOptions()
        return await self.detach_policy_2approval_process_with_options_async(request, runtime)

    def disable_enterprise_accelerate_policy_with_options(
        self,
        request: main_models.DisableEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEnterpriseAcceleratePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_enterprise_accelerate_policy_with_options_async(
        self,
        request: main_models.DisableEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEnterpriseAcceleratePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_enterprise_accelerate_policy(
        self,
        request: main_models.DisableEnterpriseAcceleratePolicyRequest,
    ) -> main_models.DisableEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return self.disable_enterprise_accelerate_policy_with_options(request, runtime)

    async def disable_enterprise_accelerate_policy_async(
        self,
        request: main_models.DisableEnterpriseAcceleratePolicyRequest,
    ) -> main_models.DisableEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return await self.disable_enterprise_accelerate_policy_with_options_async(request, runtime)

    def enable_enterprise_accelerate_policy_with_options(
        self,
        request: main_models.EnableEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEnterpriseAcceleratePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_enterprise_accelerate_policy_with_options_async(
        self,
        request: main_models.EnableEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEnterpriseAcceleratePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_enterprise_accelerate_policy(
        self,
        request: main_models.EnableEnterpriseAcceleratePolicyRequest,
    ) -> main_models.EnableEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return self.enable_enterprise_accelerate_policy_with_options(request, runtime)

    async def enable_enterprise_accelerate_policy_async(
        self,
        request: main_models.EnableEnterpriseAcceleratePolicyRequest,
    ) -> main_models.EnableEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return await self.enable_enterprise_accelerate_policy_with_options_async(request, runtime)

    def export_user_devices_with_options(
        self,
        request: main_models.ExportUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportUserDevicesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.app_statuses):
            body_flat['AppStatuses'] = request.app_statuses
        if not DaraCore.is_null(request.department):
            body['Department'] = request.department
        if not DaraCore.is_null(request.device_belong):
            body['DeviceBelong'] = request.device_belong
        if not DaraCore.is_null(request.device_statuses):
            body_flat['DeviceStatuses'] = request.device_statuses
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not DaraCore.is_null(request.device_types):
            body_flat['DeviceTypes'] = request.device_types
        if not DaraCore.is_null(request.dlp_statuses):
            body_flat['DlpStatuses'] = request.dlp_statuses
        if not DaraCore.is_null(request.hostname):
            body['Hostname'] = request.hostname
        if not DaraCore.is_null(request.ia_statuses):
            body_flat['IaStatuses'] = request.ia_statuses
        if not DaraCore.is_null(request.mac):
            body['Mac'] = request.mac
        if not DaraCore.is_null(request.nac_statuses):
            body_flat['NacStatuses'] = request.nac_statuses
        if not DaraCore.is_null(request.pa_statuses):
            body_flat['PaStatuses'] = request.pa_statuses
        if not DaraCore.is_null(request.sase_user_id):
            body['SaseUserId'] = request.sase_user_id
        if not DaraCore.is_null(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_user_devices_with_options_async(
        self,
        request: main_models.ExportUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportUserDevicesResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.app_statuses):
            body_flat['AppStatuses'] = request.app_statuses
        if not DaraCore.is_null(request.department):
            body['Department'] = request.department
        if not DaraCore.is_null(request.device_belong):
            body['DeviceBelong'] = request.device_belong
        if not DaraCore.is_null(request.device_statuses):
            body_flat['DeviceStatuses'] = request.device_statuses
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not DaraCore.is_null(request.device_types):
            body_flat['DeviceTypes'] = request.device_types
        if not DaraCore.is_null(request.dlp_statuses):
            body_flat['DlpStatuses'] = request.dlp_statuses
        if not DaraCore.is_null(request.hostname):
            body['Hostname'] = request.hostname
        if not DaraCore.is_null(request.ia_statuses):
            body_flat['IaStatuses'] = request.ia_statuses
        if not DaraCore.is_null(request.mac):
            body['Mac'] = request.mac
        if not DaraCore.is_null(request.nac_statuses):
            body_flat['NacStatuses'] = request.nac_statuses
        if not DaraCore.is_null(request.pa_statuses):
            body_flat['PaStatuses'] = request.pa_statuses
        if not DaraCore.is_null(request.sase_user_id):
            body['SaseUserId'] = request.sase_user_id
        if not DaraCore.is_null(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_user_devices(
        self,
        request: main_models.ExportUserDevicesRequest,
    ) -> main_models.ExportUserDevicesResponse:
        runtime = RuntimeOptions()
        return self.export_user_devices_with_options(request, runtime)

    async def export_user_devices_async(
        self,
        request: main_models.ExportUserDevicesRequest,
    ) -> main_models.ExportUserDevicesResponse:
        runtime = RuntimeOptions()
        return await self.export_user_devices_with_options_async(request, runtime)

    def get_active_idp_config_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetActiveIdpConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetActiveIdpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetActiveIdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_active_idp_config_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetActiveIdpConfigResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetActiveIdpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetActiveIdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_active_idp_config(self) -> main_models.GetActiveIdpConfigResponse:
        runtime = RuntimeOptions()
        return self.get_active_idp_config_with_options(runtime)

    async def get_active_idp_config_async(self) -> main_models.GetActiveIdpConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_active_idp_config_with_options_async(runtime)

    def get_approval_with_options(
        self,
        request: main_models.GetApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApproval',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_approval_with_options_async(
        self,
        request: main_models.GetApprovalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApproval',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_approval(
        self,
        request: main_models.GetApprovalRequest,
    ) -> main_models.GetApprovalResponse:
        runtime = RuntimeOptions()
        return self.get_approval_with_options(request, runtime)

    async def get_approval_async(
        self,
        request: main_models.GetApprovalRequest,
    ) -> main_models.GetApprovalResponse:
        runtime = RuntimeOptions()
        return await self.get_approval_with_options_async(request, runtime)

    def get_approval_process_with_options(
        self,
        request: main_models.GetApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalProcessResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_approval_process_with_options_async(
        self,
        request: main_models.GetApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalProcessResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_approval_process(
        self,
        request: main_models.GetApprovalProcessRequest,
    ) -> main_models.GetApprovalProcessResponse:
        runtime = RuntimeOptions()
        return self.get_approval_process_with_options(request, runtime)

    async def get_approval_process_async(
        self,
        request: main_models.GetApprovalProcessRequest,
    ) -> main_models.GetApprovalProcessResponse:
        runtime = RuntimeOptions()
        return await self.get_approval_process_with_options_async(request, runtime)

    def get_approval_schema_with_options(
        self,
        request: main_models.GetApprovalSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApprovalSchema',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_approval_schema_with_options_async(
        self,
        request: main_models.GetApprovalSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApprovalSchemaResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApprovalSchema',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApprovalSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_approval_schema(
        self,
        request: main_models.GetApprovalSchemaRequest,
    ) -> main_models.GetApprovalSchemaResponse:
        runtime = RuntimeOptions()
        return self.get_approval_schema_with_options(request, runtime)

    async def get_approval_schema_async(
        self,
        request: main_models.GetApprovalSchemaRequest,
    ) -> main_models.GetApprovalSchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_approval_schema_with_options_async(request, runtime)

    def get_boot_and_anti_uninstall_policy_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetBootAndAntiUninstallPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetBootAndAntiUninstallPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBootAndAntiUninstallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_boot_and_anti_uninstall_policy_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetBootAndAntiUninstallPolicyResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetBootAndAntiUninstallPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBootAndAntiUninstallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_boot_and_anti_uninstall_policy(self) -> main_models.GetBootAndAntiUninstallPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_boot_and_anti_uninstall_policy_with_options(runtime)

    async def get_boot_and_anti_uninstall_policy_async(self) -> main_models.GetBootAndAntiUninstallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_boot_and_anti_uninstall_policy_with_options_async(runtime)

    def get_client_user_with_options(
        self,
        request: main_models.GetClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientUserResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_user_with_options_async(
        self,
        request: main_models.GetClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClientUserResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_user(
        self,
        request: main_models.GetClientUserRequest,
    ) -> main_models.GetClientUserResponse:
        runtime = RuntimeOptions()
        return self.get_client_user_with_options(request, runtime)

    async def get_client_user_async(
        self,
        request: main_models.GetClientUserRequest,
    ) -> main_models.GetClientUserResponse:
        runtime = RuntimeOptions()
        return await self.get_client_user_with_options_async(request, runtime)

    def get_dynamic_route_with_options(
        self,
        request: main_models.GetDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dynamic_route_with_options_async(
        self,
        request: main_models.GetDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dynamic_route(
        self,
        request: main_models.GetDynamicRouteRequest,
    ) -> main_models.GetDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.get_dynamic_route_with_options(request, runtime)

    async def get_dynamic_route_async(
        self,
        request: main_models.GetDynamicRouteRequest,
    ) -> main_models.GetDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.get_dynamic_route_with_options_async(request, runtime)

    def get_idp_config_with_options(
        self,
        request: main_models.GetIdpConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdpConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_idp_config_with_options_async(
        self,
        request: main_models.GetIdpConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIdpConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIdpConfig',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_idp_config(
        self,
        request: main_models.GetIdpConfigRequest,
    ) -> main_models.GetIdpConfigResponse:
        runtime = RuntimeOptions()
        return self.get_idp_config_with_options(request, runtime)

    async def get_idp_config_async(
        self,
        request: main_models.GetIdpConfigRequest,
    ) -> main_models.GetIdpConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_idp_config_with_options_async(request, runtime)

    def get_private_access_application_with_options(
        self,
        request: main_models.GetPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_application_with_options_async(
        self,
        request: main_models.GetPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_application(
        self,
        request: main_models.GetPrivateAccessApplicationRequest,
    ) -> main_models.GetPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_private_access_application_with_options(request, runtime)

    async def get_private_access_application_async(
        self,
        request: main_models.GetPrivateAccessApplicationRequest,
    ) -> main_models.GetPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_private_access_application_with_options_async(request, runtime)

    def get_private_access_policy_with_options(
        self,
        request: main_models.GetPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_policy_with_options_async(
        self,
        request: main_models.GetPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_policy(
        self,
        request: main_models.GetPrivateAccessPolicyRequest,
    ) -> main_models.GetPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_private_access_policy_with_options(request, runtime)

    async def get_private_access_policy_async(
        self,
        request: main_models.GetPrivateAccessPolicyRequest,
    ) -> main_models.GetPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_private_access_policy_with_options_async(request, runtime)

    def get_registration_policy_with_options(
        self,
        request: main_models.GetRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistrationPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registration_policy_with_options_async(
        self,
        request: main_models.GetRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistrationPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registration_policy(
        self,
        request: main_models.GetRegistrationPolicyRequest,
    ) -> main_models.GetRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_registration_policy_with_options(request, runtime)

    async def get_registration_policy_async(
        self,
        request: main_models.GetRegistrationPolicyRequest,
    ) -> main_models.GetRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_registration_policy_with_options_async(request, runtime)

    def get_user_device_with_options(
        self,
        request: main_models.GetUserDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserDeviceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserDevice',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_device_with_options_async(
        self,
        request: main_models.GetUserDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserDeviceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserDevice',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_device(
        self,
        request: main_models.GetUserDeviceRequest,
    ) -> main_models.GetUserDeviceResponse:
        runtime = RuntimeOptions()
        return self.get_user_device_with_options(request, runtime)

    async def get_user_device_async(
        self,
        request: main_models.GetUserDeviceRequest,
    ) -> main_models.GetUserDeviceResponse:
        runtime = RuntimeOptions()
        return await self.get_user_device_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: main_models.GetUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: main_models.GetUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group(
        self,
        request: main_models.GetUserGroupRequest,
    ) -> main_models.GetUserGroupResponse:
        runtime = RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: main_models.GetUserGroupRequest,
    ) -> main_models.GetUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def get_wm_embed_task_with_options(
        self,
        request: main_models.GetWmEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWmEmbedTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWmEmbedTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWmEmbedTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_wm_embed_task_with_options_async(
        self,
        request: main_models.GetWmEmbedTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWmEmbedTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWmEmbedTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWmEmbedTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_wm_embed_task(
        self,
        request: main_models.GetWmEmbedTaskRequest,
    ) -> main_models.GetWmEmbedTaskResponse:
        runtime = RuntimeOptions()
        return self.get_wm_embed_task_with_options(request, runtime)

    async def get_wm_embed_task_async(
        self,
        request: main_models.GetWmEmbedTaskRequest,
    ) -> main_models.GetWmEmbedTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_wm_embed_task_with_options_async(request, runtime)

    def get_wm_extract_task_with_options(
        self,
        request: main_models.GetWmExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWmExtractTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWmExtractTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWmExtractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_wm_extract_task_with_options_async(
        self,
        request: main_models.GetWmExtractTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWmExtractTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWmExtractTask',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWmExtractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_wm_extract_task(
        self,
        request: main_models.GetWmExtractTaskRequest,
    ) -> main_models.GetWmExtractTaskResponse:
        runtime = RuntimeOptions()
        return self.get_wm_extract_task_with_options(request, runtime)

    async def get_wm_extract_task_async(
        self,
        request: main_models.GetWmExtractTaskRequest,
    ) -> main_models.GetWmExtractTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_wm_extract_task_with_options_async(request, runtime)

    def import_enterprise_accelerate_targets_with_options(
        self,
        request: main_models.ImportEnterpriseAccelerateTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportEnterpriseAccelerateTargetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportEnterpriseAccelerateTargets',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportEnterpriseAccelerateTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_enterprise_accelerate_targets_with_options_async(
        self,
        request: main_models.ImportEnterpriseAccelerateTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportEnterpriseAccelerateTargetsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        if not DaraCore.is_null(request.file_url):
            body['FileUrl'] = request.file_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ImportEnterpriseAccelerateTargets',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportEnterpriseAccelerateTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_enterprise_accelerate_targets(
        self,
        request: main_models.ImportEnterpriseAccelerateTargetsRequest,
    ) -> main_models.ImportEnterpriseAccelerateTargetsResponse:
        runtime = RuntimeOptions()
        return self.import_enterprise_accelerate_targets_with_options(request, runtime)

    async def import_enterprise_accelerate_targets_async(
        self,
        request: main_models.ImportEnterpriseAccelerateTargetsRequest,
    ) -> main_models.ImportEnterpriseAccelerateTargetsResponse:
        runtime = RuntimeOptions()
        return await self.import_enterprise_accelerate_targets_with_options_async(request, runtime)

    def list_applications_for_private_access_policy_with_options(
        self,
        request: main_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_policy_with_options_async(
        self,
        request: main_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_policy(
        self,
        request: main_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> main_models.ListApplicationsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_private_access_policy_with_options(request, runtime)

    async def list_applications_for_private_access_policy_async(
        self,
        request: main_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> main_models.ListApplicationsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_private_access_policy_with_options_async(request, runtime)

    def list_applications_for_private_access_tag_with_options(
        self,
        request: main_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForPrivateAccessTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForPrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_tag_with_options_async(
        self,
        request: main_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsForPrivateAccessTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationsForPrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_tag(
        self,
        request: main_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> main_models.ListApplicationsForPrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return self.list_applications_for_private_access_tag_with_options(request, runtime)

    async def list_applications_for_private_access_tag_async(
        self,
        request: main_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> main_models.ListApplicationsForPrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_for_private_access_tag_with_options_async(request, runtime)

    def list_approval_processes_with_options(
        self,
        request: main_models.ListApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approval_processes_with_options_async(
        self,
        request: main_models.ListApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approval_processes(
        self,
        request: main_models.ListApprovalProcessesRequest,
    ) -> main_models.ListApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return self.list_approval_processes_with_options(request, runtime)

    async def list_approval_processes_async(
        self,
        request: main_models.ListApprovalProcessesRequest,
    ) -> main_models.ListApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return await self.list_approval_processes_with_options_async(request, runtime)

    def list_approval_processes_for_approval_schemas_with_options(
        self,
        request: main_models.ListApprovalProcessesForApprovalSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalProcessesForApprovalSchemasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalProcessesForApprovalSchemas',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalProcessesForApprovalSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approval_processes_for_approval_schemas_with_options_async(
        self,
        request: main_models.ListApprovalProcessesForApprovalSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalProcessesForApprovalSchemasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalProcessesForApprovalSchemas',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalProcessesForApprovalSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approval_processes_for_approval_schemas(
        self,
        request: main_models.ListApprovalProcessesForApprovalSchemasRequest,
    ) -> main_models.ListApprovalProcessesForApprovalSchemasResponse:
        runtime = RuntimeOptions()
        return self.list_approval_processes_for_approval_schemas_with_options(request, runtime)

    async def list_approval_processes_for_approval_schemas_async(
        self,
        request: main_models.ListApprovalProcessesForApprovalSchemasRequest,
    ) -> main_models.ListApprovalProcessesForApprovalSchemasResponse:
        runtime = RuntimeOptions()
        return await self.list_approval_processes_for_approval_schemas_with_options_async(request, runtime)

    def list_approval_schemas_with_options(
        self,
        request: main_models.ListApprovalSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalSchemasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalSchemas',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approval_schemas_with_options_async(
        self,
        request: main_models.ListApprovalSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalSchemasResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalSchemas',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approval_schemas(
        self,
        request: main_models.ListApprovalSchemasRequest,
    ) -> main_models.ListApprovalSchemasResponse:
        runtime = RuntimeOptions()
        return self.list_approval_schemas_with_options(request, runtime)

    async def list_approval_schemas_async(
        self,
        request: main_models.ListApprovalSchemasRequest,
    ) -> main_models.ListApprovalSchemasResponse:
        runtime = RuntimeOptions()
        return await self.list_approval_schemas_with_options_async(request, runtime)

    def list_approval_schemas_for_approval_processes_with_options(
        self,
        request: main_models.ListApprovalSchemasForApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalSchemasForApprovalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalSchemasForApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalSchemasForApprovalProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approval_schemas_for_approval_processes_with_options_async(
        self,
        request: main_models.ListApprovalSchemasForApprovalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalSchemasForApprovalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovalSchemasForApprovalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalSchemasForApprovalProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approval_schemas_for_approval_processes(
        self,
        request: main_models.ListApprovalSchemasForApprovalProcessesRequest,
    ) -> main_models.ListApprovalSchemasForApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return self.list_approval_schemas_for_approval_processes_with_options(request, runtime)

    async def list_approval_schemas_for_approval_processes_async(
        self,
        request: main_models.ListApprovalSchemasForApprovalProcessesRequest,
    ) -> main_models.ListApprovalSchemasForApprovalProcessesResponse:
        runtime = RuntimeOptions()
        return await self.list_approval_schemas_for_approval_processes_with_options_async(request, runtime)

    def list_approvals_with_options(
        self,
        request: main_models.ListApprovalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovals',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_approvals_with_options_async(
        self,
        request: main_models.ListApprovalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApprovalsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApprovals',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApprovalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_approvals(
        self,
        request: main_models.ListApprovalsRequest,
    ) -> main_models.ListApprovalsResponse:
        runtime = RuntimeOptions()
        return self.list_approvals_with_options(request, runtime)

    async def list_approvals_async(
        self,
        request: main_models.ListApprovalsRequest,
    ) -> main_models.ListApprovalsResponse:
        runtime = RuntimeOptions()
        return await self.list_approvals_with_options_async(request, runtime)

    def list_client_users_with_options(
        self,
        request: main_models.ListClientUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientUsers',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_users_with_options_async(
        self,
        request: main_models.ListClientUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientUsers',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_users(
        self,
        request: main_models.ListClientUsersRequest,
    ) -> main_models.ListClientUsersResponse:
        runtime = RuntimeOptions()
        return self.list_client_users_with_options(request, runtime)

    async def list_client_users_async(
        self,
        request: main_models.ListClientUsersRequest,
    ) -> main_models.ListClientUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_client_users_with_options_async(request, runtime)

    def list_connectors_with_options(
        self,
        request: main_models.ListConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectorsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnectors',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connectors_with_options_async(
        self,
        request: main_models.ListConnectorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListConnectorsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListConnectors',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connectors(
        self,
        request: main_models.ListConnectorsRequest,
    ) -> main_models.ListConnectorsResponse:
        runtime = RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    async def list_connectors_async(
        self,
        request: main_models.ListConnectorsRequest,
    ) -> main_models.ListConnectorsResponse:
        runtime = RuntimeOptions()
        return await self.list_connectors_with_options_async(request, runtime)

    def list_dynamic_disposal_processes_with_options(
        self,
        request: main_models.ListDynamicDisposalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicDisposalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicDisposalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicDisposalProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_disposal_processes_with_options_async(
        self,
        request: main_models.ListDynamicDisposalProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicDisposalProcessesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicDisposalProcesses',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicDisposalProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_disposal_processes(
        self,
        request: main_models.ListDynamicDisposalProcessesRequest,
    ) -> main_models.ListDynamicDisposalProcessesResponse:
        runtime = RuntimeOptions()
        return self.list_dynamic_disposal_processes_with_options(request, runtime)

    async def list_dynamic_disposal_processes_async(
        self,
        request: main_models.ListDynamicDisposalProcessesRequest,
    ) -> main_models.ListDynamicDisposalProcessesResponse:
        runtime = RuntimeOptions()
        return await self.list_dynamic_disposal_processes_with_options_async(request, runtime)

    def list_dynamic_route_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicRouteRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListDynamicRouteRegions',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicRouteRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_route_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicRouteRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListDynamicRouteRegions',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicRouteRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_route_regions(self) -> main_models.ListDynamicRouteRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_dynamic_route_regions_with_options(runtime)

    async def list_dynamic_route_regions_async(self) -> main_models.ListDynamicRouteRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_dynamic_route_regions_with_options_async(runtime)

    def list_dynamic_routes_with_options(
        self,
        request: main_models.ListDynamicRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicRoutesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicRoutes',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_routes_with_options_async(
        self,
        request: main_models.ListDynamicRoutesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDynamicRoutesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDynamicRoutes',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDynamicRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_routes(
        self,
        request: main_models.ListDynamicRoutesRequest,
    ) -> main_models.ListDynamicRoutesResponse:
        runtime = RuntimeOptions()
        return self.list_dynamic_routes_with_options(request, runtime)

    async def list_dynamic_routes_async(
        self,
        request: main_models.ListDynamicRoutesRequest,
    ) -> main_models.ListDynamicRoutesResponse:
        runtime = RuntimeOptions()
        return await self.list_dynamic_routes_with_options_async(request, runtime)

    def list_enterprise_accelerate_logs_with_options(
        self,
        request: main_models.ListEnterpriseAccelerateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAccelerateLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAccelerateLogs',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAccelerateLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_accelerate_logs_with_options_async(
        self,
        request: main_models.ListEnterpriseAccelerateLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAccelerateLogsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAccelerateLogs',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAccelerateLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_accelerate_logs(
        self,
        request: main_models.ListEnterpriseAccelerateLogsRequest,
    ) -> main_models.ListEnterpriseAccelerateLogsResponse:
        runtime = RuntimeOptions()
        return self.list_enterprise_accelerate_logs_with_options(request, runtime)

    async def list_enterprise_accelerate_logs_async(
        self,
        request: main_models.ListEnterpriseAccelerateLogsRequest,
    ) -> main_models.ListEnterpriseAccelerateLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_enterprise_accelerate_logs_with_options_async(request, runtime)

    def list_enterprise_accelerate_policies_with_options(
        self,
        request: main_models.ListEnterpriseAcceleratePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAcceleratePoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAcceleratePolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAcceleratePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_accelerate_policies_with_options_async(
        self,
        request: main_models.ListEnterpriseAcceleratePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAcceleratePoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAcceleratePolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAcceleratePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_accelerate_policies(
        self,
        request: main_models.ListEnterpriseAcceleratePoliciesRequest,
    ) -> main_models.ListEnterpriseAcceleratePoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_enterprise_accelerate_policies_with_options(request, runtime)

    async def list_enterprise_accelerate_policies_async(
        self,
        request: main_models.ListEnterpriseAcceleratePoliciesRequest,
    ) -> main_models.ListEnterpriseAcceleratePoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_enterprise_accelerate_policies_with_options_async(request, runtime)

    def list_enterprise_accelerate_targets_with_options(
        self,
        request: main_models.ListEnterpriseAccelerateTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAccelerateTargetsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAccelerateTargets',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAccelerateTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprise_accelerate_targets_with_options_async(
        self,
        request: main_models.ListEnterpriseAccelerateTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterpriseAccelerateTargetsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterpriseAccelerateTargets',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterpriseAccelerateTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprise_accelerate_targets(
        self,
        request: main_models.ListEnterpriseAccelerateTargetsRequest,
    ) -> main_models.ListEnterpriseAccelerateTargetsResponse:
        runtime = RuntimeOptions()
        return self.list_enterprise_accelerate_targets_with_options(request, runtime)

    async def list_enterprise_accelerate_targets_async(
        self,
        request: main_models.ListEnterpriseAccelerateTargetsRequest,
    ) -> main_models.ListEnterpriseAccelerateTargetsResponse:
        runtime = RuntimeOptions()
        return await self.list_enterprise_accelerate_targets_with_options_async(request, runtime)

    def list_excessive_device_registration_applications_with_options(
        self,
        request: main_models.ListExcessiveDeviceRegistrationApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExcessiveDeviceRegistrationApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExcessiveDeviceRegistrationApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_excessive_device_registration_applications_with_options_async(
        self,
        request: main_models.ListExcessiveDeviceRegistrationApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExcessiveDeviceRegistrationApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExcessiveDeviceRegistrationApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_excessive_device_registration_applications(
        self,
        request: main_models.ListExcessiveDeviceRegistrationApplicationsRequest,
    ) -> main_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_excessive_device_registration_applications_with_options(request, runtime)

    async def list_excessive_device_registration_applications_async(
        self,
        request: main_models.ListExcessiveDeviceRegistrationApplicationsRequest,
    ) -> main_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_excessive_device_registration_applications_with_options_async(request, runtime)

    def list_idp_configs_with_options(
        self,
        request: main_models.ListIdpConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdpConfigsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdpConfigs',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdpConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_idp_configs_with_options_async(
        self,
        request: main_models.ListIdpConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdpConfigsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdpConfigs',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdpConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_idp_configs(
        self,
        request: main_models.ListIdpConfigsRequest,
    ) -> main_models.ListIdpConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_idp_configs_with_options(request, runtime)

    async def list_idp_configs_async(
        self,
        request: main_models.ListIdpConfigsRequest,
    ) -> main_models.ListIdpConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_idp_configs_with_options_async(request, runtime)

    def list_idp_departments_with_options(
        self,
        request: main_models.ListIdpDepartmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdpDepartmentsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdpDepartments',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdpDepartmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_idp_departments_with_options_async(
        self,
        request: main_models.ListIdpDepartmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIdpDepartmentsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIdpDepartments',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIdpDepartmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_idp_departments(
        self,
        request: main_models.ListIdpDepartmentsRequest,
    ) -> main_models.ListIdpDepartmentsResponse:
        runtime = RuntimeOptions()
        return self.list_idp_departments_with_options(request, runtime)

    async def list_idp_departments_async(
        self,
        request: main_models.ListIdpDepartmentsRequest,
    ) -> main_models.ListIdpDepartmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_idp_departments_with_options_async(request, runtime)

    def list_nac_user_cert_with_options(
        self,
        request: main_models.ListNacUserCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacUserCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacUserCert',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacUserCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nac_user_cert_with_options_async(
        self,
        request: main_models.ListNacUserCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNacUserCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.device_type):
            query['DeviceType'] = request.device_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNacUserCert',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNacUserCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nac_user_cert(
        self,
        request: main_models.ListNacUserCertRequest,
    ) -> main_models.ListNacUserCertResponse:
        runtime = RuntimeOptions()
        return self.list_nac_user_cert_with_options(request, runtime)

    async def list_nac_user_cert_async(
        self,
        request: main_models.ListNacUserCertRequest,
    ) -> main_models.ListNacUserCertResponse:
        runtime = RuntimeOptions()
        return await self.list_nac_user_cert_with_options_async(request, runtime)

    def list_polices_for_private_access_application_with_options(
        self,
        request: main_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_application_with_options_async(
        self,
        request: main_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_application(
        self,
        request: main_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> main_models.ListPolicesForPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_polices_for_private_access_application_with_options(request, runtime)

    async def list_polices_for_private_access_application_async(
        self,
        request: main_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> main_models.ListPolicesForPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_polices_for_private_access_application_with_options_async(request, runtime)

    def list_polices_for_private_access_tag_with_options(
        self,
        request: main_models.ListPolicesForPrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForPrivateAccessTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForPrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_tag_with_options_async(
        self,
        request: main_models.ListPolicesForPrivateAccessTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForPrivateAccessTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForPrivateAccessTag',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_tag(
        self,
        request: main_models.ListPolicesForPrivateAccessTagRequest,
    ) -> main_models.ListPolicesForPrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return self.list_polices_for_private_access_tag_with_options(request, runtime)

    async def list_polices_for_private_access_tag_async(
        self,
        request: main_models.ListPolicesForPrivateAccessTagRequest,
    ) -> main_models.ListPolicesForPrivateAccessTagResponse:
        runtime = RuntimeOptions()
        return await self.list_polices_for_private_access_tag_with_options_async(request, runtime)

    def list_polices_for_user_group_with_options(
        self,
        request: main_models.ListPolicesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_user_group_with_options_async(
        self,
        request: main_models.ListPolicesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPolicesForUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicesForUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPolicesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_user_group(
        self,
        request: main_models.ListPolicesForUserGroupRequest,
    ) -> main_models.ListPolicesForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_polices_for_user_group_with_options(request, runtime)

    async def list_polices_for_user_group_async(
        self,
        request: main_models.ListPolicesForUserGroupRequest,
    ) -> main_models.ListPolicesForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_polices_for_user_group_with_options_async(request, runtime)

    def list_pop_traffic_statistics_with_options(
        self,
        request: main_models.ListPopTrafficStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPopTrafficStatisticsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPopTrafficStatistics',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPopTrafficStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pop_traffic_statistics_with_options_async(
        self,
        request: main_models.ListPopTrafficStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPopTrafficStatisticsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPopTrafficStatistics',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPopTrafficStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pop_traffic_statistics(
        self,
        request: main_models.ListPopTrafficStatisticsRequest,
    ) -> main_models.ListPopTrafficStatisticsResponse:
        runtime = RuntimeOptions()
        return self.list_pop_traffic_statistics_with_options(request, runtime)

    async def list_pop_traffic_statistics_async(
        self,
        request: main_models.ListPopTrafficStatisticsRequest,
    ) -> main_models.ListPopTrafficStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.list_pop_traffic_statistics_with_options_async(request, runtime)

    def list_private_access_applications_with_options(
        self,
        request: main_models.ListPrivateAccessApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_modes):
            query['AccessModes'] = request.access_modes
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_with_options_async(
        self,
        request: main_models.ListPrivateAccessApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_modes):
            query['AccessModes'] = request.access_modes
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.application_ids):
            query['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.connector_id):
            query['ConnectorId'] = request.connector_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_id):
            query['TagId'] = request.tag_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications(
        self,
        request: main_models.ListPrivateAccessApplicationsRequest,
    ) -> main_models.ListPrivateAccessApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_private_access_applications_with_options(request, runtime)

    async def list_private_access_applications_async(
        self,
        request: main_models.ListPrivateAccessApplicationsRequest,
    ) -> main_models.ListPrivateAccessApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_private_access_applications_with_options_async(request, runtime)

    def list_private_access_applications_for_dynamic_route_with_options(
        self,
        request: main_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessApplicationsForDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_for_dynamic_route_with_options_async(
        self,
        request: main_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessApplicationsForDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications_for_dynamic_route(
        self,
        request: main_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> main_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.list_private_access_applications_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_applications_for_dynamic_route_async(
        self,
        request: main_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> main_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.list_private_access_applications_for_dynamic_route_with_options_async(request, runtime)

    def list_private_access_polices_with_options(
        self,
        request: main_models.ListPrivateAccessPolicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessPolicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessPolices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessPolicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_polices_with_options_async(
        self,
        request: main_models.ListPrivateAccessPolicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessPolicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessPolices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessPolicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_polices(
        self,
        request: main_models.ListPrivateAccessPolicesRequest,
    ) -> main_models.ListPrivateAccessPolicesResponse:
        runtime = RuntimeOptions()
        return self.list_private_access_polices_with_options(request, runtime)

    async def list_private_access_polices_async(
        self,
        request: main_models.ListPrivateAccessPolicesRequest,
    ) -> main_models.ListPrivateAccessPolicesResponse:
        runtime = RuntimeOptions()
        return await self.list_private_access_polices_with_options_async(request, runtime)

    def list_private_access_tags_with_options(
        self,
        request: main_models.ListPrivateAccessTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessTags',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_with_options_async(
        self,
        request: main_models.ListPrivateAccessTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessTagsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessTags',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags(
        self,
        request: main_models.ListPrivateAccessTagsRequest,
    ) -> main_models.ListPrivateAccessTagsResponse:
        runtime = RuntimeOptions()
        return self.list_private_access_tags_with_options(request, runtime)

    async def list_private_access_tags_async(
        self,
        request: main_models.ListPrivateAccessTagsRequest,
    ) -> main_models.ListPrivateAccessTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_private_access_tags_with_options_async(request, runtime)

    def list_private_access_tags_for_dynamic_route_with_options(
        self,
        request: main_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessTagsForDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessTagsForDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_for_dynamic_route_with_options_async(
        self,
        request: main_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivateAccessTagsForDynamicRouteResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivateAccessTagsForDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags_for_dynamic_route(
        self,
        request: main_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> main_models.ListPrivateAccessTagsForDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.list_private_access_tags_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_tags_for_dynamic_route_async(
        self,
        request: main_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> main_models.ListPrivateAccessTagsForDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.list_private_access_tags_for_dynamic_route_with_options_async(request, runtime)

    def list_registration_policies_with_options(
        self,
        request: main_models.ListRegistrationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistrationPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistrationPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registration_policies_with_options_async(
        self,
        request: main_models.ListRegistrationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistrationPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistrationPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registration_policies(
        self,
        request: main_models.ListRegistrationPoliciesRequest,
    ) -> main_models.ListRegistrationPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_registration_policies_with_options(request, runtime)

    async def list_registration_policies_async(
        self,
        request: main_models.ListRegistrationPoliciesRequest,
    ) -> main_models.ListRegistrationPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_registration_policies_with_options_async(request, runtime)

    def list_registration_policies_for_user_group_with_options(
        self,
        request: main_models.ListRegistrationPoliciesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistrationPoliciesForUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistrationPoliciesForUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistrationPoliciesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registration_policies_for_user_group_with_options_async(
        self,
        request: main_models.ListRegistrationPoliciesForUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistrationPoliciesForUserGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistrationPoliciesForUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistrationPoliciesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registration_policies_for_user_group(
        self,
        request: main_models.ListRegistrationPoliciesForUserGroupRequest,
    ) -> main_models.ListRegistrationPoliciesForUserGroupResponse:
        runtime = RuntimeOptions()
        return self.list_registration_policies_for_user_group_with_options(request, runtime)

    async def list_registration_policies_for_user_group_async(
        self,
        request: main_models.ListRegistrationPoliciesForUserGroupRequest,
    ) -> main_models.ListRegistrationPoliciesForUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_registration_policies_for_user_group_with_options_async(request, runtime)

    def list_software_for_user_device_with_options(
        self,
        request: main_models.ListSoftwareForUserDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSoftwareForUserDeviceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSoftwareForUserDevice',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSoftwareForUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_software_for_user_device_with_options_async(
        self,
        request: main_models.ListSoftwareForUserDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSoftwareForUserDeviceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSoftwareForUserDevice',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSoftwareForUserDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_software_for_user_device(
        self,
        request: main_models.ListSoftwareForUserDeviceRequest,
    ) -> main_models.ListSoftwareForUserDeviceResponse:
        runtime = RuntimeOptions()
        return self.list_software_for_user_device_with_options(request, runtime)

    async def list_software_for_user_device_async(
        self,
        request: main_models.ListSoftwareForUserDeviceRequest,
    ) -> main_models.ListSoftwareForUserDeviceResponse:
        runtime = RuntimeOptions()
        return await self.list_software_for_user_device_with_options_async(request, runtime)

    def list_tags_for_private_access_application_with_options(
        self,
        request: main_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsForPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagsForPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_application_with_options_async(
        self,
        request: main_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsForPrivateAccessApplicationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagsForPrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_application(
        self,
        request: main_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> main_models.ListTagsForPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.list_tags_for_private_access_application_with_options(request, runtime)

    async def list_tags_for_private_access_application_async(
        self,
        request: main_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> main_models.ListTagsForPrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.list_tags_for_private_access_application_with_options_async(request, runtime)

    def list_tags_for_private_access_policy_with_options(
        self,
        request: main_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_policy_with_options_async(
        self,
        request: main_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_policy(
        self,
        request: main_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> main_models.ListTagsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_tags_for_private_access_policy_with_options(request, runtime)

    async def list_tags_for_private_access_policy_async(
        self,
        request: main_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> main_models.ListTagsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_tags_for_private_access_policy_with_options_async(request, runtime)

    def list_uninstall_applications_with_options(
        self,
        request: main_models.ListUninstallApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUninstallApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUninstallApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUninstallApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_uninstall_applications_with_options_async(
        self,
        request: main_models.ListUninstallApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUninstallApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUninstallApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUninstallApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_uninstall_applications(
        self,
        request: main_models.ListUninstallApplicationsRequest,
    ) -> main_models.ListUninstallApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_uninstall_applications_with_options(request, runtime)

    async def list_uninstall_applications_async(
        self,
        request: main_models.ListUninstallApplicationsRequest,
    ) -> main_models.ListUninstallApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_uninstall_applications_with_options_async(request, runtime)

    def list_user_applications_with_options(
        self,
        request: main_models.ListUserApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_applications_with_options_async(
        self,
        request: main_models.ListUserApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserApplicationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserApplications',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_applications(
        self,
        request: main_models.ListUserApplicationsRequest,
    ) -> main_models.ListUserApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_user_applications_with_options(request, runtime)

    async def list_user_applications_async(
        self,
        request: main_models.ListUserApplicationsRequest,
    ) -> main_models.ListUserApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_applications_with_options_async(request, runtime)

    def list_user_devices_with_options(
        self,
        request: main_models.ListUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDevicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_devices_with_options_async(
        self,
        request: main_models.ListUserDevicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserDevicesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserDevices',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_devices(
        self,
        request: main_models.ListUserDevicesRequest,
    ) -> main_models.ListUserDevicesResponse:
        runtime = RuntimeOptions()
        return self.list_user_devices_with_options(request, runtime)

    async def list_user_devices_async(
        self,
        request: main_models.ListUserDevicesRequest,
    ) -> main_models.ListUserDevicesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_devices_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: main_models.ListUserGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroups',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups(
        self,
        request: main_models.ListUserGroupsRequest,
    ) -> main_models.ListUserGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: main_models.ListUserGroupsRequest,
    ) -> main_models.ListUserGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_user_groups_for_private_access_policy_with_options(
        self,
        request: main_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_for_private_access_policy_with_options_async(
        self,
        request: main_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsForPrivateAccessPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsForPrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_for_private_access_policy(
        self,
        request: main_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> main_models.ListUserGroupsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_for_private_access_policy_with_options(request, runtime)

    async def list_user_groups_for_private_access_policy_async(
        self,
        request: main_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> main_models.ListUserGroupsForPrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_for_private_access_policy_with_options_async(request, runtime)

    def list_user_groups_for_registration_policy_with_options(
        self,
        request: main_models.ListUserGroupsForRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsForRegistrationPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsForRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsForRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_for_registration_policy_with_options_async(
        self,
        request: main_models.ListUserGroupsForRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserGroupsForRegistrationPolicyResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserGroupsForRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserGroupsForRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_for_registration_policy(
        self,
        request: main_models.ListUserGroupsForRegistrationPolicyRequest,
    ) -> main_models.ListUserGroupsForRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return self.list_user_groups_for_registration_policy_with_options(request, runtime)

    async def list_user_groups_for_registration_policy_async(
        self,
        request: main_models.ListUserGroupsForRegistrationPolicyRequest,
    ) -> main_models.ListUserGroupsForRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.list_user_groups_for_registration_policy_with_options_async(request, runtime)

    def list_user_private_access_policies_with_options(
        self,
        request: main_models.ListUserPrivateAccessPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPrivateAccessPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPrivateAccessPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserPrivateAccessPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_private_access_policies_with_options_async(
        self,
        request: main_models.ListUserPrivateAccessPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserPrivateAccessPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserPrivateAccessPolicies',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserPrivateAccessPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_private_access_policies(
        self,
        request: main_models.ListUserPrivateAccessPoliciesRequest,
    ) -> main_models.ListUserPrivateAccessPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_user_private_access_policies_with_options(request, runtime)

    async def list_user_private_access_policies_async(
        self,
        request: main_models.ListUserPrivateAccessPoliciesRequest,
    ) -> main_models.ListUserPrivateAccessPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_private_access_policies_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def lookup_wm_info_mapping_with_options(
        self,
        request: main_models.LookupWmInfoMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupWmInfoMappingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupWmInfoMapping',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupWmInfoMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_wm_info_mapping_with_options_async(
        self,
        request: main_models.LookupWmInfoMappingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LookupWmInfoMappingResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LookupWmInfoMapping',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LookupWmInfoMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_wm_info_mapping(
        self,
        request: main_models.LookupWmInfoMappingRequest,
    ) -> main_models.LookupWmInfoMappingResponse:
        runtime = RuntimeOptions()
        return self.lookup_wm_info_mapping_with_options(request, runtime)

    async def lookup_wm_info_mapping_async(
        self,
        request: main_models.LookupWmInfoMappingRequest,
    ) -> main_models.LookupWmInfoMappingResponse:
        runtime = RuntimeOptions()
        return await self.lookup_wm_info_mapping_with_options_async(request, runtime)

    def modify_enterprise_accelerate_policy_with_options(
        self,
        request: main_models.ModifyEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acceleration_type):
            body['AccelerationType'] = request.acceleration_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.on_tls):
            body['OnTls'] = request.on_tls
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.show_in_client):
            body['ShowInClient'] = request.show_in_client
        if not DaraCore.is_null(request.upstream_host):
            body['UpstreamHost'] = request.upstream_host
        if not DaraCore.is_null(request.upstream_port):
            body['UpstreamPort'] = request.upstream_port
        if not DaraCore.is_null(request.upstream_type):
            body['UpstreamType'] = request.upstream_type
        if not DaraCore.is_null(request.user_attribute_group):
            body['UserAttributeGroup'] = request.user_attribute_group
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEnterpriseAcceleratePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_enterprise_accelerate_policy_with_options_async(
        self,
        request: main_models.ModifyEnterpriseAcceleratePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEnterpriseAcceleratePolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acceleration_type):
            body['AccelerationType'] = request.acceleration_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.eap_id):
            body['EapId'] = request.eap_id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.on_tls):
            body['OnTls'] = request.on_tls
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.show_in_client):
            body['ShowInClient'] = request.show_in_client
        if not DaraCore.is_null(request.upstream_host):
            body['UpstreamHost'] = request.upstream_host
        if not DaraCore.is_null(request.upstream_port):
            body['UpstreamPort'] = request.upstream_port
        if not DaraCore.is_null(request.upstream_type):
            body['UpstreamType'] = request.upstream_type
        if not DaraCore.is_null(request.user_attribute_group):
            body['UserAttributeGroup'] = request.user_attribute_group
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEnterpriseAcceleratePolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEnterpriseAcceleratePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_enterprise_accelerate_policy(
        self,
        request: main_models.ModifyEnterpriseAcceleratePolicyRequest,
    ) -> main_models.ModifyEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_enterprise_accelerate_policy_with_options(request, runtime)

    async def modify_enterprise_accelerate_policy_async(
        self,
        request: main_models.ModifyEnterpriseAcceleratePolicyRequest,
    ) -> main_models.ModifyEnterpriseAcceleratePolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_enterprise_accelerate_policy_with_options_async(request, runtime)

    def revoke_user_session_with_options(
        self,
        request: main_models.RevokeUserSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeUserSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ids):
            query['ExternalIds'] = request.external_ids
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeUserSession',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeUserSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_user_session_with_options_async(
        self,
        request: main_models.RevokeUserSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeUserSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external_ids):
            query['ExternalIds'] = request.external_ids
        if not DaraCore.is_null(request.idp_id):
            query['IdpId'] = request.idp_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeUserSession',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeUserSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_user_session(
        self,
        request: main_models.RevokeUserSessionRequest,
    ) -> main_models.RevokeUserSessionResponse:
        runtime = RuntimeOptions()
        return self.revoke_user_session_with_options(request, runtime)

    async def revoke_user_session_async(
        self,
        request: main_models.RevokeUserSessionRequest,
    ) -> main_models.RevokeUserSessionResponse:
        runtime = RuntimeOptions()
        return await self.revoke_user_session_with_options_async(request, runtime)

    def update_approval_process_with_options(
        self,
        tmp_req: main_models.UpdateApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApprovalProcessResponse:
        tmp_req.validate()
        request = main_models.UpdateApprovalProcessShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.match_schema_configs):
            request.match_schema_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schema_configs, 'MatchSchemaConfigs', 'json')
        if not DaraCore.is_null(tmp_req.match_schemas):
            request.match_schemas_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schemas, 'MatchSchemas', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.event_label):
            query['EventLabel'] = request.event_label
        if not DaraCore.is_null(request.external_config):
            query['ExternalConfig'] = request.external_config
        if not DaraCore.is_null(request.match_schema_configs_shrink):
            query['MatchSchemaConfigs'] = request.match_schema_configs_shrink
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_schemas_shrink):
            body['MatchSchemas'] = request.match_schemas_shrink
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_name):
            body['ProcessName'] = request.process_name
        body_flat = {}
        if not DaraCore.is_null(request.process_nodes):
            body_flat['ProcessNodes'] = request.process_nodes
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApprovalProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_approval_process_with_options_async(
        self,
        tmp_req: main_models.UpdateApprovalProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApprovalProcessResponse:
        tmp_req.validate()
        request = main_models.UpdateApprovalProcessShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.match_schema_configs):
            request.match_schema_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schema_configs, 'MatchSchemaConfigs', 'json')
        if not DaraCore.is_null(tmp_req.match_schemas):
            request.match_schemas_shrink = Utils.array_to_string_with_specified_style(tmp_req.match_schemas, 'MatchSchemas', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.event_label):
            query['EventLabel'] = request.event_label
        if not DaraCore.is_null(request.external_config):
            query['ExternalConfig'] = request.external_config
        if not DaraCore.is_null(request.match_schema_configs_shrink):
            query['MatchSchemaConfigs'] = request.match_schema_configs_shrink
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_schemas_shrink):
            body['MatchSchemas'] = request.match_schemas_shrink
        if not DaraCore.is_null(request.process_id):
            body['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_name):
            body['ProcessName'] = request.process_name
        body_flat = {}
        if not DaraCore.is_null(request.process_nodes):
            body_flat['ProcessNodes'] = request.process_nodes
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApprovalProcess',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApprovalProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_approval_process(
        self,
        request: main_models.UpdateApprovalProcessRequest,
    ) -> main_models.UpdateApprovalProcessResponse:
        runtime = RuntimeOptions()
        return self.update_approval_process_with_options(request, runtime)

    async def update_approval_process_async(
        self,
        request: main_models.UpdateApprovalProcessRequest,
    ) -> main_models.UpdateApprovalProcessResponse:
        runtime = RuntimeOptions()
        return await self.update_approval_process_with_options_async(request, runtime)

    def update_approval_status_with_options(
        self,
        request: main_models.UpdateApprovalStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApprovalStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApprovalStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApprovalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_approval_status_with_options_async(
        self,
        request: main_models.UpdateApprovalStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApprovalStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.approval_id):
            query['ApprovalId'] = request.approval_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApprovalStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApprovalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_approval_status(
        self,
        request: main_models.UpdateApprovalStatusRequest,
    ) -> main_models.UpdateApprovalStatusResponse:
        runtime = RuntimeOptions()
        return self.update_approval_status_with_options(request, runtime)

    async def update_approval_status_async(
        self,
        request: main_models.UpdateApprovalStatusRequest,
    ) -> main_models.UpdateApprovalStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_approval_status_with_options_async(request, runtime)

    def update_boot_and_anti_uninstall_policy_with_options(
        self,
        tmp_req: main_models.UpdateBootAndAntiUninstallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBootAndAntiUninstallPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateBootAndAntiUninstallPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.block_content):
            request.block_content_shrink = Utils.array_to_string_with_specified_style(tmp_req.block_content, 'BlockContent', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_report):
            body['AllowReport'] = request.allow_report
        if not DaraCore.is_null(request.block_content_shrink):
            body['BlockContent'] = request.block_content_shrink
        if not DaraCore.is_null(request.is_anti_uninstall):
            body['IsAntiUninstall'] = request.is_anti_uninstall
        if not DaraCore.is_null(request.is_boot):
            body['IsBoot'] = request.is_boot
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist_users):
            body_flat['WhitelistUsers'] = request.whitelist_users
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBootAndAntiUninstallPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBootAndAntiUninstallPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_boot_and_anti_uninstall_policy_with_options_async(
        self,
        tmp_req: main_models.UpdateBootAndAntiUninstallPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBootAndAntiUninstallPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateBootAndAntiUninstallPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.block_content):
            request.block_content_shrink = Utils.array_to_string_with_specified_style(tmp_req.block_content, 'BlockContent', 'json')
        body = {}
        if not DaraCore.is_null(request.allow_report):
            body['AllowReport'] = request.allow_report
        if not DaraCore.is_null(request.block_content_shrink):
            body['BlockContent'] = request.block_content_shrink
        if not DaraCore.is_null(request.is_anti_uninstall):
            body['IsAntiUninstall'] = request.is_anti_uninstall
        if not DaraCore.is_null(request.is_boot):
            body['IsBoot'] = request.is_boot
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist_users):
            body_flat['WhitelistUsers'] = request.whitelist_users
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBootAndAntiUninstallPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBootAndAntiUninstallPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_boot_and_anti_uninstall_policy(
        self,
        request: main_models.UpdateBootAndAntiUninstallPolicyRequest,
    ) -> main_models.UpdateBootAndAntiUninstallPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_boot_and_anti_uninstall_policy_with_options(request, runtime)

    async def update_boot_and_anti_uninstall_policy_async(
        self,
        request: main_models.UpdateBootAndAntiUninstallPolicyRequest,
    ) -> main_models.UpdateBootAndAntiUninstallPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_boot_and_anti_uninstall_policy_with_options_async(request, runtime)

    def update_client_user_with_options(
        self,
        request: main_models.UpdateClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_with_options_async(
        self,
        request: main_models.UpdateClientUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUser',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user(
        self,
        request: main_models.UpdateClientUserRequest,
    ) -> main_models.UpdateClientUserResponse:
        runtime = RuntimeOptions()
        return self.update_client_user_with_options(request, runtime)

    async def update_client_user_async(
        self,
        request: main_models.UpdateClientUserRequest,
    ) -> main_models.UpdateClientUserResponse:
        runtime = RuntimeOptions()
        return await self.update_client_user_with_options_async(request, runtime)

    def update_client_user_password_with_options(
        self,
        request: main_models.UpdateClientUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUserPassword',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_password_with_options_async(
        self,
        request: main_models.UpdateClientUserPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUserPassword',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user_password(
        self,
        request: main_models.UpdateClientUserPasswordRequest,
    ) -> main_models.UpdateClientUserPasswordResponse:
        runtime = RuntimeOptions()
        return self.update_client_user_password_with_options(request, runtime)

    async def update_client_user_password_async(
        self,
        request: main_models.UpdateClientUserPasswordRequest,
    ) -> main_models.UpdateClientUserPasswordResponse:
        runtime = RuntimeOptions()
        return await self.update_client_user_password_with_options_async(request, runtime)

    def update_client_user_status_with_options(
        self,
        request: main_models.UpdateClientUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUserStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_status_with_options_async(
        self,
        request: main_models.UpdateClientUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientUserStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user_status(
        self,
        request: main_models.UpdateClientUserStatusRequest,
    ) -> main_models.UpdateClientUserStatusResponse:
        runtime = RuntimeOptions()
        return self.update_client_user_status_with_options(request, runtime)

    async def update_client_user_status_async(
        self,
        request: main_models.UpdateClientUserStatusRequest,
    ) -> main_models.UpdateClientUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_client_user_status_with_options_async(request, runtime)

    def update_dynamic_route_with_options(
        self,
        request: main_models.UpdateDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDynamicRouteResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not DaraCore.is_null(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_hop):
            body['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dynamic_route_with_options_async(
        self,
        request: main_models.UpdateDynamicRouteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDynamicRouteResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not DaraCore.is_null(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_hop):
            body['NextHop'] = request.next_hop
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDynamicRoute',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dynamic_route(
        self,
        request: main_models.UpdateDynamicRouteRequest,
    ) -> main_models.UpdateDynamicRouteResponse:
        runtime = RuntimeOptions()
        return self.update_dynamic_route_with_options(request, runtime)

    async def update_dynamic_route_async(
        self,
        request: main_models.UpdateDynamicRouteRequest,
    ) -> main_models.UpdateDynamicRouteResponse:
        runtime = RuntimeOptions()
        return await self.update_dynamic_route_with_options_async(request, runtime)

    def update_excessive_device_registration_applications_status_with_options(
        self,
        request: main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExcessiveDeviceRegistrationApplicationsStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_excessive_device_registration_applications_status_with_options_async(
        self,
        request: main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExcessiveDeviceRegistrationApplicationsStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_excessive_device_registration_applications_status(
        self,
        request: main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
    ) -> main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        runtime = RuntimeOptions()
        return self.update_excessive_device_registration_applications_status_with_options(request, runtime)

    async def update_excessive_device_registration_applications_status_async(
        self,
        request: main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
    ) -> main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_excessive_device_registration_applications_status_with_options_async(request, runtime)

    def update_idp_department_with_options(
        self,
        request: main_models.UpdateIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_idp_department_with_options_async(
        self,
        request: main_models.UpdateIdpDepartmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIdpDepartmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.department_id):
            query['DepartmentId'] = request.department_id
        if not DaraCore.is_null(request.department_name):
            query['DepartmentName'] = request.department_name
        if not DaraCore.is_null(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIdpDepartment',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_idp_department(
        self,
        request: main_models.UpdateIdpDepartmentRequest,
    ) -> main_models.UpdateIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return self.update_idp_department_with_options(request, runtime)

    async def update_idp_department_async(
        self,
        request: main_models.UpdateIdpDepartmentRequest,
    ) -> main_models.UpdateIdpDepartmentResponse:
        runtime = RuntimeOptions()
        return await self.update_idp_department_with_options_async(request, runtime)

    def update_nac_user_cert_status_with_options(
        self,
        request: main_models.UpdateNacUserCertStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacUserCertStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.id_list):
            body_flat['IdList'] = request.id_list
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacUserCertStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacUserCertStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nac_user_cert_status_with_options_async(
        self,
        request: main_models.UpdateNacUserCertStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNacUserCertStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.id_list):
            body_flat['IdList'] = request.id_list
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNacUserCertStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNacUserCertStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nac_user_cert_status(
        self,
        request: main_models.UpdateNacUserCertStatusRequest,
    ) -> main_models.UpdateNacUserCertStatusResponse:
        runtime = RuntimeOptions()
        return self.update_nac_user_cert_status_with_options(request, runtime)

    async def update_nac_user_cert_status_async(
        self,
        request: main_models.UpdateNacUserCertStatusRequest,
    ) -> main_models.UpdateNacUserCertStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_nac_user_cert_status_with_options_async(request, runtime)

    def update_private_access_application_with_options(
        self,
        tmp_req: main_models.UpdatePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateAccessApplicationResponse:
        tmp_req.validate()
        request = main_models.UpdatePrivateAccessApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.l_7config):
            request.l_7config_shrink = Utils.array_to_string_with_specified_style(tmp_req.l_7config, 'L7Config', 'json')
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.address_groups):
            body_flat['AddressGroups'] = request.address_groups
        if not DaraCore.is_null(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.config_mode):
            body['ConfigMode'] = request.config_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.l_7config_shrink):
            body['L7Config'] = request.l_7config_shrink
        if not DaraCore.is_null(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not DaraCore.is_null(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not DaraCore.is_null(request.l_7proxy_domain_private):
            body['L7ProxyDomainPrivate'] = request.l_7proxy_domain_private
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_application_with_options_async(
        self,
        tmp_req: main_models.UpdatePrivateAccessApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateAccessApplicationResponse:
        tmp_req.validate()
        request = main_models.UpdatePrivateAccessApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.l_7config):
            request.l_7config_shrink = Utils.array_to_string_with_specified_style(tmp_req.l_7config, 'L7Config', 'json')
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.address_groups):
            body_flat['AddressGroups'] = request.address_groups
        if not DaraCore.is_null(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not DaraCore.is_null(request.application_id):
            body['ApplicationId'] = request.application_id
        if not DaraCore.is_null(request.config_mode):
            body['ConfigMode'] = request.config_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.l_7config_shrink):
            body['L7Config'] = request.l_7config_shrink
        if not DaraCore.is_null(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not DaraCore.is_null(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not DaraCore.is_null(request.l_7proxy_domain_private):
            body['L7ProxyDomainPrivate'] = request.l_7proxy_domain_private
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not DaraCore.is_null(request.protocol):
            body['Protocol'] = request.protocol
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateAccessApplication',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_application(
        self,
        request: main_models.UpdatePrivateAccessApplicationRequest,
    ) -> main_models.UpdatePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return self.update_private_access_application_with_options(request, runtime)

    async def update_private_access_application_async(
        self,
        request: main_models.UpdatePrivateAccessApplicationRequest,
    ) -> main_models.UpdatePrivateAccessApplicationResponse:
        runtime = RuntimeOptions()
        return await self.update_private_access_application_with_options_async(request, runtime)

    def update_private_access_policy_with_options(
        self,
        request: main_models.UpdatePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not DaraCore.is_null(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not DaraCore.is_null(request.trigger_template_id):
            body['TriggerTemplateId'] = request.trigger_template_id
        if not DaraCore.is_null(request.trusted_process_group_ids):
            body_flat['TrustedProcessGroupIds'] = request.trusted_process_group_ids
        if not DaraCore.is_null(request.trusted_process_status):
            body['TrustedProcessStatus'] = request.trusted_process_status
        if not DaraCore.is_null(request.trusted_software_ids):
            body_flat['TrustedSoftwareIds'] = request.trusted_software_ids
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        if not DaraCore.is_null(request.valid_from):
            body['ValidFrom'] = request.valid_from
        if not DaraCore.is_null(request.valid_time_status):
            body['ValidTimeStatus'] = request.valid_time_status
        if not DaraCore.is_null(request.valid_until):
            body['ValidUntil'] = request.valid_until
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_policy_with_options_async(
        self,
        request: main_models.UpdatePrivateAccessPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrivateAccessPolicyResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.application_type):
            body['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not DaraCore.is_null(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not DaraCore.is_null(request.trigger_template_id):
            body['TriggerTemplateId'] = request.trigger_template_id
        if not DaraCore.is_null(request.trusted_process_group_ids):
            body_flat['TrustedProcessGroupIds'] = request.trusted_process_group_ids
        if not DaraCore.is_null(request.trusted_process_status):
            body['TrustedProcessStatus'] = request.trusted_process_status
        if not DaraCore.is_null(request.trusted_software_ids):
            body_flat['TrustedSoftwareIds'] = request.trusted_software_ids
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        if not DaraCore.is_null(request.valid_from):
            body['ValidFrom'] = request.valid_from
        if not DaraCore.is_null(request.valid_time_status):
            body['ValidTimeStatus'] = request.valid_time_status
        if not DaraCore.is_null(request.valid_until):
            body['ValidUntil'] = request.valid_until
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrivateAccessPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_policy(
        self,
        request: main_models.UpdatePrivateAccessPolicyRequest,
    ) -> main_models.UpdatePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_private_access_policy_with_options(request, runtime)

    async def update_private_access_policy_async(
        self,
        request: main_models.UpdatePrivateAccessPolicyRequest,
    ) -> main_models.UpdatePrivateAccessPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_private_access_policy_with_options_async(request, runtime)

    def update_registration_policy_with_options(
        self,
        tmp_req: main_models.UpdateRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistrationPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateRegistrationPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.company_limit_count):
            request.company_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not DaraCore.is_null(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not DaraCore.is_null(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not DaraCore.is_null(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not DaraCore.is_null(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registration_policy_with_options_async(
        self,
        tmp_req: main_models.UpdateRegistrationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistrationPolicyResponse:
        tmp_req.validate()
        request = main_models.UpdateRegistrationPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.company_limit_count):
            request.company_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not DaraCore.is_null(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not DaraCore.is_null(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not DaraCore.is_null(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not DaraCore.is_null(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not DaraCore.is_null(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not DaraCore.is_null(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistrationPolicy',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registration_policy(
        self,
        request: main_models.UpdateRegistrationPolicyRequest,
    ) -> main_models.UpdateRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_registration_policy_with_options(request, runtime)

    async def update_registration_policy_async(
        self,
        request: main_models.UpdateRegistrationPolicyRequest,
    ) -> main_models.UpdateRegistrationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_registration_policy_with_options_async(request, runtime)

    def update_uninstall_applications_status_with_options(
        self,
        request: main_models.UpdateUninstallApplicationsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUninstallApplicationsStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUninstallApplicationsStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUninstallApplicationsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_uninstall_applications_status_with_options_async(
        self,
        request: main_models.UpdateUninstallApplicationsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUninstallApplicationsStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUninstallApplicationsStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUninstallApplicationsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_uninstall_applications_status(
        self,
        request: main_models.UpdateUninstallApplicationsStatusRequest,
    ) -> main_models.UpdateUninstallApplicationsStatusResponse:
        runtime = RuntimeOptions()
        return self.update_uninstall_applications_status_with_options(request, runtime)

    async def update_uninstall_applications_status_async(
        self,
        request: main_models.UpdateUninstallApplicationsStatusRequest,
    ) -> main_models.UpdateUninstallApplicationsStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_uninstall_applications_status_with_options_async(request, runtime)

    def update_user_devices_sharing_status_with_options(
        self,
        request: main_models.UpdateUserDevicesSharingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDevicesSharingStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not DaraCore.is_null(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDevicesSharingStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDevicesSharingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_devices_sharing_status_with_options_async(
        self,
        request: main_models.UpdateUserDevicesSharingStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDevicesSharingStatusResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not DaraCore.is_null(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDevicesSharingStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDevicesSharingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_devices_sharing_status(
        self,
        request: main_models.UpdateUserDevicesSharingStatusRequest,
    ) -> main_models.UpdateUserDevicesSharingStatusResponse:
        runtime = RuntimeOptions()
        return self.update_user_devices_sharing_status_with_options(request, runtime)

    async def update_user_devices_sharing_status_async(
        self,
        request: main_models.UpdateUserDevicesSharingStatusRequest,
    ) -> main_models.UpdateUserDevicesSharingStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_user_devices_sharing_status_with_options_async(request, runtime)

    def update_user_devices_status_with_options(
        self,
        request: main_models.UpdateUserDevicesStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDevicesStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_action):
            body['DeviceAction'] = request.device_action
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDevicesStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDevicesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_devices_status_with_options_async(
        self,
        request: main_models.UpdateUserDevicesStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserDevicesStatusResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_action):
            body['DeviceAction'] = request.device_action
        body_flat = {}
        if not DaraCore.is_null(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserDevicesStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserDevicesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_devices_status(
        self,
        request: main_models.UpdateUserDevicesStatusRequest,
    ) -> main_models.UpdateUserDevicesStatusResponse:
        runtime = RuntimeOptions()
        return self.update_user_devices_status_with_options(request, runtime)

    async def update_user_devices_status_async(
        self,
        request: main_models.UpdateUserDevicesStatusRequest,
    ) -> main_models.UpdateUserDevicesStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_user_devices_status_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: main_models.UpdateUserGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserGroupResponse:
        request.validate()
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserGroup',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: main_models.UpdateUserGroupRequest,
    ) -> main_models.UpdateUserGroupResponse:
        runtime = RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: main_models.UpdateUserGroupRequest,
    ) -> main_models.UpdateUserGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_users_status_with_options(
        self,
        request: main_models.UpdateUsersStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUsersStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sase_user_ids):
            query['SaseUserIds'] = request.sase_user_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUsersStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUsersStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_users_status_with_options_async(
        self,
        request: main_models.UpdateUsersStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUsersStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.sase_user_ids):
            query['SaseUserIds'] = request.sase_user_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUsersStatus',
            version = '2023-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUsersStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_users_status(
        self,
        request: main_models.UpdateUsersStatusRequest,
    ) -> main_models.UpdateUsersStatusResponse:
        runtime = RuntimeOptions()
        return self.update_users_status_with_options(request, runtime)

    async def update_users_status_async(
        self,
        request: main_models.UpdateUsersStatusRequest,
    ) -> main_models.UpdateUsersStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_users_status_with_options_async(request, runtime)
