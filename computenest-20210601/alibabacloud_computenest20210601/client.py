# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenest20210601 import models as compute_nest_20210601_models
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
        self._endpoint = self.get_endpoint('computenest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeleteServiceInstancesResponse(),
            self.do_rpcrequest('DeleteServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeleteServiceInstancesResponse(),
            await self.do_rpcrequest_async('DeleteServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_instances(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    async def delete_service_instances_async(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceResponse(),
            self.do_rpcrequest('GetServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceResponse(),
            await self.do_rpcrequest_async('GetServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_instance(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def list_service_instance_logs_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceLogsResponse(),
            self.do_rpcrequest('ListServiceInstanceLogs', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_instance_logs_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceLogsResponse(),
            await self.do_rpcrequest_async('ListServiceInstanceLogs', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_instance_logs(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_logs_with_options(request, runtime)

    async def list_service_instance_logs_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_logs_with_options_async(request, runtime)

    def create_service_instance_with_options(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceInstanceResponse(),
            self.do_rpcrequest('CreateServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_instance_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceInstanceResponse(),
            await self.do_rpcrequest_async('CreateServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_instance(
        self,
        request: compute_nest_20210601_models.CreateServiceInstanceRequest,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    async def create_service_instance_async(
        self,
        request: compute_nest_20210601_models.CreateServiceInstanceRequest,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def continue_deploy_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ContinueDeployServiceInstanceResponse(),
            self.do_rpcrequest('ContinueDeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def continue_deploy_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ContinueDeployServiceInstanceResponse(),
            await self.do_rpcrequest_async('ContinueDeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continue_deploy_service_instance(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    async def continue_deploy_service_instance_async(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continue_deploy_service_instance_with_options_async(request, runtime)

    def disable_operation_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.DisableOperationServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DisableOperationServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DisableOperationServiceInstanceResponse(),
            self.do_rpcrequest('DisableOperationServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_operation_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.DisableOperationServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DisableOperationServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DisableOperationServiceInstanceResponse(),
            await self.do_rpcrequest_async('DisableOperationServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_operation_service_instance(
        self,
        request: compute_nest_20210601_models.DisableOperationServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DisableOperationServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_operation_service_instance_with_options(request, runtime)

    async def disable_operation_service_instance_async(
        self,
        request: compute_nest_20210601_models.DisableOperationServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DisableOperationServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_operation_service_instance_with_options_async(request, runtime)

    def deploy_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeployServiceInstanceResponse(),
            self.do_rpcrequest('DeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeployServiceInstanceResponse(),
            await self.do_rpcrequest_async('DeployServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_service_instance(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_service_instance_with_options(request, runtime)

    async def deploy_service_instance_async(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_service_instance_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstancesResponse(),
            self.do_rpcrequest('ListServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstancesResponse(),
            await self.do_rpcrequest_async('ListServiceInstances', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_service_instances(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListPoliciesResponse(),
            self.do_rpcrequest('ListPolicies', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListPoliciesResponse(),
            await self.do_rpcrequest_async('ListPolicies', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_policies(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_inuse_services_with_options(
        self,
        request: compute_nest_20210601_models.ListInuseServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListInuseServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListInuseServicesResponse(),
            self.do_rpcrequest('ListInuseServices', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_inuse_services_with_options_async(
        self,
        request: compute_nest_20210601_models.ListInuseServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListInuseServicesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListInuseServicesResponse(),
            await self.do_rpcrequest_async('ListInuseServices', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_inuse_services(
        self,
        request: compute_nest_20210601_models.ListInuseServicesRequest,
    ) -> compute_nest_20210601_models.ListInuseServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inuse_services_with_options(request, runtime)

    async def list_inuse_services_async(
        self,
        request: compute_nest_20210601_models.ListInuseServicesRequest,
    ) -> compute_nest_20210601_models.ListInuseServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inuse_services_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def enable_operation_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.EnableOperationServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.EnableOperationServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.EnableOperationServiceInstanceResponse(),
            self.do_rpcrequest('EnableOperationServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_operation_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.EnableOperationServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.EnableOperationServiceInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.EnableOperationServiceInstanceResponse(),
            await self.do_rpcrequest_async('EnableOperationServiceInstance', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_operation_service_instance(
        self,
        request: compute_nest_20210601_models.EnableOperationServiceInstanceRequest,
    ) -> compute_nest_20210601_models.EnableOperationServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_operation_service_instance_with_options(request, runtime)

    async def enable_operation_service_instance_async(
        self,
        request: compute_nest_20210601_models.EnableOperationServiceInstanceRequest,
    ) -> compute_nest_20210601_models.EnableOperationServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_operation_service_instance_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceResponse(),
            self.do_rpcrequest('GetService', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceResponse(),
            await self.do_rpcrequest_async('GetService', '2021-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)
