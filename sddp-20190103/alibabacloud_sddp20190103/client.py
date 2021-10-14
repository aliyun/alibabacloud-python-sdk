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
        query = {}
        query['Code'] = request.code
        query['Description'] = request.description
        query['Lang'] = request.lang
        query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_with_options_async(
        self,
        request: sddp_20190103_models.CreateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Code'] = request.code
        query['Description'] = request.description
        query['Lang'] = request.lang
        query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AuditStatus'] = request.audit_status
        query['AutoScan'] = request.auto_scan
        query['EngineType'] = request.engine_type
        query['EventStatus'] = request.event_status
        query['Lang'] = request.lang
        query['LogStoreDay'] = request.log_store_day
        query['OcrStatus'] = request.ocr_status
        query['ParentId'] = request.parent_id
        query['Password'] = request.password
        query['Port'] = request.port
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.CreateDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateDataLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['AutoScan'] = request.auto_scan
        query['EngineType'] = request.engine_type
        query['EventStatus'] = request.event_status
        query['Lang'] = request.lang
        query['LogStoreDay'] = request.log_store_day
        query['OcrStatus'] = request.ocr_status
        query['ParentId'] = request.parent_id
        query['Password'] = request.password
        query['Port'] = request.port
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Category'] = request.category
        query['Content'] = request.content
        query['ContentCategory'] = request.content_category
        query['Description'] = request.description
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['StatExpress'] = request.stat_express
        query['Status'] = request.status
        query['Target'] = request.target
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: sddp_20190103_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['Content'] = request.content
        query['ContentCategory'] = request.content_category
        query['Description'] = request.description
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['StatExpress'] = request.stat_express
        query['Status'] = request.status
        query['Target'] = request.target
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DataLimitId'] = request.data_limit_id
        query['IntervalDay'] = request.interval_day
        query['OssScanPath'] = request.oss_scan_path
        query['ResourceType'] = request.resource_type
        query['RunHour'] = request.run_hour
        query['RunMinute'] = request.run_minute
        query['ScanRange'] = request.scan_range
        query['ScanRangeContent'] = request.scan_range_content
        query['TaskName'] = request.task_name
        query['TaskUserName'] = request.task_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScanTask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scan_task_with_options_async(
        self,
        request: sddp_20190103_models.CreateScanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.CreateScanTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataLimitId'] = request.data_limit_id
        query['IntervalDay'] = request.interval_day
        query['OssScanPath'] = request.oss_scan_path
        query['ResourceType'] = request.resource_type
        query['RunHour'] = request.run_hour
        query['RunMinute'] = request.run_minute
        query['ScanRange'] = request.scan_range
        query['ScanRangeContent'] = request.scan_range_content
        query['TaskName'] = request.task_name
        query['TaskUserName'] = request.task_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScanTask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.CreateScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.DeleteDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteDataLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: sddp_20190103_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['RuleName'] = request.rule_name
        query['SensLevelName'] = request.sens_level_name
        query['TableId'] = request.table_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: sddp_20190103_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['InstanceName'] = request.instance_name
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['RuleName'] = request.rule_name
        query['SensLevelName'] = request.sens_level_name
        query['TableId'] = request.table_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeConfigs',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configs_with_options_async(
        self,
        request: sddp_20190103_models.DescribeConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeConfigs',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeConfigsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['RangeId'] = request.range_id
        query['RiskLevels'] = request.risk_levels
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataAssets',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_assets_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataAssetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataAssetsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['RangeId'] = request.range_id
        query['RiskLevels'] = request.risk_levels
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataAssets',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limit_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['NetworkType'] = request.network_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_data_limit_set_with_options(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ParentId'] = request.parent_id
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitSet',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limit_set_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitSetResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ParentId'] = request.parent_id
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimitSet',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitSetResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_data_limits_with_options(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['CheckStatus'] = request.check_status
        query['CurrentPage'] = request.current_page
        query['DatamaskStatus'] = request.datamask_status
        query['Enable'] = request.enable
        query['EndTime'] = request.end_time
        query['EngineType'] = request.engine_type
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ParentId'] = request.parent_id
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimits',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limits_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataLimitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataLimitsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['CheckStatus'] = request.check_status
        query['CurrentPage'] = request.current_page
        query['DatamaskStatus'] = request.datamask_status
        query['Enable'] = request.enable
        query['EndTime'] = request.end_time
        query['EngineType'] = request.engine_type
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ParentId'] = request.parent_id
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataLimits',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataLimitsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_data_masking_run_history_with_options(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DstType'] = request.dst_type
        query['EndTime'] = request.end_time
        query['Lang'] = request.lang
        query['MainProcessId'] = request.main_process_id
        query['PageSize'] = request.page_size
        query['SrcTableName'] = request.src_table_name
        query['SrcType'] = request.src_type
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingRunHistory',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingRunHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_masking_run_history_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingRunHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingRunHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DstType'] = request.dst_type
        query['EndTime'] = request.end_time
        query['Lang'] = request.lang
        query['MainProcessId'] = request.main_process_id
        query['PageSize'] = request.page_size
        query['SrcTableName'] = request.src_table_name
        query['SrcType'] = request.src_type
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingRunHistory',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingRunHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['DstType'] = request.dst_type
        query['EndTime'] = request.end_time
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['SearchKey'] = request.search_key
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingTasks',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_masking_tasks_with_options_async(
        self,
        request: sddp_20190103_models.DescribeDataMaskingTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeDataMaskingTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DstType'] = request.dst_type
        query['EndTime'] = request.end_time
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['SearchKey'] = request.search_key
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataMaskingTasks',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeDataMaskingTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_event_types_with_options(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ParentTypeId'] = request.parent_type_id
        query['ResourceId'] = request.resource_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventTypes',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_types_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['ParentTypeId'] = request.parent_type_id
        query['ResourceId'] = request.resource_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventTypes',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventTypesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_events_with_options(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DealUserId'] = request.deal_user_id
        query['EndTime'] = request.end_time
        query['Id'] = request.id
        query['InstanceName'] = request.instance_name
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['SubTypeCode'] = request.sub_type_code
        query['TargetProductCode'] = request.target_product_code
        query['TypeCode'] = request.type_code
        query['UserId'] = request.user_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: sddp_20190103_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['DealUserId'] = request.deal_user_id
        query['EndTime'] = request.end_time
        query['Id'] = request.id
        query['InstanceName'] = request.instance_name
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['SubTypeCode'] = request.sub_type_code
        query['TargetProductCode'] = request.target_product_code
        query['TypeCode'] = request.type_code
        query['UserId'] = request.user_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEvents',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_instance_sources_with_options(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['EngineType'] = request.engine_type
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ProductId'] = request.product_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSources',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstanceSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sources_with_options_async(
        self,
        request: sddp_20190103_models.DescribeInstanceSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstanceSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['EngineType'] = request.engine_type
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['PageSize'] = request.page_size
        query['ProductId'] = request.product_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSources',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstanceSourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_instances_with_options(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['FeatureType'] = request.feature_type
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: sddp_20190103_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['FeatureType'] = request.feature_type
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_oss_object_detail_with_options(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssObjectDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_object_detail_with_options_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssObjectDetail',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['LastScanTimeEnd'] = request.last_scan_time_end
        query['LastScanTimeStart'] = request.last_scan_time_start
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssObjects',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_objects_with_options_async(
        self,
        request: sddp_20190103_models.DescribeOssObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeOssObjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['LastScanTimeEnd'] = request.last_scan_time_end
        query['LastScanTimeStart'] = request.last_scan_time_start
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOssObjects',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeOssObjectsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePackages',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_packages_with_options_async(
        self,
        request: sddp_20190103_models.DescribePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribePackagesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePackages',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribePackagesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRiskLevels',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_levels_with_options_async(
        self,
        request: sddp_20190103_models.DescribeRiskLevelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRiskLevelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRiskLevels',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRiskLevelsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Category'] = request.category
        query['ContentCategory'] = request.content_category
        query['CurrentPage'] = request.current_page
        query['CustomType'] = request.custom_type
        query['GroupId'] = request.group_id
        query['KeywordCompatible'] = request.keyword_compatible
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['Status'] = request.status
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: sddp_20190103_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['ContentCategory'] = request.content_category
        query['CurrentPage'] = request.current_page
        query['CustomType'] = request.custom_type
        query['GroupId'] = request.group_id
        query['KeywordCompatible'] = request.keyword_compatible
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['Status'] = request.status
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PackageId'] = request.package_id
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: sddp_20190103_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['InstanceId'] = request.instance_id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['PackageId'] = request.package_id
        query['PageSize'] = request.page_size
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleId'] = request.rule_id
        query['ServiceRegionId'] = request.service_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: sddp_20190103_models.DescribeUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DescribeUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DescribeUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Code'] = request.code
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableUserConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DisableUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_user_config_with_options_async(
        self,
        request: sddp_20190103_models.DisableUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.DisableUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Code'] = request.code
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableUserConfig',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.DisableUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Data'] = request.data
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecDatamask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ExecDatamaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_datamask_with_options_async(
        self,
        request: sddp_20190103_models.ExecDatamaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ExecDatamaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecDatamask',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ExecDatamaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ManualTriggerMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ManualTriggerMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_trigger_masking_process_with_options_async(
        self,
        request: sddp_20190103_models.ManualTriggerMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ManualTriggerMaskingProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ManualTriggerMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ManualTriggerMaskingProcessResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['AuditStatus'] = request.audit_status
        query['AutoScan'] = request.auto_scan
        query['EngineType'] = request.engine_type
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['LogStoreDay'] = request.log_store_day
        query['ModifyPassword'] = request.modify_password
        query['Password'] = request.password
        query['Port'] = request.port
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_limit_with_options_async(
        self,
        request: sddp_20190103_models.ModifyDataLimitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDataLimitResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AuditStatus'] = request.audit_status
        query['AutoScan'] = request.auto_scan
        query['EngineType'] = request.engine_type
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['LogStoreDay'] = request.log_store_day
        query['ModifyPassword'] = request.modify_password
        query['Password'] = request.password
        query['Port'] = request.port
        query['ResourceType'] = request.resource_type
        query['ServiceRegionId'] = request.service_region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDataLimit',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['DefaultId'] = request.default_id
        query['Lang'] = request.lang
        query['SensitiveIds'] = request.sensitive_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDefaultLevel',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDefaultLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_default_level_with_options_async(
        self,
        request: sddp_20190103_models.ModifyDefaultLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyDefaultLevelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DefaultId'] = request.default_id
        query['Lang'] = request.lang
        query['SensitiveIds'] = request.sensitive_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDefaultLevel',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyDefaultLevelResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Backed'] = request.backed
        query['DealReason'] = request.deal_reason
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyEventStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_event_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyEventStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Backed'] = request.backed
        query['DealReason'] = request.deal_reason
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyEventStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Lang'] = request.lang
        query['SubTypeIds'] = request.sub_type_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyEventTypeStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventTypeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_event_type_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyEventTypeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyEventTypeStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Lang'] = request.lang
        query['SubTypeIds'] = request.sub_type_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyEventTypeStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyEventTypeStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Category'] = request.category
        query['Content'] = request.content
        query['CustomType'] = request.custom_type
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['StatExpress'] = request.stat_express
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        request: sddp_20190103_models.ModifyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Category'] = request.category
        query['Content'] = request.content
        query['CustomType'] = request.custom_type
        query['Id'] = request.id
        query['Lang'] = request.lang
        query['Name'] = request.name
        query['ProductCode'] = request.product_code
        query['ProductId'] = request.product_id
        query['RiskLevelId'] = request.risk_level_id
        query['RuleType'] = request.rule_type
        query['StatExpress'] = request.stat_express
        query['WarnLevel'] = request.warn_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRule',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Ids'] = request.ids
        query['Lang'] = request.lang
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRuleStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_status_with_options_async(
        self,
        request: sddp_20190103_models.ModifyRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.ModifyRuleStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Ids'] = request.ids
        query['Lang'] = request.lang
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRuleStatus',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.ModifyRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.StopMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_masking_process_with_options_async(
        self,
        request: sddp_20190103_models.StopMaskingProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> sddp_20190103_models.StopMaskingProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Lang'] = request.lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopMaskingProcess',
            version='2019-01-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            sddp_20190103_models.StopMaskingProcessResponse(),
            await self.call_api_async(params, req, runtime)
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
