# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_sddp20190103 import models as sddp_20190103_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint_map = {
            'cn-hongkong': 'sddp-api.cn-hongkong.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sddp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_config_with_options(
        self,
        request: sddp_20190103_models.CreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateConfigResponse(),
            self.do_rpcrequest('CreateConfig', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_config_with_options_async(
        self,
        request: sddp_20190103_models.CreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateConfigResponse(),
            await self.do_rpcrequest_async('CreateConfig', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_config(
        self,
        request: sddp_20190103_models.CreateConfigRequest,
    ) -> sddp_20190103_models.CreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_config_with_options(request, runtime)

    async def create_config_async(
        self,
        request: sddp_20190103_models.CreateConfigRequest,
    ) -> sddp_20190103_models.CreateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_config_with_options_async(request, runtime)

    def create_data_limit_with_options(
        self,
        request: sddp_20190103_models.CreateDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateDataLimitResponse(),
            self.do_rpcrequest('CreateDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.CreateDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateDataLimitResponse(),
            await self.do_rpcrequest_async('CreateDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_limit(
        self,
        request: sddp_20190103_models.CreateDataLimitRequest,
    ) -> sddp_20190103_models.CreateDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_limit_with_options(request, runtime)

    async def create_data_limit_async(
        self,
        request: sddp_20190103_models.CreateDataLimitRequest,
    ) -> sddp_20190103_models.CreateDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_limit_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: sddp_20190103_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateRuleResponse(),
            self.do_rpcrequest('CreateRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: sddp_20190103_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateRuleResponse(),
            await self.do_rpcrequest_async('CreateRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(
        self,
        request: sddp_20190103_models.CreateRuleRequest,
    ) -> sddp_20190103_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: sddp_20190103_models.CreateRuleRequest,
    ) -> sddp_20190103_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_scan_task_with_options(
        self,
        request: sddp_20190103_models.CreateScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateScanTaskResponse(),
            self.do_rpcrequest('CreateScanTask', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scan_task_with_options_async(
        self,
        request: sddp_20190103_models.CreateScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateScanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateScanTaskResponse(),
            await self.do_rpcrequest_async('CreateScanTask', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scan_task(
        self,
        request: sddp_20190103_models.CreateScanTaskRequest,
    ) -> sddp_20190103_models.CreateScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scan_task_with_options(request, runtime)

    async def create_scan_task_async(
        self,
        request: sddp_20190103_models.CreateScanTaskRequest,
    ) -> sddp_20190103_models.CreateScanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scan_task_with_options_async(request, runtime)

    def delete_data_limit_with_options(
        self,
        request: sddp_20190103_models.DeleteDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteDataLimitResponse(),
            self.do_rpcrequest('DeleteDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.DeleteDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteDataLimitResponse(),
            await self.do_rpcrequest_async('DeleteDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_limit(
        self,
        request: sddp_20190103_models.DeleteDataLimitRequest,
    ) -> sddp_20190103_models.DeleteDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_limit_with_options(request, runtime)

    async def delete_data_limit_async(
        self,
        request: sddp_20190103_models.DeleteDataLimitRequest,
    ) -> sddp_20190103_models.DeleteDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_limit_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: sddp_20190103_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteRuleResponse(),
            self.do_rpcrequest('DeleteRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: sddp_20190103_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteRuleResponse(),
            await self.do_rpcrequest_async('DeleteRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(
        self,
        request: sddp_20190103_models.DeleteRuleRequest,
    ) -> sddp_20190103_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: sddp_20190103_models.DeleteRuleRequest,
    ) -> sddp_20190103_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: sddp_20190103_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsResponse(),
            self.do_rpcrequest('DescribeColumns', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: sddp_20190103_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsResponse(),
            await self.do_rpcrequest_async('DescribeColumns', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_columns(
        self,
        request: sddp_20190103_models.DescribeColumnsRequest,
    ) -> sddp_20190103_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: sddp_20190103_models.DescribeColumnsRequest,
    ) -> sddp_20190103_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_configs_with_options(
        self,
        request: sddp_20190103_models.DescribeConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeConfigsResponse(),
            self.do_rpcrequest('DescribeConfigs', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_configs_with_options_async(
        self,
        request: sddp_20190103_models.DescribeConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeConfigsResponse(),
            await self.do_rpcrequest_async('DescribeConfigs', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_configs(
        self,
        request: sddp_20190103_models.DescribeConfigsRequest,
    ) -> sddp_20190103_models.DescribeConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_configs_with_options(request, runtime)

    async def describe_configs_async(
        self,
        request: sddp_20190103_models.DescribeConfigsRequest,
    ) -> sddp_20190103_models.DescribeConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_configs_with_options_async(request, runtime)

    def describe_data_assets_with_options(
        self,
        request: sddp_20190103_models.DescribeDataAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataAssetsResponse(),
            self.do_rpcrequest('DescribeDataAssets', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_assets_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataAssetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataAssetsResponse(),
            await self.do_rpcrequest_async('DescribeDataAssets', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_assets(
        self,
        request: sddp_20190103_models.DescribeDataAssetsRequest,
    ) -> sddp_20190103_models.DescribeDataAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_assets_with_options(request, runtime)

    async def describe_data_assets_async(
        self,
        request: sddp_20190103_models.DescribeDataAssetsRequest,
    ) -> sddp_20190103_models.DescribeDataAssetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_assets_with_options_async(request, runtime)

    def describe_data_limit_detail_with_options(
        self,
        request: sddp_20190103_models.DescribeDataLimitDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitDetailResponse(),
            self.do_rpcrequest('DescribeDataLimitDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_limit_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitDetailResponse(),
            await self.do_rpcrequest_async('DescribeDataLimitDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_limit_detail(
        self,
        request: sddp_20190103_models.DescribeDataLimitDetailRequest,
    ) -> sddp_20190103_models.DescribeDataLimitDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limit_detail_with_options(request, runtime)

    async def describe_data_limit_detail_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitDetailRequest,
    ) -> sddp_20190103_models.DescribeDataLimitDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_limit_detail_with_options_async(request, runtime)

    def describe_data_limits_with_options(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitsResponse(),
            self.do_rpcrequest('DescribeDataLimits', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_limits_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitsResponse(),
            await self.do_rpcrequest_async('DescribeDataLimits', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_limits(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limits_with_options(request, runtime)

    async def describe_data_limits_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_limits_with_options_async(request, runtime)

    def describe_data_limit_set_with_options(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitSetResponse(),
            self.do_rpcrequest('DescribeDataLimitSet', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_limit_set_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitSetResponse(),
            await self.do_rpcrequest_async('DescribeDataLimitSet', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_limit_set(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_limit_set_with_options(request, runtime)

    async def describe_data_limit_set_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_limit_set_with_options_async(request, runtime)

    def describe_data_masking_run_history_with_options(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingRunHistoryResponse(),
            self.do_rpcrequest('DescribeDataMaskingRunHistory', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_masking_run_history_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingRunHistoryResponse(),
            await self.do_rpcrequest_async('DescribeDataMaskingRunHistory', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_masking_run_history(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_masking_run_history_with_options(request, runtime)

    async def describe_data_masking_run_history_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_masking_run_history_with_options_async(request, runtime)

    def describe_data_masking_tasks_with_options(
        self,
        request: sddp_20190103_models.DescribeDataMaskingTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingTasksResponse(),
            self.do_rpcrequest('DescribeDataMaskingTasks', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_masking_tasks_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingTasksResponse(),
            await self.do_rpcrequest_async('DescribeDataMaskingTasks', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_masking_tasks(
        self,
        request: sddp_20190103_models.DescribeDataMaskingTasksRequest,
    ) -> sddp_20190103_models.DescribeDataMaskingTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_masking_tasks_with_options(request, runtime)

    async def describe_data_masking_tasks_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingTasksRequest,
    ) -> sddp_20190103_models.DescribeDataMaskingTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_masking_tasks_with_options_async(request, runtime)

    def describe_event_detail_with_options(
        self,
        request: sddp_20190103_models.DescribeEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventDetailResponse(),
            self.do_rpcrequest('DescribeEventDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_event_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventDetailResponse(),
            await self.do_rpcrequest_async('DescribeEventDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_event_detail(
        self,
        request: sddp_20190103_models.DescribeEventDetailRequest,
    ) -> sddp_20190103_models.DescribeEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_detail_with_options(request, runtime)

    async def describe_event_detail_async(
        self,
        request: sddp_20190103_models.DescribeEventDetailRequest,
    ) -> sddp_20190103_models.DescribeEventDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_detail_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventsResponse(),
            self.do_rpcrequest('DescribeEvents', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventsResponse(),
            await self.do_rpcrequest_async('DescribeEvents', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_events(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_event_types_with_options(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventTypesResponse(),
            self.do_rpcrequest('DescribeEventTypes', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_event_types_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventTypesResponse(),
            await self.do_rpcrequest_async('DescribeEventTypes', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_event_types(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_types_with_options(request, runtime)

    async def describe_event_types_async(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_types_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstancesResponse(),
            self.do_rpcrequest('DescribeInstances', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstancesResponse(),
            await self.do_rpcrequest_async('DescribeInstances', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instance_sources_with_options(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstanceSourcesResponse(),
            self.do_rpcrequest('DescribeInstanceSources', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_sources_with_options_async(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstanceSourcesResponse(),
            await self.do_rpcrequest_async('DescribeInstanceSources', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_sources(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sources_with_options(request, runtime)

    async def describe_instance_sources_async(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sources_with_options_async(request, runtime)

    def describe_oss_object_detail_with_options(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailResponse(),
            self.do_rpcrequest('DescribeOssObjectDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_object_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailResponse(),
            await self.do_rpcrequest_async('DescribeOssObjectDetail', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_object_detail(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_object_detail_with_options(request, runtime)

    async def describe_oss_object_detail_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_object_detail_with_options_async(request, runtime)

    def describe_oss_objects_with_options(
        self,
        request: sddp_20190103_models.DescribeOssObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectsResponse(),
            self.do_rpcrequest('DescribeOssObjects', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_objects_with_options_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectsResponse(),
            await self.do_rpcrequest_async('DescribeOssObjects', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_objects(
        self,
        request: sddp_20190103_models.DescribeOssObjectsRequest,
    ) -> sddp_20190103_models.DescribeOssObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_objects_with_options(request, runtime)

    async def describe_oss_objects_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectsRequest,
    ) -> sddp_20190103_models.DescribeOssObjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_objects_with_options_async(request, runtime)

    def describe_packages_with_options(
        self,
        request: sddp_20190103_models.DescribePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribePackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribePackagesResponse(),
            self.do_rpcrequest('DescribePackages', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_packages_with_options_async(
        self,
        request: sddp_20190103_models.DescribePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribePackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribePackagesResponse(),
            await self.do_rpcrequest_async('DescribePackages', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_packages(
        self,
        request: sddp_20190103_models.DescribePackagesRequest,
    ) -> sddp_20190103_models.DescribePackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_packages_with_options(request, runtime)

    async def describe_packages_async(
        self,
        request: sddp_20190103_models.DescribePackagesRequest,
    ) -> sddp_20190103_models.DescribePackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_packages_with_options_async(request, runtime)

    def describe_risk_levels_with_options(
        self,
        request: sddp_20190103_models.DescribeRiskLevelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRiskLevelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRiskLevelsResponse(),
            self.do_rpcrequest('DescribeRiskLevels', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_risk_levels_with_options_async(
        self,
        request: sddp_20190103_models.DescribeRiskLevelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRiskLevelsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRiskLevelsResponse(),
            await self.do_rpcrequest_async('DescribeRiskLevels', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_risk_levels(
        self,
        request: sddp_20190103_models.DescribeRiskLevelsRequest,
    ) -> sddp_20190103_models.DescribeRiskLevelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_risk_levels_with_options(request, runtime)

    async def describe_risk_levels_async(
        self,
        request: sddp_20190103_models.DescribeRiskLevelsRequest,
    ) -> sddp_20190103_models.DescribeRiskLevelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_risk_levels_with_options_async(request, runtime)

    def describe_rules_with_options(
        self,
        request: sddp_20190103_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRulesResponse(),
            self.do_rpcrequest('DescribeRules', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: sddp_20190103_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRulesResponse(),
            await self.do_rpcrequest_async('DescribeRules', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rules(
        self,
        request: sddp_20190103_models.DescribeRulesRequest,
    ) -> sddp_20190103_models.DescribeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    async def describe_rules_async(
        self,
        request: sddp_20190103_models.DescribeRulesRequest,
    ) -> sddp_20190103_models.DescribeRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rules_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: sddp_20190103_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: sddp_20190103_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTablesResponse(),
            await self.do_rpcrequest_async('DescribeTables', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(
        self,
        request: sddp_20190103_models.DescribeTablesRequest,
    ) -> sddp_20190103_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: sddp_20190103_models.DescribeTablesRequest,
    ) -> sddp_20190103_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_user_status_with_options(
        self,
        request: sddp_20190103_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeUserStatusResponse(),
            self.do_rpcrequest('DescribeUserStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: sddp_20190103_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeUserStatusResponse(),
            await self.do_rpcrequest_async('DescribeUserStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_status(
        self,
        request: sddp_20190103_models.DescribeUserStatusRequest,
    ) -> sddp_20190103_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    async def describe_user_status_async(
        self,
        request: sddp_20190103_models.DescribeUserStatusRequest,
    ) -> sddp_20190103_models.DescribeUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_status_with_options_async(request, runtime)

    def disable_user_config_with_options(
        self,
        request: sddp_20190103_models.DisableUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DisableUserConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DisableUserConfigResponse(),
            self.do_rpcrequest('DisableUserConfig', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_user_config_with_options_async(
        self,
        request: sddp_20190103_models.DisableUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DisableUserConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.DisableUserConfigResponse(),
            await self.do_rpcrequest_async('DisableUserConfig', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_user_config(
        self,
        request: sddp_20190103_models.DisableUserConfigRequest,
    ) -> sddp_20190103_models.DisableUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_user_config_with_options(request, runtime)

    async def disable_user_config_async(
        self,
        request: sddp_20190103_models.DisableUserConfigRequest,
    ) -> sddp_20190103_models.DisableUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_user_config_with_options_async(request, runtime)

    def exec_datamask_with_options(
        self,
        request: sddp_20190103_models.ExecDatamaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ExecDatamaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ExecDatamaskResponse(),
            self.do_rpcrequest('ExecDatamask', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def exec_datamask_with_options_async(
        self,
        request: sddp_20190103_models.ExecDatamaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ExecDatamaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ExecDatamaskResponse(),
            await self.do_rpcrequest_async('ExecDatamask', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def exec_datamask(
        self,
        request: sddp_20190103_models.ExecDatamaskRequest,
    ) -> sddp_20190103_models.ExecDatamaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.exec_datamask_with_options(request, runtime)

    async def exec_datamask_async(
        self,
        request: sddp_20190103_models.ExecDatamaskRequest,
    ) -> sddp_20190103_models.ExecDatamaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.exec_datamask_with_options_async(request, runtime)

    def manual_trigger_masking_process_with_options(
        self,
        request: sddp_20190103_models.ManualTriggerMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ManualTriggerMaskingProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ManualTriggerMaskingProcessResponse(),
            self.do_rpcrequest('ManualTriggerMaskingProcess', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def manual_trigger_masking_process_with_options_async(
        self,
        request: sddp_20190103_models.ManualTriggerMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ManualTriggerMaskingProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ManualTriggerMaskingProcessResponse(),
            await self.do_rpcrequest_async('ManualTriggerMaskingProcess', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def manual_trigger_masking_process(
        self,
        request: sddp_20190103_models.ManualTriggerMaskingProcessRequest,
    ) -> sddp_20190103_models.ManualTriggerMaskingProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.manual_trigger_masking_process_with_options(request, runtime)

    async def manual_trigger_masking_process_async(
        self,
        request: sddp_20190103_models.ManualTriggerMaskingProcessRequest,
    ) -> sddp_20190103_models.ManualTriggerMaskingProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.manual_trigger_masking_process_with_options_async(request, runtime)

    def modify_data_limit_with_options(
        self,
        request: sddp_20190103_models.ModifyDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDataLimitResponse(),
            self.do_rpcrequest('ModifyDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.ModifyDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDataLimitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDataLimitResponse(),
            await self.do_rpcrequest_async('ModifyDataLimit', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_data_limit(
        self,
        request: sddp_20190103_models.ModifyDataLimitRequest,
    ) -> sddp_20190103_models.ModifyDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_data_limit_with_options(request, runtime)

    async def modify_data_limit_async(
        self,
        request: sddp_20190103_models.ModifyDataLimitRequest,
    ) -> sddp_20190103_models.ModifyDataLimitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_limit_with_options_async(request, runtime)

    def modify_default_level_with_options(
        self,
        request: sddp_20190103_models.ModifyDefaultLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDefaultLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDefaultLevelResponse(),
            self.do_rpcrequest('ModifyDefaultLevel', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_default_level_with_options_async(
        self,
        request: sddp_20190103_models.ModifyDefaultLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDefaultLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDefaultLevelResponse(),
            await self.do_rpcrequest_async('ModifyDefaultLevel', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_default_level(
        self,
        request: sddp_20190103_models.ModifyDefaultLevelRequest,
    ) -> sddp_20190103_models.ModifyDefaultLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_default_level_with_options(request, runtime)

    async def modify_default_level_async(
        self,
        request: sddp_20190103_models.ModifyDefaultLevelRequest,
    ) -> sddp_20190103_models.ModifyDefaultLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_default_level_with_options_async(request, runtime)

    def modify_event_status_with_options(
        self,
        request: sddp_20190103_models.ModifyEventStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventStatusResponse(),
            self.do_rpcrequest('ModifyEventStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_event_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyEventStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventStatusResponse(),
            await self.do_rpcrequest_async('ModifyEventStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_event_status(
        self,
        request: sddp_20190103_models.ModifyEventStatusRequest,
    ) -> sddp_20190103_models.ModifyEventStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_event_status_with_options(request, runtime)

    async def modify_event_status_async(
        self,
        request: sddp_20190103_models.ModifyEventStatusRequest,
    ) -> sddp_20190103_models.ModifyEventStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_event_status_with_options_async(request, runtime)

    def modify_event_type_status_with_options(
        self,
        request: sddp_20190103_models.ModifyEventTypeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventTypeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventTypeStatusResponse(),
            self.do_rpcrequest('ModifyEventTypeStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_event_type_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyEventTypeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventTypeStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventTypeStatusResponse(),
            await self.do_rpcrequest_async('ModifyEventTypeStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_event_type_status(
        self,
        request: sddp_20190103_models.ModifyEventTypeStatusRequest,
    ) -> sddp_20190103_models.ModifyEventTypeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_event_type_status_with_options(request, runtime)

    async def modify_event_type_status_async(
        self,
        request: sddp_20190103_models.ModifyEventTypeStatusRequest,
    ) -> sddp_20190103_models.ModifyEventTypeStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_event_type_status_with_options_async(request, runtime)

    def modify_rule_with_options(
        self,
        request: sddp_20190103_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleResponse(),
            self.do_rpcrequest('ModifyRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        request: sddp_20190103_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleResponse(),
            await self.do_rpcrequest_async('ModifyRule', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rule(
        self,
        request: sddp_20190103_models.ModifyRuleRequest,
    ) -> sddp_20190103_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    async def modify_rule_async(
        self,
        request: sddp_20190103_models.ModifyRuleRequest,
    ) -> sddp_20190103_models.ModifyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rule_with_options_async(request, runtime)

    def modify_rule_status_with_options(
        self,
        request: sddp_20190103_models.ModifyRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleStatusResponse(),
            self.do_rpcrequest('ModifyRuleStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_rule_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleStatusResponse(),
            await self.do_rpcrequest_async('ModifyRuleStatus', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rule_status(
        self,
        request: sddp_20190103_models.ModifyRuleStatusRequest,
    ) -> sddp_20190103_models.ModifyRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rule_status_with_options(request, runtime)

    async def modify_rule_status_async(
        self,
        request: sddp_20190103_models.ModifyRuleStatusRequest,
    ) -> sddp_20190103_models.ModifyRuleStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rule_status_with_options_async(request, runtime)

    def stop_masking_process_with_options(
        self,
        request: sddp_20190103_models.StopMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.StopMaskingProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.StopMaskingProcessResponse(),
            self.do_rpcrequest('StopMaskingProcess', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_masking_process_with_options_async(
        self,
        request: sddp_20190103_models.StopMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.StopMaskingProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            sddp_20190103_models.StopMaskingProcessResponse(),
            await self.do_rpcrequest_async('StopMaskingProcess', '2019-01-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_masking_process(
        self,
        request: sddp_20190103_models.StopMaskingProcessRequest,
    ) -> sddp_20190103_models.StopMaskingProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_masking_process_with_options(request, runtime)

    async def stop_masking_process_async(
        self,
        request: sddp_20190103_models.StopMaskingProcessRequest,
    ) -> sddp_20190103_models.StopMaskingProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_masking_process_with_options_async(request, runtime)
