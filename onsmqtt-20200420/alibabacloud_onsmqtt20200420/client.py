# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_onsmqtt20200420 import models as ons_mqtt_20200420_models
from alibabacloud_tea_util import models as util_models


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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def apply_token_with_options(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.ApplyTokenResponse().from_map(
            self.do_rpcrequest('ApplyToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.ApplyTokenResponse().from_map(
            await self.do_rpcrequest_async('ApplyToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_token(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_token_with_options(request, runtime)

    async def apply_token_async(
        self,
        request: ons_mqtt_20200420_models.ApplyTokenRequest,
    ) -> ons_mqtt_20200420_models.ApplyTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_token_with_options_async(request, runtime)

    def batch_query_session_by_client_ids_with_options(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse().from_map(
            self.do_rpcrequest('BatchQuerySessionByClientIds', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_query_session_by_client_ids_with_options_async(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse().from_map(
            await self.do_rpcrequest_async('BatchQuerySessionByClientIds', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_query_session_by_client_ids(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_query_session_by_client_ids_with_options(request, runtime)

    async def batch_query_session_by_client_ids_async(
        self,
        request: ons_mqtt_20200420_models.BatchQuerySessionByClientIdsRequest,
    ) -> ons_mqtt_20200420_models.BatchQuerySessionByClientIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_query_session_by_client_ids_with_options_async(request, runtime)

    def create_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.CreateGroupIdResponse().from_map(
            self.do_rpcrequest('CreateGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.CreateGroupIdResponse().from_map(
            await self.do_rpcrequest_async('CreateGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group_id(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_id_with_options(request, runtime)

    async def create_group_id_async(
        self,
        request: ons_mqtt_20200420_models.CreateGroupIdRequest,
    ) -> ons_mqtt_20200420_models.CreateGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_id_with_options_async(request, runtime)

    def delete_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.DeleteGroupIdResponse().from_map(
            self.do_rpcrequest('DeleteGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.DeleteGroupIdResponse().from_map(
            await self.do_rpcrequest_async('DeleteGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group_id(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_group_id_with_options(request, runtime)

    async def delete_group_id_async(
        self,
        request: ons_mqtt_20200420_models.DeleteGroupIdRequest,
    ) -> ons_mqtt_20200420_models.DeleteGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_group_id_with_options_async(request, runtime)

    def get_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.GetDeviceCredentialResponse().from_map(
            self.do_rpcrequest('GetDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.GetDeviceCredentialResponse().from_map(
            await self.do_rpcrequest_async('GetDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_credential(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_device_credential_with_options(request, runtime)

    async def get_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.GetDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.GetDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_device_credential_with_options_async(request, runtime)

    def list_group_id_with_options(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.ListGroupIdResponse().from_map(
            self.do_rpcrequest('ListGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_group_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.ListGroupIdResponse().from_map(
            await self.do_rpcrequest_async('ListGroupId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_group_id(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_group_id_with_options(request, runtime)

    async def list_group_id_async(
        self,
        request: ons_mqtt_20200420_models.ListGroupIdRequest,
    ) -> ons_mqtt_20200420_models.ListGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_group_id_with_options_async(request, runtime)

    def query_session_by_client_id_with_options(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.QuerySessionByClientIdResponse().from_map(
            self.do_rpcrequest('QuerySessionByClientId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_session_by_client_id_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.QuerySessionByClientIdResponse().from_map(
            await self.do_rpcrequest_async('QuerySessionByClientId', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_session_by_client_id(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_session_by_client_id_with_options(request, runtime)

    async def query_session_by_client_id_async(
        self,
        request: ons_mqtt_20200420_models.QuerySessionByClientIdRequest,
    ) -> ons_mqtt_20200420_models.QuerySessionByClientIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_session_by_client_id_with_options_async(request, runtime)

    def query_token_with_options(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.QueryTokenResponse().from_map(
            self.do_rpcrequest('QueryToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.QueryTokenResponse().from_map(
            await self.do_rpcrequest_async('QueryToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_token(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_token_with_options(request, runtime)

    async def query_token_async(
        self,
        request: ons_mqtt_20200420_models.QueryTokenRequest,
    ) -> ons_mqtt_20200420_models.QueryTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_token_with_options_async(request, runtime)

    def refresh_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RefreshDeviceCredentialResponse().from_map(
            self.do_rpcrequest('RefreshDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RefreshDeviceCredentialResponse().from_map(
            await self.do_rpcrequest_async('RefreshDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_device_credential(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_credential_with_options(request, runtime)

    async def refresh_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.RefreshDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RefreshDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_device_credential_with_options_async(request, runtime)

    def register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RegisterDeviceCredentialResponse().from_map(
            self.do_rpcrequest('RegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RegisterDeviceCredentialResponse().from_map(
            await self.do_rpcrequest_async('RegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_device_credential(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_device_credential_with_options(request, runtime)

    async def register_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.RegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.RegisterDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_device_credential_with_options_async(request, runtime)

    def revoke_token_with_options(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RevokeTokenResponse().from_map(
            self.do_rpcrequest('RevokeToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_token_with_options_async(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.RevokeTokenResponse().from_map(
            await self.do_rpcrequest_async('RevokeToken', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_token(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_token_with_options(request, runtime)

    async def revoke_token_async(
        self,
        request: ons_mqtt_20200420_models.RevokeTokenRequest,
    ) -> ons_mqtt_20200420_models.RevokeTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_token_with_options_async(request, runtime)

    def send_message_with_options(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.SendMessageResponse().from_map(
            self.do_rpcrequest('SendMessage', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_message_with_options_async(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.SendMessageResponse().from_map(
            await self.do_rpcrequest_async('SendMessage', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_message_with_options(request, runtime)

    async def send_message_async(
        self,
        request: ons_mqtt_20200420_models.SendMessageRequest,
    ) -> ons_mqtt_20200420_models.SendMessageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_message_with_options_async(request, runtime)

    def un_register_device_credential_with_options(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse().from_map(
            self.do_rpcrequest('UnRegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_register_device_credential_with_options_async(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse().from_map(
            await self.do_rpcrequest_async('UnRegisterDeviceCredential', '2020-04-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_register_device_credential(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_register_device_credential_with_options(request, runtime)

    async def un_register_device_credential_async(
        self,
        request: ons_mqtt_20200420_models.UnRegisterDeviceCredentialRequest,
    ) -> ons_mqtt_20200420_models.UnRegisterDeviceCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_register_device_credential_with_options_async(request, runtime)
