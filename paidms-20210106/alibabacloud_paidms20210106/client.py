# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paidms20210106 import models as paidms_20210106_models
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
        self._endpoint = self.get_endpoint('paidms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_stream_group(
        self,
        request: paidms_20210106_models.AddStreamGroupRequest,
    ) -> paidms_20210106_models.AddStreamGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = paidms_20210106_models.AddStreamGroupHeaders()
        return self.add_stream_group_with_options(request, headers, runtime)

    async def add_stream_group_async(
        self,
        request: paidms_20210106_models.AddStreamGroupRequest,
    ) -> paidms_20210106_models.AddStreamGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = paidms_20210106_models.AddStreamGroupHeaders()
        return await self.add_stream_group_with_options_async(request, headers, runtime)

    def add_stream_group_with_options(
        self,
        request: paidms_20210106_models.AddStreamGroupRequest,
        headers: paidms_20210106_models.AddStreamGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.AddStreamGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algo_type_enum):
            body['AlgoTypeEnum'] = request.algo_type_enum
        if not UtilClient.is_unset(request.alink_job_user):
            body['AlinkJobUser'] = request.alink_job_user
        if not UtilClient.is_unset(request.stream_id):
            body['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.stream_task_id):
            body['StreamTaskId'] = request.stream_task_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_number):
            body['UserNumber'] = request.user_number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.trans_to_alink):
            real_headers['TransToAlink'] = UtilClient.to_jsonstring(headers.trans_to_alink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStreamGroup',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/stream.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.AddStreamGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_stream_group_with_options_async(
        self,
        request: paidms_20210106_models.AddStreamGroupRequest,
        headers: paidms_20210106_models.AddStreamGroupHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.AddStreamGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algo_type_enum):
            body['AlgoTypeEnum'] = request.algo_type_enum
        if not UtilClient.is_unset(request.alink_job_user):
            body['AlinkJobUser'] = request.alink_job_user
        if not UtilClient.is_unset(request.stream_id):
            body['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.stream_task_id):
            body['StreamTaskId'] = request.stream_task_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.user_number):
            body['UserNumber'] = request.user_number
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.trans_to_alink):
            real_headers['TransToAlink'] = UtilClient.to_jsonstring(headers.trans_to_alink)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStreamGroup',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/stream.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.AddStreamGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_experiment(
        self,
        request: paidms_20210106_models.ExportExperimentRequest,
    ) -> paidms_20210106_models.ExportExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_experiment_with_options(request, headers, runtime)

    async def export_experiment_async(
        self,
        request: paidms_20210106_models.ExportExperimentRequest,
    ) -> paidms_20210106_models.ExportExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_experiment_with_options_async(request, headers, runtime)

    def export_experiment_with_options(
        self,
        request: paidms_20210106_models.ExportExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperiment',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperiment.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_experiment_with_options_async(
        self,
        request: paidms_20210106_models.ExportExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperiment',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperiment.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_experiment_tree(
        self,
        request: paidms_20210106_models.ExportExperimentTreeRequest,
    ) -> paidms_20210106_models.ExportExperimentTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_experiment_tree_with_options(request, headers, runtime)

    async def export_experiment_tree_async(
        self,
        request: paidms_20210106_models.ExportExperimentTreeRequest,
    ) -> paidms_20210106_models.ExportExperimentTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_experiment_tree_with_options_async(request, headers, runtime)

    def export_experiment_tree_with_options(
        self,
        request: paidms_20210106_models.ExportExperimentTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperimentTree',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperimentTree.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_experiment_tree_with_options_async(
        self,
        request: paidms_20210106_models.ExportExperimentTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperimentTree',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperimentTree.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_experiment_tree_by_project_owner(
        self,
        request: paidms_20210106_models.ExportExperimentTreeByProjectOwnerRequest,
    ) -> paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_experiment_tree_by_project_owner_with_options(request, headers, runtime)

    async def export_experiment_tree_by_project_owner_async(
        self,
        request: paidms_20210106_models.ExportExperimentTreeByProjectOwnerRequest,
    ) -> paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_experiment_tree_by_project_owner_with_options_async(request, headers, runtime)

    def export_experiment_tree_by_project_owner_with_options(
        self,
        request: paidms_20210106_models.ExportExperimentTreeByProjectOwnerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tree_owner_id):
            query['TreeOwnerId'] = request.tree_owner_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperimentTreeByProjectOwner',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperimentTreeByProjectOwner.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_experiment_tree_by_project_owner_with_options_async(
        self,
        request: paidms_20210106_models.ExportExperimentTreeByProjectOwnerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.tree_owner_id):
            query['TreeOwnerId'] = request.tree_owner_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportExperimentTreeByProjectOwner',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/exportExperimentTreeByProjectOwner.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ExportExperimentTreeByProjectOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alink_algo_info(
        self,
        request: paidms_20210106_models.GetAlinkAlgoInfoRequest,
    ) -> paidms_20210106_models.GetAlinkAlgoInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alink_algo_info_with_options(request, headers, runtime)

    async def get_alink_algo_info_async(
        self,
        request: paidms_20210106_models.GetAlinkAlgoInfoRequest,
    ) -> paidms_20210106_models.GetAlinkAlgoInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_alink_algo_info_with_options_async(request, headers, runtime)

    def get_alink_algo_info_with_options(
        self,
        request: paidms_20210106_models.GetAlinkAlgoInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetAlinkAlgoInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_name):
            query['AlgoName'] = request.algo_name
        if not UtilClient.is_unset(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlinkAlgoInfo',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/getAlinkAlgoInfo.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetAlinkAlgoInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alink_algo_info_with_options_async(
        self,
        request: paidms_20210106_models.GetAlinkAlgoInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetAlinkAlgoInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_name):
            query['AlgoName'] = request.algo_name
        if not UtilClient.is_unset(request.user_number):
            query['UserNumber'] = request.user_number
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlinkAlgoInfo',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/getAlinkAlgoInfo.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetAlinkAlgoInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alink_algo_public_key(self) -> paidms_20210106_models.GetAlinkAlgoPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_alink_algo_public_key_with_options(headers, runtime)

    async def get_alink_algo_public_key_async(self) -> paidms_20210106_models.GetAlinkAlgoPublicKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_alink_algo_public_key_with_options_async(headers, runtime)

    def get_alink_algo_public_key_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetAlinkAlgoPublicKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlinkAlgoPublicKey',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/getAlinkAlgoPublicKey.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetAlinkAlgoPublicKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alink_algo_public_key_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetAlinkAlgoPublicKeyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAlinkAlgoPublicKey',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/getAlinkAlgoPublicKey.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetAlinkAlgoPublicKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_info(
        self,
        request: paidms_20210106_models.GetProjectInfoRequest,
    ) -> paidms_20210106_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_info_with_options(request, headers, runtime)

    async def get_project_info_async(
        self,
        request: paidms_20210106_models.GetProjectInfoRequest,
    ) -> paidms_20210106_models.GetProjectInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_info_with_options_async(request, headers, runtime)

    def get_project_info_with_options(
        self,
        request: paidms_20210106_models.GetProjectInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetProjectInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/getProjectInfo.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetProjectInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_info_with_options_async(
        self,
        request: paidms_20210106_models.GetProjectInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.GetProjectInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProjectInfo',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/getProjectInfo.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.GetProjectInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_used_projects(self) -> paidms_20210106_models.ListUsedProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_used_projects_with_options(headers, runtime)

    async def list_used_projects_async(self) -> paidms_20210106_models.ListUsedProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_used_projects_with_options_async(headers, runtime)

    def list_used_projects_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ListUsedProjectsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsedProjects',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/listUsedProjects.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ListUsedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_used_projects_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ListUsedProjectsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsedProjects',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/listUsedProjects.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ListUsedProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_used_projects_by_owner(self) -> paidms_20210106_models.ListUsedProjectsByOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_used_projects_by_owner_with_options(headers, runtime)

    async def list_used_projects_by_owner_async(self) -> paidms_20210106_models.ListUsedProjectsByOwnerResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_used_projects_by_owner_with_options_async(headers, runtime)

    def list_used_projects_by_owner_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ListUsedProjectsByOwnerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsedProjectsByOwner',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/listUsedProjectsByOwner.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ListUsedProjectsByOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_used_projects_by_owner_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.ListUsedProjectsByOwnerResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsedProjectsByOwner',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/migrate/listUsedProjectsByOwner.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.ListUsedProjectsByOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_automl_job_id(
        self,
        request: paidms_20210106_models.SaveAutomlJobIdRequest,
    ) -> paidms_20210106_models.SaveAutomlJobIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_automl_job_id_with_options(request, headers, runtime)

    async def save_automl_job_id_async(
        self,
        request: paidms_20210106_models.SaveAutomlJobIdRequest,
    ) -> paidms_20210106_models.SaveAutomlJobIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_automl_job_id_with_options_async(request, headers, runtime)

    def save_automl_job_id_with_options(
        self,
        request: paidms_20210106_models.SaveAutomlJobIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveAutomlJobIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAutomlJobId',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/automlJob.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveAutomlJobIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_automl_job_id_with_options_async(
        self,
        request: paidms_20210106_models.SaveAutomlJobIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveAutomlJobIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveAutomlJobId',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/automlJob.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveAutomlJobIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_automl_model(
        self,
        request: paidms_20210106_models.SaveAutomlModelRequest,
    ) -> paidms_20210106_models.SaveAutomlModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_automl_model_with_options(request, headers, runtime)

    async def save_automl_model_async(
        self,
        request: paidms_20210106_models.SaveAutomlModelRequest,
    ) -> paidms_20210106_models.SaveAutomlModelResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_automl_model_with_options_async(request, headers, runtime)

    def save_automl_model_with_options(
        self,
        request: paidms_20210106_models.SaveAutomlModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveAutomlModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not UtilClient.is_unset(request.auc):
            body['Auc'] = request.auc
        if not UtilClient.is_unset(request.execution_record_id):
            body['ExecutionRecordId'] = request.execution_record_id
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.f_1score):
            body['F1score'] = request.f_1score
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.indicator):
            body['Indicator'] = request.indicator
        if not UtilClient.is_unset(request.indicator_data):
            body['IndicatorData'] = request.indicator_data
        if not UtilClient.is_unset(request.is_migrate):
            body['IsMigrate'] = request.is_migrate
        if not UtilClient.is_unset(request.iterations):
            body['Iterations'] = request.iterations
        if not UtilClient.is_unset(request.model_index):
            body['ModelIndex'] = request.model_index
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_param):
            body['ModelParam'] = request.model_param
        if not UtilClient.is_unset(request.precision_score):
            body['PrecisionScore'] = request.precision_score
        if not UtilClient.is_unset(request.recall):
            body['Recall'] = request.recall
        if not UtilClient.is_unset(request.roc):
            body['Roc'] = request.roc
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAutomlModel',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/automl.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveAutomlModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_automl_model_with_options_async(
        self,
        request: paidms_20210106_models.SaveAutomlModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveAutomlModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        body = {}
        if not UtilClient.is_unset(request.auc):
            body['Auc'] = request.auc
        if not UtilClient.is_unset(request.execution_record_id):
            body['ExecutionRecordId'] = request.execution_record_id
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.f_1score):
            body['F1score'] = request.f_1score
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.indicator):
            body['Indicator'] = request.indicator
        if not UtilClient.is_unset(request.indicator_data):
            body['IndicatorData'] = request.indicator_data
        if not UtilClient.is_unset(request.is_migrate):
            body['IsMigrate'] = request.is_migrate
        if not UtilClient.is_unset(request.iterations):
            body['Iterations'] = request.iterations
        if not UtilClient.is_unset(request.model_index):
            body['ModelIndex'] = request.model_index
        if not UtilClient.is_unset(request.model_name):
            body['ModelName'] = request.model_name
        if not UtilClient.is_unset(request.model_param):
            body['ModelParam'] = request.model_param
        if not UtilClient.is_unset(request.precision_score):
            body['PrecisionScore'] = request.precision_score
        if not UtilClient.is_unset(request.recall):
            body['Recall'] = request.recall
        if not UtilClient.is_unset(request.roc):
            body['Roc'] = request.roc
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveAutomlModel',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/automl.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveAutomlModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_odps_instance(
        self,
        request: paidms_20210106_models.SaveOdpsInstanceRequest,
    ) -> paidms_20210106_models.SaveOdpsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_odps_instance_with_options(request, headers, runtime)

    async def save_odps_instance_async(
        self,
        request: paidms_20210106_models.SaveOdpsInstanceRequest,
    ) -> paidms_20210106_models.SaveOdpsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_odps_instance_with_options_async(request, headers, runtime)

    def save_odps_instance_with_options(
        self,
        request: paidms_20210106_models.SaveOdpsInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveOdpsInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.node_instance_id):
            body['NodeInstanceId'] = request.node_instance_id
        if not UtilClient.is_unset(request.odps_instance_id):
            body['OdpsInstanceId'] = request.odps_instance_id
        if not UtilClient.is_unset(request.odps_instance_status):
            body['OdpsInstanceStatus'] = request.odps_instance_status
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveOdpsInstance',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/instance.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveOdpsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_odps_instance_with_options_async(
        self,
        request: paidms_20210106_models.SaveOdpsInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paidms_20210106_models.SaveOdpsInstanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.node_instance_id):
            body['NodeInstanceId'] = request.node_instance_id
        if not UtilClient.is_unset(request.odps_instance_id):
            body['OdpsInstanceId'] = request.odps_instance_id
        if not UtilClient.is_unset(request.odps_instance_status):
            body['OdpsInstanceStatus'] = request.odps_instance_status
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveOdpsInstance',
            version='2021-01-06',
            protocol='HTTPS',
            pathname=f'/pop/roa/api/v1.0/instance.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            paidms_20210106_models.SaveOdpsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )
