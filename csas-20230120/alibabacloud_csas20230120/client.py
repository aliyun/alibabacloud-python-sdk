# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_csas20230120 import models as csas_20230120_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_application_2connector_with_options(
        self,
        tmp_req: csas_20230120_models.AttachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.AttachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.AttachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_application_2connector_with_options_async(
        self,
        tmp_req: csas_20230120_models.AttachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.AttachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.AttachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_application_2connector(
        self,
        request: csas_20230120_models.AttachApplication2ConnectorRequest,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_application_2connector_with_options(request, runtime)

    async def attach_application_2connector_async(
        self,
        request: csas_20230120_models.AttachApplication2ConnectorRequest,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_application_2connector_with_options_async(request, runtime)

    def create_dynamic_route_with_options(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dynamic_route(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_route_with_options(request, runtime)

    async def create_dynamic_route_async(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dynamic_route_with_options_async(request, runtime)

    def create_private_access_application_with_options(
        self,
        tmp_req: csas_20230120_models.CreatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_application_with_options_async(
        self,
        tmp_req: csas_20230120_models.CreatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_application(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_application_with_options(request, runtime)

    async def create_private_access_application_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_application_with_options_async(request, runtime)

    def create_private_access_policy_with_options(
        self,
        tmp_req: csas_20230120_models.CreatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_policy_with_options_async(
        self,
        tmp_req: csas_20230120_models.CreatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_policy(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_policy_with_options(request, runtime)

    async def create_private_access_policy_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_policy_with_options_async(request, runtime)

    def create_private_access_tag_with_options(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_tag(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_tag_with_options(request, runtime)

    async def create_private_access_tag_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_tag_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def delete_dynamic_route_with_options(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_route(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_route_with_options(request, runtime)

    async def delete_dynamic_route_async(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dynamic_route_with_options_async(request, runtime)

    def delete_private_access_application_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_application(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_application_with_options(request, runtime)

    async def delete_private_access_application_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_application_with_options_async(request, runtime)

    def delete_private_access_policy_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_policy(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_policy_with_options(request, runtime)

    async def delete_private_access_policy_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_policy_with_options_async(request, runtime)

    def delete_private_access_tag_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_tag(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_tag_with_options(request, runtime)

    async def delete_private_access_tag_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_tag_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def detach_application_2connector_with_options(
        self,
        tmp_req: csas_20230120_models.DetachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.DetachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DetachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_application_2connector_with_options_async(
        self,
        tmp_req: csas_20230120_models.DetachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.DetachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DetachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_application_2connector(
        self,
        request: csas_20230120_models.DetachApplication2ConnectorRequest,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_application_2connector_with_options(request, runtime)

    async def detach_application_2connector_async(
        self,
        request: csas_20230120_models.DetachApplication2ConnectorRequest,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_application_2connector_with_options_async(request, runtime)

    def get_dynamic_route_with_options(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dynamic_route(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dynamic_route_with_options(request, runtime)

    async def get_dynamic_route_async(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dynamic_route_with_options_async(request, runtime)

    def get_private_access_application_with_options(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_application(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_application_with_options(request, runtime)

    async def get_private_access_application_async(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_private_access_application_with_options_async(request, runtime)

    def get_private_access_policy_with_options(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_policy(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_policy_with_options(request, runtime)

    async def get_private_access_policy_async(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_private_access_policy_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
    ) -> csas_20230120_models.GetUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
    ) -> csas_20230120_models.GetUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def list_applications_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_policy(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_policy_with_options(request, runtime)

    async def list_applications_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_private_access_policy_with_options_async(request, runtime)

    def list_applications_for_private_access_tag_with_options(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_tag(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_tag_with_options(request, runtime)

    async def list_applications_for_private_access_tag_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_private_access_tag_with_options_async(request, runtime)

    def list_connectors_with_options(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListConnectorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectors',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connectors_with_options_async(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListConnectorsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectors',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connectors(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
    ) -> csas_20230120_models.ListConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    async def list_connectors_async(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
    ) -> csas_20230120_models.ListConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connectors_with_options_async(request, runtime)

    def list_dynamic_route_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDynamicRouteRegions',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRouteRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_route_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDynamicRouteRegions',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRouteRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_route_regions(self) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_route_regions_with_options(runtime)

    async def list_dynamic_route_regions_async(self) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_route_regions_with_options_async(runtime)

    def list_dynamic_routes_with_options(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicRoutes',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_routes_with_options_async(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicRoutes',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_routes(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_routes_with_options(request, runtime)

    async def list_dynamic_routes_async(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_routes_with_options_async(request, runtime)

    def list_polices_for_private_access_application_with_options(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_application(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_application_with_options(request, runtime)

    async def list_polices_for_private_access_application_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_private_access_application_with_options_async(request, runtime)

    def list_polices_for_private_access_tag_with_options(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_tag(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_tag_with_options(request, runtime)

    async def list_polices_for_private_access_tag_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_private_access_tag_with_options_async(request, runtime)

    def list_polices_for_user_group_with_options(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_user_group_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_user_group(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_user_group_with_options(request, runtime)

    async def list_polices_for_user_group_async(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_user_group_with_options_async(request, runtime)

    def list_private_access_applications_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_with_options(request, runtime)

    async def list_private_access_applications_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_applications_with_options_async(request, runtime)

    def list_private_access_applications_for_dynamic_route_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplicationsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_for_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplicationsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications_for_dynamic_route(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_applications_for_dynamic_route_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_applications_for_dynamic_route_with_options_async(request, runtime)

    def list_private_access_polices_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessPolices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessPolicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_polices_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessPolices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessPolicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_polices(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_polices_with_options(request, runtime)

    async def list_private_access_polices_async(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_polices_with_options_async(request, runtime)

    def list_private_access_tags_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTags',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTags',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_with_options(request, runtime)

    async def list_private_access_tags_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_tags_with_options_async(request, runtime)

    def list_private_access_tags_for_dynamic_route_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTagsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_for_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTagsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags_for_dynamic_route(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_tags_for_dynamic_route_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_tags_for_dynamic_route_with_options_async(request, runtime)

    def list_tags_for_private_access_application_with_options(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_application(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_application_with_options(request, runtime)

    async def list_tags_for_private_access_application_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_for_private_access_application_with_options_async(request, runtime)

    def list_tags_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_policy(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_policy_with_options(request, runtime)

    async def list_tags_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_for_private_access_policy_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_user_groups_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_for_private_access_policy(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_for_private_access_policy_with_options(request, runtime)

    async def list_user_groups_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_for_private_access_policy_with_options_async(request, runtime)

    def update_dynamic_route_with_options(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dynamic_route(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dynamic_route_with_options(request, runtime)

    async def update_dynamic_route_async(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dynamic_route_with_options_async(request, runtime)

    def update_private_access_application_with_options(
        self,
        tmp_req: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_application_with_options_async(
        self,
        tmp_req: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.addresses):
            request.addresses_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.addresses, 'Addresses', 'json')
        if not UtilClient.is_unset(tmp_req.port_ranges):
            request.port_ranges_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.port_ranges, 'PortRanges', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.addresses_shrink):
            body['Addresses'] = request.addresses_shrink
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges_shrink):
            body['PortRanges'] = request.port_ranges_shrink
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_application(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_application_with_options(request, runtime)

    async def update_private_access_application_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_private_access_application_with_options_async(request, runtime)

    def update_private_access_policy_with_options(
        self,
        tmp_req: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_policy_with_options_async(
        self,
        tmp_req: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdatePrivateAccessPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        if not UtilClient.is_unset(tmp_req.custom_user_attributes):
            request.custom_user_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_user_attributes, 'CustomUserAttributes', 'json')
        if not UtilClient.is_unset(tmp_req.tag_ids):
            request.tag_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_ids, 'TagIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_group_ids):
            request.user_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_group_ids, 'UserGroupIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes_shrink):
            body['CustomUserAttributes'] = request.custom_user_attributes_shrink
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids_shrink):
            body['TagIds'] = request.tag_ids_shrink
        if not UtilClient.is_unset(request.user_group_ids_shrink):
            body['UserGroupIds'] = request.user_group_ids_shrink
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_policy(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_policy_with_options(request, runtime)

    async def update_private_access_policy_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_private_access_policy_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)
