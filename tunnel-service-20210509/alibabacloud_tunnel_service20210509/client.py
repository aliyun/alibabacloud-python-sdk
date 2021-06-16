# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tunnel_service20210509 import models as tunnel__service_20210509_models
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
        self._endpoint = self.get_endpoint('tunnel-service', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_session(
        self,
        session_id: str,
    ) -> tunnel__service_20210509_models.DeleteSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_session_with_options(session_id, headers, runtime)

    async def delete_session_async(
        self,
        session_id: str,
    ) -> tunnel__service_20210509_models.DeleteSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_session_with_options_async(session_id, headers, runtime)

    def delete_session_with_options(
        self,
        session_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.DeleteSessionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.DeleteSessionResponse(),
            self.do_roarequest('DeleteSession', '2021-05-09', 'HTTPS', 'DELETE', 'AK', f'/v1/sessions/{session_id}', 'json', req, runtime)
        )

    async def delete_session_with_options_async(
        self,
        session_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.DeleteSessionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.DeleteSessionResponse(),
            await self.do_roarequest_async('DeleteSession', '2021-05-09', 'HTTPS', 'DELETE', 'AK', f'/v1/sessions/{session_id}', 'json', req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> tunnel__service_20210509_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> tunnel__service_20210509_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetInstanceResponse(),
            self.do_roarequest('GetInstance', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/instances/{instance_id}', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.GetInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetInstanceResponse(),
            await self.do_roarequest_async('GetInstance', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/instances/{instance_id}', 'json', req, runtime)
        )

    def heart_beat(
        self,
        request: tunnel__service_20210509_models.HeartBeatRequest,
    ) -> tunnel__service_20210509_models.HeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.heart_beat_with_options(request, headers, runtime)

    async def heart_beat_async(
        self,
        request: tunnel__service_20210509_models.HeartBeatRequest,
    ) -> tunnel__service_20210509_models.HeartBeatResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.heart_beat_with_options_async(request, headers, runtime)

    def heart_beat_with_options(
        self,
        request: tunnel__service_20210509_models.HeartBeatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.HeartBeatResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.session_status):
            body['sessionStatus'] = request.session_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.HeartBeatResponse(),
            self.do_roarequest('HeartBeat', '2021-05-09', 'HTTPS', 'PUT', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )

    async def heart_beat_with_options_async(
        self,
        request: tunnel__service_20210509_models.HeartBeatRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.HeartBeatResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.session_status):
            body['sessionStatus'] = request.session_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.HeartBeatResponse(),
            await self.do_roarequest_async('HeartBeat', '2021-05-09', 'HTTPS', 'PUT', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )

    def un_register_instance(
        self,
        instance_id: str,
    ) -> tunnel__service_20210509_models.UnRegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_register_instance_with_options(instance_id, headers, runtime)

    async def un_register_instance_async(
        self,
        instance_id: str,
    ) -> tunnel__service_20210509_models.UnRegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_register_instance_with_options_async(instance_id, headers, runtime)

    def un_register_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.UnRegisterInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.UnRegisterInstanceResponse(),
            self.do_roarequest('UnRegisterInstance', '2021-05-09', 'HTTPS', 'PUT', 'AK', f'/v1/instances/{instance_id}', 'json', req, runtime)
        )

    async def un_register_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.UnRegisterInstanceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.UnRegisterInstanceResponse(),
            await self.do_roarequest_async('UnRegisterInstance', '2021-05-09', 'HTTPS', 'PUT', 'AK', f'/v1/instances/{instance_id}', 'json', req, runtime)
        )

    def create_session(
        self,
        request: tunnel__service_20210509_models.CreateSessionRequest,
    ) -> tunnel__service_20210509_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_session_with_options(request, headers, runtime)

    async def create_session_async(
        self,
        request: tunnel__service_20210509_models.CreateSessionRequest,
    ) -> tunnel__service_20210509_models.CreateSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_session_with_options_async(request, headers, runtime)

    def create_session_with_options(
        self,
        request: tunnel__service_20210509_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_name):
            body['sessionName'] = request.session_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.CreateSessionResponse(),
            self.do_roarequest('CreateSession', '2021-05-09', 'HTTPS', 'POST', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: tunnel__service_20210509_models.CreateSessionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.CreateSessionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_name):
            body['sessionName'] = request.session_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.CreateSessionResponse(),
            await self.do_roarequest_async('CreateSession', '2021-05-09', 'HTTPS', 'POST', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )

    def register_instance(
        self,
        request: tunnel__service_20210509_models.RegisterInstanceRequest,
    ) -> tunnel__service_20210509_models.RegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.register_instance_with_options(request, headers, runtime)

    async def register_instance_async(
        self,
        request: tunnel__service_20210509_models.RegisterInstanceRequest,
    ) -> tunnel__service_20210509_models.RegisterInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.register_instance_with_options_async(request, headers, runtime)

    def register_instance_with_options(
        self,
        request: tunnel__service_20210509_models.RegisterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.RegisterInstanceResponse(),
            self.do_roarequest('RegisterInstance', '2021-05-09', 'HTTPS', 'POST', 'AK', f'/v1/instances/', 'json', req, runtime)
        )

    async def register_instance_with_options_async(
        self,
        request: tunnel__service_20210509_models.RegisterInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.RegisterInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.RegisterInstanceResponse(),
            await self.do_roarequest_async('RegisterInstance', '2021-05-09', 'HTTPS', 'POST', 'AK', f'/v1/instances/', 'json', req, runtime)
        )

    def get_session(
        self,
        session_id: str,
    ) -> tunnel__service_20210509_models.GetSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_session_with_options(session_id, headers, runtime)

    async def get_session_async(
        self,
        session_id: str,
    ) -> tunnel__service_20210509_models.GetSessionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_session_with_options_async(session_id, headers, runtime)

    def get_session_with_options(
        self,
        session_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.GetSessionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetSessionResponse(),
            self.do_roarequest('GetSession', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/sessions/{session_id}', 'json', req, runtime)
        )

    async def get_session_with_options_async(
        self,
        session_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.GetSessionResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.GetSessionResponse(),
            await self.do_roarequest_async('GetSession', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/sessions/{session_id}', 'json', req, runtime)
        )

    def list_sessions(
        self,
        request: tunnel__service_20210509_models.ListSessionsRequest,
    ) -> tunnel__service_20210509_models.ListSessionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_sessions_with_options(request, headers, runtime)

    async def list_sessions_async(
        self,
        request: tunnel__service_20210509_models.ListSessionsRequest,
    ) -> tunnel__service_20210509_models.ListSessionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_sessions_with_options_async(request, headers, runtime)

    def list_sessions_with_options(
        self,
        request: tunnel__service_20210509_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.ListSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.ListSessionsResponse(),
            self.do_roarequest('ListSessions', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )

    async def list_sessions_with_options_async(
        self,
        request: tunnel__service_20210509_models.ListSessionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tunnel__service_20210509_models.ListSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            tunnel__service_20210509_models.ListSessionsResponse(),
            await self.do_roarequest_async('ListSessions', '2021-05-09', 'HTTPS', 'GET', 'AK', f'/v1/sessions/', 'json', req, runtime)
        )
