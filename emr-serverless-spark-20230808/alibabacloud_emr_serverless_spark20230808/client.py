# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr_serverless_spark20230808 import models as emr_serverless_spark_20230808_models
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
        self._endpoint = self.get_endpoint('emr-serverless-spark', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_members_with_options(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.AddMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_members_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddMembersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.member_arns):
            body['memberArns'] = request.member_arns
        if not UtilClient.is_unset(request.workspace_id):
            body['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMembers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/members',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.AddMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_members(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @return: AddMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_members_with_options(request, headers, runtime)

    async def add_members_async(
        self,
        request: emr_serverless_spark_20230808_models.AddMembersRequest,
    ) -> emr_serverless_spark_20230808_models.AddMembersResponse:
        """
        @summary Adds a RAM user or RAM role to a workspace as a member.
        
        @param request: AddMembersRequest
        @return: AddMembersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_members_with_options_async(request, headers, runtime)

    def cancel_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CancelJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @return: CancelJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def cancel_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.CancelJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.CancelJobRunResponse:
        """
        @summary Terminates a Spark job.
        
        @param request: CancelJobRunRequest
        @return: CancelJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def create_sql_statement_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary 使用session运行SQL
        
        @param request: CreateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.code_content):
            body['codeContent'] = request.code_content
        if not UtilClient.is_unset(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not UtilClient.is_unset(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_statement_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary 使用session运行SQL
        
        @param request: CreateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.code_content):
            body['codeContent'] = request.code_content
        if not UtilClient.is_unset(request.default_catalog):
            body['defaultCatalog'] = request.default_catalog
        if not UtilClient.is_unset(request.default_database):
            body['defaultDatabase'] = request.default_database
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.sql_compute_id):
            body['sqlComputeId'] = request.sql_compute_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.CreateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_statement(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary 使用session运行SQL
        
        @param request: CreateSqlStatementRequest
        @return: CreateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sql_statement_with_options(workspace_id, request, headers, runtime)

    async def create_sql_statement_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.CreateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.CreateSqlStatementResponse:
        """
        @summary 使用session运行SQL
        
        @param request: CreateSqlStatementRequest
        @return: CreateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sql_statement_with_options_async(workspace_id, request, headers, runtime)

    def get_job_run_with_options(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_run_with_options_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns/{OpenApiUtilClient.get_encode_param(job_run_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_run(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @return: GetJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_run_with_options(workspace_id, job_run_id, request, headers, runtime)

    async def get_job_run_async(
        self,
        workspace_id: str,
        job_run_id: str,
        request: emr_serverless_spark_20230808_models.GetJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.GetJobRunResponse:
        """
        @summary Obtain the job details.
        
        @param request: GetJobRunRequest
        @return: GetJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_run_with_options_async(workspace_id, job_run_id, request, headers, runtime)

    def get_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary 获取Sql Statement状态
        
        @param request: GetSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary 获取Sql Statement状态
        
        @param request: GetSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GetSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary 获取Sql Statement状态
        
        @param request: GetSqlStatementRequest
        @return: GetSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def get_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.GetSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.GetSqlStatementResponse:
        """
        @summary 获取Sql Statement状态
        
        @param request: GetSqlStatementRequest
        @return: GetSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantRoleToUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.role_arn):
            body['roleArn'] = request.role_arn
        if not UtilClient.is_unset(request.user_arns):
            body['userArns'] = request.user_arns
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantRoleToUsers',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/auth/roles/grant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: emr_serverless_spark_20230808_models.GrantRoleToUsersRequest,
    ) -> emr_serverless_spark_20230808_models.GrantRoleToUsersResponse:
        """
        @summary Assigns a specified role to users.
        
        @param request: GrantRoleToUsersRequest
        @return: GrantRoleToUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def list_job_runs_with_options(
        self,
        workspace_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param tmp_req: ListJobRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobRunsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_runs_with_options_async(
        self,
        workspace_id: str,
        tmp_req: emr_serverless_spark_20230808_models.ListJobRunsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param tmp_req: ListJobRunsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobRunsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_serverless_spark_20230808_models.ListJobRunsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time):
            request.end_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time, 'endTime', 'json')
        if not UtilClient.is_unset(tmp_req.start_time):
            request.start_time_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time, 'startTime', 'json')
        if not UtilClient.is_unset(tmp_req.states):
            request.states_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.states, 'states', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.creator):
            query['creator'] = request.creator
        if not UtilClient.is_unset(request.end_time_shrink):
            query['endTime'] = request.end_time_shrink
        if not UtilClient.is_unset(request.job_run_deployment_id):
            query['jobRunDeploymentId'] = request.job_run_deployment_id
        if not UtilClient.is_unset(request.job_run_id):
            query['jobRunId'] = request.job_run_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_queue_id):
            query['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.start_time_shrink):
            query['startTime'] = request.start_time_shrink
        if not UtilClient.is_unset(request.states_shrink):
            query['states'] = request.states_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobRuns',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListJobRunsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_runs(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListJobRunsRequest,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param request: ListJobRunsRequest
        @return: ListJobRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_runs_with_options(workspace_id, request, headers, runtime)

    async def list_job_runs_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListJobRunsRequest,
    ) -> emr_serverless_spark_20230808_models.ListJobRunsResponse:
        """
        @summary Queries a list of Spark jobs.
        
        @param request: ListJobRunsRequest
        @return: ListJobRunsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_runs_with_options_async(workspace_id, request, headers, runtime)

    def list_release_versions_with_options(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary 获取发布版本列表
        
        @param request: ListReleaseVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_type):
            query['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.release_version):
            query['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/releaseVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_release_versions_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary 获取发布版本列表
        
        @param request: ListReleaseVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.release_type):
            query['releaseType'] = request.release_type
        if not UtilClient.is_unset(request.release_version):
            query['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.release_version_status):
            query['releaseVersionStatus'] = request.release_version_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/releaseVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListReleaseVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_release_versions(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary 获取发布版本列表
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_release_versions_with_options(request, headers, runtime)

    async def list_release_versions_async(
        self,
        request: emr_serverless_spark_20230808_models.ListReleaseVersionsRequest,
    ) -> emr_serverless_spark_20230808_models.ListReleaseVersionsResponse:
        """
        @summary 获取发布版本列表
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_release_versions_with_options_async(request, headers, runtime)

    def list_session_clusters_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary 查询run列表
        
        @param request: ListSessionClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.queue_name):
            query['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSessionClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_clusters_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary 查询run列表
        
        @param request: ListSessionClustersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.queue_name):
            query['queueName'] = request.queue_name
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.session_cluster_id):
            query['sessionClusterId'] = request.session_cluster_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionClusters',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/sessionClusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListSessionClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_clusters(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary 查询run列表
        
        @param request: ListSessionClustersRequest
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_session_clusters_with_options(workspace_id, request, headers, runtime)

    async def list_session_clusters_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListSessionClustersRequest,
    ) -> emr_serverless_spark_20230808_models.ListSessionClustersResponse:
        """
        @summary 查询run列表
        
        @param request: ListSessionClustersRequest
        @return: ListSessionClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_session_clusters_with_options_async(workspace_id, request, headers, runtime)

    def list_workspace_queues_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary 查看工作空间队列列表
        
        @param request: ListWorkspaceQueuesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceQueuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceQueues',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/queues',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_queues_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary 查看工作空间队列列表
        
        @param request: ListWorkspaceQueuesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspaceQueuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment):
            query['environment'] = request.environment
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaceQueues',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/queues',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_queues(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary 查看工作空间队列列表
        
        @param request: ListWorkspaceQueuesRequest
        @return: ListWorkspaceQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspace_queues_with_options(workspace_id, request, headers, runtime)

    async def list_workspace_queues_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.ListWorkspaceQueuesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspaceQueuesResponse:
        """
        @summary 查看工作空间队列列表
        
        @param request: ListWorkspaceQueuesRequest
        @return: ListWorkspaceQueuesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspace_queues_with_options_async(workspace_id, request, headers, runtime)

    def list_workspaces_with_options(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['state'] = request.state
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: emr_serverless_spark_20230808_models.ListWorkspacesRequest,
    ) -> emr_serverless_spark_20230808_models.ListWorkspacesResponse:
        """
        @summary Queries a list of workspaces.
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def start_job_run_with_options(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_job_run_with_options_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartJobRunResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code_type):
            body['codeType'] = request.code_type
        if not UtilClient.is_unset(request.configuration_overrides):
            body['configurationOverrides'] = request.configuration_overrides
        if not UtilClient.is_unset(request.execution_timeout_seconds):
            body['executionTimeoutSeconds'] = request.execution_timeout_seconds
        if not UtilClient.is_unset(request.job_driver):
            body['jobDriver'] = request.job_driver
        if not UtilClient.is_unset(request.job_id):
            body['jobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.release_version):
            body['releaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_queue_id):
            body['resourceQueueId'] = request.resource_queue_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartJobRun',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/workspaces/{OpenApiUtilClient.get_encode_param(workspace_id)}/jobRuns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.StartJobRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_job_run(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @return: StartJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_job_run_with_options(workspace_id, request, headers, runtime)

    async def start_job_run_async(
        self,
        workspace_id: str,
        request: emr_serverless_spark_20230808_models.StartJobRunRequest,
    ) -> emr_serverless_spark_20230808_models.StartJobRunResponse:
        """
        @summary Starts a Spark job.
        
        @param request: StartJobRunRequest
        @return: StartJobRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_job_run_with_options_async(workspace_id, request, headers, runtime)

    def terminate_sql_statement_with_options(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary 终止 session statement
        
        @param request: TerminateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.TerminateSqlStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_sql_statement_with_options_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary 终止 session statement
        
        @param request: TerminateSqlStatementRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TerminateSqlStatementResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TerminateSqlStatement',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/interactive/v1/workspace/{OpenApiUtilClient.get_encode_param(workspace_id)}/statement/{OpenApiUtilClient.get_encode_param(statement_id)}/terminate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_serverless_spark_20230808_models.TerminateSqlStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_sql_statement(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary 终止 session statement
        
        @param request: TerminateSqlStatementRequest
        @return: TerminateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.terminate_sql_statement_with_options(workspace_id, statement_id, request, headers, runtime)

    async def terminate_sql_statement_async(
        self,
        workspace_id: str,
        statement_id: str,
        request: emr_serverless_spark_20230808_models.TerminateSqlStatementRequest,
    ) -> emr_serverless_spark_20230808_models.TerminateSqlStatementResponse:
        """
        @summary 终止 session statement
        
        @param request: TerminateSqlStatementRequest
        @return: TerminateSqlStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.terminate_sql_statement_with_options_async(workspace_id, statement_id, request, headers, runtime)
