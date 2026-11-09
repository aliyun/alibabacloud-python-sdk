# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_onsmqtt20200420 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._product_id = 'OnsMqtt'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('onsmqtt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_ca_certificate_with_options(
        self,
        request: main_models.ActiveCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_ca_certificate_with_options_async(
        self,
        request: main_models.ActiveCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_ca_certificate(
        self,
        request: main_models.ActiveCaCertificateRequest,
    ) -> main_models.ActiveCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.active_ca_certificate_with_options(request, runtime)

    async def active_ca_certificate_async(
        self,
        request: main_models.ActiveCaCertificateRequest,
    ) -> main_models.ActiveCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.active_ca_certificate_with_options_async(request, runtime)

    def active_device_certificate_with_options(
        self,
        request: main_models.ActiveDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_device_certificate_with_options_async(
        self,
        request: main_models.ActiveDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ActiveDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ActiveDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ActiveDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_device_certificate(
        self,
        request: main_models.ActiveDeviceCertificateRequest,
    ) -> main_models.ActiveDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return self.active_device_certificate_with_options(request, runtime)

    async def active_device_certificate_async(
        self,
        request: main_models.ActiveDeviceCertificateRequest,
    ) -> main_models.ActiveDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return await self.active_device_certificate_with_options_async(request, runtime)

    def add_custom_auth_connect_black_with_options(
        self,
        request: main_models.AddCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthConnectBlackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthConnectBlackResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_auth_connect_black_with_options_async(
        self,
        request: main_models.AddCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthConnectBlackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthConnectBlackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_auth_connect_black(
        self,
        request: main_models.AddCustomAuthConnectBlackRequest,
    ) -> main_models.AddCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return self.add_custom_auth_connect_black_with_options(request, runtime)

    async def add_custom_auth_connect_black_async(
        self,
        request: main_models.AddCustomAuthConnectBlackRequest,
    ) -> main_models.AddCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_auth_connect_black_with_options_async(request, runtime)

    def add_custom_auth_identity_with_options(
        self,
        request: main_models.AddCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret):
            body['Secret'] = request.secret
        if not DaraCore.is_null(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_auth_identity_with_options_async(
        self,
        request: main_models.AddCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret):
            body['Secret'] = request.secret
        if not DaraCore.is_null(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_auth_identity(
        self,
        request: main_models.AddCustomAuthIdentityRequest,
    ) -> main_models.AddCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return self.add_custom_auth_identity_with_options(request, runtime)

    async def add_custom_auth_identity_async(
        self,
        request: main_models.AddCustomAuthIdentityRequest,
    ) -> main_models.AddCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_auth_identity_with_options_async(request, runtime)

    def add_custom_auth_permission_with_options(
        self,
        request: main_models.AddCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.effect):
            body['Effect'] = request.effect
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_custom_auth_permission_with_options_async(
        self,
        request: main_models.AddCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.effect):
            body['Effect'] = request.effect
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomAuthPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_custom_auth_permission(
        self,
        request: main_models.AddCustomAuthPermissionRequest,
    ) -> main_models.AddCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return self.add_custom_auth_permission_with_options(request, runtime)

    async def add_custom_auth_permission_async(
        self,
        request: main_models.AddCustomAuthPermissionRequest,
    ) -> main_models.AddCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return await self.add_custom_auth_permission_with_options_async(request, runtime)

    def apply_token_with_options(
        self,
        request: main_models.ApplyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actions):
            query['Actions'] = request.actions
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_token_with_options_async(
        self,
        request: main_models.ApplyTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.actions):
            query['Actions'] = request.actions
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_token(
        self,
        request: main_models.ApplyTokenRequest,
    ) -> main_models.ApplyTokenResponse:
        runtime = RuntimeOptions()
        return self.apply_token_with_options(request, runtime)

    async def apply_token_async(
        self,
        request: main_models.ApplyTokenRequest,
    ) -> main_models.ApplyTokenResponse:
        runtime = RuntimeOptions()
        return await self.apply_token_with_options_async(request, runtime)

    def batch_query_session_by_client_ids_with_options(
        self,
        request: main_models.BatchQuerySessionByClientIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQuerySessionByClientIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQuerySessionByClientIds',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQuerySessionByClientIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_session_by_client_ids_with_options_async(
        self,
        request: main_models.BatchQuerySessionByClientIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchQuerySessionByClientIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id_list):
            query['ClientIdList'] = request.client_id_list
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQuerySessionByClientIds',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQuerySessionByClientIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_session_by_client_ids(
        self,
        request: main_models.BatchQuerySessionByClientIdsRequest,
    ) -> main_models.BatchQuerySessionByClientIdsResponse:
        runtime = RuntimeOptions()
        return self.batch_query_session_by_client_ids_with_options(request, runtime)

    async def batch_query_session_by_client_ids_async(
        self,
        request: main_models.BatchQuerySessionByClientIdsRequest,
    ) -> main_models.BatchQuerySessionByClientIdsResponse:
        runtime = RuntimeOptions()
        return await self.batch_query_session_by_client_ids_with_options_async(request, runtime)

    def close_connection_with_options(
        self,
        request: main_models.CloseConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseConnection',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_connection_with_options_async(
        self,
        request: main_models.CloseConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseConnection',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_connection(
        self,
        request: main_models.CloseConnectionRequest,
    ) -> main_models.CloseConnectionResponse:
        runtime = RuntimeOptions()
        return self.close_connection_with_options(request, runtime)

    async def close_connection_async(
        self,
        request: main_models.CloseConnectionRequest,
    ) -> main_models.CloseConnectionResponse:
        runtime = RuntimeOptions()
        return await self.close_connection_with_options_async(request, runtime)

    def create_group_id_with_options(
        self,
        request: main_models.CreateGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_id_with_options_async(
        self,
        request: main_models.CreateGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_id(
        self,
        request: main_models.CreateGroupIdRequest,
    ) -> main_models.CreateGroupIdResponse:
        runtime = RuntimeOptions()
        return self.create_group_id_with_options(request, runtime)

    async def create_group_id_async(
        self,
        request: main_models.CreateGroupIdRequest,
    ) -> main_models.CreateGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.create_group_id_with_options_async(request, runtime)

    def delete_ca_certificate_with_options(
        self,
        request: main_models.DeleteCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ca_certificate_with_options_async(
        self,
        request: main_models.DeleteCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ca_certificate(
        self,
        request: main_models.DeleteCaCertificateRequest,
    ) -> main_models.DeleteCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_ca_certificate_with_options(request, runtime)

    async def delete_ca_certificate_async(
        self,
        request: main_models.DeleteCaCertificateRequest,
    ) -> main_models.DeleteCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_ca_certificate_with_options_async(request, runtime)

    def delete_custom_auth_connect_black_with_options(
        self,
        request: main_models.DeleteCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthConnectBlackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthConnectBlackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_auth_connect_black_with_options_async(
        self,
        request: main_models.DeleteCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthConnectBlackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthConnectBlackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_auth_connect_black(
        self,
        request: main_models.DeleteCustomAuthConnectBlackRequest,
    ) -> main_models.DeleteCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_auth_connect_black_with_options(request, runtime)

    async def delete_custom_auth_connect_black_async(
        self,
        request: main_models.DeleteCustomAuthConnectBlackRequest,
    ) -> main_models.DeleteCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_auth_connect_black_with_options_async(request, runtime)

    def delete_custom_auth_identity_with_options(
        self,
        request: main_models.DeleteCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_auth_identity_with_options_async(
        self,
        request: main_models.DeleteCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_auth_identity(
        self,
        request: main_models.DeleteCustomAuthIdentityRequest,
    ) -> main_models.DeleteCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_auth_identity_with_options(request, runtime)

    async def delete_custom_auth_identity_async(
        self,
        request: main_models.DeleteCustomAuthIdentityRequest,
    ) -> main_models.DeleteCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_auth_identity_with_options_async(request, runtime)

    def delete_custom_auth_permission_with_options(
        self,
        request: main_models.DeleteCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_auth_permission_with_options_async(
        self,
        request: main_models.DeleteCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAuthPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_auth_permission(
        self,
        request: main_models.DeleteCustomAuthPermissionRequest,
    ) -> main_models.DeleteCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_auth_permission_with_options(request, runtime)

    async def delete_custom_auth_permission_async(
        self,
        request: main_models.DeleteCustomAuthPermissionRequest,
    ) -> main_models.DeleteCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_auth_permission_with_options_async(request, runtime)

    def delete_device_certificate_with_options(
        self,
        request: main_models.DeleteDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_device_certificate_with_options_async(
        self,
        request: main_models.DeleteDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_device_certificate(
        self,
        request: main_models.DeleteDeviceCertificateRequest,
    ) -> main_models.DeleteDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_device_certificate_with_options(request, runtime)

    async def delete_device_certificate_async(
        self,
        request: main_models.DeleteDeviceCertificateRequest,
    ) -> main_models.DeleteDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_device_certificate_with_options_async(request, runtime)

    def delete_group_id_with_options(
        self,
        request: main_models.DeleteGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_id_with_options_async(
        self,
        request: main_models.DeleteGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_id(
        self,
        request: main_models.DeleteGroupIdRequest,
    ) -> main_models.DeleteGroupIdResponse:
        runtime = RuntimeOptions()
        return self.delete_group_id_with_options(request, runtime)

    async def delete_group_id_async(
        self,
        request: main_models.DeleteGroupIdRequest,
    ) -> main_models.DeleteGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_id_with_options_async(request, runtime)

    def delete_wildcard_by_topic_with_options(
        self,
        request: main_models.DeleteWildcardByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWildcardByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.first_topic):
            query['FirstTopic'] = request.first_topic
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.wildcards):
            query['Wildcards'] = request.wildcards
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWildcardByTopic',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWildcardByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_wildcard_by_topic_with_options_async(
        self,
        request: main_models.DeleteWildcardByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWildcardByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.first_topic):
            query['FirstTopic'] = request.first_topic
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.wildcards):
            query['Wildcards'] = request.wildcards
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWildcardByTopic',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWildcardByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_wildcard_by_topic(
        self,
        request: main_models.DeleteWildcardByTopicRequest,
    ) -> main_models.DeleteWildcardByTopicResponse:
        runtime = RuntimeOptions()
        return self.delete_wildcard_by_topic_with_options(request, runtime)

    async def delete_wildcard_by_topic_async(
        self,
        request: main_models.DeleteWildcardByTopicRequest,
    ) -> main_models.DeleteWildcardByTopicResponse:
        runtime = RuntimeOptions()
        return await self.delete_wildcard_by_topic_with_options_async(request, runtime)

    def disaster_downgrade_with_options(
        self,
        request: main_models.DisasterDowngradeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisasterDowngradeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.downgrade_instance_id):
            body['DowngradeInstanceId'] = request.downgrade_instance_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisasterDowngrade',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisasterDowngradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def disaster_downgrade_with_options_async(
        self,
        request: main_models.DisasterDowngradeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisasterDowngradeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.downgrade_instance_id):
            body['DowngradeInstanceId'] = request.downgrade_instance_id
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisasterDowngrade',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisasterDowngradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disaster_downgrade(
        self,
        request: main_models.DisasterDowngradeRequest,
    ) -> main_models.DisasterDowngradeResponse:
        runtime = RuntimeOptions()
        return self.disaster_downgrade_with_options(request, runtime)

    async def disaster_downgrade_async(
        self,
        request: main_models.DisasterDowngradeRequest,
    ) -> main_models.DisasterDowngradeResponse:
        runtime = RuntimeOptions()
        return await self.disaster_downgrade_with_options_async(request, runtime)

    def disaster_recovery_with_options(
        self,
        request: main_models.DisasterRecoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisasterRecoveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.recovery_instance_id):
            body['RecoveryInstanceId'] = request.recovery_instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisasterRecovery',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisasterRecoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def disaster_recovery_with_options_async(
        self,
        request: main_models.DisasterRecoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisasterRecoveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.recovery_instance_id):
            body['RecoveryInstanceId'] = request.recovery_instance_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisasterRecovery',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisasterRecoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disaster_recovery(
        self,
        request: main_models.DisasterRecoveryRequest,
    ) -> main_models.DisasterRecoveryResponse:
        runtime = RuntimeOptions()
        return self.disaster_recovery_with_options(request, runtime)

    async def disaster_recovery_async(
        self,
        request: main_models.DisasterRecoveryRequest,
    ) -> main_models.DisasterRecoveryResponse:
        runtime = RuntimeOptions()
        return await self.disaster_recovery_with_options_async(request, runtime)

    def get_ca_certificate_with_options(
        self,
        request: main_models.GetCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCaCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ca_certificate_with_options_async(
        self,
        request: main_models.GetCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCaCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ca_certificate(
        self,
        request: main_models.GetCaCertificateRequest,
    ) -> main_models.GetCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.get_ca_certificate_with_options(request, runtime)

    async def get_ca_certificate_async(
        self,
        request: main_models.GetCaCertificateRequest,
    ) -> main_models.GetCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.get_ca_certificate_with_options_async(request, runtime)

    def get_device_certificate_with_options(
        self,
        request: main_models.GetDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_certificate_with_options_async(
        self,
        request: main_models.GetDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_certificate(
        self,
        request: main_models.GetDeviceCertificateRequest,
    ) -> main_models.GetDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return self.get_device_certificate_with_options(request, runtime)

    async def get_device_certificate_async(
        self,
        request: main_models.GetDeviceCertificateRequest,
    ) -> main_models.GetDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return await self.get_device_certificate_with_options_async(request, runtime)

    def get_device_credential_with_options(
        self,
        request: main_models.GetDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_device_credential_with_options_async(
        self,
        request: main_models.GetDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_device_credential(
        self,
        request: main_models.GetDeviceCredentialRequest,
    ) -> main_models.GetDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return self.get_device_credential_with_options(request, runtime)

    async def get_device_credential_async(
        self,
        request: main_models.GetDeviceCredentialRequest,
    ) -> main_models.GetDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return await self.get_device_credential_with_options_async(request, runtime)

    def get_register_code_with_options(
        self,
        request: main_models.GetRegisterCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegisterCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegisterCode',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegisterCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_register_code_with_options_async(
        self,
        request: main_models.GetRegisterCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRegisterCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRegisterCode',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegisterCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_register_code(
        self,
        request: main_models.GetRegisterCodeRequest,
    ) -> main_models.GetRegisterCodeResponse:
        runtime = RuntimeOptions()
        return self.get_register_code_with_options(request, runtime)

    async def get_register_code_async(
        self,
        request: main_models.GetRegisterCodeRequest,
    ) -> main_models.GetRegisterCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_register_code_with_options_async(request, runtime)

    def inactivate_ca_certificate_with_options(
        self,
        request: main_models.InactivateCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InactivateCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InactivateCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InactivateCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def inactivate_ca_certificate_with_options_async(
        self,
        request: main_models.InactivateCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InactivateCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sn):
            query['Sn'] = request.sn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InactivateCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InactivateCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inactivate_ca_certificate(
        self,
        request: main_models.InactivateCaCertificateRequest,
    ) -> main_models.InactivateCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.inactivate_ca_certificate_with_options(request, runtime)

    async def inactivate_ca_certificate_async(
        self,
        request: main_models.InactivateCaCertificateRequest,
    ) -> main_models.InactivateCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.inactivate_ca_certificate_with_options_async(request, runtime)

    def inactivate_device_certificate_with_options(
        self,
        request: main_models.InactivateDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InactivateDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InactivateDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InactivateDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def inactivate_device_certificate_with_options_async(
        self,
        request: main_models.InactivateDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InactivateDeviceCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_sn):
            query['CaSn'] = request.ca_sn
        if not DaraCore.is_null(request.device_sn):
            query['DeviceSn'] = request.device_sn
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InactivateDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InactivateDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inactivate_device_certificate(
        self,
        request: main_models.InactivateDeviceCertificateRequest,
    ) -> main_models.InactivateDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return self.inactivate_device_certificate_with_options(request, runtime)

    async def inactivate_device_certificate_async(
        self,
        request: main_models.InactivateDeviceCertificateRequest,
    ) -> main_models.InactivateDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return await self.inactivate_device_certificate_with_options_async(request, runtime)

    def list_ca_certificate_with_options(
        self,
        request: main_models.ListCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCaCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ca_certificate_with_options_async(
        self,
        request: main_models.ListCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCaCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ca_certificate(
        self,
        request: main_models.ListCaCertificateRequest,
    ) -> main_models.ListCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_ca_certificate_with_options(request, runtime)

    async def list_ca_certificate_async(
        self,
        request: main_models.ListCaCertificateRequest,
    ) -> main_models.ListCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_ca_certificate_with_options_async(request, runtime)

    def list_device_certificate_with_options(
        self,
        request: main_models.ListDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_certificate_with_options_async(
        self,
        request: main_models.ListDeviceCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCertificateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_certificate(
        self,
        request: main_models.ListDeviceCertificateRequest,
    ) -> main_models.ListDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_device_certificate_with_options(request, runtime)

    async def list_device_certificate_async(
        self,
        request: main_models.ListDeviceCertificateRequest,
    ) -> main_models.ListDeviceCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_device_certificate_with_options_async(request, runtime)

    def list_device_certificate_by_ca_sn_with_options(
        self,
        request: main_models.ListDeviceCertificateByCaSnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCertificateByCaSnResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCertificateByCaSn',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCertificateByCaSnResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_certificate_by_ca_sn_with_options_async(
        self,
        request: main_models.ListDeviceCertificateByCaSnRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCertificateByCaSnResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCertificateByCaSn',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCertificateByCaSnResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_certificate_by_ca_sn(
        self,
        request: main_models.ListDeviceCertificateByCaSnRequest,
    ) -> main_models.ListDeviceCertificateByCaSnResponse:
        runtime = RuntimeOptions()
        return self.list_device_certificate_by_ca_sn_with_options(request, runtime)

    async def list_device_certificate_by_ca_sn_async(
        self,
        request: main_models.ListDeviceCertificateByCaSnRequest,
    ) -> main_models.ListDeviceCertificateByCaSnResponse:
        runtime = RuntimeOptions()
        return await self.list_device_certificate_by_ca_sn_with_options_async(request, runtime)

    def list_device_credential_client_id_with_options(
        self,
        request: main_models.ListDeviceCredentialClientIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCredentialClientIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCredentialClientId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCredentialClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_device_credential_client_id_with_options_async(
        self,
        request: main_models.ListDeviceCredentialClientIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeviceCredentialClientIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeviceCredentialClientId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeviceCredentialClientIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_device_credential_client_id(
        self,
        request: main_models.ListDeviceCredentialClientIdRequest,
    ) -> main_models.ListDeviceCredentialClientIdResponse:
        runtime = RuntimeOptions()
        return self.list_device_credential_client_id_with_options(request, runtime)

    async def list_device_credential_client_id_async(
        self,
        request: main_models.ListDeviceCredentialClientIdRequest,
    ) -> main_models.ListDeviceCredentialClientIdResponse:
        runtime = RuntimeOptions()
        return await self.list_device_credential_client_id_with_options_async(request, runtime)

    def list_group_id_with_options(
        self,
        request: main_models.ListGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_id_with_options_async(
        self,
        request: main_models.ListGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroupId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group_id(
        self,
        request: main_models.ListGroupIdRequest,
    ) -> main_models.ListGroupIdResponse:
        runtime = RuntimeOptions()
        return self.list_group_id_with_options(request, runtime)

    async def list_group_id_async(
        self,
        request: main_models.ListGroupIdRequest,
    ) -> main_models.ListGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.list_group_id_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def query_custom_auth_connect_black_with_options(
        self,
        request: main_models.QueryCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthConnectBlackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthConnectBlackResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_custom_auth_connect_black_with_options_async(
        self,
        request: main_models.QueryCustomAuthConnectBlackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthConnectBlackResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthConnectBlack',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthConnectBlackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_custom_auth_connect_black(
        self,
        request: main_models.QueryCustomAuthConnectBlackRequest,
    ) -> main_models.QueryCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return self.query_custom_auth_connect_black_with_options(request, runtime)

    async def query_custom_auth_connect_black_async(
        self,
        request: main_models.QueryCustomAuthConnectBlackRequest,
    ) -> main_models.QueryCustomAuthConnectBlackResponse:
        runtime = RuntimeOptions()
        return await self.query_custom_auth_connect_black_with_options_async(request, runtime)

    def query_custom_auth_identity_with_options(
        self,
        request: main_models.QueryCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthIdentityResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_custom_auth_identity_with_options_async(
        self,
        request: main_models.QueryCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthIdentityResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_custom_auth_identity(
        self,
        request: main_models.QueryCustomAuthIdentityRequest,
    ) -> main_models.QueryCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return self.query_custom_auth_identity_with_options(request, runtime)

    async def query_custom_auth_identity_async(
        self,
        request: main_models.QueryCustomAuthIdentityRequest,
    ) -> main_models.QueryCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return await self.query_custom_auth_identity_with_options_async(request, runtime)

    def query_custom_auth_permission_with_options(
        self,
        request: main_models.QueryCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthPermissionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_custom_auth_permission_with_options_async(
        self,
        request: main_models.QueryCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomAuthPermissionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomAuthPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_custom_auth_permission(
        self,
        request: main_models.QueryCustomAuthPermissionRequest,
    ) -> main_models.QueryCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return self.query_custom_auth_permission_with_options(request, runtime)

    async def query_custom_auth_permission_async(
        self,
        request: main_models.QueryCustomAuthPermissionRequest,
    ) -> main_models.QueryCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return await self.query_custom_auth_permission_with_options_async(request, runtime)

    def query_mqtt_trace_device_with_options(
        self,
        request: main_models.QueryMqttTraceDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceDevice',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_device_with_options_async(
        self,
        request: main_models.QueryMqttTraceDeviceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceDeviceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceDevice',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_device(
        self,
        request: main_models.QueryMqttTraceDeviceRequest,
    ) -> main_models.QueryMqttTraceDeviceResponse:
        runtime = RuntimeOptions()
        return self.query_mqtt_trace_device_with_options(request, runtime)

    async def query_mqtt_trace_device_async(
        self,
        request: main_models.QueryMqttTraceDeviceRequest,
    ) -> main_models.QueryMqttTraceDeviceResponse:
        runtime = RuntimeOptions()
        return await self.query_mqtt_trace_device_with_options_async(request, runtime)

    def query_mqtt_trace_message_of_client_with_options(
        self,
        request: main_models.QueryMqttTraceMessageOfClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessageOfClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessageOfClient',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessageOfClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_of_client_with_options_async(
        self,
        request: main_models.QueryMqttTraceMessageOfClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessageOfClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessageOfClient',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessageOfClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_of_client(
        self,
        request: main_models.QueryMqttTraceMessageOfClientRequest,
    ) -> main_models.QueryMqttTraceMessageOfClientResponse:
        runtime = RuntimeOptions()
        return self.query_mqtt_trace_message_of_client_with_options(request, runtime)

    async def query_mqtt_trace_message_of_client_async(
        self,
        request: main_models.QueryMqttTraceMessageOfClientRequest,
    ) -> main_models.QueryMqttTraceMessageOfClientResponse:
        runtime = RuntimeOptions()
        return await self.query_mqtt_trace_message_of_client_with_options_async(request, runtime)

    def query_mqtt_trace_message_publish_with_options(
        self,
        request: main_models.QueryMqttTraceMessagePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessagePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessagePublish',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessagePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_publish_with_options_async(
        self,
        request: main_models.QueryMqttTraceMessagePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessagePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessagePublish',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessagePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_publish(
        self,
        request: main_models.QueryMqttTraceMessagePublishRequest,
    ) -> main_models.QueryMqttTraceMessagePublishResponse:
        runtime = RuntimeOptions()
        return self.query_mqtt_trace_message_publish_with_options(request, runtime)

    async def query_mqtt_trace_message_publish_async(
        self,
        request: main_models.QueryMqttTraceMessagePublishRequest,
    ) -> main_models.QueryMqttTraceMessagePublishResponse:
        runtime = RuntimeOptions()
        return await self.query_mqtt_trace_message_publish_with_options_async(request, runtime)

    def query_mqtt_trace_message_subscribe_with_options(
        self,
        request: main_models.QueryMqttTraceMessageSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessageSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessageSubscribe',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessageSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_mqtt_trace_message_subscribe_with_options_async(
        self,
        request: main_models.QueryMqttTraceMessageSubscribeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMqttTraceMessageSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_region_id):
            query['MqttRegionId'] = request.mqtt_region_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMqttTraceMessageSubscribe',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMqttTraceMessageSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_mqtt_trace_message_subscribe(
        self,
        request: main_models.QueryMqttTraceMessageSubscribeRequest,
    ) -> main_models.QueryMqttTraceMessageSubscribeResponse:
        runtime = RuntimeOptions()
        return self.query_mqtt_trace_message_subscribe_with_options(request, runtime)

    async def query_mqtt_trace_message_subscribe_async(
        self,
        request: main_models.QueryMqttTraceMessageSubscribeRequest,
    ) -> main_models.QueryMqttTraceMessageSubscribeResponse:
        runtime = RuntimeOptions()
        return await self.query_mqtt_trace_message_subscribe_with_options_async(request, runtime)

    def query_session_by_client_id_with_options(
        self,
        request: main_models.QuerySessionByClientIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionByClientIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionByClientId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionByClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_by_client_id_with_options_async(
        self,
        request: main_models.QuerySessionByClientIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionByClientIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionByClientId',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionByClientIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_by_client_id(
        self,
        request: main_models.QuerySessionByClientIdRequest,
    ) -> main_models.QuerySessionByClientIdResponse:
        runtime = RuntimeOptions()
        return self.query_session_by_client_id_with_options(request, runtime)

    async def query_session_by_client_id_async(
        self,
        request: main_models.QuerySessionByClientIdRequest,
    ) -> main_models.QuerySessionByClientIdResponse:
        runtime = RuntimeOptions()
        return await self.query_session_by_client_id_with_options_async(request, runtime)

    def query_token_with_options(
        self,
        request: main_models.QueryTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_token_with_options_async(
        self,
        request: main_models.QueryTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_token(
        self,
        request: main_models.QueryTokenRequest,
    ) -> main_models.QueryTokenResponse:
        runtime = RuntimeOptions()
        return self.query_token_with_options(request, runtime)

    async def query_token_async(
        self,
        request: main_models.QueryTokenRequest,
    ) -> main_models.QueryTokenResponse:
        runtime = RuntimeOptions()
        return await self.query_token_with_options_async(request, runtime)

    def query_wildcard_by_topic_with_options(
        self,
        request: main_models.QueryWildcardByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWildcardByTopicResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWildcardByTopic',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWildcardByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_wildcard_by_topic_with_options_async(
        self,
        request: main_models.QueryWildcardByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryWildcardByTopicResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryWildcardByTopic',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryWildcardByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_wildcard_by_topic(
        self,
        request: main_models.QueryWildcardByTopicRequest,
    ) -> main_models.QueryWildcardByTopicResponse:
        runtime = RuntimeOptions()
        return self.query_wildcard_by_topic_with_options(request, runtime)

    async def query_wildcard_by_topic_async(
        self,
        request: main_models.QueryWildcardByTopicRequest,
    ) -> main_models.QueryWildcardByTopicResponse:
        runtime = RuntimeOptions()
        return await self.query_wildcard_by_topic_with_options_async(request, runtime)

    def refresh_device_credential_with_options(
        self,
        request: main_models.RefreshDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_device_credential_with_options_async(
        self,
        request: main_models.RefreshDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_device_credential(
        self,
        request: main_models.RefreshDeviceCredentialRequest,
    ) -> main_models.RefreshDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return self.refresh_device_credential_with_options(request, runtime)

    async def refresh_device_credential_async(
        self,
        request: main_models.RefreshDeviceCredentialRequest,
    ) -> main_models.RefreshDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return await self.refresh_device_credential_with_options_async(request, runtime)

    def register_ca_certificate_with_options(
        self,
        request: main_models.RegisterCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_content):
            query['CaContent'] = request.ca_content
        if not DaraCore.is_null(request.ca_name):
            query['CaName'] = request.ca_name
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.verification_content):
            query['VerificationContent'] = request.verification_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_ca_certificate_with_options_async(
        self,
        request: main_models.RegisterCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_content):
            query['CaContent'] = request.ca_content
        if not DaraCore.is_null(request.ca_name):
            query['CaName'] = request.ca_name
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.verification_content):
            query['VerificationContent'] = request.verification_content
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterCaCertificate',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_ca_certificate(
        self,
        request: main_models.RegisterCaCertificateRequest,
    ) -> main_models.RegisterCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.register_ca_certificate_with_options(request, runtime)

    async def register_ca_certificate_async(
        self,
        request: main_models.RegisterCaCertificateRequest,
    ) -> main_models.RegisterCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.register_ca_certificate_with_options_async(request, runtime)

    def register_device_credential_with_options(
        self,
        request: main_models.RegisterDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_device_credential_with_options_async(
        self,
        request: main_models.RegisterDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_device_credential(
        self,
        request: main_models.RegisterDeviceCredentialRequest,
    ) -> main_models.RegisterDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return self.register_device_credential_with_options(request, runtime)

    async def register_device_credential_async(
        self,
        request: main_models.RegisterDeviceCredentialRequest,
    ) -> main_models.RegisterDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return await self.register_device_credential_with_options_async(request, runtime)

    def revoke_token_with_options(
        self,
        request: main_models.RevokeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_token_with_options_async(
        self,
        request: main_models.RevokeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevokeToken',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_token(
        self,
        request: main_models.RevokeTokenRequest,
    ) -> main_models.RevokeTokenResponse:
        runtime = RuntimeOptions()
        return self.revoke_token_with_options(request, runtime)

    async def revoke_token_async(
        self,
        request: main_models.RevokeTokenRequest,
    ) -> main_models.RevokeTokenResponse:
        runtime = RuntimeOptions()
        return await self.revoke_token_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: main_models.SendMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_topic):
            query['MqttTopic'] = request.mqtt_topic
        if not DaraCore.is_null(request.payload):
            query['Payload'] = request.payload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: main_models.SendMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMessageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.mqtt_topic):
            query['MqttTopic'] = request.mqtt_topic
        if not DaraCore.is_null(request.payload):
            query['Payload'] = request.payload
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMessage',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_message(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: main_models.SendMessageRequest,
    ) -> main_models.SendMessageResponse:
        runtime = RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def set_sni_config_with_options(
        self,
        request: main_models.SetSniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSniConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_certificate):
            query['DefaultCertificate'] = request.default_certificate
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sni_config):
            query['SniConfig'] = request.sni_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSniConfig',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_sni_config_with_options_async(
        self,
        request: main_models.SetSniConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSniConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_certificate):
            query['DefaultCertificate'] = request.default_certificate
        if not DaraCore.is_null(request.mqtt_instance_id):
            query['MqttInstanceId'] = request.mqtt_instance_id
        if not DaraCore.is_null(request.sni_config):
            query['SniConfig'] = request.sni_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetSniConfig',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSniConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_sni_config(
        self,
        request: main_models.SetSniConfigRequest,
    ) -> main_models.SetSniConfigResponse:
        runtime = RuntimeOptions()
        return self.set_sni_config_with_options(request, runtime)

    async def set_sni_config_async(
        self,
        request: main_models.SetSniConfigRequest,
    ) -> main_models.SetSniConfigResponse:
        runtime = RuntimeOptions()
        return await self.set_sni_config_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_register_device_credential_with_options(
        self,
        request: main_models.UnRegisterDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnRegisterDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnRegisterDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnRegisterDeviceCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_register_device_credential_with_options_async(
        self,
        request: main_models.UnRegisterDeviceCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnRegisterDeviceCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnRegisterDeviceCredential',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnRegisterDeviceCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_register_device_credential(
        self,
        request: main_models.UnRegisterDeviceCredentialRequest,
    ) -> main_models.UnRegisterDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return self.un_register_device_credential_with_options(request, runtime)

    async def un_register_device_credential_async(
        self,
        request: main_models.UnRegisterDeviceCredentialRequest,
    ) -> main_models.UnRegisterDeviceCredentialResponse:
        runtime = RuntimeOptions()
        return await self.un_register_device_credential_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_auth_identity_with_options(
        self,
        request: main_models.UpdateCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret):
            body['Secret'] = request.secret
        if not DaraCore.is_null(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAuthIdentityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_auth_identity_with_options_async(
        self,
        request: main_models.UpdateCustomAuthIdentityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAuthIdentityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.secret):
            body['Secret'] = request.secret
        if not DaraCore.is_null(request.sign_mode):
            body['SignMode'] = request.sign_mode
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAuthIdentity',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAuthIdentityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_auth_identity(
        self,
        request: main_models.UpdateCustomAuthIdentityRequest,
    ) -> main_models.UpdateCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return self.update_custom_auth_identity_with_options(request, runtime)

    async def update_custom_auth_identity_async(
        self,
        request: main_models.UpdateCustomAuthIdentityRequest,
    ) -> main_models.UpdateCustomAuthIdentityResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_auth_identity_with_options_async(request, runtime)

    def update_custom_auth_permission_with_options(
        self,
        request: main_models.UpdateCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.effect):
            body['Effect'] = request.effect
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAuthPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_auth_permission_with_options_async(
        self,
        request: main_models.UpdateCustomAuthPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCustomAuthPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.effect):
            body['Effect'] = request.effect
        if not DaraCore.is_null(request.identity):
            body['Identity'] = request.identity
        if not DaraCore.is_null(request.identity_type):
            body['IdentityType'] = request.identity_type
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.permit_action):
            body['PermitAction'] = request.permit_action
        if not DaraCore.is_null(request.topic):
            body['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCustomAuthPermission',
            version = '2020-04-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCustomAuthPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_auth_permission(
        self,
        request: main_models.UpdateCustomAuthPermissionRequest,
    ) -> main_models.UpdateCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return self.update_custom_auth_permission_with_options(request, runtime)

    async def update_custom_auth_permission_async(
        self,
        request: main_models.UpdateCustomAuthPermissionRequest,
    ) -> main_models.UpdateCustomAuthPermissionResponse:
        runtime = RuntimeOptions()
        return await self.update_custom_auth_permission_with_options_async(request, runtime)
