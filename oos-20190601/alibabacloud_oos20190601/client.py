# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_oos20190601 import models as oos_20190601_models
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
        self._endpoint = self.get_endpoint('oos', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_execution_with_options(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CancelExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CancelExecutionResponse().from_map(
            self.do_rpcrequest('CancelExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_execution_with_options_async(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CancelExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CancelExecutionResponse().from_map(
            await self.do_rpcrequest_async('CancelExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_execution(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
    ) -> oos_20190601_models.CancelExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_execution_with_options(request, runtime)

    async def cancel_execution_async(
        self,
        request: oos_20190601_models.CancelExecutionRequest,
    ) -> oos_20190601_models.CancelExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_execution_with_options_async(request, runtime)

    def create_parameter_with_options(
        self,
        request: oos_20190601_models.CreateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateParameterResponse().from_map(
            self.do_rpcrequest('CreateParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_parameter_with_options_async(
        self,
        request: oos_20190601_models.CreateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateParameterResponse().from_map(
            await self.do_rpcrequest_async('CreateParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_parameter(
        self,
        request: oos_20190601_models.CreateParameterRequest,
    ) -> oos_20190601_models.CreateParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_with_options(request, runtime)

    async def create_parameter_async(
        self,
        request: oos_20190601_models.CreateParameterRequest,
    ) -> oos_20190601_models.CreateParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_with_options_async(request, runtime)

    def create_secret_parameter_with_options(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateSecretParameterResponse().from_map(
            self.do_rpcrequest('CreateSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateSecretParameterResponse().from_map(
            await self.do_rpcrequest_async('CreateSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_secret_parameter(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_secret_parameter_with_options(request, runtime)

    async def create_secret_parameter_async(
        self,
        request: oos_20190601_models.CreateSecretParameterRequest,
    ) -> oos_20190601_models.CreateSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_secret_parameter_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        tmp_req: oos_20190601_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateTemplateResponse().from_map(
            self.do_rpcrequest('CreateTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tmp_req: oos_20190601_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.CreateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.CreateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.CreateTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(
        self,
        request: oos_20190601_models.CreateTemplateRequest,
    ) -> oos_20190601_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: oos_20190601_models.CreateTemplateRequest,
    ) -> oos_20190601_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_executions_with_options(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteExecutionsResponse().from_map(
            self.do_rpcrequest('DeleteExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_executions_with_options_async(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteExecutionsResponse().from_map(
            await self.do_rpcrequest_async('DeleteExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_executions(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_executions_with_options(request, runtime)

    async def delete_executions_async(
        self,
        request: oos_20190601_models.DeleteExecutionsRequest,
    ) -> oos_20190601_models.DeleteExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_executions_with_options_async(request, runtime)

    def delete_parameter_with_options(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteParameterResponse().from_map(
            self.do_rpcrequest('DeleteParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_parameter_with_options_async(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteParameterResponse().from_map(
            await self.do_rpcrequest_async('DeleteParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_parameter(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
    ) -> oos_20190601_models.DeleteParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_with_options(request, runtime)

    async def delete_parameter_async(
        self,
        request: oos_20190601_models.DeleteParameterRequest,
    ) -> oos_20190601_models.DeleteParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_with_options_async(request, runtime)

    def delete_secret_parameter_with_options(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteSecretParameterResponse().from_map(
            self.do_rpcrequest('DeleteSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteSecretParameterResponse().from_map(
            await self.do_rpcrequest_async('DeleteSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_secret_parameter(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_secret_parameter_with_options(request, runtime)

    async def delete_secret_parameter_async(
        self,
        request: oos_20190601_models.DeleteSecretParameterRequest,
    ) -> oos_20190601_models.DeleteSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_secret_parameter_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteTemplateResponse().from_map(
            self.do_rpcrequest('DeleteTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: oos_20190601_models.DeleteTemplateRequest,
    ) -> oos_20190601_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_templates_with_options(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteTemplatesResponse().from_map(
            self.do_rpcrequest('DeleteTemplates', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_templates_with_options_async(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DeleteTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DeleteTemplates', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_templates(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_templates_with_options(request, runtime)

    async def delete_templates_async(
        self,
        request: oos_20190601_models.DeleteTemplatesRequest,
    ) -> oos_20190601_models.DeleteTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_templates_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: oos_20190601_models.DescribeRegionsRequest,
    ) -> oos_20190601_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def generate_execution_policy_with_options(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GenerateExecutionPolicyResponse().from_map(
            self.do_rpcrequest('GenerateExecutionPolicy', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_execution_policy_with_options_async(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GenerateExecutionPolicyResponse().from_map(
            await self.do_rpcrequest_async('GenerateExecutionPolicy', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_execution_policy(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_execution_policy_with_options(request, runtime)

    async def generate_execution_policy_async(
        self,
        request: oos_20190601_models.GenerateExecutionPolicyRequest,
    ) -> oos_20190601_models.GenerateExecutionPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_execution_policy_with_options_async(request, runtime)

    def get_execution_template_with_options(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetExecutionTemplateResponse().from_map(
            self.do_rpcrequest('GetExecutionTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_execution_template_with_options_async(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetExecutionTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetExecutionTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_execution_template(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_execution_template_with_options(request, runtime)

    async def get_execution_template_async(
        self,
        request: oos_20190601_models.GetExecutionTemplateRequest,
    ) -> oos_20190601_models.GetExecutionTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_execution_template_with_options_async(request, runtime)

    def get_inventory_schema_with_options(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetInventorySchemaResponse().from_map(
            self.do_rpcrequest('GetInventorySchema', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_inventory_schema_with_options_async(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetInventorySchemaResponse().from_map(
            await self.do_rpcrequest_async('GetInventorySchema', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_inventory_schema(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_schema_with_options(request, runtime)

    async def get_inventory_schema_async(
        self,
        request: oos_20190601_models.GetInventorySchemaRequest,
    ) -> oos_20190601_models.GetInventorySchemaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inventory_schema_with_options_async(request, runtime)

    def get_parameter_with_options(
        self,
        request: oos_20190601_models.GetParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParameterResponse().from_map(
            self.do_rpcrequest('GetParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_parameter_with_options_async(
        self,
        request: oos_20190601_models.GetParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParameterResponse().from_map(
            await self.do_rpcrequest_async('GetParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_parameter(
        self,
        request: oos_20190601_models.GetParameterRequest,
    ) -> oos_20190601_models.GetParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parameter_with_options(request, runtime)

    async def get_parameter_async(
        self,
        request: oos_20190601_models.GetParameterRequest,
    ) -> oos_20190601_models.GetParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parameter_with_options_async(request, runtime)

    def get_parameters_with_options(
        self,
        request: oos_20190601_models.GetParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParametersResponse().from_map(
            self.do_rpcrequest('GetParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_parameters_with_options_async(
        self,
        request: oos_20190601_models.GetParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParametersResponse().from_map(
            await self.do_rpcrequest_async('GetParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_parameters(
        self,
        request: oos_20190601_models.GetParametersRequest,
    ) -> oos_20190601_models.GetParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_with_options(request, runtime)

    async def get_parameters_async(
        self,
        request: oos_20190601_models.GetParametersRequest,
    ) -> oos_20190601_models.GetParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_with_options_async(request, runtime)

    def get_parameters_by_path_with_options(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParametersByPathResponse().from_map(
            self.do_rpcrequest('GetParametersByPath', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_parameters_by_path_with_options_async(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetParametersByPathResponse().from_map(
            await self.do_rpcrequest_async('GetParametersByPath', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_parameters_by_path(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_parameters_by_path_with_options(request, runtime)

    async def get_parameters_by_path_async(
        self,
        request: oos_20190601_models.GetParametersByPathRequest,
    ) -> oos_20190601_models.GetParametersByPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_parameters_by_path_with_options_async(request, runtime)

    def get_secret_parameter_with_options(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParameterResponse().from_map(
            self.do_rpcrequest('GetSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParameterResponse().from_map(
            await self.do_rpcrequest_async('GetSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_secret_parameter(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameter_with_options(request, runtime)

    async def get_secret_parameter_async(
        self,
        request: oos_20190601_models.GetSecretParameterRequest,
    ) -> oos_20190601_models.GetSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameter_with_options_async(request, runtime)

    def get_secret_parameters_with_options(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParametersResponse().from_map(
            self.do_rpcrequest('GetSecretParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_secret_parameters_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParametersResponse().from_map(
            await self.do_rpcrequest_async('GetSecretParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_secret_parameters(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameters_with_options(request, runtime)

    async def get_secret_parameters_async(
        self,
        request: oos_20190601_models.GetSecretParametersRequest,
    ) -> oos_20190601_models.GetSecretParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameters_with_options_async(request, runtime)

    def get_secret_parameters_by_path_with_options(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParametersByPathResponse().from_map(
            self.do_rpcrequest('GetSecretParametersByPath', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_secret_parameters_by_path_with_options_async(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetSecretParametersByPathResponse().from_map(
            await self.do_rpcrequest_async('GetSecretParametersByPath', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_secret_parameters_by_path(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_secret_parameters_by_path_with_options(request, runtime)

    async def get_secret_parameters_by_path_async(
        self,
        request: oos_20190601_models.GetSecretParametersByPathRequest,
    ) -> oos_20190601_models.GetSecretParametersByPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_secret_parameters_by_path_with_options_async(request, runtime)

    def get_service_settings_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        req = open_api_models.OpenApiRequest()
        return oos_20190601_models.GetServiceSettingsResponse().from_map(
            self.do_rpcrequest('GetServiceSettings', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_settings_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetServiceSettingsResponse:
        req = open_api_models.OpenApiRequest()
        return oos_20190601_models.GetServiceSettingsResponse().from_map(
            await self.do_rpcrequest_async('GetServiceSettings', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_settings(self) -> oos_20190601_models.GetServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_settings_with_options(runtime)

    async def get_service_settings_async(self) -> oos_20190601_models.GetServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_settings_with_options_async(runtime)

    def get_template_with_options(
        self,
        request: oos_20190601_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetTemplateResponse().from_map(
            self.do_rpcrequest('GetTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: oos_20190601_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.GetTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: oos_20190601_models.GetTemplateRequest,
    ) -> oos_20190601_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: oos_20190601_models.GetTemplateRequest,
    ) -> oos_20190601_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def list_actions_with_options(
        self,
        request: oos_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListActionsResponse().from_map(
            self.do_rpcrequest('ListActions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_actions_with_options_async(
        self,
        request: oos_20190601_models.ListActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListActionsResponse().from_map(
            await self.do_rpcrequest_async('ListActions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_actions(
        self,
        request: oos_20190601_models.ListActionsRequest,
    ) -> oos_20190601_models.ListActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_actions_with_options(request, runtime)

    async def list_actions_async(
        self,
        request: oos_20190601_models.ListActionsRequest,
    ) -> oos_20190601_models.ListActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_actions_with_options_async(request, runtime)

    def list_execution_logs_with_options(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionLogsResponse().from_map(
            self.do_rpcrequest('ListExecutionLogs', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_execution_logs_with_options_async(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionLogsResponse().from_map(
            await self.do_rpcrequest_async('ListExecutionLogs', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_execution_logs(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_execution_logs_with_options(request, runtime)

    async def list_execution_logs_async(
        self,
        request: oos_20190601_models.ListExecutionLogsRequest,
    ) -> oos_20190601_models.ListExecutionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_logs_with_options_async(request, runtime)

    def list_execution_risky_tasks_with_options(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionRiskyTasksResponse().from_map(
            self.do_rpcrequest('ListExecutionRiskyTasks', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_execution_risky_tasks_with_options_async(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionRiskyTasksResponse().from_map(
            await self.do_rpcrequest_async('ListExecutionRiskyTasks', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_execution_risky_tasks(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_execution_risky_tasks_with_options(request, runtime)

    async def list_execution_risky_tasks_async(
        self,
        request: oos_20190601_models.ListExecutionRiskyTasksRequest,
    ) -> oos_20190601_models.ListExecutionRiskyTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_risky_tasks_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        tmp_req: oos_20190601_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionsResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionsResponse().from_map(
            self.do_rpcrequest('ListExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListExecutionsResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListExecutionsResponse().from_map(
            await self.do_rpcrequest_async('ListExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_executions(
        self,
        request: oos_20190601_models.ListExecutionsRequest,
    ) -> oos_20190601_models.ListExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: oos_20190601_models.ListExecutionsRequest,
    ) -> oos_20190601_models.ListExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_inventory_entries_with_options(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListInventoryEntriesResponse().from_map(
            self.do_rpcrequest('ListInventoryEntries', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_inventory_entries_with_options_async(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListInventoryEntriesResponse().from_map(
            await self.do_rpcrequest_async('ListInventoryEntries', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_inventory_entries(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_inventory_entries_with_options(request, runtime)

    async def list_inventory_entries_async(
        self,
        request: oos_20190601_models.ListInventoryEntriesRequest,
    ) -> oos_20190601_models.ListInventoryEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_inventory_entries_with_options_async(request, runtime)

    def list_parameters_with_options(
        self,
        request: oos_20190601_models.ListParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListParametersResponse().from_map(
            self.do_rpcrequest('ListParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_parameters_with_options_async(
        self,
        request: oos_20190601_models.ListParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListParametersResponse().from_map(
            await self.do_rpcrequest_async('ListParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_parameters(
        self,
        request: oos_20190601_models.ListParametersRequest,
    ) -> oos_20190601_models.ListParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parameters_with_options(request, runtime)

    async def list_parameters_async(
        self,
        request: oos_20190601_models.ListParametersRequest,
    ) -> oos_20190601_models.ListParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parameters_with_options_async(request, runtime)

    def list_parameter_versions_with_options(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListParameterVersionsResponse().from_map(
            self.do_rpcrequest('ListParameterVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_parameter_versions_with_options_async(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListParameterVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListParameterVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_parameter_versions(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parameter_versions_with_options(request, runtime)

    async def list_parameter_versions_async(
        self,
        request: oos_20190601_models.ListParameterVersionsRequest,
    ) -> oos_20190601_models.ListParameterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parameter_versions_with_options_async(request, runtime)

    def list_resource_execution_status_with_options(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListResourceExecutionStatusResponse().from_map(
            self.do_rpcrequest('ListResourceExecutionStatus', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_execution_status_with_options_async(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListResourceExecutionStatusResponse().from_map(
            await self.do_rpcrequest_async('ListResourceExecutionStatus', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_execution_status(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_execution_status_with_options(request, runtime)

    async def list_resource_execution_status_async(
        self,
        request: oos_20190601_models.ListResourceExecutionStatusRequest,
    ) -> oos_20190601_models.ListResourceExecutionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_execution_status_with_options_async(request, runtime)

    def list_secret_parameters_with_options(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListSecretParametersResponse().from_map(
            self.do_rpcrequest('ListSecretParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_secret_parameters_with_options_async(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListSecretParametersResponse().from_map(
            await self.do_rpcrequest_async('ListSecretParameters', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_secret_parameters(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_secret_parameters_with_options(request, runtime)

    async def list_secret_parameters_async(
        self,
        request: oos_20190601_models.ListSecretParametersRequest,
    ) -> oos_20190601_models.ListSecretParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_parameters_with_options_async(request, runtime)

    def list_secret_parameter_versions_with_options(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListSecretParameterVersionsResponse().from_map(
            self.do_rpcrequest('ListSecretParameterVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_secret_parameter_versions_with_options_async(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListSecretParameterVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListSecretParameterVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_secret_parameter_versions(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_secret_parameter_versions_with_options(request, runtime)

    async def list_secret_parameter_versions_async(
        self,
        request: oos_20190601_models.ListSecretParameterVersionsRequest,
    ) -> oos_20190601_models.ListSecretParameterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_secret_parameter_versions_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
    ) -> oos_20190601_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: oos_20190601_models.ListTagKeysRequest,
    ) -> oos_20190601_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: oos_20190601_models.ListTagResourcesRequest,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: oos_20190601_models.ListTagResourcesRequest,
    ) -> oos_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagValuesResponse().from_map(
            self.do_rpcrequest('ListTagValues', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTagValuesResponse().from_map(
            await self.do_rpcrequest_async('ListTagValues', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
    ) -> oos_20190601_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: oos_20190601_models.ListTagValuesRequest,
    ) -> oos_20190601_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_task_executions_with_options(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTaskExecutionsResponse().from_map(
            self.do_rpcrequest('ListTaskExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_executions_with_options_async(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTaskExecutionsResponse().from_map(
            await self.do_rpcrequest_async('ListTaskExecutions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_task_executions(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_task_executions_with_options(request, runtime)

    async def list_task_executions_async(
        self,
        request: oos_20190601_models.ListTaskExecutionsRequest,
    ) -> oos_20190601_models.ListTaskExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_executions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        tmp_req: oos_20190601_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTemplatesResponse().from_map(
            self.do_rpcrequest('ListTemplates', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        tmp_req: oos_20190601_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplatesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.ListTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTemplatesResponse().from_map(
            await self.do_rpcrequest_async('ListTemplates', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: oos_20190601_models.ListTemplatesRequest,
    ) -> oos_20190601_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: oos_20190601_models.ListTemplatesRequest,
    ) -> oos_20190601_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTemplateVersionsResponse().from_map(
            self.do_rpcrequest('ListTemplateVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ListTemplateVersionsResponse().from_map(
            await self.do_rpcrequest_async('ListTemplateVersions', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_template_versions(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: oos_20190601_models.ListTemplateVersionsRequest,
    ) -> oos_20190601_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def notify_execution_with_options(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.NotifyExecutionResponse().from_map(
            self.do_rpcrequest('NotifyExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def notify_execution_with_options_async(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.NotifyExecutionResponse().from_map(
            await self.do_rpcrequest_async('NotifyExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def notify_execution(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_execution_with_options(request, runtime)

    async def notify_execution_async(
        self,
        request: oos_20190601_models.NotifyExecutionRequest,
    ) -> oos_20190601_models.NotifyExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_execution_with_options_async(request, runtime)

    def search_inventory_with_options(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SearchInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.SearchInventoryResponse().from_map(
            self.do_rpcrequest('SearchInventory', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_inventory_with_options_async(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SearchInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.SearchInventoryResponse().from_map(
            await self.do_rpcrequest_async('SearchInventory', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_inventory(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
    ) -> oos_20190601_models.SearchInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_inventory_with_options(request, runtime)

    async def search_inventory_async(
        self,
        request: oos_20190601_models.SearchInventoryRequest,
    ) -> oos_20190601_models.SearchInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_inventory_with_options_async(request, runtime)

    def set_service_settings_with_options(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.SetServiceSettingsResponse().from_map(
            self.do_rpcrequest('SetServiceSettings', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_service_settings_with_options_async(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.SetServiceSettingsResponse().from_map(
            await self.do_rpcrequest_async('SetServiceSettings', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_service_settings(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_service_settings_with_options(request, runtime)

    async def set_service_settings_async(
        self,
        request: oos_20190601_models.SetServiceSettingsRequest,
    ) -> oos_20190601_models.SetServiceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_service_settings_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        tmp_req: oos_20190601_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.StartExecutionResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.StartExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.StartExecutionResponse().from_map(
            self.do_rpcrequest('StartExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        tmp_req: oos_20190601_models.StartExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.StartExecutionResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.StartExecutionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.StartExecutionResponse().from_map(
            await self.do_rpcrequest_async('StartExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_execution(
        self,
        request: oos_20190601_models.StartExecutionRequest,
    ) -> oos_20190601_models.StartExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: oos_20190601_models.StartExecutionRequest,
    ) -> oos_20190601_models.StartExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.TagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: oos_20190601_models.TagResourcesRequest,
    ) -> oos_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: oos_20190601_models.TagResourcesRequest,
    ) -> oos_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def trigger_execution_with_options(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.TriggerExecutionResponse().from_map(
            self.do_rpcrequest('TriggerExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def trigger_execution_with_options_async(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.TriggerExecutionResponse().from_map(
            await self.do_rpcrequest_async('TriggerExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def trigger_execution(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.trigger_execution_with_options(request, runtime)

    async def trigger_execution_async(
        self,
        request: oos_20190601_models.TriggerExecutionRequest,
    ) -> oos_20190601_models.TriggerExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.trigger_execution_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: oos_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: oos_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: oos_20190601_models.UntagResourcesRequest,
    ) -> oos_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: oos_20190601_models.UntagResourcesRequest,
    ) -> oos_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_execution_with_options(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateExecutionResponse().from_map(
            self.do_rpcrequest('UpdateExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_execution_with_options_async(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateExecutionResponse().from_map(
            await self.do_rpcrequest_async('UpdateExecution', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_execution(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_execution_with_options(request, runtime)

    async def update_execution_async(
        self,
        request: oos_20190601_models.UpdateExecutionRequest,
    ) -> oos_20190601_models.UpdateExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_execution_with_options_async(request, runtime)

    def update_instance_information_with_options(
        self,
        request: oos_20190601_models.UpdateInstanceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateInstanceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateInstanceInformationResponse().from_map(
            self.do_rpcrequest('UpdateInstanceInformation', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_information_with_options_async(
        self,
        request: oos_20190601_models.UpdateInstanceInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateInstanceInformationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateInstanceInformationResponse().from_map(
            await self.do_rpcrequest_async('UpdateInstanceInformation', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_information(
        self,
        request: oos_20190601_models.UpdateInstanceInformationRequest,
    ) -> oos_20190601_models.UpdateInstanceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_information_with_options(request, runtime)

    async def update_instance_information_async(
        self,
        request: oos_20190601_models.UpdateInstanceInformationRequest,
    ) -> oos_20190601_models.UpdateInstanceInformationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_information_with_options_async(request, runtime)

    def update_parameter_with_options(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateParameterResponse().from_map(
            self.do_rpcrequest('UpdateParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_parameter_with_options_async(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateParameterResponse().from_map(
            await self.do_rpcrequest_async('UpdateParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_parameter(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
    ) -> oos_20190601_models.UpdateParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_parameter_with_options(request, runtime)

    async def update_parameter_async(
        self,
        request: oos_20190601_models.UpdateParameterRequest,
    ) -> oos_20190601_models.UpdateParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_parameter_with_options_async(request, runtime)

    def update_secret_parameter_with_options(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateSecretParameterResponse().from_map(
            self.do_rpcrequest('UpdateSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_secret_parameter_with_options_async(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateSecretParameterResponse().from_map(
            await self.do_rpcrequest_async('UpdateSecretParameter', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_secret_parameter(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_secret_parameter_with_options(request, runtime)

    async def update_secret_parameter_async(
        self,
        request: oos_20190601_models.UpdateSecretParameterRequest,
    ) -> oos_20190601_models.UpdateSecretParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_secret_parameter_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        tmp_req: oos_20190601_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateTemplateResponse().from_map(
            self.do_rpcrequest('UpdateTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tmp_req: oos_20190601_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = oos_20190601_models.UpdateTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.UpdateTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateTemplate', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: oos_20190601_models.UpdateTemplateRequest,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: oos_20190601_models.UpdateTemplateRequest,
    ) -> oos_20190601_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def validate_template_content_with_options(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ValidateTemplateContentResponse().from_map(
            self.do_rpcrequest('ValidateTemplateContent', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_template_content_with_options_async(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return oos_20190601_models.ValidateTemplateContentResponse().from_map(
            await self.do_rpcrequest_async('ValidateTemplateContent', '2019-06-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_template_content(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_template_content_with_options(request, runtime)

    async def validate_template_content_async(
        self,
        request: oos_20190601_models.ValidateTemplateContentRequest,
    ) -> oos_20190601_models.ValidateTemplateContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_template_content_with_options_async(request, runtime)
