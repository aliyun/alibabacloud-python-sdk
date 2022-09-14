# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpc20170714 import models as ehpc20170714_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ehpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_nodes_with_options(
        self,
        request: ehpc20170714_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.AddNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.AddNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_nodes_with_options_async(
        self,
        request: ehpc20170714_models.AddNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.AddNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.AddNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_nodes(
        self,
        request: ehpc20170714_models.AddNodesRequest,
    ) -> ehpc20170714_models.AddNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_nodes_with_options(request, runtime)

    async def add_nodes_async(
        self,
        request: ehpc20170714_models.AddNodesRequest,
    ) -> ehpc20170714_models.AddNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_nodes_with_options_async(request, runtime)

    def add_users_with_options(
        self,
        request: ehpc20170714_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.AddUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.AddUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_users_with_options_async(
        self,
        request: ehpc20170714_models.AddUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.AddUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.AddUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_users(
        self,
        request: ehpc20170714_models.AddUsersRequest,
    ) -> ehpc20170714_models.AddUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_users_with_options(request, runtime)

    async def add_users_async(
        self,
        request: ehpc20170714_models.AddUsersRequest,
    ) -> ehpc20170714_models.AddUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: ehpc20170714_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: ehpc20170714_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: ehpc20170714_models.CreateClusterRequest,
    ) -> ehpc20170714_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: ehpc20170714_models.CreateClusterRequest,
    ) -> ehpc20170714_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_job_template_with_options(
        self,
        request: ehpc20170714_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.CreateJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobTemplate',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.CreateJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_template_with_options_async(
        self,
        request: ehpc20170714_models.CreateJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.CreateJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobTemplate',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.CreateJobTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_template(
        self,
        request: ehpc20170714_models.CreateJobTemplateRequest,
    ) -> ehpc20170714_models.CreateJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_template_with_options(request, runtime)

    async def create_job_template_async(
        self,
        request: ehpc20170714_models.CreateJobTemplateRequest,
    ) -> ehpc20170714_models.CreateJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_template_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: ehpc20170714_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: ehpc20170714_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: ehpc20170714_models.DeleteClusterRequest,
    ) -> ehpc20170714_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: ehpc20170714_models.DeleteClusterRequest,
    ) -> ehpc20170714_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_job_templates_with_options(
        self,
        request: ehpc20170714_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobTemplates',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_templates_with_options_async(
        self,
        request: ehpc20170714_models.DeleteJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobTemplates',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteJobTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_templates(
        self,
        request: ehpc20170714_models.DeleteJobTemplatesRequest,
    ) -> ehpc20170714_models.DeleteJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_templates_with_options(request, runtime)

    async def delete_job_templates_async(
        self,
        request: ehpc20170714_models.DeleteJobTemplatesRequest,
    ) -> ehpc20170714_models.DeleteJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_templates_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        request: ehpc20170714_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        request: ehpc20170714_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: ehpc20170714_models.DeleteJobsRequest,
    ) -> ehpc20170714_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: ehpc20170714_models.DeleteJobsRequest,
    ) -> ehpc20170714_models.DeleteJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def delete_nodes_with_options(
        self,
        request: ehpc20170714_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nodes_with_options_async(
        self,
        request: ehpc20170714_models.DeleteNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nodes(
        self,
        request: ehpc20170714_models.DeleteNodesRequest,
    ) -> ehpc20170714_models.DeleteNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nodes_with_options(request, runtime)

    async def delete_nodes_async(
        self,
        request: ehpc20170714_models.DeleteNodesRequest,
    ) -> ehpc20170714_models.DeleteNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nodes_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        request: ehpc20170714_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        request: ehpc20170714_models.DeleteUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DeleteUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: ehpc20170714_models.DeleteUsersRequest,
    ) -> ehpc20170714_models.DeleteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: ehpc20170714_models.DeleteUsersRequest,
    ) -> ehpc20170714_models.DeleteUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: ehpc20170714_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: ehpc20170714_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.DescribeClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.DescribeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster(
        self,
        request: ehpc20170714_models.DescribeClusterRequest,
    ) -> ehpc20170714_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: ehpc20170714_models.DescribeClusterRequest,
    ) -> ehpc20170714_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def edit_job_template_with_options(
        self,
        request: ehpc20170714_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.EditJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditJobTemplate',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.EditJobTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_job_template_with_options_async(
        self,
        request: ehpc20170714_models.EditJobTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.EditJobTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditJobTemplate',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.EditJobTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_job_template(
        self,
        request: ehpc20170714_models.EditJobTemplateRequest,
    ) -> ehpc20170714_models.EditJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_job_template_with_options(request, runtime)

    async def edit_job_template_async(
        self,
        request: ehpc20170714_models.EditJobTemplateRequest,
    ) -> ehpc20170714_models.EditJobTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_job_template_with_options_async(request, runtime)

    def get_auto_scale_config_with_options(
        self,
        request: ehpc20170714_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.GetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScaleConfig',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.GetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scale_config_with_options_async(
        self,
        request: ehpc20170714_models.GetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.GetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScaleConfig',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.GetAutoScaleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scale_config(
        self,
        request: ehpc20170714_models.GetAutoScaleConfigRequest,
    ) -> ehpc20170714_models.GetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scale_config_with_options(request, runtime)

    async def get_auto_scale_config_async(
        self,
        request: ehpc20170714_models.GetAutoScaleConfigRequest,
    ) -> ehpc20170714_models.GetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scale_config_with_options_async(request, runtime)

    def list_cluster_logs_with_options(
        self,
        request: ehpc20170714_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListClusterLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterLogs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_logs_with_options_async(
        self,
        request: ehpc20170714_models.ListClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListClusterLogsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterLogs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListClusterLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_logs(
        self,
        request: ehpc20170714_models.ListClusterLogsRequest,
    ) -> ehpc20170714_models.ListClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_logs_with_options(request, runtime)

    async def list_cluster_logs_async(
        self,
        request: ehpc20170714_models.ListClusterLogsRequest,
    ) -> ehpc20170714_models.ListClusterLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_logs_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: ehpc20170714_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: ehpc20170714_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: ehpc20170714_models.ListClustersRequest,
    ) -> ehpc20170714_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ehpc20170714_models.ListClustersRequest,
    ) -> ehpc20170714_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_current_client_version_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListCurrentClientVersionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCurrentClientVersion',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListCurrentClientVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_current_client_version_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListCurrentClientVersionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCurrentClientVersion',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListCurrentClientVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_current_client_version(self) -> ehpc20170714_models.ListCurrentClientVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_current_client_version_with_options(runtime)

    async def list_current_client_version_async(self) -> ehpc20170714_models.ListCurrentClientVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_current_client_version_with_options_async(runtime)

    def list_custom_images_with_options(
        self,
        request: ehpc20170714_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListCustomImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_images_with_options_async(
        self,
        request: ehpc20170714_models.ListCustomImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListCustomImagesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomImages',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListCustomImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_images(
        self,
        request: ehpc20170714_models.ListCustomImagesRequest,
    ) -> ehpc20170714_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_custom_images_with_options(request, runtime)

    async def list_custom_images_async(
        self,
        request: ehpc20170714_models.ListCustomImagesRequest,
    ) -> ehpc20170714_models.ListCustomImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_images_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListImagesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListImages',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListImagesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListImages',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(self) -> ehpc20170714_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(runtime)

    async def list_images_async(self) -> ehpc20170714_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(runtime)

    def list_job_templates_with_options(
        self,
        request: ehpc20170714_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobTemplates',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListJobTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_templates_with_options_async(
        self,
        request: ehpc20170714_models.ListJobTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListJobTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobTemplates',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListJobTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_templates(
        self,
        request: ehpc20170714_models.ListJobTemplatesRequest,
    ) -> ehpc20170714_models.ListJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_templates_with_options(request, runtime)

    async def list_job_templates_async(
        self,
        request: ehpc20170714_models.ListJobTemplatesRequest,
    ) -> ehpc20170714_models.ListJobTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_templates_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: ehpc20170714_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: ehpc20170714_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: ehpc20170714_models.ListJobsRequest,
    ) -> ehpc20170714_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc20170714_models.ListJobsRequest,
    ) -> ehpc20170714_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: ehpc20170714_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: ehpc20170714_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: ehpc20170714_models.ListNodesRequest,
    ) -> ehpc20170714_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: ehpc20170714_models.ListNodesRequest,
    ) -> ehpc20170714_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_nodes_no_paging_with_options(
        self,
        request: ehpc20170714_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListNodesNoPagingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesNoPaging',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListNodesNoPagingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_no_paging_with_options_async(
        self,
        request: ehpc20170714_models.ListNodesNoPagingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListNodesNoPagingResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodesNoPaging',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListNodesNoPagingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes_no_paging(
        self,
        request: ehpc20170714_models.ListNodesNoPagingRequest,
    ) -> ehpc20170714_models.ListNodesNoPagingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_no_paging_with_options(request, runtime)

    async def list_nodes_no_paging_async(
        self,
        request: ehpc20170714_models.ListNodesNoPagingRequest,
    ) -> ehpc20170714_models.ListNodesNoPagingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_no_paging_with_options_async(request, runtime)

    def list_preferred_ecs_types_with_options(
        self,
        request: ehpc20170714_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListPreferredEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPreferredEcsTypes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListPreferredEcsTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_preferred_ecs_types_with_options_async(
        self,
        request: ehpc20170714_models.ListPreferredEcsTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListPreferredEcsTypesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPreferredEcsTypes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListPreferredEcsTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_preferred_ecs_types(
        self,
        request: ehpc20170714_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20170714_models.ListPreferredEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_preferred_ecs_types_with_options(request, runtime)

    async def list_preferred_ecs_types_async(
        self,
        request: ehpc20170714_models.ListPreferredEcsTypesRequest,
    ) -> ehpc20170714_models.ListPreferredEcsTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_preferred_ecs_types_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRegions',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> ehpc20170714_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> ehpc20170714_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_softwares_with_options(
        self,
        request: ehpc20170714_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListSoftwaresResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwares',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListSoftwaresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_softwares_with_options_async(
        self,
        request: ehpc20170714_models.ListSoftwaresRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListSoftwaresResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwares',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListSoftwaresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_softwares(
        self,
        request: ehpc20170714_models.ListSoftwaresRequest,
    ) -> ehpc20170714_models.ListSoftwaresResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_softwares_with_options(request, runtime)

    async def list_softwares_async(
        self,
        request: ehpc20170714_models.ListSoftwaresRequest,
    ) -> ehpc20170714_models.ListSoftwaresResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_softwares_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ehpc20170714_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ehpc20170714_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: ehpc20170714_models.ListUsersRequest,
    ) -> ehpc20170714_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ehpc20170714_models.ListUsersRequest,
    ) -> ehpc20170714_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_volumes_with_options(
        self,
        request: ehpc20170714_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVolumes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_volumes_with_options_async(
        self,
        request: ehpc20170714_models.ListVolumesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ListVolumesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVolumes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ListVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_volumes(
        self,
        request: ehpc20170714_models.ListVolumesRequest,
    ) -> ehpc20170714_models.ListVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_volumes_with_options(request, runtime)

    async def list_volumes_async(
        self,
        request: ehpc20170714_models.ListVolumesRequest,
    ) -> ehpc20170714_models.ListVolumesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_volumes_with_options_async(request, runtime)

    def modify_cluster_attributes_with_options(
        self,
        request: ehpc20170714_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyClusterAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAttributes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyClusterAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_attributes_with_options_async(
        self,
        request: ehpc20170714_models.ModifyClusterAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyClusterAttributesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAttributes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyClusterAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_attributes(
        self,
        request: ehpc20170714_models.ModifyClusterAttributesRequest,
    ) -> ehpc20170714_models.ModifyClusterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_attributes_with_options(request, runtime)

    async def modify_cluster_attributes_async(
        self,
        request: ehpc20170714_models.ModifyClusterAttributesRequest,
    ) -> ehpc20170714_models.ModifyClusterAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_attributes_with_options_async(request, runtime)

    def modify_user_groups_with_options(
        self,
        request: ehpc20170714_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroups',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_groups_with_options_async(
        self,
        request: ehpc20170714_models.ModifyUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyUserGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroups',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_groups(
        self,
        request: ehpc20170714_models.ModifyUserGroupsRequest,
    ) -> ehpc20170714_models.ModifyUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_groups_with_options(request, runtime)

    async def modify_user_groups_async(
        self,
        request: ehpc20170714_models.ModifyUserGroupsRequest,
    ) -> ehpc20170714_models.ModifyUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_groups_with_options_async(request, runtime)

    def modify_user_passwords_with_options(
        self,
        request: ehpc20170714_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyUserPasswordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPasswords',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyUserPasswordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_user_passwords_with_options_async(
        self,
        request: ehpc20170714_models.ModifyUserPasswordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ModifyUserPasswordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserPasswords',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ModifyUserPasswordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_user_passwords(
        self,
        request: ehpc20170714_models.ModifyUserPasswordsRequest,
    ) -> ehpc20170714_models.ModifyUserPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_passwords_with_options(request, runtime)

    async def modify_user_passwords_async(
        self,
        request: ehpc20170714_models.ModifyUserPasswordsRequest,
    ) -> ehpc20170714_models.ModifyUserPasswordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_passwords_with_options_async(request, runtime)

    def rerun_jobs_with_options(
        self,
        request: ehpc20170714_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.RerunJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.RerunJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_jobs_with_options_async(
        self,
        request: ehpc20170714_models.RerunJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.RerunJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.RerunJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_jobs(
        self,
        request: ehpc20170714_models.RerunJobsRequest,
    ) -> ehpc20170714_models.RerunJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.rerun_jobs_with_options(request, runtime)

    async def rerun_jobs_async(
        self,
        request: ehpc20170714_models.RerunJobsRequest,
    ) -> ehpc20170714_models.RerunJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_jobs_with_options_async(request, runtime)

    def reset_nodes_with_options(
        self,
        request: ehpc20170714_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ResetNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ResetNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_nodes_with_options_async(
        self,
        request: ehpc20170714_models.ResetNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.ResetNodesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetNodes',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.ResetNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_nodes(
        self,
        request: ehpc20170714_models.ResetNodesRequest,
    ) -> ehpc20170714_models.ResetNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_nodes_with_options(request, runtime)

    async def reset_nodes_async(
        self,
        request: ehpc20170714_models.ResetNodesRequest,
    ) -> ehpc20170714_models.ResetNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_nodes_with_options_async(request, runtime)

    def set_auto_scale_config_with_options(
        self,
        request: ehpc20170714_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAutoScaleConfig',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SetAutoScaleConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_auto_scale_config_with_options_async(
        self,
        request: ehpc20170714_models.SetAutoScaleConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SetAutoScaleConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAutoScaleConfig',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SetAutoScaleConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_auto_scale_config(
        self,
        request: ehpc20170714_models.SetAutoScaleConfigRequest,
    ) -> ehpc20170714_models.SetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_auto_scale_config_with_options(request, runtime)

    async def set_auto_scale_config_async(
        self,
        request: ehpc20170714_models.SetAutoScaleConfigRequest,
    ) -> ehpc20170714_models.SetAutoScaleConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_auto_scale_config_with_options_async(request, runtime)

    def set_job_user_with_options(
        self,
        request: ehpc20170714_models.SetJobUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SetJobUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetJobUser',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SetJobUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_job_user_with_options_async(
        self,
        request: ehpc20170714_models.SetJobUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SetJobUserResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetJobUser',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SetJobUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_job_user(
        self,
        request: ehpc20170714_models.SetJobUserRequest,
    ) -> ehpc20170714_models.SetJobUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_job_user_with_options(request, runtime)

    async def set_job_user_async(
        self,
        request: ehpc20170714_models.SetJobUserRequest,
    ) -> ehpc20170714_models.SetJobUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_job_user_with_options_async(request, runtime)

    def stop_jobs_with_options(
        self,
        request: ehpc20170714_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.StopJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.StopJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_jobs_with_options_async(
        self,
        request: ehpc20170714_models.StopJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.StopJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopJobs',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.StopJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_jobs(
        self,
        request: ehpc20170714_models.StopJobsRequest,
    ) -> ehpc20170714_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_jobs_with_options(request, runtime)

    async def stop_jobs_async(
        self,
        request: ehpc20170714_models.StopJobsRequest,
    ) -> ehpc20170714_models.StopJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_jobs_with_options_async(request, runtime)

    def submit_job_with_options(
        self,
        request: ehpc20170714_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SubmitJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJob',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SubmitJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_job_with_options_async(
        self,
        request: ehpc20170714_models.SubmitJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.SubmitJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitJob',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.SubmitJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_job(
        self,
        request: ehpc20170714_models.SubmitJobRequest,
    ) -> ehpc20170714_models.SubmitJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_job_with_options(request, runtime)

    async def submit_job_async(
        self,
        request: ehpc20170714_models.SubmitJobRequest,
    ) -> ehpc20170714_models.SubmitJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_job_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: ehpc20170714_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.UpgradeClientResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_client_with_options_async(
        self,
        request: ehpc20170714_models.UpgradeClientRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc20170714_models.UpgradeClientResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeClient',
            version='2017-07-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc20170714_models.UpgradeClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_client(
        self,
        request: ehpc20170714_models.UpgradeClientRequest,
    ) -> ehpc20170714_models.UpgradeClientResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: ehpc20170714_models.UpgradeClientRequest,
    ) -> ehpc20170714_models.UpgradeClientResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)
