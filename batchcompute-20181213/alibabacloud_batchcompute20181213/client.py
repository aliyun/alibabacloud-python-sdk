# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_batchcompute20181213 import models as batch_compute_20181213_models
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
        self._endpoint = self.get_endpoint('batchcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_job_with_options(
        self,
        request: batch_compute_20181213_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CancelJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CancelJobResponse(),
            self.do_rpcrequest('CancelJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_job_with_options_async(
        self,
        request: batch_compute_20181213_models.CancelJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CancelJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CancelJobResponse(),
            await self.do_rpcrequest_async('CancelJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_job(
        self,
        request: batch_compute_20181213_models.CancelJobRequest,
    ) -> batch_compute_20181213_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    async def cancel_job_async(
        self,
        request: batch_compute_20181213_models.CancelJobRequest,
    ) -> batch_compute_20181213_models.CancelJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_job_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: batch_compute_20181213_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateClusterResponse(),
            self.do_rpcrequest('CreateCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateClusterResponse(),
            await self.do_rpcrequest_async('CreateCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster(
        self,
        request: batch_compute_20181213_models.CreateClusterRequest,
    ) -> batch_compute_20181213_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: batch_compute_20181213_models.CreateClusterRequest,
    ) -> batch_compute_20181213_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: batch_compute_20181213_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateJobResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateJobResponse(),
            self.do_rpcrequest('CreateJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateJobResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateJobResponse(),
            await self.do_rpcrequest_async('CreateJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job(
        self,
        request: batch_compute_20181213_models.CreateJobRequest,
    ) -> batch_compute_20181213_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: batch_compute_20181213_models.CreateJobRequest,
    ) -> batch_compute_20181213_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_job_queue_with_options(
        self,
        tmp_req: batch_compute_20181213_models.CreateJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateJobQueueResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateJobQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateJobQueueResponse(),
            self.do_rpcrequest('CreateJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_queue_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.CreateJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateJobQueueResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateJobQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateJobQueueResponse(),
            await self.do_rpcrequest_async('CreateJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job_queue(
        self,
        request: batch_compute_20181213_models.CreateJobQueueRequest,
    ) -> batch_compute_20181213_models.CreateJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_queue_with_options(request, runtime)

    async def create_job_queue_async(
        self,
        request: batch_compute_20181213_models.CreateJobQueueRequest,
    ) -> batch_compute_20181213_models.CreateJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_queue_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: batch_compute_20181213_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.CreateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.CreateProjectResponse(),
            await self.do_rpcrequest_async('CreateProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: batch_compute_20181213_models.CreateProjectRequest,
    ) -> batch_compute_20181213_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: batch_compute_20181213_models.CreateProjectRequest,
    ) -> batch_compute_20181213_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: batch_compute_20181213_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteClusterResponse(),
            self.do_rpcrequest('DeleteCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: batch_compute_20181213_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteClusterResponse(),
            await self.do_rpcrequest_async('DeleteCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster(
        self,
        request: batch_compute_20181213_models.DeleteClusterRequest,
    ) -> batch_compute_20181213_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: batch_compute_20181213_models.DeleteClusterRequest,
    ) -> batch_compute_20181213_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: batch_compute_20181213_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteJobResponse(),
            self.do_rpcrequest('DeleteJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: batch_compute_20181213_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteJobResponse(),
            await self.do_rpcrequest_async('DeleteJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job(
        self,
        request: batch_compute_20181213_models.DeleteJobRequest,
    ) -> batch_compute_20181213_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: batch_compute_20181213_models.DeleteJobRequest,
    ) -> batch_compute_20181213_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_job_queue_with_options(
        self,
        request: batch_compute_20181213_models.DeleteJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteJobQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteJobQueueResponse(),
            self.do_rpcrequest('DeleteJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_queue_with_options_async(
        self,
        request: batch_compute_20181213_models.DeleteJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteJobQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteJobQueueResponse(),
            await self.do_rpcrequest_async('DeleteJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job_queue(
        self,
        request: batch_compute_20181213_models.DeleteJobQueueRequest,
    ) -> batch_compute_20181213_models.DeleteJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_queue_with_options(request, runtime)

    async def delete_job_queue_async(
        self,
        request: batch_compute_20181213_models.DeleteJobQueueRequest,
    ) -> batch_compute_20181213_models.DeleteJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_queue_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: batch_compute_20181213_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: batch_compute_20181213_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.DeleteProjectResponse(),
            await self.do_rpcrequest_async('DeleteProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: batch_compute_20181213_models.DeleteProjectRequest,
    ) -> batch_compute_20181213_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: batch_compute_20181213_models.DeleteProjectRequest,
    ) -> batch_compute_20181213_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: batch_compute_20181213_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetClusterResponse(),
            self.do_rpcrequest('GetCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: batch_compute_20181213_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetClusterResponse(),
            await self.do_rpcrequest_async('GetCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_cluster(
        self,
        request: batch_compute_20181213_models.GetClusterRequest,
    ) -> batch_compute_20181213_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: batch_compute_20181213_models.GetClusterRequest,
    ) -> batch_compute_20181213_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: batch_compute_20181213_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetJobResponse(),
            self.do_rpcrequest('GetJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: batch_compute_20181213_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetJobResponse(),
            await self.do_rpcrequest_async('GetJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job(
        self,
        request: batch_compute_20181213_models.GetJobRequest,
    ) -> batch_compute_20181213_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: batch_compute_20181213_models.GetJobRequest,
    ) -> batch_compute_20181213_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_job_queue_with_options(
        self,
        request: batch_compute_20181213_models.GetJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetJobQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetJobQueueResponse(),
            self.do_rpcrequest('GetJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_queue_with_options_async(
        self,
        request: batch_compute_20181213_models.GetJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetJobQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetJobQueueResponse(),
            await self.do_rpcrequest_async('GetJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_queue(
        self,
        request: batch_compute_20181213_models.GetJobQueueRequest,
    ) -> batch_compute_20181213_models.GetJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_queue_with_options(request, runtime)

    async def get_job_queue_async(
        self,
        request: batch_compute_20181213_models.GetJobQueueRequest,
    ) -> batch_compute_20181213_models.GetJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_queue_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: batch_compute_20181213_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: batch_compute_20181213_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetProjectResponse(),
            await self.do_rpcrequest_async('GetProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project(
        self,
        request: batch_compute_20181213_models.GetProjectRequest,
    ) -> batch_compute_20181213_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: batch_compute_20181213_models.GetProjectRequest,
    ) -> batch_compute_20181213_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_worker_with_options(
        self,
        request: batch_compute_20181213_models.GetWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetWorkerResponse(),
            self.do_rpcrequest('GetWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_worker_with_options_async(
        self,
        request: batch_compute_20181213_models.GetWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.GetWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.GetWorkerResponse(),
            await self.do_rpcrequest_async('GetWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_worker(
        self,
        request: batch_compute_20181213_models.GetWorkerRequest,
    ) -> batch_compute_20181213_models.GetWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_worker_with_options(request, runtime)

    async def get_worker_async(
        self,
        request: batch_compute_20181213_models.GetWorkerRequest,
    ) -> batch_compute_20181213_models.GetWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_worker_with_options_async(request, runtime)

    def kill_worker_with_options(
        self,
        request: batch_compute_20181213_models.KillWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.KillWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.KillWorkerResponse(),
            self.do_rpcrequest('KillWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kill_worker_with_options_async(
        self,
        request: batch_compute_20181213_models.KillWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.KillWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.KillWorkerResponse(),
            await self.do_rpcrequest_async('KillWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_worker(
        self,
        request: batch_compute_20181213_models.KillWorkerRequest,
    ) -> batch_compute_20181213_models.KillWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_worker_with_options(request, runtime)

    async def kill_worker_async(
        self,
        request: batch_compute_20181213_models.KillWorkerRequest,
    ) -> batch_compute_20181213_models.KillWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_worker_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: batch_compute_20181213_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: batch_compute_20181213_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListClustersResponse(),
            await self.do_rpcrequest_async('ListClusters', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_clusters(
        self,
        request: batch_compute_20181213_models.ListClustersRequest,
    ) -> batch_compute_20181213_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: batch_compute_20181213_models.ListClustersRequest,
    ) -> batch_compute_20181213_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_job_queues_with_options(
        self,
        request: batch_compute_20181213_models.ListJobQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListJobQueuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListJobQueuesResponse(),
            self.do_rpcrequest('ListJobQueues', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_queues_with_options_async(
        self,
        request: batch_compute_20181213_models.ListJobQueuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListJobQueuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListJobQueuesResponse(),
            await self.do_rpcrequest_async('ListJobQueues', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_queues(
        self,
        request: batch_compute_20181213_models.ListJobQueuesRequest,
    ) -> batch_compute_20181213_models.ListJobQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_queues_with_options(request, runtime)

    async def list_job_queues_async(
        self,
        request: batch_compute_20181213_models.ListJobQueuesRequest,
    ) -> batch_compute_20181213_models.ListJobQueuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_queues_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: batch_compute_20181213_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListJobsResponse(),
            self.do_rpcrequest('ListJobs', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: batch_compute_20181213_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListJobsResponse(),
            await self.do_rpcrequest_async('ListJobs', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs(
        self,
        request: batch_compute_20181213_models.ListJobsRequest,
    ) -> batch_compute_20181213_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: batch_compute_20181213_models.ListJobsRequest,
    ) -> batch_compute_20181213_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: batch_compute_20181213_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: batch_compute_20181213_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListProjectsResponse(),
            await self.do_rpcrequest_async('ListProjects', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(
        self,
        request: batch_compute_20181213_models.ListProjectsRequest,
    ) -> batch_compute_20181213_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: batch_compute_20181213_models.ListProjectsRequest,
    ) -> batch_compute_20181213_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: batch_compute_20181213_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListRegionsResponse(),
            self.do_rpcrequest('ListRegions', '2018-12-13', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: batch_compute_20181213_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListRegionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListRegionsResponse(),
            await self.do_rpcrequest_async('ListRegions', '2018-12-13', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_regions(
        self,
        request: batch_compute_20181213_models.ListRegionsRequest,
    ) -> batch_compute_20181213_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: batch_compute_20181213_models.ListRegionsRequest,
    ) -> batch_compute_20181213_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_workers_with_options(
        self,
        request: batch_compute_20181213_models.ListWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListWorkersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListWorkersResponse(),
            self.do_rpcrequest('ListWorkers', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_workers_with_options_async(
        self,
        request: batch_compute_20181213_models.ListWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.ListWorkersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.ListWorkersResponse(),
            await self.do_rpcrequest_async('ListWorkers', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_workers(
        self,
        request: batch_compute_20181213_models.ListWorkersRequest,
    ) -> batch_compute_20181213_models.ListWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_workers_with_options(request, runtime)

    async def list_workers_async(
        self,
        request: batch_compute_20181213_models.ListWorkersRequest,
    ) -> batch_compute_20181213_models.ListWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_workers_with_options_async(request, runtime)

    def open_batch_compute_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.OpenBatchComputeServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            batch_compute_20181213_models.OpenBatchComputeServiceResponse(),
            self.do_rpcrequest('OpenBatchComputeService', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_batch_compute_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.OpenBatchComputeServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            batch_compute_20181213_models.OpenBatchComputeServiceResponse(),
            await self.do_rpcrequest_async('OpenBatchComputeService', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_batch_compute_service(self) -> batch_compute_20181213_models.OpenBatchComputeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_batch_compute_service_with_options(runtime)

    async def open_batch_compute_service_async(self) -> batch_compute_20181213_models.OpenBatchComputeServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_batch_compute_service_with_options_async(runtime)

    def poll_cmd_with_options(
        self,
        request: batch_compute_20181213_models.PollCmdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.PollCmdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.PollCmdResponse(),
            self.do_rpcrequest('PollCmd', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def poll_cmd_with_options_async(
        self,
        request: batch_compute_20181213_models.PollCmdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.PollCmdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.PollCmdResponse(),
            await self.do_rpcrequest_async('PollCmd', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def poll_cmd(
        self,
        request: batch_compute_20181213_models.PollCmdRequest,
    ) -> batch_compute_20181213_models.PollCmdResponse:
        runtime = util_models.RuntimeOptions()
        return self.poll_cmd_with_options(request, runtime)

    async def poll_cmd_async(
        self,
        request: batch_compute_20181213_models.PollCmdRequest,
    ) -> batch_compute_20181213_models.PollCmdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.poll_cmd_with_options_async(request, runtime)

    def recreate_worker_with_options(
        self,
        request: batch_compute_20181213_models.RecreateWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.RecreateWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.RecreateWorkerResponse(),
            self.do_rpcrequest('RecreateWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recreate_worker_with_options_async(
        self,
        request: batch_compute_20181213_models.RecreateWorkerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.RecreateWorkerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.RecreateWorkerResponse(),
            await self.do_rpcrequest_async('RecreateWorker', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recreate_worker(
        self,
        request: batch_compute_20181213_models.RecreateWorkerRequest,
    ) -> batch_compute_20181213_models.RecreateWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return self.recreate_worker_with_options(request, runtime)

    async def recreate_worker_async(
        self,
        request: batch_compute_20181213_models.RecreateWorkerRequest,
    ) -> batch_compute_20181213_models.RecreateWorkerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recreate_worker_with_options_async(request, runtime)

    def run_job_with_options(
        self,
        tmp_req: batch_compute_20181213_models.RunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.RunJobResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.RunJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.RunJobResponse(),
            self.do_rpcrequest('RunJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_job_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.RunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.RunJobResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.RunJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.RunJobResponse(),
            await self.do_rpcrequest_async('RunJob', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_job(
        self,
        request: batch_compute_20181213_models.RunJobRequest,
    ) -> batch_compute_20181213_models.RunJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_job_with_options(request, runtime)

    async def run_job_async(
        self,
        request: batch_compute_20181213_models.RunJobRequest,
    ) -> batch_compute_20181213_models.RunJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_job_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        tmp_req: batch_compute_20181213_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateClusterResponse(),
            self.do_rpcrequest('UpdateCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateClusterResponse(),
            await self.do_rpcrequest_async('UpdateCluster', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cluster(
        self,
        request: batch_compute_20181213_models.UpdateClusterRequest,
    ) -> batch_compute_20181213_models.UpdateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: batch_compute_20181213_models.UpdateClusterRequest,
    ) -> batch_compute_20181213_models.UpdateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_job_queue_with_options(
        self,
        tmp_req: batch_compute_20181213_models.UpdateJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateJobQueueResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateJobQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateJobQueueResponse(),
            self.do_rpcrequest('UpdateJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_job_queue_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.UpdateJobQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateJobQueueResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateJobQueueShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateJobQueueResponse(),
            await self.do_rpcrequest_async('UpdateJobQueue', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_job_queue(
        self,
        request: batch_compute_20181213_models.UpdateJobQueueRequest,
    ) -> batch_compute_20181213_models.UpdateJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_job_queue_with_options(request, runtime)

    async def update_job_queue_async(
        self,
        request: batch_compute_20181213_models.UpdateJobQueueRequest,
    ) -> batch_compute_20181213_models.UpdateJobQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_job_queue_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: batch_compute_20181213_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: batch_compute_20181213_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = batch_compute_20181213_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.definition):
            request.definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.definition), 'Definition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateProjectResponse(),
            await self.do_rpcrequest_async('UpdateProject', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(
        self,
        request: batch_compute_20181213_models.UpdateProjectRequest,
    ) -> batch_compute_20181213_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: batch_compute_20181213_models.UpdateProjectRequest,
    ) -> batch_compute_20181213_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_worker_status_with_options(
        self,
        request: batch_compute_20181213_models.UpdateWorkerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateWorkerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateWorkerStatusResponse(),
            self.do_rpcrequest('UpdateWorkerStatus', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_worker_status_with_options_async(
        self,
        request: batch_compute_20181213_models.UpdateWorkerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> batch_compute_20181213_models.UpdateWorkerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            batch_compute_20181213_models.UpdateWorkerStatusResponse(),
            await self.do_rpcrequest_async('UpdateWorkerStatus', '2018-12-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_worker_status(
        self,
        request: batch_compute_20181213_models.UpdateWorkerStatusRequest,
    ) -> batch_compute_20181213_models.UpdateWorkerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_worker_status_with_options(request, runtime)

    async def update_worker_status_async(
        self,
        request: batch_compute_20181213_models.UpdateWorkerStatusRequest,
    ) -> batch_compute_20181213_models.UpdateWorkerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_worker_status_with_options_async(request, runtime)
