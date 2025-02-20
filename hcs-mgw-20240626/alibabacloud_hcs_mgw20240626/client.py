# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_oss.client import Client as GatewayClientClient
from alibabacloud_hcs_mgw20240626 import models as hcs_mgw_20240626_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
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
        self._product_id = 'hcs-mgw'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''

    def create_address_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateAddressResponse:
        """
        @summary Creates a data address.
        
        @description    To create a data address, you must have the permission on mgw:CreateImportAddress.
        If you want to use an agent to migrate data, you must create an agent first and then associate the agent with a data address when you create the data address.
        
        @param request: CreateAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def create_address_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateAddressResponse:
        """
        @summary Creates a data address.
        
        @description    To create a data address, you must have the permission on mgw:CreateImportAddress.
        If you want to use an agent to migrate data, you must create an agent first and then associate the agent with a data address when you create the data address.
        
        @param request: CreateAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_address(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAddressRequest,
    ) -> hcs_mgw_20240626_models.CreateAddressResponse:
        """
        @summary Creates a data address.
        
        @description    To create a data address, you must have the permission on mgw:CreateImportAddress.
        If you want to use an agent to migrate data, you must create an agent first and then associate the agent with a data address when you create the data address.
        
        @param request: CreateAddressRequest
        @return: CreateAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_address_with_options(userid, request, headers, runtime)

    async def create_address_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAddressRequest,
    ) -> hcs_mgw_20240626_models.CreateAddressResponse:
        """
        @summary Creates a data address.
        
        @description    To create a data address, you must have the permission on mgw:CreateImportAddress.
        If you want to use an agent to migrate data, you must create an agent first and then associate the agent with a data address when you create the data address.
        
        @param request: CreateAddressRequest
        @return: CreateAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_address_with_options_async(userid, request, headers, runtime)

    def create_agent_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateAgentResponse:
        """
        @summary The request boy for creating the agent.
        
        @description    To create an agent, you must have the permission on mgw:CreateImportAgent.
        If you want to migrate data to Alibaba Cloud over an Express Connect circuit or a VPN gateway, or migrate data from a self-managed storage space to Alibaba Cloud, you can deploy an agent.
        Before you create an agent, you must create a tunnel. An agent must be associated with a tunnel.
        
        @param request: CreateAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_agent):
            body['ImportAgent'] = request.import_agent
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateAgentResponse:
        """
        @summary The request boy for creating the agent.
        
        @description    To create an agent, you must have the permission on mgw:CreateImportAgent.
        If you want to migrate data to Alibaba Cloud over an Express Connect circuit or a VPN gateway, or migrate data from a self-managed storage space to Alibaba Cloud, you can deploy an agent.
        Before you create an agent, you must create a tunnel. An agent must be associated with a tunnel.
        
        @param request: CreateAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgentResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_agent):
            body['ImportAgent'] = request.import_agent
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_agent(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAgentRequest,
    ) -> hcs_mgw_20240626_models.CreateAgentResponse:
        """
        @summary The request boy for creating the agent.
        
        @description    To create an agent, you must have the permission on mgw:CreateImportAgent.
        If you want to migrate data to Alibaba Cloud over an Express Connect circuit or a VPN gateway, or migrate data from a self-managed storage space to Alibaba Cloud, you can deploy an agent.
        Before you create an agent, you must create a tunnel. An agent must be associated with a tunnel.
        
        @param request: CreateAgentRequest
        @return: CreateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_agent_with_options(userid, request, headers, runtime)

    async def create_agent_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateAgentRequest,
    ) -> hcs_mgw_20240626_models.CreateAgentResponse:
        """
        @summary The request boy for creating the agent.
        
        @description    To create an agent, you must have the permission on mgw:CreateImportAgent.
        If you want to migrate data to Alibaba Cloud over an Express Connect circuit or a VPN gateway, or migrate data from a self-managed storage space to Alibaba Cloud, you can deploy an agent.
        Before you create an agent, you must create a tunnel. An agent must be associated with a tunnel.
        
        @param request: CreateAgentRequest
        @return: CreateAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_agent_with_options_async(userid, request, headers, runtime)

    def create_job_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateJobResponse:
        """
        @summary Creates a migration task.
        
        @description    To create a migration task, you must have the permission on mgw:CreateImportJob.
        Before you create a migration task, you must create data addresses.
        A migration task can run multiple rounds. Each round has an execution ID.
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateJobResponse(),
            self.execute(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateJobResponse:
        """
        @summary Creates a migration task.
        
        @description    To create a migration task, you must have the permission on mgw:CreateImportJob.
        Before you create a migration task, you must create data addresses.
        A migration task can run multiple rounds. Each round has an execution ID.
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_job(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateJobRequest,
    ) -> hcs_mgw_20240626_models.CreateJobResponse:
        """
        @summary Creates a migration task.
        
        @description    To create a migration task, you must have the permission on mgw:CreateImportJob.
        Before you create a migration task, you must create data addresses.
        A migration task can run multiple rounds. Each round has an execution ID.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(userid, request, headers, runtime)

    async def create_job_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateJobRequest,
    ) -> hcs_mgw_20240626_models.CreateJobResponse:
        """
        @summary Creates a migration task.
        
        @description    To create a migration task, you must have the permission on mgw:CreateImportJob.
        Before you create a migration task, you must create data addresses.
        A migration task can run multiple rounds. Each round has an execution ID.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(userid, request, headers, runtime)

    def create_report_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateReportResponse:
        """
        @summary Creates a migration report.
        
        @description    To create a migration report, you must have the permission on mgw:CreateImportReport.
        If you specify that a migration report is to be generated when you create a migration task, you do not need to call this operation. If you do not specify that a migration report is to be generated when you create a migration task, you can call this operation to create a migration report for an execution with the specified ID.
        
        @param request: CreateReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReportResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.create_report):
            body['CreateReport'] = request.create_report
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReport',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateReportResponse(),
            self.execute(params, req, runtime)
        )

    async def create_report_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateReportResponse:
        """
        @summary Creates a migration report.
        
        @description    To create a migration report, you must have the permission on mgw:CreateImportReport.
        If you specify that a migration report is to be generated when you create a migration task, you do not need to call this operation. If you do not specify that a migration report is to be generated when you create a migration task, you can call this operation to create a migration report for an execution with the specified ID.
        
        @param request: CreateReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReportResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.create_report):
            body['CreateReport'] = request.create_report
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReport',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/report',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateReportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_report(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateReportRequest,
    ) -> hcs_mgw_20240626_models.CreateReportResponse:
        """
        @summary Creates a migration report.
        
        @description    To create a migration report, you must have the permission on mgw:CreateImportReport.
        If you specify that a migration report is to be generated when you create a migration task, you do not need to call this operation. If you do not specify that a migration report is to be generated when you create a migration task, you can call this operation to create a migration report for an execution with the specified ID.
        
        @param request: CreateReportRequest
        @return: CreateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_report_with_options(userid, request, headers, runtime)

    async def create_report_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateReportRequest,
    ) -> hcs_mgw_20240626_models.CreateReportResponse:
        """
        @summary Creates a migration report.
        
        @description    To create a migration report, you must have the permission on mgw:CreateImportReport.
        If you specify that a migration report is to be generated when you create a migration task, you do not need to call this operation. If you do not specify that a migration report is to be generated when you create a migration task, you can call this operation to create a migration report for an execution with the specified ID.
        
        @param request: CreateReportRequest
        @return: CreateReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_report_with_options_async(userid, request, headers, runtime)

    def create_tunnel_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateTunnelResponse:
        """
        @summary Creates a tunnel.
        
        @description    To create a tunnel, you must have the permission on mgw:CreateImportTunnel.
        When you use an agent to migrate data, the agent must be associated with a tunnel.
        A tunnel can be associated with multiple agents. You can throttle the traffic of the agents that are associated with the same tunnel by setting the bandwidth and the number of requests per second for the tunnel.
        
        @param request: CreateTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def create_tunnel_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.CreateTunnelResponse:
        """
        @summary Creates a tunnel.
        
        @description    To create a tunnel, you must have the permission on mgw:CreateImportTunnel.
        When you use an agent to migrate data, the agent must be associated with a tunnel.
        A tunnel can be associated with multiple agents. You can throttle the traffic of the agents that are associated with the same tunnel by setting the bandwidth and the number of requests per second for the tunnel.
        
        @param request: CreateTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.CreateTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def create_tunnel(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateTunnelRequest,
    ) -> hcs_mgw_20240626_models.CreateTunnelResponse:
        """
        @summary Creates a tunnel.
        
        @description    To create a tunnel, you must have the permission on mgw:CreateImportTunnel.
        When you use an agent to migrate data, the agent must be associated with a tunnel.
        A tunnel can be associated with multiple agents. You can throttle the traffic of the agents that are associated with the same tunnel by setting the bandwidth and the number of requests per second for the tunnel.
        
        @param request: CreateTunnelRequest
        @return: CreateTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tunnel_with_options(userid, request, headers, runtime)

    async def create_tunnel_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.CreateTunnelRequest,
    ) -> hcs_mgw_20240626_models.CreateTunnelResponse:
        """
        @summary Creates a tunnel.
        
        @description    To create a tunnel, you must have the permission on mgw:CreateImportTunnel.
        When you use an agent to migrate data, the agent must be associated with a tunnel.
        A tunnel can be associated with multiple agents. You can throttle the traffic of the agents that are associated with the same tunnel by setting the bandwidth and the number of requests per second for the tunnel.
        
        @param request: CreateTunnelRequest
        @return: CreateTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tunnel_with_options_async(userid, request, headers, runtime)

    def delete_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteAddressResponse:
        """
        @summary Deletes a data address.
        
        @description    To delete a data address, you must have the permission on mgw:DeleteImportAddress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteAddressResponse:
        """
        @summary Deletes a data address.
        
        @description    To delete a data address, you must have the permission on mgw:DeleteImportAddress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_address(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.DeleteAddressResponse:
        """
        @summary Deletes a data address.
        
        @description    To delete a data address, you must have the permission on mgw:DeleteImportAddress.
        
        @return: DeleteAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_address_with_options(userid, address_name, headers, runtime)

    async def delete_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.DeleteAddressResponse:
        """
        @summary Deletes a data address.
        
        @description    To delete a data address, you must have the permission on mgw:DeleteImportAddress.
        
        @return: DeleteAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_address_with_options_async(userid, address_name, headers, runtime)

    def delete_agent_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteAgentResponse:
        """
        @summary Deletes an agent.
        
        @description    To delete an agent, you must have the permission on mgw:DeleteImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteAgentResponse:
        """
        @summary Deletes an agent.
        
        @description    To delete an agent, you must have the permission on mgw:DeleteImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAgentResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_agent(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.DeleteAgentResponse:
        """
        @summary Deletes an agent.
        
        @description    To delete an agent, you must have the permission on mgw:DeleteImportAgent.
        
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_agent_with_options(userid, agent_name, headers, runtime)

    async def delete_agent_async(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.DeleteAgentResponse:
        """
        @summary Deletes an agent.
        
        @description    To delete an agent, you must have the permission on mgw:DeleteImportAgent.
        
        @return: DeleteAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_agent_with_options_async(userid, agent_name, headers, runtime)

    def delete_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteJobResponse:
        """
        @summary Deletes a migration task.
        
        @description    To delete a migration task, you must have the permission on mgw:DeleteImportJob.
        The operation to delete a migration task is asynchronous. The migration task remains in the Deleting state until it is deleted.
        
        @param request: DeleteJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteJobResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.DeleteJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteJobResponse:
        """
        @summary Deletes a migration task.
        
        @description    To delete a migration task, you must have the permission on mgw:DeleteImportJob.
        The operation to delete a migration task is asynchronous. The migration task remains in the Deleting state until it is deleted.
        
        @param request: DeleteJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['forceDelete'] = request.force_delete
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_job(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.DeleteJobRequest,
    ) -> hcs_mgw_20240626_models.DeleteJobResponse:
        """
        @summary Deletes a migration task.
        
        @description    To delete a migration task, you must have the permission on mgw:DeleteImportJob.
        The operation to delete a migration task is asynchronous. The migration task remains in the Deleting state until it is deleted.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_job_with_options(userid, job_name, request, headers, runtime)

    async def delete_job_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.DeleteJobRequest,
    ) -> hcs_mgw_20240626_models.DeleteJobResponse:
        """
        @summary Deletes a migration task.
        
        @description    To delete a migration task, you must have the permission on mgw:DeleteImportJob.
        The operation to delete a migration task is asynchronous. The migration task remains in the Deleting state until it is deleted.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_job_with_options_async(userid, job_name, request, headers, runtime)

    def delete_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteTunnelResponse:
        """
        @summary Deletes a tunnel.
        
        @description    To delete a tunnel, you must have the permission on mgw:DeleteImportTunnel.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTunnelResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def delete_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.DeleteTunnelResponse:
        """
        @summary Deletes a tunnel.
        
        @description    To delete a tunnel, you must have the permission on mgw:DeleteImportTunnel.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTunnelResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.DeleteTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def delete_tunnel(
        self,
        userid: str,
        tunnel_id: str,
    ) -> hcs_mgw_20240626_models.DeleteTunnelResponse:
        """
        @summary Deletes a tunnel.
        
        @description    To delete a tunnel, you must have the permission on mgw:DeleteImportTunnel.
        
        @return: DeleteTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_tunnel_with_options(userid, tunnel_id, headers, runtime)

    async def delete_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
    ) -> hcs_mgw_20240626_models.DeleteTunnelResponse:
        """
        @summary Deletes a tunnel.
        
        @description    To delete a tunnel, you must have the permission on mgw:DeleteImportTunnel.
        
        @return: DeleteTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_tunnel_with_options_async(userid, tunnel_id, headers, runtime)

    def get_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAddressResponse:
        """
        @summary Obtains the details of a data address.
        
        @description    To query the information about a data address, you must have the permission on mgw:GetImportAddress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def get_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAddressResponse:
        """
        @summary Obtains the details of a data address.
        
        @description    To query the information about a data address, you must have the permission on mgw:GetImportAddress.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_address(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.GetAddressResponse:
        """
        @summary Obtains the details of a data address.
        
        @description    To query the information about a data address, you must have the permission on mgw:GetImportAddress.
        
        @return: GetAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_address_with_options(userid, address_name, headers, runtime)

    async def get_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.GetAddressResponse:
        """
        @summary Obtains the details of a data address.
        
        @description    To query the information about a data address, you must have the permission on mgw:GetImportAddress.
        
        @return: GetAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_address_with_options_async(userid, address_name, headers, runtime)

    def get_agent_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAgentResponse:
        """
        @summary Obtains the details of an agent.
        
        @description    To query the information about an agent, you must have the permission on mgw:GetImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def get_agent_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAgentResponse:
        """
        @summary Obtains the details of an agent.
        
        @description    To query the information about an agent, you must have the permission on mgw:GetImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_agent(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.GetAgentResponse:
        """
        @summary Obtains the details of an agent.
        
        @description    To query the information about an agent, you must have the permission on mgw:GetImportAgent.
        
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_with_options(userid, agent_name, headers, runtime)

    async def get_agent_async(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.GetAgentResponse:
        """
        @summary Obtains the details of an agent.
        
        @description    To query the information about an agent, you must have the permission on mgw:GetImportAgent.
        
        @return: GetAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_with_options_async(userid, agent_name, headers, runtime)

    def get_agent_status_with_options(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAgentStatusResponse:
        """
        @summary Obtains the running status of an agent.
        
        @description    To query the status of an agent, you must have the permission on mgw:GetImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentStatusResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgentStatus',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}?status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAgentStatusResponse(),
            self.execute(params, req, runtime)
        )

    async def get_agent_status_with_options_async(
        self,
        userid: str,
        agent_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetAgentStatusResponse:
        """
        @summary Obtains the running status of an agent.
        
        @description    To query the status of an agent, you must have the permission on mgw:GetImportAgent.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAgentStatusResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAgentStatus',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agent/{agent_name}?status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetAgentStatusResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_agent_status(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.GetAgentStatusResponse:
        """
        @summary Obtains the running status of an agent.
        
        @description    To query the status of an agent, you must have the permission on mgw:GetImportAgent.
        
        @return: GetAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_agent_status_with_options(userid, agent_name, headers, runtime)

    async def get_agent_status_async(
        self,
        userid: str,
        agent_name: str,
    ) -> hcs_mgw_20240626_models.GetAgentStatusResponse:
        """
        @summary Obtains the running status of an agent.
        
        @description    To query the status of an agent, you must have the permission on mgw:GetImportAgent.
        
        @return: GetAgentStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_agent_status_with_options_async(userid, agent_name, headers, runtime)

    def get_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetJobResponse:
        """
        @summary Obtains the details of a migration task.
        
        @description    To query the information about a migration task, you must have the permission on mgw:GetImportJob.
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.by_version):
            query['byVersion'] = request.by_version
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetJobResponse(),
            self.execute(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetJobResponse:
        """
        @summary Obtains the details of a migration task.
        
        @description    To query the information about a migration task, you must have the permission on mgw:GetImportJob.
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.by_version):
            query['byVersion'] = request.by_version
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_job(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobRequest,
    ) -> hcs_mgw_20240626_models.GetJobResponse:
        """
        @summary Obtains the details of a migration task.
        
        @description    To query the information about a migration task, you must have the permission on mgw:GetImportJob.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(userid, job_name, request, headers, runtime)

    async def get_job_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobRequest,
    ) -> hcs_mgw_20240626_models.GetJobResponse:
        """
        @summary Obtains the details of a migration task.
        
        @description    To query the information about a migration task, you must have the permission on mgw:GetImportJob.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(userid, job_name, request, headers, runtime)

    def get_job_result_with_options(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetJobResultResponse:
        """
        @summary Obtains the list of files that fail to be migrated when files fail to be migrated during a migration task.
        
        @description    To query the retry information about a migration task, you must have the permission on mgw:GetImportJobResult.
        If files fail to be migrated during a migration task, a list of files that fail to be migrated is generated. You can call this operation to query this list. You can create a data address based on this list and create a subtask. This way, you can migrate these files again.
        
        @param request: GetJobResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResultResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResult',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}?jobResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetJobResultResponse(),
            self.execute(params, req, runtime)
        )

    async def get_job_result_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetJobResultResponse:
        """
        @summary Obtains the list of files that fail to be migrated when files fail to be migrated during a migration task.
        
        @description    To query the retry information about a migration task, you must have the permission on mgw:GetImportJobResult.
        If files fail to be migrated during a migration task, a list of files that fail to be migrated is generated. You can call this operation to query this list. You can create a data address based on this list and create a subtask. This way, you can migrate these files again.
        
        @param request: GetJobResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResultResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResult',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}?jobResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetJobResultResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_job_result(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobResultRequest,
    ) -> hcs_mgw_20240626_models.GetJobResultResponse:
        """
        @summary Obtains the list of files that fail to be migrated when files fail to be migrated during a migration task.
        
        @description    To query the retry information about a migration task, you must have the permission on mgw:GetImportJobResult.
        If files fail to be migrated during a migration task, a list of files that fail to be migrated is generated. You can call this operation to query this list. You can create a data address based on this list and create a subtask. This way, you can migrate these files again.
        
        @param request: GetJobResultRequest
        @return: GetJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_result_with_options(userid, job_name, request, headers, runtime)

    async def get_job_result_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.GetJobResultRequest,
    ) -> hcs_mgw_20240626_models.GetJobResultResponse:
        """
        @summary Obtains the list of files that fail to be migrated when files fail to be migrated during a migration task.
        
        @description    To query the retry information about a migration task, you must have the permission on mgw:GetImportJobResult.
        If files fail to be migrated during a migration task, a list of files that fail to be migrated is generated. You can call this operation to query this list. You can create a data address based on this list and create a subtask. This way, you can migrate these files again.
        
        @param request: GetJobResultRequest
        @return: GetJobResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_result_with_options_async(userid, job_name, request, headers, runtime)

    def get_report_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.GetReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetReportResponse:
        """
        @summary Obtains the details of a migration report.
        
        @description    To query the information about a migration report, you must have the permission on mgw:GetImportReport.
        The migration report is pushed to the destination data address. For more information, see the "View a migration report" section of the "Subsequent operations" topic in migration tutorials.
        
        @param request: GetReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReportResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReport',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetReportResponse(),
            self.execute(params, req, runtime)
        )

    async def get_report_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.GetReportRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetReportResponse:
        """
        @summary Obtains the details of a migration report.
        
        @description    To query the information about a migration report, you must have the permission on mgw:GetImportReport.
        The migration report is pushed to the destination data address. For more information, see the "View a migration report" section of the "Subsequent operations" topic in migration tutorials.
        
        @param request: GetReportRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetReportResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetReport',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/report',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetReportResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_report(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.GetReportRequest,
    ) -> hcs_mgw_20240626_models.GetReportResponse:
        """
        @summary Obtains the details of a migration report.
        
        @description    To query the information about a migration report, you must have the permission on mgw:GetImportReport.
        The migration report is pushed to the destination data address. For more information, see the "View a migration report" section of the "Subsequent operations" topic in migration tutorials.
        
        @param request: GetReportRequest
        @return: GetReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_report_with_options(userid, request, headers, runtime)

    async def get_report_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.GetReportRequest,
    ) -> hcs_mgw_20240626_models.GetReportResponse:
        """
        @summary Obtains the details of a migration report.
        
        @description    To query the information about a migration report, you must have the permission on mgw:GetImportReport.
        The migration report is pushed to the destination data address. For more information, see the "View a migration report" section of the "Subsequent operations" topic in migration tutorials.
        
        @param request: GetReportRequest
        @return: GetReportResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_report_with_options_async(userid, request, headers, runtime)

    def get_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetTunnelResponse:
        """
        @summary Obtains the details of a tunnel.
        
        @description    To query the information about a tunnel, you must have the permission on mgw:GetImportTunnel.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTunnelResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def get_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.GetTunnelResponse:
        """
        @summary Obtains the details of a tunnel.
        
        @description    To query the information about a tunnel, you must have the permission on mgw:GetImportTunnel.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTunnelResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.GetTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def get_tunnel(
        self,
        userid: str,
        tunnel_id: str,
    ) -> hcs_mgw_20240626_models.GetTunnelResponse:
        """
        @summary Obtains the details of a tunnel.
        
        @description    To query the information about a tunnel, you must have the permission on mgw:GetImportTunnel.
        
        @return: GetTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tunnel_with_options(userid, tunnel_id, headers, runtime)

    async def get_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
    ) -> hcs_mgw_20240626_models.GetTunnelResponse:
        """
        @summary Obtains the details of a tunnel.
        
        @description    To query the information about a tunnel, you must have the permission on mgw:GetImportTunnel.
        
        @return: GetTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tunnel_with_options_async(userid, tunnel_id, headers, runtime)

    def list_address_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListAddressResponse:
        """
        @summary Lists the data addresses created by a user in the specific region.
        
        @description    To query a list of data addresses, you must have the permission on mgw:ListImportAddress.
        
        @param request: ListAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/addresslist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def list_address_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListAddressResponse:
        """
        @summary Lists the data addresses created by a user in the specific region.
        
        @description    To query a list of data addresses, you must have the permission on mgw:ListImportAddress.
        
        @param request: ListAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/addresslist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_address(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAddressRequest,
    ) -> hcs_mgw_20240626_models.ListAddressResponse:
        """
        @summary Lists the data addresses created by a user in the specific region.
        
        @description    To query a list of data addresses, you must have the permission on mgw:ListImportAddress.
        
        @param request: ListAddressRequest
        @return: ListAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_address_with_options(userid, request, headers, runtime)

    async def list_address_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAddressRequest,
    ) -> hcs_mgw_20240626_models.ListAddressResponse:
        """
        @summary Lists the data addresses created by a user in the specific region.
        
        @description    To query a list of data addresses, you must have the permission on mgw:ListImportAddress.
        
        @param request: ListAddressRequest
        @return: ListAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_address_with_options_async(userid, request, headers, runtime)

    def list_agent_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListAgentResponse:
        """
        @summary Lists the agents created by a user in the specific region.
        
        @description    To query a list of agents, you must have the permission on mgw:ListImportAgent.
        
        @param request: ListAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agentlist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListAgentResponse(),
            self.execute(params, req, runtime)
        )

    async def list_agent_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAgentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListAgentResponse:
        """
        @summary Lists the agents created by a user in the specific region.
        
        @description    To query a list of agents, you must have the permission on mgw:ListImportAgent.
        
        @param request: ListAgentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAgentResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAgent',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/agentlist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListAgentResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_agent(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAgentRequest,
    ) -> hcs_mgw_20240626_models.ListAgentResponse:
        """
        @summary Lists the agents created by a user in the specific region.
        
        @description    To query a list of agents, you must have the permission on mgw:ListImportAgent.
        
        @param request: ListAgentRequest
        @return: ListAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_agent_with_options(userid, request, headers, runtime)

    async def list_agent_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListAgentRequest,
    ) -> hcs_mgw_20240626_models.ListAgentResponse:
        """
        @summary Lists the agents created by a user in the specific region.
        
        @description    To query a list of agents, you must have the permission on mgw:ListImportAgent.
        
        @param request: ListAgentRequest
        @return: ListAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_agent_with_options_async(userid, request, headers, runtime)

    def list_job_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListJobResponse:
        """
        @summary Lists the migration tasks created by a user in the specific region.
        
        @description    To query a list of migration tasks, you must have the permission on mgw:ListImportJob.
        
        @param request: ListJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.parent_name):
            query['parentName'] = request.parent_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/joblist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListJobResponse(),
            self.execute(params, req, runtime)
        )

    async def list_job_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListJobResponse:
        """
        @summary Lists the migration tasks created by a user in the specific region.
        
        @description    To query a list of migration tasks, you must have the permission on mgw:ListImportJob.
        
        @param request: ListJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.parent_name):
            query['parentName'] = request.parent_name
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/joblist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_job(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListJobRequest,
    ) -> hcs_mgw_20240626_models.ListJobResponse:
        """
        @summary Lists the migration tasks created by a user in the specific region.
        
        @description    To query a list of migration tasks, you must have the permission on mgw:ListImportJob.
        
        @param request: ListJobRequest
        @return: ListJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_with_options(userid, request, headers, runtime)

    async def list_job_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListJobRequest,
    ) -> hcs_mgw_20240626_models.ListJobResponse:
        """
        @summary Lists the migration tasks created by a user in the specific region.
        
        @description    To query a list of migration tasks, you must have the permission on mgw:ListImportJob.
        
        @param request: ListJobRequest
        @return: ListJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_with_options_async(userid, request, headers, runtime)

    def list_job_history_with_options(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.ListJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListJobHistoryResponse:
        """
        @summary Lists the running history of a migration task.
        
        @description    To query the execution history of a migration task, you must have the permission on mgw:ListImportJobHistory.
        A migration task can run multiple rounds. A unique execution ID is generated for each round.
        The execution history of a migration task records the change history of the task status.
        
        @param request: ListJobHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobHistoryResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobHistory',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/jobhistory/{job_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListJobHistoryResponse(),
            self.execute(params, req, runtime)
        )

    async def list_job_history_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.ListJobHistoryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListJobHistoryResponse:
        """
        @summary Lists the running history of a migration task.
        
        @description    To query the execution history of a migration task, you must have the permission on mgw:ListImportJobHistory.
        A migration task can run multiple rounds. A unique execution ID is generated for each round.
        The execution history of a migration task records the change history of the task status.
        
        @param request: ListJobHistoryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobHistoryResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.runtime_id):
            query['runtimeId'] = request.runtime_id
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobHistory',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/jobhistory/{job_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListJobHistoryResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_job_history(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.ListJobHistoryRequest,
    ) -> hcs_mgw_20240626_models.ListJobHistoryResponse:
        """
        @summary Lists the running history of a migration task.
        
        @description    To query the execution history of a migration task, you must have the permission on mgw:ListImportJobHistory.
        A migration task can run multiple rounds. A unique execution ID is generated for each round.
        The execution history of a migration task records the change history of the task status.
        
        @param request: ListJobHistoryRequest
        @return: ListJobHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_history_with_options(userid, job_name, request, headers, runtime)

    async def list_job_history_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.ListJobHistoryRequest,
    ) -> hcs_mgw_20240626_models.ListJobHistoryResponse:
        """
        @summary Lists the running history of a migration task.
        
        @description    To query the execution history of a migration task, you must have the permission on mgw:ListImportJobHistory.
        A migration task can run multiple rounds. A unique execution ID is generated for each round.
        The execution history of a migration task records the change history of the task status.
        
        @param request: ListJobHistoryRequest
        @return: ListJobHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_history_with_options_async(userid, job_name, request, headers, runtime)

    def list_tunnel_with_options(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListTunnelResponse:
        """
        @summary Lists tunnels.
        
        @description    To query a list of tunnels, you must have the permission on mgw:ListImportTunnel.
        
        @param request: ListTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnellist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def list_tunnel_with_options_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.ListTunnelResponse:
        """
        @summary Lists tunnels.
        
        @description    To query a list of tunnels, you must have the permission on mgw:ListImportTunnel.
        
        @param request: ListTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        query = {}
        if not UtilClient.is_unset(request.count):
            query['count'] = request.count
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnellist',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.ListTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def list_tunnel(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListTunnelRequest,
    ) -> hcs_mgw_20240626_models.ListTunnelResponse:
        """
        @summary Lists tunnels.
        
        @description    To query a list of tunnels, you must have the permission on mgw:ListImportTunnel.
        
        @param request: ListTunnelRequest
        @return: ListTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tunnel_with_options(userid, request, headers, runtime)

    async def list_tunnel_async(
        self,
        userid: str,
        request: hcs_mgw_20240626_models.ListTunnelRequest,
    ) -> hcs_mgw_20240626_models.ListTunnelResponse:
        """
        @summary Lists tunnels.
        
        @description    To query a list of tunnels, you must have the permission on mgw:ListImportTunnel.
        
        @param request: ListTunnelRequest
        @return: ListTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tunnel_with_options_async(userid, request, headers, runtime)

    def update_address_with_options(
        self,
        userid: str,
        address_name: str,
        request: hcs_mgw_20240626_models.UpdateAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateAddressResponse:
        """
        @summary Updates a data address.
        
        @description    To update a data address, you must have the permission on mgw:UpdateImportAddress.
        If the data address is associated with an agent, you can scale up or down the agent.
        
        @param request: UpdateAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def update_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        request: hcs_mgw_20240626_models.UpdateAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateAddressResponse:
        """
        @summary Updates a data address.
        
        @description    To update a data address, you must have the permission on mgw:UpdateImportAddress.
        If the data address is associated with an agent, you can scale up or down the agent.
        
        @param request: UpdateAddressRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAddressResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_address):
            body['ImportAddress'] = request.import_address
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_address(
        self,
        userid: str,
        address_name: str,
        request: hcs_mgw_20240626_models.UpdateAddressRequest,
    ) -> hcs_mgw_20240626_models.UpdateAddressResponse:
        """
        @summary Updates a data address.
        
        @description    To update a data address, you must have the permission on mgw:UpdateImportAddress.
        If the data address is associated with an agent, you can scale up or down the agent.
        
        @param request: UpdateAddressRequest
        @return: UpdateAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_address_with_options(userid, address_name, request, headers, runtime)

    async def update_address_async(
        self,
        userid: str,
        address_name: str,
        request: hcs_mgw_20240626_models.UpdateAddressRequest,
    ) -> hcs_mgw_20240626_models.UpdateAddressResponse:
        """
        @summary Updates a data address.
        
        @description    To update a data address, you must have the permission on mgw:UpdateImportAddress.
        If the data address is associated with an agent, you can scale up or down the agent.
        
        @param request: UpdateAddressRequest
        @return: UpdateAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_address_with_options_async(userid, address_name, request, headers, runtime)

    def update_job_with_options(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateJobResponse:
        """
        @summary Updates the status or throttling of a task.
        
        @description    To update a migration task, you must have the permission on mgw:UpdateImportJob.
        You can update only the status or throttling settings of a task in a single request.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateJobResponse(),
            self.execute(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.UpdateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateJobResponse:
        """
        @summary Updates the status or throttling of a task.
        
        @description    To update a migration task, you must have the permission on mgw:UpdateImportJob.
        You can update only the status or throttling settings of a task in a single request.
        
        @param request: UpdateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_job):
            body['ImportJob'] = request.import_job
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/job/{job_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateJobResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_job(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.UpdateJobRequest,
    ) -> hcs_mgw_20240626_models.UpdateJobResponse:
        """
        @summary Updates the status or throttling of a task.
        
        @description    To update a migration task, you must have the permission on mgw:UpdateImportJob.
        You can update only the status or throttling settings of a task in a single request.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_job_with_options(userid, job_name, request, headers, runtime)

    async def update_job_async(
        self,
        userid: str,
        job_name: str,
        request: hcs_mgw_20240626_models.UpdateJobRequest,
    ) -> hcs_mgw_20240626_models.UpdateJobResponse:
        """
        @summary Updates the status or throttling of a task.
        
        @description    To update a migration task, you must have the permission on mgw:UpdateImportJob.
        You can update only the status or throttling settings of a task in a single request.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_job_with_options_async(userid, job_name, request, headers, runtime)

    def update_tunnel_with_options(
        self,
        userid: str,
        tunnel_id: str,
        request: hcs_mgw_20240626_models.UpdateTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateTunnelResponse:
        """
        @summary Updates a tunnel.
        
        @description    To update a tunnel, you must have the permission on mgw:UpdateImportTunnel.
        
        @param request: UpdateTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateTunnelResponse(),
            self.execute(params, req, runtime)
        )

    async def update_tunnel_with_options_async(
        self,
        userid: str,
        tunnel_id: str,
        request: hcs_mgw_20240626_models.UpdateTunnelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.UpdateTunnelResponse:
        """
        @summary Updates a tunnel.
        
        @description    To update a tunnel, you must have the permission on mgw:UpdateImportTunnel.
        
        @param request: UpdateTunnelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTunnelResponse
        """
        UtilClient.validate_model(request)
        host_map = {}
        host_map['userid'] = userid
        body = {}
        if not UtilClient.is_unset(request.import_tunnel):
            body['ImportTunnel'] = request.import_tunnel
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTunnel',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/tunnel/{tunnel_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.UpdateTunnelResponse(),
            await self.execute_async(params, req, runtime)
        )

    def update_tunnel(
        self,
        userid: str,
        tunnel_id: str,
        request: hcs_mgw_20240626_models.UpdateTunnelRequest,
    ) -> hcs_mgw_20240626_models.UpdateTunnelResponse:
        """
        @summary Updates a tunnel.
        
        @description    To update a tunnel, you must have the permission on mgw:UpdateImportTunnel.
        
        @param request: UpdateTunnelRequest
        @return: UpdateTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tunnel_with_options(userid, tunnel_id, request, headers, runtime)

    async def update_tunnel_async(
        self,
        userid: str,
        tunnel_id: str,
        request: hcs_mgw_20240626_models.UpdateTunnelRequest,
    ) -> hcs_mgw_20240626_models.UpdateTunnelResponse:
        """
        @summary Updates a tunnel.
        
        @description    To update a tunnel, you must have the permission on mgw:UpdateImportTunnel.
        
        @param request: UpdateTunnelRequest
        @return: UpdateTunnelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_tunnel_with_options_async(userid, tunnel_id, request, headers, runtime)

    def verify_address_with_options(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.VerifyAddressResponse:
        """
        @summary Verifies whether a data address is available.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='VerifyAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}?verify',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.VerifyAddressResponse(),
            self.execute(params, req, runtime)
        )

    async def verify_address_with_options_async(
        self,
        userid: str,
        address_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> hcs_mgw_20240626_models.VerifyAddressResponse:
        """
        @summary Verifies whether a data address is available.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAddressResponse
        """
        host_map = {}
        host_map['userid'] = userid
        req = open_api_models.OpenApiRequest(
            host_map=host_map,
            headers=headers
        )
        params = open_api_models.Params(
            action='VerifyAddress',
            version='2024-06-26',
            protocol='HTTPS',
            pathname=f'/address/{address_name}?verify',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='xml',
            body_type='xml'
        )
        return TeaCore.from_map(
            hcs_mgw_20240626_models.VerifyAddressResponse(),
            await self.execute_async(params, req, runtime)
        )

    def verify_address(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.VerifyAddressResponse:
        """
        @summary Verifies whether a data address is available.
        
        @return: VerifyAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_address_with_options(userid, address_name, headers, runtime)

    async def verify_address_async(
        self,
        userid: str,
        address_name: str,
    ) -> hcs_mgw_20240626_models.VerifyAddressResponse:
        """
        @summary Verifies whether a data address is available.
        
        @return: VerifyAddressResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_address_with_options_async(userid, address_name, headers, runtime)
