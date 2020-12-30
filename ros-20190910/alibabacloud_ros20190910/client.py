# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ros20190910 import models as ros20190910_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ros', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_update_stack_with_options(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CancelUpdateStackResponse().from_map(
            self.do_rpcrequest('CancelUpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_update_stack_with_options_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CancelUpdateStackResponse().from_map(
            await self.do_rpcrequest_async('CancelUpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_update_stack(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    async def cancel_update_stack_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_update_stack_with_options_async(request, runtime)

    def continue_create_stack_with_options(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ContinueCreateStackResponse().from_map(
            self.do_rpcrequest('ContinueCreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def continue_create_stack_with_options_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ContinueCreateStackResponse().from_map(
            await self.do_rpcrequest_async('ContinueCreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continue_create_stack(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    async def continue_create_stack_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continue_create_stack_with_options_async(request, runtime)

    def create_change_set_with_options(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateChangeSetResponse().from_map(
            self.do_rpcrequest('CreateChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_change_set_with_options_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateChangeSetResponse().from_map(
            await self.do_rpcrequest_async('CreateChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_change_set(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    async def create_change_set_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_change_set_with_options_async(request, runtime)

    def create_stack_with_options(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackResponse().from_map(
            self.do_rpcrequest('CreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_stack_with_options_async(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackResponse().from_map(
            await self.do_rpcrequest_async('CreateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stack(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    async def create_stack_async(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_with_options_async(request, runtime)

    def create_stack_group_with_options(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackGroupResponse().from_map(
            self.do_rpcrequest('CreateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_stack_group_with_options_async(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stack_group(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    async def create_stack_group_async(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_group_with_options_async(request, runtime)

    def create_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackInstancesResponse().from_map(
            self.do_rpcrequest('CreateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateStackInstancesResponse().from_map(
            await self.do_rpcrequest_async('CreateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stack_instances(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    async def create_stack_instances_async(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_instances_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateTemplateResponse().from_map(
            self.do_rpcrequest('CreateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.CreateTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_change_set_with_options(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteChangeSetResponse().from_map(
            self.do_rpcrequest('DeleteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_change_set_with_options_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteChangeSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_change_set(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    async def delete_change_set_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_change_set_with_options_async(request, runtime)

    def delete_stack_with_options(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackResponse().from_map(
            self.do_rpcrequest('DeleteStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stack_with_options_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackResponse().from_map(
            await self.do_rpcrequest_async('DeleteStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stack(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    async def delete_stack_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_with_options_async(request, runtime)

    def delete_stack_group_with_options(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackGroupResponse().from_map(
            self.do_rpcrequest('DeleteStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stack_group_with_options_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stack_group(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    async def delete_stack_group_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_group_with_options_async(request, runtime)

    def delete_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackInstancesResponse().from_map(
            self.do_rpcrequest('DeleteStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteStackInstancesResponse().from_map(
            await self.do_rpcrequest_async('DeleteStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_stack_instances(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    async def delete_stack_instances_async(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_instances_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteTemplateResponse().from_map(
            self.do_rpcrequest('DeleteTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DeleteTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detect_stack_drift_with_options(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackDriftResponse().from_map(
            self.do_rpcrequest('DetectStackDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_stack_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackDriftResponse().from_map(
            await self.do_rpcrequest_async('DetectStackDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_stack_drift(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    async def detect_stack_drift_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_drift_with_options_async(request, runtime)

    def detect_stack_group_drift_with_options(
        self,
        tmp_req: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackGroupDriftResponse().from_map(
            self.do_rpcrequest('DetectStackGroupDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_stack_group_drift_with_options_async(
        self,
        tmp_req: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackGroupDriftResponse().from_map(
            await self.do_rpcrequest_async('DetectStackGroupDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_stack_group_drift(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    async def detect_stack_group_drift_async(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_group_drift_with_options_async(request, runtime)

    def detect_stack_resource_drift_with_options(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackResourceDriftResponse().from_map(
            self.do_rpcrequest('DetectStackResourceDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_stack_resource_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.DetectStackResourceDriftResponse().from_map(
            await self.do_rpcrequest_async('DetectStackResourceDrift', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_stack_resource_drift(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    async def detect_stack_resource_drift_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_resource_drift_with_options_async(request, runtime)

    def execute_change_set_with_options(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ExecuteChangeSetResponse().from_map(
            self.do_rpcrequest('ExecuteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_change_set_with_options_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ExecuteChangeSetResponse().from_map(
            await self.do_rpcrequest_async('ExecuteChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_change_set(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    async def execute_change_set_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_change_set_with_options_async(request, runtime)

    def generate_template_policy_with_options(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GenerateTemplatePolicyResponse().from_map(
            self.do_rpcrequest('GenerateTemplatePolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_template_policy_with_options_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GenerateTemplatePolicyResponse().from_map(
            await self.do_rpcrequest_async('GenerateTemplatePolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_template_policy(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    async def generate_template_policy_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_template_policy_with_options_async(request, runtime)

    def get_change_set_with_options(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetChangeSetResponse().from_map(
            self.do_rpcrequest('GetChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_change_set_with_options_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetChangeSetResponse().from_map(
            await self.do_rpcrequest_async('GetChangeSet', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_change_set(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    async def get_change_set_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_change_set_with_options_async(request, runtime)

    def get_resource_type_with_options(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetResourceTypeResponse().from_map(
            self.do_rpcrequest('GetResourceType', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetResourceTypeResponse().from_map(
            await self.do_rpcrequest_async('GetResourceType', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_type(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    async def get_resource_type_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_with_options_async(request, runtime)

    def get_resource_type_template_with_options(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetResourceTypeTemplateResponse().from_map(
            self.do_rpcrequest('GetResourceTypeTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_type_template_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetResourceTypeTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetResourceTypeTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_type_template(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    async def get_resource_type_template_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_template_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackResponse().from_map(
            self.do_rpcrequest('GetStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackResponse().from_map(
            await self.do_rpcrequest_async('GetStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_stack_drift_detection_status_with_options(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackDriftDetectionStatusResponse().from_map(
            self.do_rpcrequest('GetStackDriftDetectionStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_drift_detection_status_with_options_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackDriftDetectionStatusResponse().from_map(
            await self.do_rpcrequest_async('GetStackDriftDetectionStatus', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_drift_detection_status(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    async def get_stack_drift_detection_status_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_drift_detection_status_with_options_async(request, runtime)

    def get_stack_group_with_options(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackGroupResponse().from_map(
            self.do_rpcrequest('GetStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_group_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackGroupResponse().from_map(
            await self.do_rpcrequest_async('GetStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_group(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    async def get_stack_group_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_with_options_async(request, runtime)

    def get_stack_group_operation_with_options(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackGroupOperationResponse().from_map(
            self.do_rpcrequest('GetStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackGroupOperationResponse().from_map(
            await self.do_rpcrequest_async('GetStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_group_operation(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    async def get_stack_group_operation_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_operation_with_options_async(request, runtime)

    def get_stack_instance_with_options(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackInstanceResponse().from_map(
            self.do_rpcrequest('GetStackInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_instance_with_options_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackInstanceResponse().from_map(
            await self.do_rpcrequest_async('GetStackInstance', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_instance(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    async def get_stack_instance_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_instance_with_options_async(request, runtime)

    def get_stack_policy_with_options(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackPolicyResponse().from_map(
            self.do_rpcrequest('GetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_policy_with_options_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackPolicyResponse().from_map(
            await self.do_rpcrequest_async('GetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_policy(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    async def get_stack_policy_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_policy_with_options_async(request, runtime)

    def get_stack_resource_with_options(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackResourceResponse().from_map(
            self.do_rpcrequest('GetStackResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_resource_with_options_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetStackResourceResponse().from_map(
            await self.do_rpcrequest_async('GetStackResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack_resource(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    async def get_stack_resource_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_resource_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateResponse().from_map(
            self.do_rpcrequest('GetTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_estimate_cost_with_options(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateEstimateCostResponse().from_map(
            self.do_rpcrequest('GetTemplateEstimateCost', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_estimate_cost_with_options_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateEstimateCostResponse().from_map(
            await self.do_rpcrequest_async('GetTemplateEstimateCost', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template_estimate_cost(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    async def get_template_estimate_cost_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_estimate_cost_with_options_async(request, runtime)

    def get_template_summary_with_options(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateSummaryResponse().from_map(
            self.do_rpcrequest('GetTemplateSummary', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_summary_with_options_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.GetTemplateSummaryResponse().from_map(
            await self.do_rpcrequest_async('GetTemplateSummary', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template_summary(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    async def get_template_summary_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_summary_with_options_async(request, runtime)

    def list_change_sets_with_options(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListChangeSetsResponse().from_map(
            self.do_rpcrequest('ListChangeSets', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_change_sets_with_options_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListChangeSetsResponse().from_map(
            await self.do_rpcrequest_async('ListChangeSets', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_change_sets(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    async def list_change_sets_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_change_sets_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        return ros20190910_models.ListResourceTypesResponse().from_map(
            self.do_rpcrequest('ListResourceTypes', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        return ros20190910_models.ListResourceTypesResponse().from_map(
            await self.do_rpcrequest_async('ListResourceTypes', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_types(self) -> ros20190910_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(runtime)

    async def list_resource_types_async(self) -> ros20190910_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(runtime)

    def list_stack_events_with_options(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackEventsResponse().from_map(
            self.do_rpcrequest('ListStackEvents', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_events_with_options_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackEventsResponse().from_map(
            await self.do_rpcrequest_async('ListStackEvents', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_events(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    async def list_stack_events_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_events_with_options_async(request, runtime)

    def list_stack_group_operation_results_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupOperationResultsResponse().from_map(
            self.do_rpcrequest('ListStackGroupOperationResults', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_group_operation_results_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupOperationResultsResponse().from_map(
            await self.do_rpcrequest_async('ListStackGroupOperationResults', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_group_operation_results(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    async def list_stack_group_operation_results_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operation_results_with_options_async(request, runtime)

    def list_stack_group_operations_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupOperationsResponse().from_map(
            self.do_rpcrequest('ListStackGroupOperations', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_group_operations_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupOperationsResponse().from_map(
            await self.do_rpcrequest_async('ListStackGroupOperations', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_group_operations(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    async def list_stack_group_operations_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operations_with_options_async(request, runtime)

    def list_stack_groups_with_options(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupsResponse().from_map(
            self.do_rpcrequest('ListStackGroups', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_groups_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListStackGroups', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_groups(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    async def list_stack_groups_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_groups_with_options_async(request, runtime)

    def list_stack_instances_with_options(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackInstancesResponse().from_map(
            self.do_rpcrequest('ListStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_instances_with_options_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_instances(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    async def list_stack_instances_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_instances_with_options_async(request, runtime)

    def list_stack_operation_risks_with_options(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackOperationRisksResponse().from_map(
            self.do_rpcrequest('ListStackOperationRisks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_operation_risks_with_options_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackOperationRisksResponse().from_map(
            await self.do_rpcrequest_async('ListStackOperationRisks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_operation_risks(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    async def list_stack_operation_risks_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_operation_risks_with_options_async(request, runtime)

    def list_stack_resource_drifts_with_options(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackResourceDriftsResponse().from_map(
            self.do_rpcrequest('ListStackResourceDrifts', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_resource_drifts_with_options_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackResourceDriftsResponse().from_map(
            await self.do_rpcrequest_async('ListStackResourceDrifts', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_resource_drifts(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    async def list_stack_resource_drifts_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resource_drifts_with_options_async(request, runtime)

    def list_stack_resources_with_options(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackResourcesResponse().from_map(
            self.do_rpcrequest('ListStackResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_resources_with_options_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStackResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListStackResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack_resources(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    async def list_stack_resources_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resources_with_options_async(request, runtime)

    def list_stacks_with_options(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStacksResponse().from_map(
            self.do_rpcrequest('ListStacks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stacks_with_options_async(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListStacksResponse().from_map(
            await self.do_rpcrequest_async('ListStacks', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stacks(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    async def list_stacks_async(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stacks_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagValuesResponse().from_map(
            self.do_rpcrequest('ListTagValues', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTagValuesResponse().from_map(
            await self.do_rpcrequest_async('ListTagValues', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTemplatesResponse().from_map(
            self.do_rpcrequest('ListTemplates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTemplatesResponse().from_map(
            await self.do_rpcrequest_async('ListTemplates', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTemplateVersionsResponse().from_map(
            self.do_rpcrequest('ListTemplateVersions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ListTemplateVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListTemplateVersions', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_template_versions(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def preview_stack_with_options(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.PreviewStackResponse().from_map(
            self.do_rpcrequest('PreviewStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preview_stack_with_options_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.PreviewStackResponse().from_map(
            await self.do_rpcrequest_async('PreviewStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preview_stack(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    async def preview_stack_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preview_stack_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetDeletionProtectionResponse().from_map(
            self.do_rpcrequest('SetDeletionProtection', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetDeletionProtectionResponse().from_map(
            await self.do_rpcrequest_async('SetDeletionProtection', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_deletion_protection(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def set_stack_policy_with_options(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetStackPolicyResponse().from_map(
            self.do_rpcrequest('SetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_stack_policy_with_options_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetStackPolicyResponse().from_map(
            await self.do_rpcrequest_async('SetStackPolicy', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_stack_policy(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    async def set_stack_policy_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_stack_policy_with_options_async(request, runtime)

    def set_template_permission_with_options(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetTemplatePermissionResponse().from_map(
            self.do_rpcrequest('SetTemplatePermission', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_template_permission_with_options_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SetTemplatePermissionResponse().from_map(
            await self.do_rpcrequest_async('SetTemplatePermission', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_template_permission(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    async def set_template_permission_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_template_permission_with_options_async(request, runtime)

    def signal_resource_with_options(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SignalResourceResponse().from_map(
            self.do_rpcrequest('SignalResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def signal_resource_with_options_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.SignalResourceResponse().from_map(
            await self.do_rpcrequest_async('SignalResource', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def signal_resource(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    async def signal_resource_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.signal_resource_with_options_async(request, runtime)

    def stop_stack_group_operation_with_options(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.StopStackGroupOperationResponse().from_map(
            self.do_rpcrequest('StopStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.StopStackGroupOperationResponse().from_map(
            await self.do_rpcrequest_async('StopStackGroupOperation', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_stack_group_operation(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    async def stop_stack_group_operation_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_stack_group_operation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_stack_with_options(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackResponse().from_map(
            self.do_rpcrequest('UpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_stack_with_options_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackResponse().from_map(
            await self.do_rpcrequest_async('UpdateStack', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    async def update_stack_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_with_options_async(request, runtime)

    def update_stack_group_with_options(
        self,
        tmp_req: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackGroupResponse().from_map(
            self.do_rpcrequest('UpdateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_stack_group_with_options_async(
        self,
        tmp_req: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateStackGroup', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack_group(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    async def update_stack_group_async(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_group_with_options_async(request, runtime)

    def update_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackInstancesResponse().from_map(
            self.do_rpcrequest('UpdateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackInstancesResponse().from_map(
            await self.do_rpcrequest_async('UpdateStackInstances', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack_instances(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    async def update_stack_instances_async(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_instances_with_options_async(request, runtime)

    def update_stack_template_by_resources_with_options(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackTemplateByResourcesResponse().from_map(
            self.do_rpcrequest('UpdateStackTemplateByResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_stack_template_by_resources_with_options_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateStackTemplateByResourcesResponse().from_map(
            await self.do_rpcrequest_async('UpdateStackTemplateByResources', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_stack_template_by_resources(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    async def update_stack_template_by_resources_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_template_by_resources_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateTemplateResponse().from_map(
            self.do_rpcrequest('UpdateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.UpdateTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def validate_template_with_options(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ValidateTemplateResponse().from_map(
            self.do_rpcrequest('ValidateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_template_with_options_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ros20190910_models.ValidateTemplateResponse().from_map(
            await self.do_rpcrequest_async('ValidateTemplate', '2019-09-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_template(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)

    async def validate_template_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_template_with_options_async(request, runtime)
