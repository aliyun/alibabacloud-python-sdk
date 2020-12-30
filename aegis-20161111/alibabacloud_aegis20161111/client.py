# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aegis20161111 import models as aegis_20161111_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aegis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_instance_with_options(
        self,
        request: aegis_20161111_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: aegis_20161111_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.CreateInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: aegis_20161111_models.CreateInstanceRequest,
    ) -> aegis_20161111_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: aegis_20161111_models.CreateInstanceRequest,
    ) -> aegis_20161111_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: aegis_20161111_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DeleteRuleResponse().from_map(
            self.do_rpcrequest('DeleteRule', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: aegis_20161111_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DeleteRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteRule', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rule(
        self,
        request: aegis_20161111_models.DeleteRuleRequest,
    ) -> aegis_20161111_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: aegis_20161111_models.DeleteRuleRequest,
    ) -> aegis_20161111_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def describe_auto_del_config_with_options(
        self,
        request: aegis_20161111_models.DescribeAutoDelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeAutoDelConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeAutoDelConfigResponse().from_map(
            self.do_rpcrequest('DescribeAutoDelConfig', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_del_config_with_options_async(
        self,
        request: aegis_20161111_models.DescribeAutoDelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeAutoDelConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeAutoDelConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoDelConfig', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_del_config(
        self,
        request: aegis_20161111_models.DescribeAutoDelConfigRequest,
    ) -> aegis_20161111_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_del_config_with_options(request, runtime)

    async def describe_auto_del_config_async(
        self,
        request: aegis_20161111_models.DescribeAutoDelConfigRequest,
    ) -> aegis_20161111_models.DescribeAutoDelConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_del_config_with_options_async(request, runtime)

    def describe_check_warning_detail_with_options(
        self,
        request: aegis_20161111_models.DescribeCheckWarningDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeCheckWarningDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeCheckWarningDetailResponse().from_map(
            self.do_rpcrequest('DescribeCheckWarningDetail', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_warning_detail_with_options_async(
        self,
        request: aegis_20161111_models.DescribeCheckWarningDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeCheckWarningDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeCheckWarningDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeCheckWarningDetail', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_warning_detail(
        self,
        request: aegis_20161111_models.DescribeCheckWarningDetailRequest,
    ) -> aegis_20161111_models.DescribeCheckWarningDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_warning_detail_with_options(request, runtime)

    async def describe_check_warning_detail_async(
        self,
        request: aegis_20161111_models.DescribeCheckWarningDetailRequest,
    ) -> aegis_20161111_models.DescribeCheckWarningDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_warning_detail_with_options_async(request, runtime)

    def describe_concern_necessity_with_options(
        self,
        request: aegis_20161111_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeConcernNecessityResponse().from_map(
            self.do_rpcrequest('DescribeConcernNecessity', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_concern_necessity_with_options_async(
        self,
        request: aegis_20161111_models.DescribeConcernNecessityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeConcernNecessityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeConcernNecessityResponse().from_map(
            await self.do_rpcrequest_async('DescribeConcernNecessity', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_concern_necessity(
        self,
        request: aegis_20161111_models.DescribeConcernNecessityRequest,
    ) -> aegis_20161111_models.DescribeConcernNecessityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_concern_necessity_with_options(request, runtime)

    async def describe_concern_necessity_async(
        self,
        request: aegis_20161111_models.DescribeConcernNecessityRequest,
    ) -> aegis_20161111_models.DescribeConcernNecessityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_concern_necessity_with_options_async(request, runtime)

    def describe_instance_statistics_with_options(
        self,
        request: aegis_20161111_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeInstanceStatisticsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatistics', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_statistics_with_options_async(
        self,
        request: aegis_20161111_models.DescribeInstanceStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeInstanceStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeInstanceStatisticsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatistics', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_statistics(
        self,
        request: aegis_20161111_models.DescribeInstanceStatisticsRequest,
    ) -> aegis_20161111_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_statistics_with_options(request, runtime)

    async def describe_instance_statistics_async(
        self,
        request: aegis_20161111_models.DescribeInstanceStatisticsRequest,
    ) -> aegis_20161111_models.DescribeInstanceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_statistics_with_options_async(request, runtime)

    def describe_strategy_exec_detail_with_options(
        self,
        request: aegis_20161111_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeStrategyExecDetailResponse().from_map(
            self.do_rpcrequest('DescribeStrategyExecDetail', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_strategy_exec_detail_with_options_async(
        self,
        request: aegis_20161111_models.DescribeStrategyExecDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeStrategyExecDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeStrategyExecDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeStrategyExecDetail', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_strategy_exec_detail(
        self,
        request: aegis_20161111_models.DescribeStrategyExecDetailRequest,
    ) -> aegis_20161111_models.DescribeStrategyExecDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_strategy_exec_detail_with_options(request, runtime)

    async def describe_strategy_exec_detail_async(
        self,
        request: aegis_20161111_models.DescribeStrategyExecDetailRequest,
    ) -> aegis_20161111_models.DescribeStrategyExecDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_strategy_exec_detail_with_options_async(request, runtime)

    def describe_stratety_with_options(
        self,
        request: aegis_20161111_models.DescribeStratetyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeStratetyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeStratetyResponse().from_map(
            self.do_rpcrequest('DescribeStratety', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_stratety_with_options_async(
        self,
        request: aegis_20161111_models.DescribeStratetyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeStratetyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeStratetyResponse().from_map(
            await self.do_rpcrequest_async('DescribeStratety', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stratety(
        self,
        request: aegis_20161111_models.DescribeStratetyRequest,
    ) -> aegis_20161111_models.DescribeStratetyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_stratety_with_options(request, runtime)

    async def describe_stratety_async(
        self,
        request: aegis_20161111_models.DescribeStratetyRequest,
    ) -> aegis_20161111_models.DescribeStratetyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_stratety_with_options_async(request, runtime)

    def describe_vul_whitelist_with_options(
        self,
        request: aegis_20161111_models.DescribeVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeVulWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeVulWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeVulWhitelist', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vul_whitelist_with_options_async(
        self,
        request: aegis_20161111_models.DescribeVulWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.DescribeVulWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.DescribeVulWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeVulWhitelist', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vul_whitelist(
        self,
        request: aegis_20161111_models.DescribeVulWhitelistRequest,
    ) -> aegis_20161111_models.DescribeVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vul_whitelist_with_options(request, runtime)

    async def describe_vul_whitelist_async(
        self,
        request: aegis_20161111_models.DescribeVulWhitelistRequest,
    ) -> aegis_20161111_models.DescribeVulWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vul_whitelist_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: aegis_20161111_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: aegis_20161111_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: aegis_20161111_models.RenewInstanceRequest,
    ) -> aegis_20161111_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: aegis_20161111_models.RenewInstanceRequest,
    ) -> aegis_20161111_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def upgrade_instance_with_options(
        self,
        request: aegis_20161111_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.UpgradeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.UpgradeInstanceResponse().from_map(
            self.do_rpcrequest('UpgradeInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_instance_with_options_async(
        self,
        request: aegis_20161111_models.UpgradeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aegis_20161111_models.UpgradeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return aegis_20161111_models.UpgradeInstanceResponse().from_map(
            await self.do_rpcrequest_async('UpgradeInstance', '2016-11-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance(
        self,
        request: aegis_20161111_models.UpgradeInstanceRequest,
    ) -> aegis_20161111_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_with_options(request, runtime)

    async def upgrade_instance_async(
        self,
        request: aegis_20161111_models.UpgradeInstanceRequest,
    ) -> aegis_20161111_models.UpgradeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_with_options_async(request, runtime)
