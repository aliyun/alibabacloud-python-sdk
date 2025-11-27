# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ehpcinstant20230701 import models as ehpc_instant_20230701_models
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
        self._endpoint = self.get_endpoint('ehpcinstant', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.AddImageResponse:
        """
        @summary Add a custom image.
        
        @param tmp_req: AddImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.container_image_spec):
            request.container_image_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container_image_spec, 'ContainerImageSpec', 'json')
        if not UtilClient.is_unset(tmp_req.vmimage_spec):
            request.vmimage_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vmimage_spec, 'VMImageSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.container_image_spec_shrink):
            query['ContainerImageSpec'] = request.container_image_spec_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_version):
            query['ImageVersion'] = request.image_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.vmimage_spec_shrink):
            query['VMImageSpec'] = request.vmimage_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.AddImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.AddImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.AddImageResponse:
        """
        @summary Add a custom image.
        
        @param tmp_req: AddImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.AddImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.container_image_spec):
            request.container_image_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container_image_spec, 'ContainerImageSpec', 'json')
        if not UtilClient.is_unset(tmp_req.vmimage_spec):
            request.vmimage_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vmimage_spec, 'VMImageSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.container_image_spec_shrink):
            query['ContainerImageSpec'] = request.container_image_spec_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.image_version):
            query['ImageVersion'] = request.image_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.vmimage_spec_shrink):
            query['VMImageSpec'] = request.vmimage_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.AddImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image(
        self,
        request: ehpc_instant_20230701_models.AddImageRequest,
    ) -> ehpc_instant_20230701_models.AddImageResponse:
        """
        @summary Add a custom image.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_image_with_options(request, runtime)

    async def add_image_async(
        self,
        request: ehpc_instant_20230701_models.AddImageRequest,
    ) -> ehpc_instant_20230701_models.AddImageResponse:
        """
        @summary Add a custom image.
        
        @param request: AddImageRequest
        @return: AddImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_image_with_options_async(request, runtime)

    def create_action_plan_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.CreateActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreateActionPlanResponse:
        """
        @summary Create a E-HPC execution plan.
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).
        
        @param tmp_req: CreateActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateActionPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreateActionPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.regions):
            request.regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_plan_name):
            query['ActionPlanName'] = request.action_plan_name
        if not UtilClient.is_unset(request.allocation_spec):
            query['AllocationSpec'] = request.allocation_spec
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.prolog_script):
            query['PrologScript'] = request.prolog_script
        if not UtilClient.is_unset(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resources_shrink):
            query['Resources'] = request.resources_shrink
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreateActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_action_plan_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.CreateActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreateActionPlanResponse:
        """
        @summary Create a E-HPC execution plan.
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).
        
        @param tmp_req: CreateActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateActionPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreateActionPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.regions):
            request.regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        if not UtilClient.is_unset(tmp_req.resources):
            request.resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resources, 'Resources', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_plan_name):
            query['ActionPlanName'] = request.action_plan_name
        if not UtilClient.is_unset(request.allocation_spec):
            query['AllocationSpec'] = request.allocation_spec
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.level):
            query['Level'] = request.level
        if not UtilClient.is_unset(request.prolog_script):
            query['PrologScript'] = request.prolog_script
        if not UtilClient.is_unset(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resources_shrink):
            query['Resources'] = request.resources_shrink
        if not UtilClient.is_unset(request.script):
            query['Script'] = request.script
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreateActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_action_plan(
        self,
        request: ehpc_instant_20230701_models.CreateActionPlanRequest,
    ) -> ehpc_instant_20230701_models.CreateActionPlanResponse:
        """
        @summary Create a E-HPC execution plan.
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).
        
        @param request: CreateActionPlanRequest
        @return: CreateActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_action_plan_with_options(request, runtime)

    async def create_action_plan_async(
        self,
        request: ehpc_instant_20230701_models.CreateActionPlanRequest,
    ) -> ehpc_instant_20230701_models.CreateActionPlanResponse:
        """
        @summary Create a E-HPC execution plan.
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).
        
        @param request: CreateActionPlanRequest
        @return: CreateActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_action_plan_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreateJobResponse:
        """
        @summary Create a E-HPC Instant job.
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependency_policy):
            request.dependency_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependency_policy, 'DependencyPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_policy):
            request.deployment_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_policy, 'DeploymentPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.tasks):
            request.tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.dependency_policy_shrink):
            query['DependencyPolicy'] = request.dependency_policy_shrink
        if not UtilClient.is_unset(request.deployment_policy_shrink):
            query['DeploymentPolicy'] = request.deployment_policy_shrink
        if not UtilClient.is_unset(request.job_description):
            query['JobDescription'] = request.job_description
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not UtilClient.is_unset(request.security_policy_shrink):
            query['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.tasks_shrink):
            query['Tasks'] = request.tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreateJobResponse:
        """
        @summary Create a E-HPC Instant job.
        
        @param tmp_req: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dependency_policy):
            request.dependency_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dependency_policy, 'DependencyPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_policy):
            request.deployment_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_policy, 'DeploymentPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.security_policy):
            request.security_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.security_policy, 'SecurityPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.tasks):
            request.tasks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tasks, 'Tasks', 'json')
        query = {}
        if not UtilClient.is_unset(request.dependency_policy_shrink):
            query['DependencyPolicy'] = request.dependency_policy_shrink
        if not UtilClient.is_unset(request.deployment_policy_shrink):
            query['DeploymentPolicy'] = request.deployment_policy_shrink
        if not UtilClient.is_unset(request.job_description):
            query['JobDescription'] = request.job_description
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not UtilClient.is_unset(request.security_policy_shrink):
            query['SecurityPolicy'] = request.security_policy_shrink
        if not UtilClient.is_unset(request.tasks_shrink):
            query['Tasks'] = request.tasks_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: ehpc_instant_20230701_models.CreateJobRequest,
    ) -> ehpc_instant_20230701_models.CreateJobResponse:
        """
        @summary Create a E-HPC Instant job.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: ehpc_instant_20230701_models.CreateJobRequest,
    ) -> ehpc_instant_20230701_models.CreateJobResponse:
        """
        @summary Create a E-HPC Instant job.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_pool_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.CreatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreatePoolResponse:
        """
        @summary Creates a resource pool.
        
        @param tmp_req: CreatePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreatePoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_limits):
            request.resource_limits_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreatePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pool_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.CreatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.CreatePoolResponse:
        """
        @summary Creates a resource pool.
        
        @param tmp_req: CreatePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.CreatePoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_limits):
            request.resource_limits_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.CreatePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pool(
        self,
        request: ehpc_instant_20230701_models.CreatePoolRequest,
    ) -> ehpc_instant_20230701_models.CreatePoolResponse:
        """
        @summary Creates a resource pool.
        
        @param request: CreatePoolRequest
        @return: CreatePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pool_with_options(request, runtime)

    async def create_pool_async(
        self,
        request: ehpc_instant_20230701_models.CreatePoolRequest,
    ) -> ehpc_instant_20230701_models.CreatePoolResponse:
        """
        @summary Creates a resource pool.
        
        @param request: CreatePoolRequest
        @return: CreatePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pool_with_options_async(request, runtime)

    def delete_action_plan_with_options(
        self,
        request: ehpc_instant_20230701_models.DeleteActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteActionPlanResponse:
        """
        @summary Delete an execution plan
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).**\
        This operation stops all Instant jobs that are managed by ActionPlanId.
        
        @param request: DeleteActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_action_plan_with_options_async(
        self,
        request: ehpc_instant_20230701_models.DeleteActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteActionPlanResponse:
        """
        @summary Delete an execution plan
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).**\
        This operation stops all Instant jobs that are managed by ActionPlanId.
        
        @param request: DeleteActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_action_plan(
        self,
        request: ehpc_instant_20230701_models.DeleteActionPlanRequest,
    ) -> ehpc_instant_20230701_models.DeleteActionPlanResponse:
        """
        @summary Delete an execution plan
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).**\
        This operation stops all Instant jobs that are managed by ActionPlanId.
        
        @param request: DeleteActionPlanRequest
        @return: DeleteActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_action_plan_with_options(request, runtime)

    async def delete_action_plan_async(
        self,
        request: ehpc_instant_20230701_models.DeleteActionPlanRequest,
    ) -> ehpc_instant_20230701_models.DeleteActionPlanResponse:
        """
        @summary Delete an execution plan
        
        @description *Make sure that you fully understand E-HPC Instnat billing methods and [prices](https://help.aliyun.com/zh/e-hpc/e-hpc-instant/product-overview/billing-overview?spm=a2c4g.11186623.help-menu-57664.d_0_2_0.5fdd28422y6UvO).**\
        This operation stops all Instant jobs that are managed by ActionPlanId.
        
        @param request: DeleteActionPlanRequest
        @return: DeleteActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_action_plan_with_options_async(request, runtime)

    def delete_job_records_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.DeleteJobRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteJobRecordsResponse:
        """
        @summary Deletes one or more job records that are in the final state from a specified cluster.
        
        @param tmp_req: DeleteJobRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DeleteJobRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobRecords',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteJobRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_records_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.DeleteJobRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteJobRecordsResponse:
        """
        @summary Deletes one or more job records that are in the final state from a specified cluster.
        
        @param tmp_req: DeleteJobRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DeleteJobRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_ids):
            request.job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_ids, 'JobIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_ids_shrink):
            query['JobIds'] = request.job_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobRecords',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteJobRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_records(
        self,
        request: ehpc_instant_20230701_models.DeleteJobRecordsRequest,
    ) -> ehpc_instant_20230701_models.DeleteJobRecordsResponse:
        """
        @summary Deletes one or more job records that are in the final state from a specified cluster.
        
        @param request: DeleteJobRecordsRequest
        @return: DeleteJobRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_job_records_with_options(request, runtime)

    async def delete_job_records_async(
        self,
        request: ehpc_instant_20230701_models.DeleteJobRecordsRequest,
    ) -> ehpc_instant_20230701_models.DeleteJobRecordsResponse:
        """
        @summary Deletes one or more job records that are in the final state from a specified cluster.
        
        @param request: DeleteJobRecordsRequest
        @return: DeleteJobRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_records_with_options_async(request, runtime)

    def delete_jobs_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteJobsResponse:
        """
        @summary Deletes one or more jobs from a specified cluster.
        
        @param tmp_req: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'ExecutorIds', 'json')
        if not UtilClient.is_unset(tmp_req.job_spec):
            request.job_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.executor_ids_shrink):
            query['ExecutorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not UtilClient.is_unset(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_jobs_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.DeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeleteJobsResponse:
        """
        @summary Deletes one or more jobs from a specified cluster.
        
        @param tmp_req: DeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DeleteJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.executor_ids):
            request.executor_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executor_ids, 'ExecutorIds', 'json')
        if not UtilClient.is_unset(tmp_req.job_spec):
            request.job_spec_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_spec, 'JobSpec', 'json')
        query = {}
        if not UtilClient.is_unset(request.executor_ids_shrink):
            query['ExecutorIds'] = request.executor_ids_shrink
        if not UtilClient.is_unset(request.job_scheduler):
            query['JobScheduler'] = request.job_scheduler
        if not UtilClient.is_unset(request.job_spec_shrink):
            query['JobSpec'] = request.job_spec_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_jobs(
        self,
        request: ehpc_instant_20230701_models.DeleteJobsRequest,
    ) -> ehpc_instant_20230701_models.DeleteJobsResponse:
        """
        @summary Deletes one or more jobs from a specified cluster.
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_jobs_with_options(request, runtime)

    async def delete_jobs_async(
        self,
        request: ehpc_instant_20230701_models.DeleteJobsRequest,
    ) -> ehpc_instant_20230701_models.DeleteJobsResponse:
        """
        @summary Deletes one or more jobs from a specified cluster.
        
        @param request: DeleteJobsRequest
        @return: DeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_jobs_with_options_async(request, runtime)

    def delete_pool_with_options(
        self,
        request: ehpc_instant_20230701_models.DeletePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeletePoolResponse:
        """
        @summary You can execute this statement to delete a resource pool.
        
        @param request: DeletePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeletePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pool_with_options_async(
        self,
        request: ehpc_instant_20230701_models.DeletePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DeletePoolResponse:
        """
        @summary You can execute this statement to delete a resource pool.
        
        @param request: DeletePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DeletePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pool(
        self,
        request: ehpc_instant_20230701_models.DeletePoolRequest,
    ) -> ehpc_instant_20230701_models.DeletePoolResponse:
        """
        @summary You can execute this statement to delete a resource pool.
        
        @param request: DeletePoolRequest
        @return: DeletePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_pool_with_options(request, runtime)

    async def delete_pool_async(
        self,
        request: ehpc_instant_20230701_models.DeletePoolRequest,
    ) -> ehpc_instant_20230701_models.DeletePoolResponse:
        """
        @summary You can execute this statement to delete a resource pool.
        
        @param request: DeletePoolRequest
        @return: DeletePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_pool_with_options_async(request, runtime)

    def describe_job_metric_data_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.DescribeJobMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricDataResponse:
        """
        @summary You can query the monitoring time series dataset of a job by specifying the job array index and query metric parameters.
        
        @param tmp_req: DescribeJobMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMetricDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DescribeJobMetricDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_index):
            request.array_index_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMetricData',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DescribeJobMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_metric_data_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.DescribeJobMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricDataResponse:
        """
        @summary You can query the monitoring time series dataset of a job by specifying the job array index and query metric parameters.
        
        @param tmp_req: DescribeJobMetricDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMetricDataResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DescribeJobMetricDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_index):
            request.array_index_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMetricData',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DescribeJobMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_metric_data(
        self,
        request: ehpc_instant_20230701_models.DescribeJobMetricDataRequest,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricDataResponse:
        """
        @summary You can query the monitoring time series dataset of a job by specifying the job array index and query metric parameters.
        
        @param request: DescribeJobMetricDataRequest
        @return: DescribeJobMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_metric_data_with_options(request, runtime)

    async def describe_job_metric_data_async(
        self,
        request: ehpc_instant_20230701_models.DescribeJobMetricDataRequest,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricDataResponse:
        """
        @summary You can query the monitoring time series dataset of a job by specifying the job array index and query metric parameters.
        
        @param request: DescribeJobMetricDataRequest
        @return: DescribeJobMetricDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_metric_data_with_options_async(request, runtime)

    def describe_job_metric_last_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.DescribeJobMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricLastResponse:
        """
        @summary Queries all instant monitoring metrics in the job array list by specifying a specific job array index list.
        
        @param tmp_req: DescribeJobMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMetricLastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DescribeJobMetricLastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_index):
            request.array_index_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMetricLast',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DescribeJobMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_metric_last_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.DescribeJobMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricLastResponse:
        """
        @summary Queries all instant monitoring metrics in the job array list by specifying a specific job array index list.
        
        @param tmp_req: DescribeJobMetricLastRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobMetricLastResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.DescribeJobMetricLastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.array_index):
            request.array_index_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.array_index, 'ArrayIndex', 'json')
        query = {}
        if not UtilClient.is_unset(request.array_index_shrink):
            query['ArrayIndex'] = request.array_index_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMetricLast',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.DescribeJobMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_metric_last(
        self,
        request: ehpc_instant_20230701_models.DescribeJobMetricLastRequest,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricLastResponse:
        """
        @summary Queries all instant monitoring metrics in the job array list by specifying a specific job array index list.
        
        @param request: DescribeJobMetricLastRequest
        @return: DescribeJobMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_metric_last_with_options(request, runtime)

    async def describe_job_metric_last_async(
        self,
        request: ehpc_instant_20230701_models.DescribeJobMetricLastRequest,
    ) -> ehpc_instant_20230701_models.DescribeJobMetricLastResponse:
        """
        @summary Queries all instant monitoring metrics in the job array list by specifying a specific job array index list.
        
        @param request: DescribeJobMetricLastRequest
        @return: DescribeJobMetricLastResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_metric_last_with_options_async(request, runtime)

    def get_action_plan_with_options(
        self,
        request: ehpc_instant_20230701_models.GetActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetActionPlanResponse:
        """
        @summary Querying Execution Plan Details
        
        @param request: GetActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_action_plan_with_options_async(
        self,
        request: ehpc_instant_20230701_models.GetActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetActionPlanResponse:
        """
        @summary Querying Execution Plan Details
        
        @param request: GetActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_action_plan(
        self,
        request: ehpc_instant_20230701_models.GetActionPlanRequest,
    ) -> ehpc_instant_20230701_models.GetActionPlanResponse:
        """
        @summary Querying Execution Plan Details
        
        @param request: GetActionPlanRequest
        @return: GetActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_action_plan_with_options(request, runtime)

    async def get_action_plan_async(
        self,
        request: ehpc_instant_20230701_models.GetActionPlanRequest,
    ) -> ehpc_instant_20230701_models.GetActionPlanResponse:
        """
        @summary Querying Execution Plan Details
        
        @param request: GetActionPlanRequest
        @return: GetActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_action_plan_with_options_async(request, runtime)

    def get_app_versions_with_options(
        self,
        request: ehpc_instant_20230701_models.GetAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetAppVersionsResponse:
        """
        @summary Obtains the application version list.
        
        @param request: GetAppVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppVersions',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_versions_with_options_async(
        self,
        request: ehpc_instant_20230701_models.GetAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetAppVersionsResponse:
        """
        @summary Obtains the application version list.
        
        @param request: GetAppVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppVersions',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_versions(
        self,
        request: ehpc_instant_20230701_models.GetAppVersionsRequest,
    ) -> ehpc_instant_20230701_models.GetAppVersionsResponse:
        """
        @summary Obtains the application version list.
        
        @param request: GetAppVersionsRequest
        @return: GetAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_versions_with_options(request, runtime)

    async def get_app_versions_async(
        self,
        request: ehpc_instant_20230701_models.GetAppVersionsRequest,
    ) -> ehpc_instant_20230701_models.GetAppVersionsResponse:
        """
        @summary Obtains the application version list.
        
        @param request: GetAppVersionsRequest
        @return: GetAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_versions_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param tmp_req: GetImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.GetImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_region_ids):
            request.additional_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_region_ids, 'AdditionalRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.additional_region_ids_shrink):
            query['AdditionalRegionIds'] = request.additional_region_ids_shrink
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param tmp_req: GetImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.GetImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.additional_region_ids):
            request.additional_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.additional_region_ids, 'AdditionalRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.additional_region_ids_shrink):
            query['AdditionalRegionIds'] = request.additional_region_ids_shrink
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: ehpc_instant_20230701_models.GetImageRequest,
    ) -> ehpc_instant_20230701_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: ehpc_instant_20230701_models.GetImageRequest,
    ) -> ehpc_instant_20230701_models.GetImageResponse:
        """
        @summary Obtains the information about an image.
        
        @param request: GetImageRequest
        @return: GetImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_job_with_options(
        self,
        request: ehpc_instant_20230701_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetJobResponse:
        """
        @summary Obtains the details of an execution job.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        request: ehpc_instant_20230701_models.GetJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetJobResponse:
        """
        @summary Obtains the details of an execution job.
        
        @param request: GetJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        request: ehpc_instant_20230701_models.GetJobRequest,
    ) -> ehpc_instant_20230701_models.GetJobResponse:
        """
        @summary Obtains the details of an execution job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_with_options(request, runtime)

    async def get_job_async(
        self,
        request: ehpc_instant_20230701_models.GetJobRequest,
    ) -> ehpc_instant_20230701_models.GetJobResponse:
        """
        @summary Obtains the details of an execution job.
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_with_options_async(request, runtime)

    def get_pool_with_options(
        self,
        request: ehpc_instant_20230701_models.GetPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetPoolResponse:
        """
        @summary Obtains the details of a resource pool.
        
        @param request: GetPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetPoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pool_with_options_async(
        self,
        request: ehpc_instant_20230701_models.GetPoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.GetPoolResponse:
        """
        @summary Obtains the details of a resource pool.
        
        @param request: GetPoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPoolResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.GetPoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pool(
        self,
        request: ehpc_instant_20230701_models.GetPoolRequest,
    ) -> ehpc_instant_20230701_models.GetPoolResponse:
        """
        @summary Obtains the details of a resource pool.
        
        @param request: GetPoolRequest
        @return: GetPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pool_with_options(request, runtime)

    async def get_pool_async(
        self,
        request: ehpc_instant_20230701_models.GetPoolRequest,
    ) -> ehpc_instant_20230701_models.GetPoolResponse:
        """
        @summary Obtains the details of a resource pool.
        
        @param request: GetPoolRequest
        @return: GetPoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pool_with_options_async(request, runtime)

    def list_action_plan_activities_with_options(
        self,
        request: ehpc_instant_20230701_models.ListActionPlanActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListActionPlanActivitiesResponse:
        """
        @summary Queries the execution status of an execution plan.
        
        @param request: ListActionPlanActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionPlanActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActionPlanActivities',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListActionPlanActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_action_plan_activities_with_options_async(
        self,
        request: ehpc_instant_20230701_models.ListActionPlanActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListActionPlanActivitiesResponse:
        """
        @summary Queries the execution status of an execution plan.
        
        @param request: ListActionPlanActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionPlanActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActionPlanActivities',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListActionPlanActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_action_plan_activities(
        self,
        request: ehpc_instant_20230701_models.ListActionPlanActivitiesRequest,
    ) -> ehpc_instant_20230701_models.ListActionPlanActivitiesResponse:
        """
        @summary Queries the execution status of an execution plan.
        
        @param request: ListActionPlanActivitiesRequest
        @return: ListActionPlanActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_action_plan_activities_with_options(request, runtime)

    async def list_action_plan_activities_async(
        self,
        request: ehpc_instant_20230701_models.ListActionPlanActivitiesRequest,
    ) -> ehpc_instant_20230701_models.ListActionPlanActivitiesResponse:
        """
        @summary Queries the execution status of an execution plan.
        
        @param request: ListActionPlanActivitiesRequest
        @return: ListActionPlanActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_action_plan_activities_with_options_async(request, runtime)

    def list_action_plans_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.ListActionPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListActionPlansResponse:
        """
        @summary Queries the list of execution plans.
        
        @param tmp_req: ListActionPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionPlansResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListActionPlansShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_plan_ids):
            request.action_plan_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_plan_ids, 'ActionPlanIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_plan_ids_shrink):
            query['ActionPlanIds'] = request.action_plan_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActionPlans',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListActionPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_action_plans_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.ListActionPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListActionPlansResponse:
        """
        @summary Queries the list of execution plans.
        
        @param tmp_req: ListActionPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListActionPlansResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListActionPlansShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.action_plan_ids):
            request.action_plan_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.action_plan_ids, 'ActionPlanIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.action_plan_ids_shrink):
            query['ActionPlanIds'] = request.action_plan_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActionPlans',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListActionPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_action_plans(
        self,
        request: ehpc_instant_20230701_models.ListActionPlansRequest,
    ) -> ehpc_instant_20230701_models.ListActionPlansResponse:
        """
        @summary Queries the list of execution plans.
        
        @param request: ListActionPlansRequest
        @return: ListActionPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_action_plans_with_options(request, runtime)

    async def list_action_plans_async(
        self,
        request: ehpc_instant_20230701_models.ListActionPlansRequest,
    ) -> ehpc_instant_20230701_models.ListActionPlansResponse:
        """
        @summary Queries the list of execution plans.
        
        @param request: ListActionPlansRequest
        @return: ListActionPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_action_plans_with_options_async(request, runtime)

    def list_executors_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.ListExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListExecutorsResponse:
        """
        @summary Querying Global Executor Information
        
        @param tmp_req: ListExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListExecutorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutors',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executors_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.ListExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListExecutorsResponse:
        """
        @summary Querying Global Executor Information
        
        @param tmp_req: ListExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExecutorsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListExecutorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExecutors',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executors(
        self,
        request: ehpc_instant_20230701_models.ListExecutorsRequest,
    ) -> ehpc_instant_20230701_models.ListExecutorsResponse:
        """
        @summary Querying Global Executor Information
        
        @param request: ListExecutorsRequest
        @return: ListExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_executors_with_options(request, runtime)

    async def list_executors_async(
        self,
        request: ehpc_instant_20230701_models.ListExecutorsRequest,
    ) -> ehpc_instant_20230701_models.ListExecutorsResponse:
        """
        @summary Querying Global Executor Information
        
        @param request: ListExecutorsRequest
        @return: ListExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_executors_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListImagesResponse:
        """
        @summary Queries the image list.
        
        @param tmp_req: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_ids):
            request.image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_ids_shrink):
            query['ImageIds'] = request.image_ids_shrink
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListImagesResponse:
        """
        @summary Queries the image list.
        
        @param tmp_req: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListImagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.image_ids):
            request.image_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_ids, 'ImageIds', 'json')
        if not UtilClient.is_unset(tmp_req.image_names):
            request.image_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_names, 'ImageNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_ids_shrink):
            query['ImageIds'] = request.image_ids_shrink
        if not UtilClient.is_unset(request.image_names_shrink):
            query['ImageNames'] = request.image_names_shrink
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: ehpc_instant_20230701_models.ListImagesRequest,
    ) -> ehpc_instant_20230701_models.ListImagesResponse:
        """
        @summary Queries the image list.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: ehpc_instant_20230701_models.ListImagesRequest,
    ) -> ehpc_instant_20230701_models.ListImagesResponse:
        """
        @summary Queries the image list.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_job_executors_with_options(
        self,
        request: ehpc_instant_20230701_models.ListJobExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListJobExecutorsResponse:
        """
        @summary Queries job executor information.
        
        @description Queries job executor information.
        
        @param request: ListJobExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobExecutorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobExecutors',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListJobExecutorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_executors_with_options_async(
        self,
        request: ehpc_instant_20230701_models.ListJobExecutorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListJobExecutorsResponse:
        """
        @summary Queries job executor information.
        
        @description Queries job executor information.
        
        @param request: ListJobExecutorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobExecutorsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobExecutors',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListJobExecutorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_executors(
        self,
        request: ehpc_instant_20230701_models.ListJobExecutorsRequest,
    ) -> ehpc_instant_20230701_models.ListJobExecutorsResponse:
        """
        @summary Queries job executor information.
        
        @description Queries job executor information.
        
        @param request: ListJobExecutorsRequest
        @return: ListJobExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_job_executors_with_options(request, runtime)

    async def list_job_executors_async(
        self,
        request: ehpc_instant_20230701_models.ListJobExecutorsRequest,
    ) -> ehpc_instant_20230701_models.ListJobExecutorsResponse:
        """
        @summary Queries job executor information.
        
        @description Queries job executor information.
        
        @param request: ListJobExecutorsRequest
        @return: ListJobExecutorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_job_executors_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param tmp_req: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not UtilClient.is_unset(tmp_req.sort_by):
            request.sort_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_by, 'SortBy', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by_shrink):
            query['SortBy'] = request.sort_by_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param tmp_req: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not UtilClient.is_unset(tmp_req.sort_by):
            request.sort_by_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort_by, 'SortBy', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by_shrink):
            query['SortBy'] = request.sort_by_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: ehpc_instant_20230701_models.ListJobsRequest,
    ) -> ehpc_instant_20230701_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: ehpc_instant_20230701_models.ListJobsRequest,
    ) -> ehpc_instant_20230701_models.ListJobsResponse:
        """
        @summary Queries the jobs in a cluster.
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_pools_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.ListPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListPoolsResponse:
        """
        @summary Queries the resource pool list.
        
        @param tmp_req: ListPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoolsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListPoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPools',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListPoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pools_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.ListPoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListPoolsResponse:
        """
        @summary Queries the resource pool list.
        
        @param tmp_req: ListPoolsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoolsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.ListPoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPools',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListPoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pools(
        self,
        request: ehpc_instant_20230701_models.ListPoolsRequest,
    ) -> ehpc_instant_20230701_models.ListPoolsResponse:
        """
        @summary Queries the resource pool list.
        
        @param request: ListPoolsRequest
        @return: ListPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_pools_with_options(request, runtime)

    async def list_pools_async(
        self,
        request: ehpc_instant_20230701_models.ListPoolsRequest,
    ) -> ehpc_instant_20230701_models.ListPoolsResponse:
        """
        @summary Queries the resource pool list.
        
        @param request: ListPoolsRequest
        @return: ListPoolsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_pools_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ehpc_instant_20230701_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more Instant resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ehpc_instant_20230701_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more Instant resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ehpc_instant_20230701_models.ListTagResourcesRequest,
    ) -> ehpc_instant_20230701_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more Instant resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ehpc_instant_20230701_models.ListTagResourcesRequest,
    ) -> ehpc_instant_20230701_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to one or more Instant resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def remove_image_with_options(
        self,
        request: ehpc_instant_20230701_models.RemoveImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.RemoveImageResponse:
        """
        @summary Remove a custom image
        
        @param request: RemoveImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.RemoveImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_image_with_options_async(
        self,
        request: ehpc_instant_20230701_models.RemoveImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.RemoveImageResponse:
        """
        @summary Remove a custom image
        
        @param request: RemoveImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_type):
            query['ImageType'] = request.image_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveImage',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.RemoveImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_image(
        self,
        request: ehpc_instant_20230701_models.RemoveImageRequest,
    ) -> ehpc_instant_20230701_models.RemoveImageResponse:
        """
        @summary Remove a custom image
        
        @param request: RemoveImageRequest
        @return: RemoveImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_image_with_options(request, runtime)

    async def remove_image_async(
        self,
        request: ehpc_instant_20230701_models.RemoveImageRequest,
    ) -> ehpc_instant_20230701_models.RemoveImageResponse:
        """
        @summary Remove a custom image
        
        @param request: RemoveImageRequest
        @return: RemoveImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_image_with_options_async(request, runtime)

    def synchronize_app_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.SynchronizeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.SynchronizeAppResponse:
        """
        @summary Application cross-region synchronization
        
        @param tmp_req: SynchronizeAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SynchronizeAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.SynchronizeAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_region_ids):
            request.target_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_region_ids, 'TargetRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.target_region_ids_shrink):
            query['TargetRegionIds'] = request.target_region_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeApp',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.SynchronizeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def synchronize_app_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.SynchronizeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.SynchronizeAppResponse:
        """
        @summary Application cross-region synchronization
        
        @param tmp_req: SynchronizeAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SynchronizeAppResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.SynchronizeAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.target_region_ids):
            request.target_region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_region_ids, 'TargetRegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.target_region_ids_shrink):
            query['TargetRegionIds'] = request.target_region_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SynchronizeApp',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.SynchronizeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def synchronize_app(
        self,
        request: ehpc_instant_20230701_models.SynchronizeAppRequest,
    ) -> ehpc_instant_20230701_models.SynchronizeAppResponse:
        """
        @summary Application cross-region synchronization
        
        @param request: SynchronizeAppRequest
        @return: SynchronizeAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.synchronize_app_with_options(request, runtime)

    async def synchronize_app_async(
        self,
        request: ehpc_instant_20230701_models.SynchronizeAppRequest,
    ) -> ehpc_instant_20230701_models.SynchronizeAppResponse:
        """
        @summary Application cross-region synchronization
        
        @param request: SynchronizeAppRequest
        @return: SynchronizeAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.synchronize_app_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ehpc_instant_20230701_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.TagResourcesResponse:
        """
        @summary Create and bind tags to Instant resource list
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ehpc_instant_20230701_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.TagResourcesResponse:
        """
        @summary Create and bind tags to Instant resource list
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ehpc_instant_20230701_models.TagResourcesRequest,
    ) -> ehpc_instant_20230701_models.TagResourcesResponse:
        """
        @summary Create and bind tags to Instant resource list
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ehpc_instant_20230701_models.TagResourcesRequest,
    ) -> ehpc_instant_20230701_models.TagResourcesResponse:
        """
        @summary Create and bind tags to Instant resource list
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: ehpc_instant_20230701_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UnTagResourcesResponse:
        """
        @summary Unbind tags from Instant resource list. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: ehpc_instant_20230701_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UnTagResourcesResponse:
        """
        @summary Unbind tags from Instant resource list. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: ehpc_instant_20230701_models.UnTagResourcesRequest,
    ) -> ehpc_instant_20230701_models.UnTagResourcesResponse:
        """
        @summary Unbind tags from Instant resource list. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: ehpc_instant_20230701_models.UnTagResourcesRequest,
    ) -> ehpc_instant_20230701_models.UnTagResourcesResponse:
        """
        @summary Unbind tags from Instant resource list. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_action_plan_with_options(
        self,
        request: ehpc_instant_20230701_models.UpdateActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UpdateActionPlanResponse:
        """
        @summary Adjust the resource scale of the execution plan or modify the execution status
        
        @param request: UpdateActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UpdateActionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_action_plan_with_options_async(
        self,
        request: ehpc_instant_20230701_models.UpdateActionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UpdateActionPlanResponse:
        """
        @summary Adjust the resource scale of the execution plan or modify the execution status
        
        @param request: UpdateActionPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateActionPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_plan_id):
            query['ActionPlanId'] = request.action_plan_id
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateActionPlan',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UpdateActionPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_action_plan(
        self,
        request: ehpc_instant_20230701_models.UpdateActionPlanRequest,
    ) -> ehpc_instant_20230701_models.UpdateActionPlanResponse:
        """
        @summary Adjust the resource scale of the execution plan or modify the execution status
        
        @param request: UpdateActionPlanRequest
        @return: UpdateActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_action_plan_with_options(request, runtime)

    async def update_action_plan_async(
        self,
        request: ehpc_instant_20230701_models.UpdateActionPlanRequest,
    ) -> ehpc_instant_20230701_models.UpdateActionPlanResponse:
        """
        @summary Adjust the resource scale of the execution plan or modify the execution status
        
        @param request: UpdateActionPlanRequest
        @return: UpdateActionPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_action_plan_with_options_async(request, runtime)

    def update_pool_with_options(
        self,
        tmp_req: ehpc_instant_20230701_models.UpdatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UpdatePoolResponse:
        """
        @summary Update the resource pool configuration.
        
        @param tmp_req: UpdatePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.UpdatePoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_limits):
            request.resource_limits_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UpdatePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pool_with_options_async(
        self,
        tmp_req: ehpc_instant_20230701_models.UpdatePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ehpc_instant_20230701_models.UpdatePoolResponse:
        """
        @summary Update the resource pool configuration.
        
        @param tmp_req: UpdatePoolRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePoolResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ehpc_instant_20230701_models.UpdatePoolShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_limits):
            request.resource_limits_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_limits, 'ResourceLimits', 'json')
        query = {}
        if not UtilClient.is_unset(request.pool_name):
            query['PoolName'] = request.pool_name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.resource_limits_shrink):
            query['ResourceLimits'] = request.resource_limits_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePool',
            version='2023-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ehpc_instant_20230701_models.UpdatePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pool(
        self,
        request: ehpc_instant_20230701_models.UpdatePoolRequest,
    ) -> ehpc_instant_20230701_models.UpdatePoolResponse:
        """
        @summary Update the resource pool configuration.
        
        @param request: UpdatePoolRequest
        @return: UpdatePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_pool_with_options(request, runtime)

    async def update_pool_async(
        self,
        request: ehpc_instant_20230701_models.UpdatePoolRequest,
    ) -> ehpc_instant_20230701_models.UpdatePoolResponse:
        """
        @summary Update the resource pool configuration.
        
        @param request: UpdatePoolRequest
        @return: UpdatePoolResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_pool_with_options_async(request, runtime)
