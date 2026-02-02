# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_oss.client import Client as GatewayClientClient
from alibabacloud_hcs_mgw20240626 import models as main_models
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
        self._product_id = 'hcs-mgw'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''

    def create_address_with_options(
        self,
        userid: str,
        request: main_models.CreateAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def create_address_with_options_async(
        self,
        userid: str,
        request: main_models.CreateAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_address(
        self,
        userid: str,
        request: main_models.CreateAddressRequest,
    ) -> main_models.CreateAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_address_with_options(userid, request, headers, runtime)

    async def create_address_async(
        self,
        userid: str,
        request: main_models.CreateAddressRequest,
    ) -> main_models.CreateAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_address_with_options_async(userid, request, headers, runtime)

    def create_agent_with_options(
        self,
        userid: str,
        request: main_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_agent):
            body['ImportAgent'] = request.import_agent
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        userid: str,
        request: main_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_agent):
            body['ImportAgent'] = request.import_agent
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_agent(
        self,
        userid: str,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_with_options(userid, request, headers, runtime)

    async def create_agent_async(
        self,
        userid: str,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_with_options_async(userid, request, headers, runtime)

    def create_job_with_options(
        self,
        userid: str,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.execute(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        userid: str,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_job(
        self,
        userid: str,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_job_with_options(userid, request, headers, runtime)

    async def create_job_async(
        self,
        userid: str,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(userid, request, headers, runtime)

    def create_report_with_options(
        self,
        userid: str,
        request: main_models.CreateReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateReportResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.create_report):
            body['CreateReport'] = request.create_report
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReport',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateReportResponse(),
            self.execute(params, req, runtime)
        )

    async def create_report_with_options_async(
        self,
        userid: str,
        request: main_models.CreateReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateReportResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.create_report):
            body['CreateReport'] = request.create_report
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReport',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/report',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateReportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_report(
        self,
        userid: str,
        request: main_models.CreateReportRequest,
    ) -> main_models.CreateReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_report_with_options(userid, request, headers, runtime)

    async def create_report_async(
        self,
        userid: str,
        request: main_models.CreateReportRequest,
    ) -> main_models.CreateReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_report_with_options_async(userid, request, headers, runtime)

    def create_tunnel_with_options(
        self,
        userid: str,
        request: main_models.CreateTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def create_tunnel_with_options_async(
        self,
        userid: str,
        request: main_models.CreateTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.CreateTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_tunnel(
        self,
        userid: str,
        request: main_models.CreateTunnelRequest,
    ) -> main_models.CreateTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_tunnel_with_options(userid, request, headers, runtime)

    async def create_tunnel_async(
        self,
        userid: str,
        request: main_models.CreateTunnelRequest,
    ) -> main_models.CreateTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_tunnel_with_options_async(userid, request, headers, runtime)

    def delete_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_address(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.DeleteAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_address_with_options(userid, address_name, headers, runtime)

    async def delete_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.DeleteAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_address_with_options_async(userid, address_name, headers, runtime)

    def delete_agent_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_agent(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_with_options(userid, agent_name, headers, runtime)

    async def delete_agent_async(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_with_options_async(userid, agent_name, headers, runtime)

    def delete_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: main_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_job(
        self,
        userid: str,
        job_name: str,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(userid, job_name, request, headers, runtime)

    async def delete_job_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.DeleteJobRequest,
    ) -> main_models.DeleteJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(userid, job_name, request, headers, runtime)

    def delete_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTunnelResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTunnelResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.DeleteTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_tunnel(
        self,
        userid: str,
        tunnel_id: str,
    ) -> main_models.DeleteTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_tunnel_with_options(userid, tunnel_id, headers, runtime)

    async def delete_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
    ) -> main_models.DeleteTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_tunnel_with_options_async(userid, tunnel_id, headers, runtime)

    def get_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def get_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_address(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.GetAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_address_with_options(userid, address_name, headers, runtime)

    async def get_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.GetAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_address_with_options_async(userid, address_name, headers, runtime)

    def get_agent_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_agent(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_with_options(userid, agent_name, headers, runtime)

    async def get_agent_async(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.GetAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_with_options_async(userid, agent_name, headers, runtime)

    def get_agent_status_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentStatusResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentStatus',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}?status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAgentStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_agent_status_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentStatusResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetAgentStatus',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agent/{agent_name}?status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetAgentStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_agent_status(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.GetAgentStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_agent_status_with_options(userid, agent_name, headers, runtime)

    async def get_agent_status_async(
        self,
        userid: str,
        agent_name: str,
    ) -> main_models.GetAgentStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_agent_status_with_options_async(userid, agent_name, headers, runtime)

    def get_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.by_version):
            query['byVersion'] = request.by_version
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.execute(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.by_version):
            query['byVersion'] = request.by_version
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_job(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_with_options(userid, job_name, request, headers, runtime)

    async def get_job_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(userid, job_name, request, headers, runtime)

    def get_job_result_with_options(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResultResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobResult',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}?jobResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetJobResultResponse(),
            self.execute(params, req, runtime)
        )

    async def get_job_result_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResultResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobResult',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}?jobResult',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetJobResultResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_job_result(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobResultRequest,
    ) -> main_models.GetJobResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_result_with_options(userid, job_name, request, headers, runtime)

    async def get_job_result_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.GetJobResultRequest,
    ) -> main_models.GetJobResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_result_with_options_async(userid, job_name, request, headers, runtime)

    def get_report_with_options(
        self,
        userid: str,
        request: main_models.GetReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReportResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReport',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetReportResponse(),
            self.execute(params, req, runtime)
        )

    async def get_report_with_options_async(
        self,
        userid: str,
        request: main_models.GetReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReportResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        if not DaraCore.is_null(request.version):
            query['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetReport',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/report',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetReportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_report(
        self,
        userid: str,
        request: main_models.GetReportRequest,
    ) -> main_models.GetReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_report_with_options(userid, request, headers, runtime)

    async def get_report_async(
        self,
        userid: str,
        request: main_models.GetReportRequest,
    ) -> main_models.GetReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_report_with_options_async(userid, request, headers, runtime)

    def get_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTunnelResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def get_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTunnelResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.GetTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_tunnel(
        self,
        userid: str,
        tunnel_id: str,
    ) -> main_models.GetTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_tunnel_with_options(userid, tunnel_id, headers, runtime)

    async def get_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
    ) -> main_models.GetTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_tunnel_with_options_async(userid, tunnel_id, headers, runtime)

    def list_address_with_options(
        self,
        userid: str,
        request: main_models.ListAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/addresslist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def list_address_with_options_async(
        self,
        userid: str,
        request: main_models.ListAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/addresslist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_address(
        self,
        userid: str,
        request: main_models.ListAddressRequest,
    ) -> main_models.ListAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_address_with_options(userid, request, headers, runtime)

    async def list_address_async(
        self,
        userid: str,
        request: main_models.ListAddressRequest,
    ) -> main_models.ListAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_address_with_options_async(userid, request, headers, runtime)

    def list_agent_with_options(
        self,
        userid: str,
        request: main_models.ListAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agentlist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def list_agent_with_options_async(
        self,
        userid: str,
        request: main_models.ListAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgent',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/agentlist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_agent(
        self,
        userid: str,
        request: main_models.ListAgentRequest,
    ) -> main_models.ListAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agent_with_options(userid, request, headers, runtime)

    async def list_agent_async(
        self,
        userid: str,
        request: main_models.ListAgentRequest,
    ) -> main_models.ListAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agent_with_options_async(userid, request, headers, runtime)

    def list_job_with_options(
        self,
        userid: str,
        request: main_models.ListJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.parent_name):
            query['parentName'] = request.parent_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/joblist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListJobResponse(),
            self.execute(params, req, runtime)
        )

    async def list_job_with_options_async(
        self,
        userid: str,
        request: main_models.ListJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.all):
            query['all'] = request.all
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.parent_name):
            query['parentName'] = request.parent_name
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/joblist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_job(
        self,
        userid: str,
        request: main_models.ListJobRequest,
    ) -> main_models.ListJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_with_options(userid, request, headers, runtime)

    async def list_job_async(
        self,
        userid: str,
        request: main_models.ListJobRequest,
    ) -> main_models.ListJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_with_options_async(userid, request, headers, runtime)

    def list_job_history_with_options(
        self,
        userid: str,
        job_name: str,
        request: main_models.ListJobHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobHistoryResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobHistory',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/jobhistory/{job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListJobHistoryResponse(),
            self.execute(params, req, runtime)
        )

    async def list_job_history_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.ListJobHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobHistoryResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobHistory',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/jobhistory/{job_name}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListJobHistoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_job_history(
        self,
        userid: str,
        job_name: str,
        request: main_models.ListJobHistoryRequest,
    ) -> main_models.ListJobHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_history_with_options(userid, job_name, request, headers, runtime)

    async def list_job_history_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.ListJobHistoryRequest,
    ) -> main_models.ListJobHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_history_with_options_async(userid, job_name, request, headers, runtime)

    def list_tunnel_with_options(
        self,
        userid: str,
        request: main_models.ListTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnellist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tunnel_with_options_async(
        self,
        userid: str,
        request: main_models.ListTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not DaraCore.is_null(request.count):
            query['count'] = request.count
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnellist',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.ListTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tunnel(
        self,
        userid: str,
        request: main_models.ListTunnelRequest,
    ) -> main_models.ListTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tunnel_with_options(userid, request, headers, runtime)

    async def list_tunnel_async(
        self,
        userid: str,
        request: main_models.ListTunnelRequest,
    ) -> main_models.ListTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tunnel_with_options_async(userid, request, headers, runtime)

    def update_address_with_options(
        self,
        userid: str,
        address_name: str,
        request: main_models.UpdateAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def update_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        request: main_models.UpdateAddressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAddressResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_address(
        self,
        userid: str,
        address_name: str,
        request: main_models.UpdateAddressRequest,
    ) -> main_models.UpdateAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_address_with_options(userid, address_name, request, headers, runtime)

    async def update_address_async(
        self,
        userid: str,
        address_name: str,
        request: main_models.UpdateAddressRequest,
    ) -> main_models.UpdateAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_address_with_options_async(userid, address_name, request, headers, runtime)

    def update_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            self.execute(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJob',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/job/{job_name}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_job(
        self,
        userid: str,
        job_name: str,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_job_with_options(userid, job_name, request, headers, runtime)

    async def update_job_async(
        self,
        userid: str,
        job_name: str,
        request: main_models.UpdateJobRequest,
    ) -> main_models.UpdateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(userid, job_name, request, headers, runtime)

    def update_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        request: main_models.UpdateTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def update_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        request: main_models.UpdateTunnelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTunnelResponse:
        request.validate()
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not DaraCore.is_null(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTunnel',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/tunnel/{tunnel_id}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.UpdateTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_tunnel(
        self,
        userid: str,
        tunnel_id: str,
        request: main_models.UpdateTunnelRequest,
    ) -> main_models.UpdateTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_tunnel_with_options(userid, tunnel_id, request, headers, runtime)

    async def update_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
        request: main_models.UpdateTunnelRequest,
    ) -> main_models.UpdateTunnelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_tunnel_with_options_async(userid, tunnel_id, request, headers, runtime)

    def verify_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'VerifyAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}?verify',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.VerifyAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def verify_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.VerifyAddressResponse:
        host_map = {}
        host_map['userid'] = userid
        req = open_api_util_models.OpenApiRequest(
            host_map = host_map,
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'VerifyAddress',
            version = '2024-06-26',
            protocol = 'HTTPS',
            pathname = f'/address/{address_name}?verify',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'xml',
            body_type = 'xml'
        )
        return DaraCore.from_map(
            main_models.VerifyAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def verify_address(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.VerifyAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.verify_address_with_options(userid, address_name, headers, runtime)

    async def verify_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> main_models.VerifyAddressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.verify_address_with_options_async(userid, address_name, headers, runtime)
