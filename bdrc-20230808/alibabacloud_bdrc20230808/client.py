# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bdrc20230808 import models as bdrc20230808_models
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
        self._endpoint = self.get_endpoint('bdrc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_rules_with_options(
        self,
        request: bdrc20230808_models.CheckRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.CheckRulesResponse:
        """
        @param request: CheckRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckRules',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/rules/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.CheckRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_rules_with_options_async(
        self,
        request: bdrc20230808_models.CheckRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.CheckRulesResponse:
        """
        @param request: CheckRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckRulesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckRules',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/rules/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.CheckRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_rules(
        self,
        request: bdrc20230808_models.CheckRulesRequest,
    ) -> bdrc20230808_models.CheckRulesResponse:
        """
        @param request: CheckRulesRequest
        @return: CheckRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_rules_with_options(request, headers, runtime)

    async def check_rules_async(
        self,
        request: bdrc20230808_models.CheckRulesRequest,
    ) -> bdrc20230808_models.CheckRulesResponse:
        """
        @param request: CheckRulesRequest
        @return: CheckRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_rules_with_options_async(request, headers, runtime)

    def close_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.CloseBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CloseBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service/close',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.CloseBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.CloseBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CloseBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service/close',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.CloseBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_bdrc_service(self) -> bdrc20230808_models.CloseBdrcServiceResponse:
        """
        @return: CloseBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_bdrc_service_with_options(headers, runtime)

    async def close_bdrc_service_async(self) -> bdrc20230808_models.CloseBdrcServiceResponse:
        """
        @return: CloseBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_bdrc_service_with_options_async(headers, runtime)

    def describe_check_details_with_options(
        self,
        request: bdrc20230808_models.DescribeCheckDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeCheckDetailsResponse:
        """
        @param request: DescribeCheckDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCheckDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckDetails',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/check-details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeCheckDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_check_details_with_options_async(
        self,
        request: bdrc20230808_models.DescribeCheckDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeCheckDetailsResponse:
        """
        @param request: DescribeCheckDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCheckDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceArn'] = request.resource_arn
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCheckDetails',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/check-details',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeCheckDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_check_details(
        self,
        request: bdrc20230808_models.DescribeCheckDetailsRequest,
    ) -> bdrc20230808_models.DescribeCheckDetailsResponse:
        """
        @param request: DescribeCheckDetailsRequest
        @return: DescribeCheckDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_check_details_with_options(request, headers, runtime)

    async def describe_check_details_async(
        self,
        request: bdrc20230808_models.DescribeCheckDetailsRequest,
    ) -> bdrc20230808_models.DescribeCheckDetailsResponse:
        """
        @param request: DescribeCheckDetailsRequest
        @return: DescribeCheckDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_check_details_with_options_async(request, headers, runtime)

    def describe_products_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeProductsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeProducts',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeProductsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeProducts',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products(self) -> bdrc20230808_models.DescribeProductsResponse:
        """
        @return: DescribeProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_products_with_options(headers, runtime)

    async def describe_products_async(self) -> bdrc20230808_models.DescribeProductsResponse:
        """
        @return: DescribeProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_products_with_options_async(headers, runtime)

    def describe_resources_with_options(
        self,
        request: bdrc20230808_models.DescribeResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeResourcesResponse:
        """
        @param request: DescribeResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.failed_rule_template):
            query['FailedRuleTemplate'] = request.failed_rule_template
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resources_with_options_async(
        self,
        request: bdrc20230808_models.DescribeResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeResourcesResponse:
        """
        @param request: DescribeResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.failed_rule_template):
            query['FailedRuleTemplate'] = request.failed_rule_template
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resources(
        self,
        request: bdrc20230808_models.DescribeResourcesRequest,
    ) -> bdrc20230808_models.DescribeResourcesResponse:
        """
        @param request: DescribeResourcesRequest
        @return: DescribeResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_resources_with_options(request, headers, runtime)

    async def describe_resources_async(
        self,
        request: bdrc20230808_models.DescribeResourcesRequest,
    ) -> bdrc20230808_models.DescribeResourcesResponse:
        """
        @param request: DescribeResourcesRequest
        @return: DescribeResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_resources_with_options_async(request, headers, runtime)

    def describe_rules_with_options(
        self,
        request: bdrc20230808_models.DescribeRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: bdrc20230808_models.DescribeRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/rules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules(
        self,
        request: bdrc20230808_models.DescribeRulesRequest,
    ) -> bdrc20230808_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @return: DescribeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_rules_with_options(request, headers, runtime)

    async def describe_rules_async(
        self,
        request: bdrc20230808_models.DescribeRulesRequest,
    ) -> bdrc20230808_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @return: DescribeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_rules_with_options_async(request, headers, runtime)

    def describe_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTaskResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        task_id: str,
    ) -> bdrc20230808_models.DescribeTaskResponse:
        """
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_with_options(task_id, headers, runtime)

    async def describe_task_async(
        self,
        task_id: str,
    ) -> bdrc20230808_models.DescribeTaskResponse:
        """
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_with_options_async(task_id, headers, runtime)

    def describe_tasks_with_options(
        self,
        request: bdrc20230808_models.DescribeTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: bdrc20230808_models.DescribeTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTasks',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: bdrc20230808_models.DescribeTasksRequest,
    ) -> bdrc20230808_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_tasks_with_options(request, headers, runtime)

    async def describe_tasks_async(
        self,
        request: bdrc20230808_models.DescribeTasksRequest,
    ) -> bdrc20230808_models.DescribeTasksResponse:
        """
        @param request: DescribeTasksRequest
        @return: DescribeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_tasks_with_options_async(request, headers, runtime)

    def describe_top_risky_resources_with_options(
        self,
        request: bdrc20230808_models.DescribeTopRiskyResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTopRiskyResourcesResponse:
        """
        @param request: DescribeTopRiskyResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopRiskyResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopRiskyResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/top-risky',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTopRiskyResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_top_risky_resources_with_options_async(
        self,
        request: bdrc20230808_models.DescribeTopRiskyResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DescribeTopRiskyResourcesResponse:
        """
        @param request: DescribeTopRiskyResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTopRiskyResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTopRiskyResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/top-risky',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DescribeTopRiskyResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_top_risky_resources(
        self,
        request: bdrc20230808_models.DescribeTopRiskyResourcesRequest,
    ) -> bdrc20230808_models.DescribeTopRiskyResourcesResponse:
        """
        @param request: DescribeTopRiskyResourcesRequest
        @return: DescribeTopRiskyResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_top_risky_resources_with_options(request, headers, runtime)

    async def describe_top_risky_resources_async(
        self,
        request: bdrc20230808_models.DescribeTopRiskyResourcesRequest,
    ) -> bdrc20230808_models.DescribeTopRiskyResourcesResponse:
        """
        @param request: DescribeTopRiskyResourcesRequest
        @return: DescribeTopRiskyResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_top_risky_resources_with_options_async(request, headers, runtime)

    def disable_check_product_with_options(
        self,
        request: bdrc20230808_models.DisableCheckProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DisableCheckProductResponse:
        """
        @param request: DisableCheckProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCheckProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableCheckProduct',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products/disable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DisableCheckProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_check_product_with_options_async(
        self,
        request: bdrc20230808_models.DisableCheckProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DisableCheckProductResponse:
        """
        @param request: DisableCheckProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCheckProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableCheckProduct',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products/disable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DisableCheckProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_check_product(
        self,
        request: bdrc20230808_models.DisableCheckProductRequest,
    ) -> bdrc20230808_models.DisableCheckProductResponse:
        """
        @param request: DisableCheckProductRequest
        @return: DisableCheckProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_check_product_with_options(request, headers, runtime)

    async def disable_check_product_async(
        self,
        request: bdrc20230808_models.DisableCheckProductRequest,
    ) -> bdrc20230808_models.DisableCheckProductResponse:
        """
        @param request: DisableCheckProductRequest
        @return: DisableCheckProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_check_product_with_options_async(request, headers, runtime)

    def disable_check_resource_with_options(
        self,
        request: bdrc20230808_models.DisableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DisableCheckResourceResponse:
        """
        @param request: DisableCheckResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCheckResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableCheckResource',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/disable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DisableCheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_check_resource_with_options_async(
        self,
        request: bdrc20230808_models.DisableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.DisableCheckResourceResponse:
        """
        @param request: DisableCheckResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCheckResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableCheckResource',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/disable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.DisableCheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_check_resource(
        self,
        request: bdrc20230808_models.DisableCheckResourceRequest,
    ) -> bdrc20230808_models.DisableCheckResourceResponse:
        """
        @param request: DisableCheckResourceRequest
        @return: DisableCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_check_resource_with_options(request, headers, runtime)

    async def disable_check_resource_async(
        self,
        request: bdrc20230808_models.DisableCheckResourceRequest,
    ) -> bdrc20230808_models.DisableCheckResourceResponse:
        """
        @param request: DisableCheckResourceRequest
        @return: DisableCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_check_resource_with_options_async(request, headers, runtime)

    def enable_check_product_with_options(
        self,
        request: bdrc20230808_models.EnableCheckProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.EnableCheckProductResponse:
        """
        @param request: EnableCheckProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCheckProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableCheckProduct',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products/enable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.EnableCheckProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_check_product_with_options_async(
        self,
        request: bdrc20230808_models.EnableCheckProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.EnableCheckProductResponse:
        """
        @param request: EnableCheckProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCheckProductResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableCheckProduct',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/products/enable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.EnableCheckProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_check_product(
        self,
        request: bdrc20230808_models.EnableCheckProductRequest,
    ) -> bdrc20230808_models.EnableCheckProductResponse:
        """
        @param request: EnableCheckProductRequest
        @return: EnableCheckProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_check_product_with_options(request, headers, runtime)

    async def enable_check_product_async(
        self,
        request: bdrc20230808_models.EnableCheckProductRequest,
    ) -> bdrc20230808_models.EnableCheckProductResponse:
        """
        @param request: EnableCheckProductRequest
        @return: EnableCheckProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_check_product_with_options_async(request, headers, runtime)

    def enable_check_resource_with_options(
        self,
        request: bdrc20230808_models.EnableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.EnableCheckResourceResponse:
        """
        @param request: EnableCheckResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCheckResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableCheckResource',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/enable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.EnableCheckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_check_resource_with_options_async(
        self,
        request: bdrc20230808_models.EnableCheckResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.EnableCheckResourceResponse:
        """
        @param request: EnableCheckResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCheckResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_arn):
            body['ResourceArn'] = request.resource_arn
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableCheckResource',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/enable-check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.EnableCheckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_check_resource(
        self,
        request: bdrc20230808_models.EnableCheckResourceRequest,
    ) -> bdrc20230808_models.EnableCheckResourceResponse:
        """
        @param request: EnableCheckResourceRequest
        @return: EnableCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_check_resource_with_options(request, headers, runtime)

    async def enable_check_resource_async(
        self,
        request: bdrc20230808_models.EnableCheckResourceRequest,
    ) -> bdrc20230808_models.EnableCheckResourceResponse:
        """
        @param request: EnableCheckResourceRequest
        @return: EnableCheckResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_check_resource_with_options_async(request, headers, runtime)

    def get_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.GetBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.GetBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.GetBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.GetBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bdrc_service(self) -> bdrc20230808_models.GetBdrcServiceResponse:
        """
        @return: GetBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_bdrc_service_with_options(headers, runtime)

    async def get_bdrc_service_async(self) -> bdrc20230808_models.GetBdrcServiceResponse:
        """
        @return: GetBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_bdrc_service_with_options_async(headers, runtime)

    def open_bdrc_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.OpenBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.OpenBdrcServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_bdrc_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.OpenBdrcServiceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenBdrcServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='OpenBdrcService',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/service/open',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.OpenBdrcServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_bdrc_service(self) -> bdrc20230808_models.OpenBdrcServiceResponse:
        """
        @return: OpenBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_bdrc_service_with_options(headers, runtime)

    async def open_bdrc_service_async(self) -> bdrc20230808_models.OpenBdrcServiceResponse:
        """
        @return: OpenBdrcServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_bdrc_service_with_options_async(headers, runtime)

    def update_resources_with_options(
        self,
        request: bdrc20230808_models.UpdateResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.UpdateResourcesResponse:
        """
        @param request: UpdateResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.UpdateResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resources_with_options_async(
        self,
        request: bdrc20230808_models.UpdateResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> bdrc20230808_models.UpdateResourcesResponse:
        """
        @param request: UpdateResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResources',
            version='2023-08-08',
            protocol='HTTPS',
            pathname=f'/api/v1/resources/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bdrc20230808_models.UpdateResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resources(
        self,
        request: bdrc20230808_models.UpdateResourcesRequest,
    ) -> bdrc20230808_models.UpdateResourcesResponse:
        """
        @param request: UpdateResourcesRequest
        @return: UpdateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resources_with_options(request, headers, runtime)

    async def update_resources_async(
        self,
        request: bdrc20230808_models.UpdateResourcesRequest,
    ) -> bdrc20230808_models.UpdateResourcesResponse:
        """
        @param request: UpdateResourcesRequest
        @return: UpdateResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resources_with_options_async(request, headers, runtime)
