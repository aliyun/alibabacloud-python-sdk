# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_maxcompute20220104 import models as max_compute_20220104_models
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
            'ap-northeast-1': 'maxcompute.aliyuncs.com',
            'ap-northeast-2-pop': 'maxcompute.aliyuncs.com',
            'ap-south-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-2': 'maxcompute.aliyuncs.com',
            'ap-southeast-3': 'maxcompute.aliyuncs.com',
            'ap-southeast-5': 'maxcompute.aliyuncs.com',
            'cn-beijing': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-beijing-gov-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-nu16-b01': 'maxcompute.aliyuncs.com',
            'cn-chengdu': 'maxcompute.aliyuncs.com',
            'cn-edge-1': 'maxcompute.aliyuncs.com',
            'cn-fujian': 'maxcompute.aliyuncs.com',
            'cn-haidian-cm12-c01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-finance': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-test-306': 'maxcompute.aliyuncs.com',
            'cn-hongkong': 'maxcompute.aliyuncs.com',
            'cn-hongkong-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-huhehaote': 'maxcompute.aliyuncs.com',
            'cn-north-2-gov-1': 'maxcompute.aliyuncs.com',
            'cn-qingdao': 'maxcompute.aliyuncs.com',
            'cn-qingdao-nebula': 'maxcompute.aliyuncs.com',
            'cn-shanghai': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et15-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et2-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shanghai-inner': 'maxcompute.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-inner': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'maxcompute.aliyuncs.com',
            'cn-wuhan': 'maxcompute.aliyuncs.com',
            'cn-yushanfang': 'maxcompute.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'maxcompute.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'maxcompute.aliyuncs.com',
            'eu-central-1': 'maxcompute.aliyuncs.com',
            'eu-west-1': 'maxcompute.aliyuncs.com',
            'eu-west-1-oxs': 'maxcompute.aliyuncs.com',
            'me-east-1': 'maxcompute.aliyuncs.com',
            'rus-west-1-pop': 'maxcompute.aliyuncs.com',
            'us-east-1': 'maxcompute.aliyuncs.com',
            'us-west-1': 'maxcompute.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('maxcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ApplyComputeQuotaPlanResponse:
        """
        @summary Activate a Quota Plan Immediately.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}/apply',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ApplyComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ApplyComputeQuotaPlanResponse:
        """
        @summary Activate a Quota Plan Immediately.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ApplyComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}/apply',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ApplyComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.ApplyComputeQuotaPlanResponse:
        """
        @summary Activate a Quota Plan Immediately.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @return: ApplyComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.apply_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def apply_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.ApplyComputeQuotaPlanResponse:
        """
        @summary Activate a Quota Plan Immediately.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @return: ApplyComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.apply_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def create_compute_quota_plan_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateComputeQuotaPlanResponse:
        """
        @summary Create MaxCompute ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: CreateComputeQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateComputeQuotaPlanResponse:
        """
        @summary Create MaxCompute ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: CreateComputeQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateComputeQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_quota_plan(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateComputeQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateComputeQuotaPlanResponse:
        """
        @summary Create MaxCompute ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: CreateComputeQuotaPlanRequest
        @return: CreateComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_compute_quota_plan_with_options(nickname, request, headers, runtime)

    async def create_compute_quota_plan_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateComputeQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateComputeQuotaPlanResponse:
        """
        @summary Create MaxCompute ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: CreateComputeQuotaPlanRequest
        @return: CreateComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_compute_quota_plan_with_options_async(nickname, request, headers, runtime)

    def create_mms_data_source_with_options(
        self,
        request: max_compute_20220104_models.CreateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsDataSourceResponse:
        """
        @summary CreateMmsDataSource
        
        @param request: CreateMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.networklink):
            body['networklink'] = request.networklink
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_data_source_with_options_async(
        self,
        request: max_compute_20220104_models.CreateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsDataSourceResponse:
        """
        @summary CreateMmsDataSource
        
        @param request: CreateMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.networklink):
            body['networklink'] = request.networklink
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_data_source(
        self,
        request: max_compute_20220104_models.CreateMmsDataSourceRequest,
    ) -> max_compute_20220104_models.CreateMmsDataSourceResponse:
        """
        @summary CreateMmsDataSource
        
        @param request: CreateMmsDataSourceRequest
        @return: CreateMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_mms_data_source_with_options(request, headers, runtime)

    async def create_mms_data_source_async(
        self,
        request: max_compute_20220104_models.CreateMmsDataSourceRequest,
    ) -> max_compute_20220104_models.CreateMmsDataSourceResponse:
        """
        @summary CreateMmsDataSource
        
        @param request: CreateMmsDataSourceRequest
        @return: CreateMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_mms_data_source_with_options_async(request, headers, runtime)

    def create_mms_fetch_metadata_job_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsFetchMetadataJobResponse:
        """
        @summary 创建数据源的更新元数据操作
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsFetchMetadataJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateMmsFetchMetadataJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/scans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsFetchMetadataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_fetch_metadata_job_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsFetchMetadataJobResponse:
        """
        @summary 创建数据源的更新元数据操作
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsFetchMetadataJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateMmsFetchMetadataJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/scans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsFetchMetadataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_fetch_metadata_job(
        self,
        source_id: str,
    ) -> max_compute_20220104_models.CreateMmsFetchMetadataJobResponse:
        """
        @summary 创建数据源的更新元数据操作
        
        @return: CreateMmsFetchMetadataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_mms_fetch_metadata_job_with_options(source_id, headers, runtime)

    async def create_mms_fetch_metadata_job_async(
        self,
        source_id: str,
    ) -> max_compute_20220104_models.CreateMmsFetchMetadataJobResponse:
        """
        @summary 创建数据源的更新元数据操作
        
        @return: CreateMmsFetchMetadataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_mms_fetch_metadata_job_with_options_async(source_id, headers, runtime)

    def create_mms_job_with_options(
        self,
        source_id: str,
        request: max_compute_20220104_models.CreateMmsJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsJobResponse:
        """
        @summary 创建迁移任务
        
        @param request: CreateMmsJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not UtilClient.is_unset(request.dst_db_name):
            body['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_schema_name):
            body['dstSchemaName'] = request.dst_schema_name
        if not UtilClient.is_unset(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not UtilClient.is_unset(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not UtilClient.is_unset(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not UtilClient.is_unset(request.eta):
            body['eta'] = request.eta
        if not UtilClient.is_unset(request.increment):
            body['increment'] = request.increment
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.others):
            body['others'] = request.others
        if not UtilClient.is_unset(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not UtilClient.is_unset(request.partitions):
            body['partitions'] = request.partitions
        if not UtilClient.is_unset(request.schema_only):
            body['schemaOnly'] = request.schema_only
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_name):
            body['sourceName'] = request.source_name
        if not UtilClient.is_unset(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_schema_name):
            body['srcSchemaName'] = request.src_schema_name
        if not UtilClient.is_unset(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not UtilClient.is_unset(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not UtilClient.is_unset(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not UtilClient.is_unset(request.tables):
            body['tables'] = request.tables
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_job_with_options_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.CreateMmsJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateMmsJobResponse:
        """
        @summary 创建迁移任务
        
        @param request: CreateMmsJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMmsJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not UtilClient.is_unset(request.dst_db_name):
            body['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_schema_name):
            body['dstSchemaName'] = request.dst_schema_name
        if not UtilClient.is_unset(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not UtilClient.is_unset(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not UtilClient.is_unset(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not UtilClient.is_unset(request.eta):
            body['eta'] = request.eta
        if not UtilClient.is_unset(request.increment):
            body['increment'] = request.increment
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.others):
            body['others'] = request.others
        if not UtilClient.is_unset(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not UtilClient.is_unset(request.partitions):
            body['partitions'] = request.partitions
        if not UtilClient.is_unset(request.schema_only):
            body['schemaOnly'] = request.schema_only
        if not UtilClient.is_unset(request.source_id):
            body['sourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_name):
            body['sourceName'] = request.source_name
        if not UtilClient.is_unset(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_schema_name):
            body['srcSchemaName'] = request.src_schema_name
        if not UtilClient.is_unset(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not UtilClient.is_unset(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not UtilClient.is_unset(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not UtilClient.is_unset(request.tables):
            body['tables'] = request.tables
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_job(
        self,
        source_id: str,
        request: max_compute_20220104_models.CreateMmsJobRequest,
    ) -> max_compute_20220104_models.CreateMmsJobResponse:
        """
        @summary 创建迁移任务
        
        @param request: CreateMmsJobRequest
        @return: CreateMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_mms_job_with_options(source_id, request, headers, runtime)

    async def create_mms_job_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.CreateMmsJobRequest,
    ) -> max_compute_20220104_models.CreateMmsJobResponse:
        """
        @summary 创建迁移任务
        
        @param request: CreateMmsJobRequest
        @return: CreateMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_mms_job_with_options_async(source_id, request, headers, runtime)

    def create_package_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        """
        @summary Creates a package.
        
        @param request: CreatePackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_package_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        """
        @summary Creates a package.
        
        @param request: CreatePackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_package(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        """
        @summary Creates a package.
        
        @param request: CreatePackageRequest
        @return: CreatePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_package_with_options(project_name, request, headers, runtime)

    async def create_package_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreatePackageRequest,
    ) -> max_compute_20220104_models.CreatePackageResponse:
        """
        @summary Creates a package.
        
        @param request: CreatePackageRequest
        @return: CreatePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_package_with_options_async(project_name, request, headers, runtime)

    def create_project_with_options(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        """
        @summary Creates a MaxCompute project.
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        """
        @summary Creates a MaxCompute project.
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        """
        @summary Creates a MaxCompute project.
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: max_compute_20220104_models.CreateProjectRequest,
    ) -> max_compute_20220104_models.CreateProjectResponse:
        """
        @summary Creates a MaxCompute project.
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_quota_plan_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        """
        @summary Creates a quota plan.
        
        @param request: CreateQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_plan_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        """
        @summary Creates a quota plan.
        
        @param request: CreateQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_plan(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        """
        @summary Creates a quota plan.
        
        @param request: CreateQuotaPlanRequest
        @return: CreateQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_quota_plan_with_options(nickname, request, headers, runtime)

    async def create_quota_plan_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.CreateQuotaPlanRequest,
    ) -> max_compute_20220104_models.CreateQuotaPlanResponse:
        """
        @summary Creates a quota plan.
        
        @param request: CreateQuotaPlanRequest
        @return: CreateQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_quota_plan_with_options_async(nickname, request, headers, runtime)

    def create_role_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        """
        @summary Creates a role at the MaxCompute project level.
        
        @param request: CreateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        """
        @summary Creates a role at the MaxCompute project level.
        
        @param request: CreateRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoleResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        """
        @summary Creates a role at the MaxCompute project level.
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_role_with_options(project_name, request, headers, runtime)

    async def create_role_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.CreateRoleRequest,
    ) -> max_compute_20220104_models.CreateRoleResponse:
        """
        @summary Creates a role at the MaxCompute project level.
        
        @param request: CreateRoleRequest
        @return: CreateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(project_name, request, headers, runtime)

    def delete_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteComputeQuotaPlanResponse:
        """
        @summary Delete MaxCompute compute quota plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteComputeQuotaPlanResponse:
        """
        @summary Delete MaxCompute compute quota plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.DeleteComputeQuotaPlanResponse:
        """
        @summary Delete MaxCompute compute quota plan.
        
        @return: DeleteComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def delete_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.DeleteComputeQuotaPlanResponse:
        """
        @summary Delete MaxCompute compute quota plan.
        
        @return: DeleteComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def delete_mms_data_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteMmsDataSourceResponse:
        """
        @summary 删除数据源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmsDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mms_data_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteMmsDataSourceResponse:
        """
        @summary 删除数据源
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmsDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mms_data_source(
        self,
        source_id: str,
    ) -> max_compute_20220104_models.DeleteMmsDataSourceResponse:
        """
        @summary 删除数据源
        
        @return: DeleteMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_mms_data_source_with_options(source_id, headers, runtime)

    async def delete_mms_data_source_async(
        self,
        source_id: str,
    ) -> max_compute_20220104_models.DeleteMmsDataSourceResponse:
        """
        @summary 删除数据源
        
        @return: DeleteMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_mms_data_source_with_options_async(source_id, headers, runtime)

    def delete_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteMmsJobResponse:
        """
        @summary 删除迁移计划
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteMmsJobResponse:
        """
        @summary 删除迁移计划
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.DeleteMmsJobResponse:
        """
        @summary 删除迁移计划
        
        @return: DeleteMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_mms_job_with_options(source_id, job_id, headers, runtime)

    async def delete_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.DeleteMmsJobResponse:
        """
        @summary 删除迁移计划
        
        @return: DeleteMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def delete_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        """
        @summary Deletes a quota plan.
        
        @param request: DeleteQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        """
        @summary Deletes a quota plan.
        
        @param request: DeleteQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.DeleteQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        """
        @summary Deletes a quota plan.
        
        @param request: DeleteQuotaPlanRequest
        @return: DeleteQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def delete_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.DeleteQuotaPlanRequest,
    ) -> max_compute_20220104_models.DeleteQuotaPlanResponse:
        """
        @summary Deletes a quota plan.
        
        @param request: DeleteQuotaPlanRequest
        @return: DeleteQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_compute_effective_plan_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeEffectivePlanResponse:
        """
        @summary GetComputeEffectivePlan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeEffectivePlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComputeEffectivePlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeEffectivePlan/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeEffectivePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_effective_plan_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeEffectivePlanResponse:
        """
        @summary GetComputeEffectivePlan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeEffectivePlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComputeEffectivePlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeEffectivePlan/',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeEffectivePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_effective_plan(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.GetComputeEffectivePlanResponse:
        """
        @summary GetComputeEffectivePlan.
        
        @return: GetComputeEffectivePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compute_effective_plan_with_options(nickname, headers, runtime)

    async def get_compute_effective_plan_async(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.GetComputeEffectivePlanResponse:
        """
        @summary GetComputeEffectivePlan.
        
        @return: GetComputeEffectivePlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_compute_effective_plan_with_options_async(nickname, headers, runtime)

    def get_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeQuotaPlanResponse:
        """
        @summary Get detailed information of a single compute quota plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeQuotaPlanResponse:
        """
        @summary Get detailed information of a single compute quota plan.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.GetComputeQuotaPlanResponse:
        """
        @summary Get detailed information of a single compute quota plan.
        
        @return: GetComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def get_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> max_compute_20220104_models.GetComputeQuotaPlanResponse:
        """
        @summary Get detailed information of a single compute quota plan.
        
        @return: GetComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def get_compute_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeQuotaScheduleResponse:
        """
        @summary Displays the time-specific configuration of compute quota.
        
        @param request: GetComputeQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetComputeQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaSchedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetComputeQuotaScheduleResponse:
        """
        @summary Displays the time-specific configuration of compute quota.
        
        @param request: GetComputeQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetComputeQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetComputeQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaSchedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetComputeQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetComputeQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetComputeQuotaScheduleResponse:
        """
        @summary Displays the time-specific configuration of compute quota.
        
        @param request: GetComputeQuotaScheduleRequest
        @return: GetComputeQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_compute_quota_schedule_with_options(nickname, request, headers, runtime)

    async def get_compute_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetComputeQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetComputeQuotaScheduleResponse:
        """
        @summary Displays the time-specific configuration of compute quota.
        
        @param request: GetComputeQuotaScheduleRequest
        @return: GetComputeQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_compute_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def get_job_info_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobInfoResponse:
        """
        @summary Queries the basic information about a job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(instance_id)}/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobInfoResponse:
        """
        @summary Queries the basic information about a job.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/{OpenApiUtilClient.get_encode_param(instance_id)}/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        instance_id: str,
    ) -> max_compute_20220104_models.GetJobInfoResponse:
        """
        @summary Queries the basic information about a job.
        
        @return: GetJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_info_with_options(instance_id, headers, runtime)

    async def get_job_info_async(
        self,
        instance_id: str,
    ) -> max_compute_20220104_models.GetJobInfoResponse:
        """
        @summary Queries the basic information about a job.
        
        @return: GetJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_info_with_options_async(instance_id, headers, runtime)

    def get_job_resource_usage_with_options(
        self,
        tmp_req: max_compute_20220104_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        """
        @summary Performs statistics on all jobs that are complete on a specified day and obtains the total resource usage of each job executor on a daily basis.
        
        @param tmp_req: GetJobResourceUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResourceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetJobResourceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResourceUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/resourceUsage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_resource_usage_with_options_async(
        self,
        tmp_req: max_compute_20220104_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        """
        @summary Performs statistics on all jobs that are complete on a specified day and obtains the total resource usage of each job executor on a daily basis.
        
        @param tmp_req: GetJobResourceUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResourceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetJobResourceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobResourceUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/resourceUsage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetJobResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_resource_usage(
        self,
        request: max_compute_20220104_models.GetJobResourceUsageRequest,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        """
        @summary Performs statistics on all jobs that are complete on a specified day and obtains the total resource usage of each job executor on a daily basis.
        
        @param request: GetJobResourceUsageRequest
        @return: GetJobResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_resource_usage_with_options(request, headers, runtime)

    async def get_job_resource_usage_async(
        self,
        request: max_compute_20220104_models.GetJobResourceUsageRequest,
    ) -> max_compute_20220104_models.GetJobResourceUsageResponse:
        """
        @summary Performs statistics on all jobs that are complete on a specified day and obtains the total resource usage of each job executor on a daily basis.
        
        @param request: GetJobResourceUsageRequest
        @return: GetJobResourceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_resource_usage_with_options_async(request, headers, runtime)

    def get_mms_async_task_with_options(
        self,
        source_id: str,
        async_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsAsyncTaskResponse:
        """
        @summary GetMmsAsyncTask
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsAsyncTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsAsyncTask',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/asyncTasks/{OpenApiUtilClient.get_encode_param(async_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_async_task_with_options_async(
        self,
        source_id: str,
        async_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsAsyncTaskResponse:
        """
        @summary GetMmsAsyncTask
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsAsyncTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsAsyncTask',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/asyncTasks/{OpenApiUtilClient.get_encode_param(async_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_async_task(
        self,
        source_id: str,
        async_task_id: str,
    ) -> max_compute_20220104_models.GetMmsAsyncTaskResponse:
        """
        @summary GetMmsAsyncTask
        
        @return: GetMmsAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_async_task_with_options(source_id, async_task_id, headers, runtime)

    async def get_mms_async_task_async(
        self,
        source_id: str,
        async_task_id: str,
    ) -> max_compute_20220104_models.GetMmsAsyncTaskResponse:
        """
        @summary GetMmsAsyncTask
        
        @return: GetMmsAsyncTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_async_task_with_options_async(source_id, async_task_id, headers, runtime)

    def get_mms_data_source_with_options(
        self,
        source_id: str,
        request: max_compute_20220104_models.GetMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsDataSourceResponse:
        """
        @summary 获取数据源
        
        @param request: GetMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.with_config):
            query['withConfig'] = request.with_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_data_source_with_options_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.GetMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsDataSourceResponse:
        """
        @summary 获取数据源
        
        @param request: GetMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lang):
            query['lang'] = request.lang
        if not UtilClient.is_unset(request.with_config):
            query['withConfig'] = request.with_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_data_source(
        self,
        source_id: str,
        request: max_compute_20220104_models.GetMmsDataSourceRequest,
    ) -> max_compute_20220104_models.GetMmsDataSourceResponse:
        """
        @summary 获取数据源
        
        @param request: GetMmsDataSourceRequest
        @return: GetMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_data_source_with_options(source_id, request, headers, runtime)

    async def get_mms_data_source_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.GetMmsDataSourceRequest,
    ) -> max_compute_20220104_models.GetMmsDataSourceResponse:
        """
        @summary 获取数据源
        
        @param request: GetMmsDataSourceRequest
        @return: GetMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_data_source_with_options_async(source_id, request, headers, runtime)

    def get_mms_db_with_options(
        self,
        source_id: str,
        db_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsDbResponse:
        """
        @summary GetMmsDb
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsDbResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsDb',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/dbs/{OpenApiUtilClient.get_encode_param(db_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_db_with_options_async(
        self,
        source_id: str,
        db_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsDbResponse:
        """
        @summary GetMmsDb
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsDbResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsDb',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/dbs/{OpenApiUtilClient.get_encode_param(db_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_db(
        self,
        source_id: str,
        db_id: str,
    ) -> max_compute_20220104_models.GetMmsDbResponse:
        """
        @summary GetMmsDb
        
        @return: GetMmsDbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_db_with_options(source_id, db_id, headers, runtime)

    async def get_mms_db_async(
        self,
        source_id: str,
        db_id: str,
    ) -> max_compute_20220104_models.GetMmsDbResponse:
        """
        @summary GetMmsDb
        
        @return: GetMmsDbResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_db_with_options_async(source_id, db_id, headers, runtime)

    def get_mms_fetch_metadata_job_with_options(
        self,
        source_id: str,
        scan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsFetchMetadataJobResponse:
        """
        @summary GetMmsFetchMetadataJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsFetchMetadataJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsFetchMetadataJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/scans/{OpenApiUtilClient.get_encode_param(scan_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsFetchMetadataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_fetch_metadata_job_with_options_async(
        self,
        source_id: str,
        scan_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsFetchMetadataJobResponse:
        """
        @summary GetMmsFetchMetadataJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsFetchMetadataJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsFetchMetadataJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/scans/{OpenApiUtilClient.get_encode_param(scan_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsFetchMetadataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_fetch_metadata_job(
        self,
        source_id: str,
        scan_id: str,
    ) -> max_compute_20220104_models.GetMmsFetchMetadataJobResponse:
        """
        @summary GetMmsFetchMetadataJob
        
        @return: GetMmsFetchMetadataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_fetch_metadata_job_with_options(source_id, scan_id, headers, runtime)

    async def get_mms_fetch_metadata_job_async(
        self,
        source_id: str,
        scan_id: str,
    ) -> max_compute_20220104_models.GetMmsFetchMetadataJobResponse:
        """
        @summary GetMmsFetchMetadataJob
        
        @return: GetMmsFetchMetadataJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_fetch_metadata_job_with_options_async(source_id, scan_id, headers, runtime)

    def get_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsJobResponse:
        """
        @summary 获取迁移计划
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsJobResponse:
        """
        @summary 获取迁移计划
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.GetMmsJobResponse:
        """
        @summary 获取迁移计划
        
        @return: GetMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_job_with_options(source_id, job_id, headers, runtime)

    async def get_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.GetMmsJobResponse:
        """
        @summary 获取迁移计划
        
        @return: GetMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def get_mms_partition_with_options(
        self,
        source_id: str,
        partition_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsPartitionResponse:
        """
        @summary GetMmsPartition
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsPartitionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsPartition',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/partitions/{OpenApiUtilClient.get_encode_param(partition_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_partition_with_options_async(
        self,
        source_id: str,
        partition_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsPartitionResponse:
        """
        @summary GetMmsPartition
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsPartitionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsPartition',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/partitions/{OpenApiUtilClient.get_encode_param(partition_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_partition(
        self,
        source_id: str,
        partition_id: str,
    ) -> max_compute_20220104_models.GetMmsPartitionResponse:
        """
        @summary GetMmsPartition
        
        @return: GetMmsPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_partition_with_options(source_id, partition_id, headers, runtime)

    async def get_mms_partition_async(
        self,
        source_id: str,
        partition_id: str,
    ) -> max_compute_20220104_models.GetMmsPartitionResponse:
        """
        @summary GetMmsPartition
        
        @return: GetMmsPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_partition_with_options_async(source_id, partition_id, headers, runtime)

    def get_mms_table_with_options(
        self,
        source_id: str,
        table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsTableResponse:
        """
        @summary GetMmsTable
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsTable',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tables/{OpenApiUtilClient.get_encode_param(table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_table_with_options_async(
        self,
        source_id: str,
        table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsTableResponse:
        """
        @summary GetMmsTable
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsTable',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tables/{OpenApiUtilClient.get_encode_param(table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_table(
        self,
        source_id: str,
        table_id: str,
    ) -> max_compute_20220104_models.GetMmsTableResponse:
        """
        @summary GetMmsTable
        
        @return: GetMmsTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_table_with_options(source_id, table_id, headers, runtime)

    async def get_mms_table_async(
        self,
        source_id: str,
        table_id: str,
    ) -> max_compute_20220104_models.GetMmsTableResponse:
        """
        @summary GetMmsTable
        
        @return: GetMmsTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_table_with_options_async(source_id, table_id, headers, runtime)

    def get_mms_task_with_options(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsTaskResponse:
        """
        @summary GetMmsTask
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsTask',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_task_with_options_async(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetMmsTaskResponse:
        """
        @summary GetMmsTask
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMmsTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetMmsTask',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetMmsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_task(
        self,
        source_id: str,
        task_id: str,
    ) -> max_compute_20220104_models.GetMmsTaskResponse:
        """
        @summary GetMmsTask
        
        @return: GetMmsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mms_task_with_options(source_id, task_id, headers, runtime)

    async def get_mms_task_async(
        self,
        source_id: str,
        task_id: str,
    ) -> max_compute_20220104_models.GetMmsTaskResponse:
        """
        @summary GetMmsTask
        
        @return: GetMmsTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mms_task_with_options_async(source_id, task_id, headers, runtime)

    def get_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetPackageResponse:
        """
        @summary Obtains the information about a package.
        
        @param request: GetPackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetPackageResponse:
        """
        @summary Obtains the information about a package.
        
        @param request: GetPackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPackageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
    ) -> max_compute_20220104_models.GetPackageResponse:
        """
        @summary Obtains the information about a package.
        
        @param request: GetPackageRequest
        @return: GetPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_package_with_options(project_name, package_name, request, headers, runtime)

    async def get_package_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.GetPackageRequest,
    ) -> max_compute_20220104_models.GetPackageResponse:
        """
        @summary Obtains the information about a package.
        
        @param request: GetPackageRequest
        @return: GetPackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_package_with_options_async(project_name, package_name, request, headers, runtime)

    def get_project_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.GetProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetProjectResponse:
        """
        @summary Queries the information about a MaxCompute project.
        
        @param request: GetProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.GetProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetProjectResponse:
        """
        @summary Queries the information about a MaxCompute project.
        
        @param request: GetProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_name: str,
        request: max_compute_20220104_models.GetProjectRequest,
    ) -> max_compute_20220104_models.GetProjectResponse:
        """
        @summary Queries the information about a MaxCompute project.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_name, request, headers, runtime)

    async def get_project_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.GetProjectRequest,
    ) -> max_compute_20220104_models.GetProjectResponse:
        """
        @summary Queries the information about a MaxCompute project.
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_name, request, headers, runtime)

    def get_quota_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        """
        @summary Obtains the information about a specified level-1 quota.
        
        @param request: GetQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        """
        @summary Obtains the information about a specified level-1 quota.
        
        @param request: GetQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        """
        @summary Obtains the information about a specified level-1 quota.
        
        @param request: GetQuotaRequest
        @return: GetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(nickname, request, headers, runtime)

    async def get_quota_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaRequest,
    ) -> max_compute_20220104_models.GetQuotaResponse:
        """
        @summary Obtains the information about a specified level-1 quota.
        
        @param request: GetQuotaRequest
        @return: GetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(nickname, request, headers, runtime)

    def get_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        """
        @summary Obtains the information of a quota plan.
        
        @param request: GetQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        """
        @summary Obtains the information of a quota plan.
        
        @param request: GetQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        """
        @summary Obtains the information of a quota plan.
        
        @param request: GetQuotaPlanRequest
        @return: GetQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def get_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.GetQuotaPlanRequest,
    ) -> max_compute_20220104_models.GetQuotaPlanResponse:
        """
        @summary Obtains the information of a quota plan.
        
        @param request: GetQuotaPlanRequest
        @return: GetQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        """
        @summary Obtains the scheduling plan for a quota plan.
        
        @param request: GetQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        """
        @summary Obtains the scheduling plan for a quota plan.
        
        @param request: GetQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        """
        @summary Obtains the scheduling plan for a quota plan.
        
        @param request: GetQuotaScheduleRequest
        @return: GetQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_schedule_with_options(nickname, request, headers, runtime)

    async def get_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaScheduleRequest,
    ) -> max_compute_20220104_models.GetQuotaScheduleResponse:
        """
        @summary Obtains the scheduling plan for a quota plan.
        
        @param request: GetQuotaScheduleRequest
        @return: GetQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def get_quota_usage_with_options(
        self,
        nickname: str,
        tmp_req: max_compute_20220104_models.GetQuotaUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaUsageResponse:
        """
        @summary Queries quota resource consumption information.
        
        @param tmp_req: GetQuotaUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetQuotaUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plot_types):
            request.plot_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plot_types, 'plotTypes', 'simple')
        if not UtilClient.is_unset(tmp_req.y_axis_types):
            request.y_axis_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.y_axis_types, 'yAxisTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.agg_method):
            query['aggMethod'] = request.agg_method
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.plot_types_shrink):
            query['plotTypes'] = request.plot_types_shrink
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sub_quota_nickname):
            query['subQuotaNickname'] = request.sub_quota_nickname
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.y_axis_types_shrink):
            query['yAxisTypes'] = request.y_axis_types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/usage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_usage_with_options_async(
        self,
        nickname: str,
        tmp_req: max_compute_20220104_models.GetQuotaUsageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetQuotaUsageResponse:
        """
        @summary Queries quota resource consumption information.
        
        @param tmp_req: GetQuotaUsageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQuotaUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetQuotaUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plot_types):
            request.plot_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plot_types, 'plotTypes', 'simple')
        if not UtilClient.is_unset(tmp_req.y_axis_types):
            request.y_axis_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.y_axis_types, 'yAxisTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.agg_method):
            query['aggMethod'] = request.agg_method
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.plot_types_shrink):
            query['plotTypes'] = request.plot_types_shrink
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sub_quota_nickname):
            query['subQuotaNickname'] = request.sub_quota_nickname
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        if not UtilClient.is_unset(request.y_axis_types_shrink):
            query['yAxisTypes'] = request.y_axis_types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQuotaUsage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/usage',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetQuotaUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_usage(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaUsageRequest,
    ) -> max_compute_20220104_models.GetQuotaUsageResponse:
        """
        @summary Queries quota resource consumption information.
        
        @param request: GetQuotaUsageRequest
        @return: GetQuotaUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_quota_usage_with_options(nickname, request, headers, runtime)

    async def get_quota_usage_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.GetQuotaUsageRequest,
    ) -> max_compute_20220104_models.GetQuotaUsageResponse:
        """
        @summary Queries quota resource consumption information.
        
        @param request: GetQuotaUsageRequest
        @return: GetQuotaUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_quota_usage_with_options_async(nickname, request, headers, runtime)

    def get_role_acl_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        """
        @summary Obtains the ACL-based permissions that is granted to a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleAclResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRoleAcl',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/roleAcl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        """
        @summary Obtains the ACL-based permissions that is granted to a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleAclResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRoleAcl',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/roleAcl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        """
        @summary Obtains the ACL-based permissions that is granted to a project-level role.
        
        @return: GetRoleAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_with_options(project_name, role_name, headers, runtime)

    async def get_role_acl_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRoleAclResponse:
        """
        @summary Obtains the ACL-based permissions that is granted to a project-level role.
        
        @return: GetRoleAclResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_acl_with_options_async(project_name, role_name, headers, runtime)

    def get_role_acl_on_object_with_options(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        """
        @summary Obtains ACL-based permissions on an object that are granted to a project-level role.
        
        @param request: GetRoleAclOnObjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleAclOnObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoleAclOnObject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclOnObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_on_object_with_options_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        """
        @summary Obtains ACL-based permissions on an object that are granted to a project-level role.
        
        @param request: GetRoleAclOnObjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoleAclOnObjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.object_name):
            query['objectName'] = request.object_name
        if not UtilClient.is_unset(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRoleAclOnObject',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/acl',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRoleAclOnObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl_on_object(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        """
        @summary Obtains ACL-based permissions on an object that are granted to a project-level role.
        
        @param request: GetRoleAclOnObjectRequest
        @return: GetRoleAclOnObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_acl_on_object_with_options(project_name, role_name, request, headers, runtime)

    async def get_role_acl_on_object_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.GetRoleAclOnObjectRequest,
    ) -> max_compute_20220104_models.GetRoleAclOnObjectResponse:
        """
        @summary Obtains ACL-based permissions on an object that are granted to a project-level role.
        
        @param request: GetRoleAclOnObjectRequest
        @return: GetRoleAclOnObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_acl_on_object_with_options_async(project_name, role_name, request, headers, runtime)

    def get_role_policy_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        """
        @summary Obtains the policy that is attached to a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRolePolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRolePolicy',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRolePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_policy_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        """
        @summary Obtains the policy that is attached to a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRolePolicyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRolePolicy',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/policy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRolePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_policy(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        """
        @summary Obtains the policy that is attached to a project-level role.
        
        @return: GetRolePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_role_policy_with_options(project_name, role_name, headers, runtime)

    async def get_role_policy_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.GetRolePolicyResponse:
        """
        @summary Obtains the policy that is attached to a project-level role.
        
        @return: GetRolePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_role_policy_with_options_async(project_name, role_name, headers, runtime)

    def get_running_jobs_with_options(
        self,
        tmp_req: max_compute_20220104_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        """
        @summary Obtains the running state data of jobs that are in the running state in a specified period of time.
        
        @param tmp_req: GetRunningJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunningJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetRunningJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/runningJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRunningJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_running_jobs_with_options_async(
        self,
        tmp_req: max_compute_20220104_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        """
        @summary Obtains the running state data of jobs that are in the running state in a specified period of time.
        
        @param tmp_req: GetRunningJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRunningJobsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetRunningJobsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_owner_list):
            request.job_owner_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not UtilClient.is_unset(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['from'] = request.from_
        if not UtilClient.is_unset(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not UtilClient.is_unset(request.to):
            query['to'] = request.to
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRunningJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/runningJobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetRunningJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_running_jobs(
        self,
        request: max_compute_20220104_models.GetRunningJobsRequest,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        """
        @summary Obtains the running state data of jobs that are in the running state in a specified period of time.
        
        @param request: GetRunningJobsRequest
        @return: GetRunningJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_running_jobs_with_options(request, headers, runtime)

    async def get_running_jobs_async(
        self,
        request: max_compute_20220104_models.GetRunningJobsRequest,
    ) -> max_compute_20220104_models.GetRunningJobsResponse:
        """
        @summary Obtains the running state data of jobs that are in the running state in a specified period of time.
        
        @param request: GetRunningJobsRequest
        @return: GetRunningJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_running_jobs_with_options_async(request, headers, runtime)

    def get_storage_amount_summary_with_options(
        self,
        request: max_compute_20220104_models.GetStorageAmountSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageAmountSummaryResponse:
        """
        @param request: GetStorageAmountSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageAmountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageAmountSummary',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageAmountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_amount_summary_with_options_async(
        self,
        request: max_compute_20220104_models.GetStorageAmountSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageAmountSummaryResponse:
        """
        @param request: GetStorageAmountSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageAmountSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageAmountSummary',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageAmountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_amount_summary(
        self,
        request: max_compute_20220104_models.GetStorageAmountSummaryRequest,
    ) -> max_compute_20220104_models.GetStorageAmountSummaryResponse:
        """
        @param request: GetStorageAmountSummaryRequest
        @return: GetStorageAmountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_storage_amount_summary_with_options(request, headers, runtime)

    async def get_storage_amount_summary_async(
        self,
        request: max_compute_20220104_models.GetStorageAmountSummaryRequest,
    ) -> max_compute_20220104_models.GetStorageAmountSummaryResponse:
        """
        @param request: GetStorageAmountSummaryRequest
        @return: GetStorageAmountSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_storage_amount_summary_with_options_async(request, headers, runtime)

    def get_storage_size_summary_with_options(
        self,
        request: max_compute_20220104_models.GetStorageSizeSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageSizeSummaryResponse:
        """
        @param request: GetStorageSizeSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageSizeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageSizeSummary',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/size',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageSizeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_size_summary_with_options_async(
        self,
        request: max_compute_20220104_models.GetStorageSizeSummaryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageSizeSummaryResponse:
        """
        @param request: GetStorageSizeSummaryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageSizeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageSizeSummary',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/size',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageSizeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_size_summary(
        self,
        request: max_compute_20220104_models.GetStorageSizeSummaryRequest,
    ) -> max_compute_20220104_models.GetStorageSizeSummaryResponse:
        """
        @param request: GetStorageSizeSummaryRequest
        @return: GetStorageSizeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_storage_size_summary_with_options(request, headers, runtime)

    async def get_storage_size_summary_async(
        self,
        request: max_compute_20220104_models.GetStorageSizeSummaryRequest,
    ) -> max_compute_20220104_models.GetStorageSizeSummaryResponse:
        """
        @param request: GetStorageSizeSummaryRequest
        @return: GetStorageSizeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_storage_size_summary_with_options_async(request, headers, runtime)

    def get_storage_summary_compared_with_options(
        self,
        type: str,
        tmp_req: max_compute_20220104_models.GetStorageSummaryComparedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageSummaryComparedResponse:
        """
        @param tmp_req: GetStorageSummaryComparedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageSummaryComparedResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetStorageSummaryComparedShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.projects):
            request.projects_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.projects, 'projects', 'simple')
        query = {}
        if not UtilClient.is_unset(request.begin_date):
            query['beginDate'] = request.begin_date
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.projects_shrink):
            query['projects'] = request.projects_shrink
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageSummaryCompared',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/{OpenApiUtilClient.get_encode_param(type)}/compared',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageSummaryComparedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_summary_compared_with_options_async(
        self,
        type: str,
        tmp_req: max_compute_20220104_models.GetStorageSummaryComparedRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetStorageSummaryComparedResponse:
        """
        @param tmp_req: GetStorageSummaryComparedRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStorageSummaryComparedResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.GetStorageSummaryComparedShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.projects):
            request.projects_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.projects, 'projects', 'simple')
        query = {}
        if not UtilClient.is_unset(request.begin_date):
            query['beginDate'] = request.begin_date
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.projects_shrink):
            query['projects'] = request.projects_shrink
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStorageSummaryCompared',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/{OpenApiUtilClient.get_encode_param(type)}/compared',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetStorageSummaryComparedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_summary_compared(
        self,
        type: str,
        request: max_compute_20220104_models.GetStorageSummaryComparedRequest,
    ) -> max_compute_20220104_models.GetStorageSummaryComparedResponse:
        """
        @param request: GetStorageSummaryComparedRequest
        @return: GetStorageSummaryComparedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_storage_summary_compared_with_options(type, request, headers, runtime)

    async def get_storage_summary_compared_async(
        self,
        type: str,
        request: max_compute_20220104_models.GetStorageSummaryComparedRequest,
    ) -> max_compute_20220104_models.GetStorageSummaryComparedResponse:
        """
        @param request: GetStorageSummaryComparedRequest
        @return: GetStorageSummaryComparedResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_storage_summary_compared_with_options_async(type, request, headers, runtime)

    def get_table_info_with_options(
        self,
        project_name: str,
        table_name: str,
        request: max_compute_20220104_models.GetTableInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTableInfoResponse:
        """
        @summary Views the information about MaxCompute internal tables, views, external tables, clustered tables, or transactional tables.
        
        @param request: GetTableInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTableInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_info_with_options_async(
        self,
        project_name: str,
        table_name: str,
        request: max_compute_20220104_models.GetTableInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTableInfoResponse:
        """
        @summary Views the information about MaxCompute internal tables, views, external tables, clustered tables, or transactional tables.
        
        @param request: GetTableInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTableInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTableInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_info(
        self,
        project_name: str,
        table_name: str,
        request: max_compute_20220104_models.GetTableInfoRequest,
    ) -> max_compute_20220104_models.GetTableInfoResponse:
        """
        @summary Views the information about MaxCompute internal tables, views, external tables, clustered tables, or transactional tables.
        
        @param request: GetTableInfoRequest
        @return: GetTableInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_info_with_options(project_name, table_name, request, headers, runtime)

    async def get_table_info_async(
        self,
        project_name: str,
        table_name: str,
        request: max_compute_20220104_models.GetTableInfoRequest,
    ) -> max_compute_20220104_models.GetTableInfoResponse:
        """
        @summary Views the information about MaxCompute internal tables, views, external tables, clustered tables, or transactional tables.
        
        @param request: GetTableInfoRequest
        @return: GetTableInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_info_with_options_async(project_name, table_name, request, headers, runtime)

    def get_trusted_projects_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        """
        @summary Obtains the trusted projects of the current project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrustedProjectsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrustedProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/trustedProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTrustedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trusted_projects_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        """
        @summary Obtains the trusted projects of the current project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrustedProjectsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTrustedProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/trustedProjects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.GetTrustedProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trusted_projects(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        """
        @summary Obtains the trusted projects of the current project.
        
        @return: GetTrustedProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_trusted_projects_with_options(project_name, headers, runtime)

    async def get_trusted_projects_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.GetTrustedProjectsResponse:
        """
        @summary Obtains the trusted projects of the current project.
        
        @return: GetTrustedProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_trusted_projects_with_options_async(project_name, headers, runtime)

    def kill_jobs_with_options(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.KillJobsResponse:
        """
        @summary Terminates a running job.
        
        @param request: KillJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='KillJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/kill',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.KillJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_jobs_with_options_async(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.KillJobsResponse:
        """
        @summary Terminates a running job.
        
        @param request: KillJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='KillJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/kill',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.KillJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_jobs(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
    ) -> max_compute_20220104_models.KillJobsResponse:
        """
        @summary Terminates a running job.
        
        @param request: KillJobsRequest
        @return: KillJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.kill_jobs_with_options(request, headers, runtime)

    async def kill_jobs_async(
        self,
        request: max_compute_20220104_models.KillJobsRequest,
    ) -> max_compute_20220104_models.KillJobsResponse:
        """
        @summary Terminates a running job.
        
        @param request: KillJobsRequest
        @return: KillJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.kill_jobs_with_options_async(request, headers, runtime)

    def list_compute_metrics_by_instance_with_options(
        self,
        request: max_compute_20220104_models.ListComputeMetricsByInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListComputeMetricsByInstanceResponse:
        """
        @summary Get compute usage of pay-as-you-go jobs.
        
        @param request: ListComputeMetricsByInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeMetricsByInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_owner):
            body['jobOwner'] = request.job_owner
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_names):
            body['projectNames'] = request.project_names
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.spec_codes):
            body['specCodes'] = request.spec_codes
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            body['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComputeMetricsByInstance',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/computeMetrics/listByInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListComputeMetricsByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_metrics_by_instance_with_options_async(
        self,
        request: max_compute_20220104_models.ListComputeMetricsByInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListComputeMetricsByInstanceResponse:
        """
        @summary Get compute usage of pay-as-you-go jobs.
        
        @param request: ListComputeMetricsByInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeMetricsByInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_owner):
            body['jobOwner'] = request.job_owner
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_names):
            body['projectNames'] = request.project_names
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.signature):
            body['signature'] = request.signature
        if not UtilClient.is_unset(request.spec_codes):
            body['specCodes'] = request.spec_codes
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            body['types'] = request.types
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComputeMetricsByInstance',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/computeMetrics/listByInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListComputeMetricsByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_metrics_by_instance(
        self,
        request: max_compute_20220104_models.ListComputeMetricsByInstanceRequest,
    ) -> max_compute_20220104_models.ListComputeMetricsByInstanceResponse:
        """
        @summary Get compute usage of pay-as-you-go jobs.
        
        @param request: ListComputeMetricsByInstanceRequest
        @return: ListComputeMetricsByInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_compute_metrics_by_instance_with_options(request, headers, runtime)

    async def list_compute_metrics_by_instance_async(
        self,
        request: max_compute_20220104_models.ListComputeMetricsByInstanceRequest,
    ) -> max_compute_20220104_models.ListComputeMetricsByInstanceResponse:
        """
        @summary Get compute usage of pay-as-you-go jobs.
        
        @param request: ListComputeMetricsByInstanceRequest
        @return: ListComputeMetricsByInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_compute_metrics_by_instance_with_options_async(request, headers, runtime)

    def list_compute_quota_plan_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListComputeQuotaPlanResponse:
        """
        @summary Get computeQuotaPlan list.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListComputeQuotaPlanResponse:
        """
        @summary Get computeQuotaPlan list.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComputeQuotaPlanResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_quota_plan(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.ListComputeQuotaPlanResponse:
        """
        @summary Get computeQuotaPlan list.
        
        @return: ListComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_compute_quota_plan_with_options(nickname, headers, runtime)

    async def list_compute_quota_plan_async(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.ListComputeQuotaPlanResponse:
        """
        @summary Get computeQuotaPlan list.
        
        @return: ListComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_compute_quota_plan_with_options_async(nickname, headers, runtime)

    def list_functions_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        """
        @summary Obtains functions in a MaxCompute project.
        
        @param request: ListFunctionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        """
        @summary Obtains functions in a MaxCompute project.
        
        @param request: ListFunctionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFunctionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFunctions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/functions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        """
        @summary Obtains functions in a MaxCompute project.
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(project_name, request, headers, runtime)

    async def list_functions_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListFunctionsRequest,
    ) -> max_compute_20220104_models.ListFunctionsResponse:
        """
        @summary Obtains functions in a MaxCompute project.
        
        @param request: ListFunctionsRequest
        @return: ListFunctionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(project_name, request, headers, runtime)

    def list_job_infos_with_options(
        self,
        request: max_compute_20220104_models.ListJobInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobInfosResponse:
        """
        @summary Views a list of jobs.
        
        @param request: ListJobInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not UtilClient.is_unset(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not UtilClient.is_unset(request.priority_list):
            body['priorityList'] = request.priority_list
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.scene_tag_list):
            body['sceneTagList'] = request.scene_tag_list
        if not UtilClient.is_unset(request.signature_list):
            body['signatureList'] = request.signature_list
        if not UtilClient.is_unset(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not UtilClient.is_unset(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobInfos',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_infos_with_options_async(
        self,
        request: max_compute_20220104_models.ListJobInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobInfosResponse:
        """
        @summary Views a list of jobs.
        
        @param request: ListJobInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not UtilClient.is_unset(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not UtilClient.is_unset(request.priority_list):
            body['priorityList'] = request.priority_list
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.scene_tag_list):
            body['sceneTagList'] = request.scene_tag_list
        if not UtilClient.is_unset(request.signature_list):
            body['signatureList'] = request.signature_list
        if not UtilClient.is_unset(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not UtilClient.is_unset(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobInfos',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_infos(
        self,
        request: max_compute_20220104_models.ListJobInfosRequest,
    ) -> max_compute_20220104_models.ListJobInfosResponse:
        """
        @summary Views a list of jobs.
        
        @param request: ListJobInfosRequest
        @return: ListJobInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_infos_with_options(request, headers, runtime)

    async def list_job_infos_async(
        self,
        request: max_compute_20220104_models.ListJobInfosRequest,
    ) -> max_compute_20220104_models.ListJobInfosResponse:
        """
        @summary Views a list of jobs.
        
        @param request: ListJobInfosRequest
        @return: ListJobInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_infos_with_options_async(request, headers, runtime)

    def list_job_metric_with_options(
        self,
        request: max_compute_20220104_models.ListJobMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobMetricResponse:
        """
        @summary Retrieve performance metrics for completed jobs.
        
        @param request: ListJobMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.group):
            body['group'] = request.group
        if not UtilClient.is_unset(request.metric):
            body['metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/metric',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_metric_with_options_async(
        self,
        request: max_compute_20220104_models.ListJobMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobMetricResponse:
        """
        @summary Retrieve performance metrics for completed jobs.
        
        @param request: ListJobMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.group):
            body['group'] = request.group
        if not UtilClient.is_unset(request.metric):
            body['metric'] = request.metric
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/metric',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_metric(
        self,
        request: max_compute_20220104_models.ListJobMetricRequest,
    ) -> max_compute_20220104_models.ListJobMetricResponse:
        """
        @summary Retrieve performance metrics for completed jobs.
        
        @param request: ListJobMetricRequest
        @return: ListJobMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_metric_with_options(request, headers, runtime)

    async def list_job_metric_async(
        self,
        request: max_compute_20220104_models.ListJobMetricRequest,
    ) -> max_compute_20220104_models.ListJobMetricResponse:
        """
        @summary Retrieve performance metrics for completed jobs.
        
        @param request: ListJobMetricRequest
        @return: ListJobMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_metric_with_options_async(request, headers, runtime)

    def list_job_snapshot_infos_with_options(
        self,
        request: max_compute_20220104_models.ListJobSnapshotInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobSnapshotInfosResponse:
        """
        @summary Views a list of job snapshot data at a specific point in time.
        
        @param request: ListJobSnapshotInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobSnapshotInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not UtilClient.is_unset(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not UtilClient.is_unset(request.priority_list):
            body['priorityList'] = request.priority_list
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.signature_list):
            body['signatureList'] = request.signature_list
        if not UtilClient.is_unset(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not UtilClient.is_unset(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobSnapshotInfos',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/snapshot',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobSnapshotInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_snapshot_infos_with_options_async(
        self,
        request: max_compute_20220104_models.ListJobSnapshotInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListJobSnapshotInfosResponse:
        """
        @summary Views a list of job snapshot data at a specific point in time.
        
        @param request: ListJobSnapshotInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobSnapshotInfosResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not UtilClient.is_unset(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not UtilClient.is_unset(request.priority_list):
            body['priorityList'] = request.priority_list
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.signature_list):
            body['signatureList'] = request.signature_list
        if not UtilClient.is_unset(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not UtilClient.is_unset(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not UtilClient.is_unset(request.status_list):
            body['statusList'] = request.status_list
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListJobSnapshotInfos',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/jobs/snapshot',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListJobSnapshotInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_snapshot_infos(
        self,
        request: max_compute_20220104_models.ListJobSnapshotInfosRequest,
    ) -> max_compute_20220104_models.ListJobSnapshotInfosResponse:
        """
        @summary Views a list of job snapshot data at a specific point in time.
        
        @param request: ListJobSnapshotInfosRequest
        @return: ListJobSnapshotInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_job_snapshot_infos_with_options(request, headers, runtime)

    async def list_job_snapshot_infos_async(
        self,
        request: max_compute_20220104_models.ListJobSnapshotInfosRequest,
    ) -> max_compute_20220104_models.ListJobSnapshotInfosResponse:
        """
        @summary Views a list of job snapshot data at a specific point in time.
        
        @param request: ListJobSnapshotInfosRequest
        @return: ListJobSnapshotInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_job_snapshot_infos_with_options_async(request, headers, runtime)

    def list_mms_data_sources_with_options(
        self,
        request: max_compute_20220104_models.ListMmsDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsDataSourcesResponse:
        """
        @summary ListMmsDataSources
        
        @param request: ListMmsDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsDataSources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_data_sources_with_options_async(
        self,
        request: max_compute_20220104_models.ListMmsDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsDataSourcesResponse:
        """
        @summary ListMmsDataSources
        
        @param request: ListMmsDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsDataSources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_data_sources(
        self,
        request: max_compute_20220104_models.ListMmsDataSourcesRequest,
    ) -> max_compute_20220104_models.ListMmsDataSourcesResponse:
        """
        @summary ListMmsDataSources
        
        @param request: ListMmsDataSourcesRequest
        @return: ListMmsDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_data_sources_with_options(request, headers, runtime)

    async def list_mms_data_sources_async(
        self,
        request: max_compute_20220104_models.ListMmsDataSourcesRequest,
    ) -> max_compute_20220104_models.ListMmsDataSourcesResponse:
        """
        @summary ListMmsDataSources
        
        @param request: ListMmsDataSourcesRequest
        @return: ListMmsDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_data_sources_with_options_async(request, headers, runtime)

    def list_mms_dbs_with_options(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsDbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsDbsResponse:
        """
        @summary 获取一个数据源内“库”列表
        
        @param tmp_req: ListMmsDbsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsDbsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsDbsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sorter):
            request.sorter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sorter, 'sorter', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sorter_shrink):
            query['sorter'] = request.sorter_shrink
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsDbs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/dbs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_dbs_with_options_async(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsDbsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsDbsResponse:
        """
        @summary 获取一个数据源内“库”列表
        
        @param tmp_req: ListMmsDbsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsDbsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsDbsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sorter):
            request.sorter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sorter, 'sorter', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.sorter_shrink):
            query['sorter'] = request.sorter_shrink
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsDbs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/dbs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_dbs(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsDbsRequest,
    ) -> max_compute_20220104_models.ListMmsDbsResponse:
        """
        @summary 获取一个数据源内“库”列表
        
        @param request: ListMmsDbsRequest
        @return: ListMmsDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_dbs_with_options(source_id, request, headers, runtime)

    async def list_mms_dbs_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsDbsRequest,
    ) -> max_compute_20220104_models.ListMmsDbsResponse:
        """
        @summary 获取一个数据源内“库”列表
        
        @param request: ListMmsDbsRequest
        @return: ListMmsDbsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_dbs_with_options_async(source_id, request, headers, runtime)

    def list_mms_jobs_with_options(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsJobsResponse:
        """
        @summary ListMmsJobs
        
        @param request: ListMmsJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.stopped):
            query['stopped'] = request.stopped
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_jobs_with_options_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsJobsResponse:
        """
        @summary ListMmsJobs
        
        @param request: ListMmsJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.stopped):
            query['stopped'] = request.stopped
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsJobs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_jobs(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsJobsRequest,
    ) -> max_compute_20220104_models.ListMmsJobsResponse:
        """
        @summary ListMmsJobs
        
        @param request: ListMmsJobsRequest
        @return: ListMmsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_jobs_with_options(source_id, request, headers, runtime)

    async def list_mms_jobs_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsJobsRequest,
    ) -> max_compute_20220104_models.ListMmsJobsResponse:
        """
        @summary ListMmsJobs
        
        @param request: ListMmsJobsRequest
        @return: ListMmsJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_jobs_with_options_async(source_id, request, headers, runtime)

    def list_mms_partitions_with_options(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsPartitionsResponse:
        """
        @summary 获取元数据-分区
        
        @param tmp_req: ListMmsPartitionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsPartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsPartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['dbId'] = request.db_id
        if not UtilClient.is_unset(request.db_name):
            query['dbName'] = request.db_name
        if not UtilClient.is_unset(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not UtilClient.is_unset(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_shrink):
            query['status'] = request.status_shrink
        if not UtilClient.is_unset(request.table_id):
            query['tableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        if not UtilClient.is_unset(request.updated):
            query['updated'] = request.updated
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsPartitions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/partitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_partitions_with_options_async(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsPartitionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsPartitionsResponse:
        """
        @summary 获取元数据-分区
        
        @param tmp_req: ListMmsPartitionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsPartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsPartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['dbId'] = request.db_id
        if not UtilClient.is_unset(request.db_name):
            query['dbName'] = request.db_name
        if not UtilClient.is_unset(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not UtilClient.is_unset(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_shrink):
            query['status'] = request.status_shrink
        if not UtilClient.is_unset(request.table_id):
            query['tableId'] = request.table_id
        if not UtilClient.is_unset(request.table_name):
            query['tableName'] = request.table_name
        if not UtilClient.is_unset(request.updated):
            query['updated'] = request.updated
        if not UtilClient.is_unset(request.value):
            query['value'] = request.value
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsPartitions',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/partitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_partitions(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsPartitionsRequest,
    ) -> max_compute_20220104_models.ListMmsPartitionsResponse:
        """
        @summary 获取元数据-分区
        
        @param request: ListMmsPartitionsRequest
        @return: ListMmsPartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_partitions_with_options(source_id, request, headers, runtime)

    async def list_mms_partitions_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsPartitionsRequest,
    ) -> max_compute_20220104_models.ListMmsPartitionsResponse:
        """
        @summary 获取元数据-分区
        
        @param request: ListMmsPartitionsRequest
        @return: ListMmsPartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_partitions_with_options_async(source_id, request, headers, runtime)

    def list_mms_tables_with_options(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTablesResponse:
        """
        @summary ListMmsTables
        
        @param tmp_req: ListMmsTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTablesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['dbId'] = request.db_id
        if not UtilClient.is_unset(request.db_name):
            query['dbName'] = request.db_name
        if not UtilClient.is_unset(request.dst_name):
            query['dstName'] = request.dst_name
        if not UtilClient.is_unset(request.dst_project_name):
            query['dstProjectName'] = request.dst_project_name
        if not UtilClient.is_unset(request.dst_schema_name):
            query['dstSchemaName'] = request.dst_schema_name
        if not UtilClient.is_unset(request.has_partitions):
            query['hasPartitions'] = request.has_partitions
        if not UtilClient.is_unset(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not UtilClient.is_unset(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.only_name):
            query['onlyName'] = request.only_name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_shrink):
            query['status'] = request.status_shrink
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_tables_with_options_async(
        self,
        source_id: str,
        tmp_req: max_compute_20220104_models.ListMmsTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTablesResponse:
        """
        @summary ListMmsTables
        
        @param tmp_req: ListMmsTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTablesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListMmsTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not UtilClient.is_unset(request.db_id):
            query['dbId'] = request.db_id
        if not UtilClient.is_unset(request.db_name):
            query['dbName'] = request.db_name
        if not UtilClient.is_unset(request.dst_name):
            query['dstName'] = request.dst_name
        if not UtilClient.is_unset(request.dst_project_name):
            query['dstProjectName'] = request.dst_project_name
        if not UtilClient.is_unset(request.dst_schema_name):
            query['dstSchemaName'] = request.dst_schema_name
        if not UtilClient.is_unset(request.has_partitions):
            query['hasPartitions'] = request.has_partitions
        if not UtilClient.is_unset(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not UtilClient.is_unset(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.only_name):
            query['onlyName'] = request.only_name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_shrink):
            query['status'] = request.status_shrink
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_tables(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTablesRequest,
    ) -> max_compute_20220104_models.ListMmsTablesResponse:
        """
        @summary ListMmsTables
        
        @param request: ListMmsTablesRequest
        @return: ListMmsTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_tables_with_options(source_id, request, headers, runtime)

    async def list_mms_tables_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTablesRequest,
    ) -> max_compute_20220104_models.ListMmsTablesResponse:
        """
        @summary ListMmsTables
        
        @param request: ListMmsTablesRequest
        @return: ListMmsTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_tables_with_options_async(source_id, request, headers, runtime)

    def list_mms_task_logs_with_options(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTaskLogsResponse:
        """
        @summary ListMmsTaskLogs
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTaskLogsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMmsTaskLogs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_task_logs_with_options_async(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTaskLogsResponse:
        """
        @summary ListMmsTaskLogs
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTaskLogsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListMmsTaskLogs',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_task_logs(
        self,
        source_id: str,
        task_id: str,
    ) -> max_compute_20220104_models.ListMmsTaskLogsResponse:
        """
        @summary ListMmsTaskLogs
        
        @return: ListMmsTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_task_logs_with_options(source_id, task_id, headers, runtime)

    async def list_mms_task_logs_async(
        self,
        source_id: str,
        task_id: str,
    ) -> max_compute_20220104_models.ListMmsTaskLogsResponse:
        """
        @summary ListMmsTaskLogs
        
        @return: ListMmsTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_task_logs_with_options_async(source_id, task_id, headers, runtime)

    def list_mms_tasks_with_options(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTasksResponse:
        """
        @summary ListMmsTasks
        
        @param request: ListMmsTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.job_name):
            query['jobName'] = request.job_name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        if not UtilClient.is_unset(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsTasks',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_tasks_with_options_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListMmsTasksResponse:
        """
        @summary ListMmsTasks
        
        @param request: ListMmsTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMmsTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not UtilClient.is_unset(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not UtilClient.is_unset(request.job_id):
            query['jobId'] = request.job_id
        if not UtilClient.is_unset(request.job_name):
            query['jobName'] = request.job_name
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        if not UtilClient.is_unset(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not UtilClient.is_unset(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMmsTasks',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListMmsTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_tasks(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTasksRequest,
    ) -> max_compute_20220104_models.ListMmsTasksResponse:
        """
        @summary ListMmsTasks
        
        @param request: ListMmsTasksRequest
        @return: ListMmsTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mms_tasks_with_options(source_id, request, headers, runtime)

    async def list_mms_tasks_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.ListMmsTasksRequest,
    ) -> max_compute_20220104_models.ListMmsTasksResponse:
        """
        @summary ListMmsTasks
        
        @param request: ListMmsTasksRequest
        @return: ListMmsTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mms_tasks_with_options_async(source_id, request, headers, runtime)

    def list_packages_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        """
        @summary Queries the packages in a MaxCompute project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPackagesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPackages',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_packages_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        """
        @summary Queries the packages in a MaxCompute project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPackagesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPackages',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_packages(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        """
        @summary Queries the packages in a MaxCompute project.
        
        @return: ListPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_packages_with_options(project_name, headers, runtime)

    async def list_packages_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListPackagesResponse:
        """
        @summary Queries the packages in a MaxCompute project.
        
        @return: ListPackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_packages_with_options_async(project_name, headers, runtime)

    def list_project_users_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        """
        @summary Queries a list of users in a project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectUsersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_users_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        """
        @summary Queries a list of users in a project.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectUsersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_users(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        """
        @summary Queries a list of users in a project.
        
        @return: ListProjectUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_users_with_options(project_name, headers, runtime)

    async def list_project_users_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListProjectUsersResponse:
        """
        @summary Queries a list of users in a project.
        
        @return: ListProjectUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_users_with_options_async(project_name, headers, runtime)

    def list_projects_with_options(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        """
        @summary Queries a list of MaxCompute projects.
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_system_catalog):
            query['listSystemCatalog'] = request.list_system_catalog
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.quota_name):
            query['quotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        """
        @summary Queries a list of MaxCompute projects.
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.list_system_catalog):
            query['listSystemCatalog'] = request.list_system_catalog
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.quota_name):
            query['quotaName'] = request.quota_name
        if not UtilClient.is_unset(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        """
        @summary Queries a list of MaxCompute projects.
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: max_compute_20220104_models.ListProjectsRequest,
    ) -> max_compute_20220104_models.ListProjectsResponse:
        """
        @summary Queries a list of MaxCompute projects.
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        """
        @summary Queries quotas.
        
        @param request: ListQuotasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        """
        @summary Queries quotas.
        
        @param request: ListQuotasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_type):
            query['billingType'] = request.billing_type
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.product_id):
            query['productId'] = request.product_id
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotas',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        """
        @summary Queries quotas.
        
        @param request: ListQuotasRequest
        @return: ListQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: max_compute_20220104_models.ListQuotasRequest,
    ) -> max_compute_20220104_models.ListQuotasResponse:
        """
        @summary Queries quotas.
        
        @param request: ListQuotasRequest
        @return: ListQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_quotas_plans_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        """
        @summary Obtains quota plans.
        
        @param request: ListQuotasPlansRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotasPlans',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_plans_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        """
        @summary Obtains quota plans.
        
        @param request: ListQuotasPlansRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQuotasPlansResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQuotasPlans',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListQuotasPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas_plans(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        """
        @summary Obtains quota plans.
        
        @param request: ListQuotasPlansRequest
        @return: ListQuotasPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_quotas_plans_with_options(nickname, request, headers, runtime)

    async def list_quotas_plans_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.ListQuotasPlansRequest,
    ) -> max_compute_20220104_models.ListQuotasPlansResponse:
        """
        @summary Obtains quota plans.
        
        @param request: ListQuotasPlansRequest
        @return: ListQuotasPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_quotas_plans_with_options_async(nickname, request, headers, runtime)

    def list_resources_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        """
        @summary Obtains resources in a MaxCompute project.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        """
        @summary Obtains resources in a MaxCompute project.
        
        @param request: ListResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        """
        @summary Obtains resources in a MaxCompute project.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(project_name, request, headers, runtime)

    async def list_resources_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListResourcesRequest,
    ) -> max_compute_20220104_models.ListResourcesResponse:
        """
        @summary Obtains resources in a MaxCompute project.
        
        @param request: ListResourcesRequest
        @return: ListResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(project_name, request, headers, runtime)

    def list_roles_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListRolesResponse:
        """
        @summary Obtains MaxCompute project-level roles.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListRolesResponse:
        """
        @summary Obtains MaxCompute project-level roles.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRolesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListRolesResponse:
        """
        @summary Obtains MaxCompute project-level roles.
        
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(project_name, headers, runtime)

    async def list_roles_async(
        self,
        project_name: str,
    ) -> max_compute_20220104_models.ListRolesResponse:
        """
        @summary Obtains MaxCompute project-level roles.
        
        @return: ListRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(project_name, headers, runtime)

    def list_storage_partitions_info_with_options(
        self,
        project: str,
        table: str,
        tmp_req: max_compute_20220104_models.ListStoragePartitionsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStoragePartitionsInfoResponse:
        """
        @summary Queries the storage details of a specific partition in a partitioned table in a MaxCompute project.
        
        @param tmp_req: ListStoragePartitionsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStoragePartitionsInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListStoragePartitionsInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'types', 'json')
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition_prefix):
            query['partitionPrefix'] = request.partition_prefix
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.schema):
            query['schema'] = request.schema
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStoragePartitionsInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projects/{OpenApiUtilClient.get_encode_param(project)}/tables/{OpenApiUtilClient.get_encode_param(table)}/partitionsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStoragePartitionsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_partitions_info_with_options_async(
        self,
        project: str,
        table: str,
        tmp_req: max_compute_20220104_models.ListStoragePartitionsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStoragePartitionsInfoResponse:
        """
        @summary Queries the storage details of a specific partition in a partitioned table in a MaxCompute project.
        
        @param tmp_req: ListStoragePartitionsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStoragePartitionsInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListStoragePartitionsInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'types', 'json')
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition_prefix):
            query['partitionPrefix'] = request.partition_prefix
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.schema):
            query['schema'] = request.schema
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStoragePartitionsInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projects/{OpenApiUtilClient.get_encode_param(project)}/tables/{OpenApiUtilClient.get_encode_param(table)}/partitionsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStoragePartitionsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_partitions_info(
        self,
        project: str,
        table: str,
        request: max_compute_20220104_models.ListStoragePartitionsInfoRequest,
    ) -> max_compute_20220104_models.ListStoragePartitionsInfoResponse:
        """
        @summary Queries the storage details of a specific partition in a partitioned table in a MaxCompute project.
        
        @param request: ListStoragePartitionsInfoRequest
        @return: ListStoragePartitionsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_storage_partitions_info_with_options(project, table, request, headers, runtime)

    async def list_storage_partitions_info_async(
        self,
        project: str,
        table: str,
        request: max_compute_20220104_models.ListStoragePartitionsInfoRequest,
    ) -> max_compute_20220104_models.ListStoragePartitionsInfoResponse:
        """
        @summary Queries the storage details of a specific partition in a partitioned table in a MaxCompute project.
        
        @param request: ListStoragePartitionsInfoRequest
        @return: ListStoragePartitionsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_storage_partitions_info_with_options_async(project, table, request, headers, runtime)

    def list_storage_projects_info_with_options(
        self,
        request: max_compute_20220104_models.ListStorageProjectsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStorageProjectsInfoResponse:
        """
        @param request: ListStorageProjectsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStorageProjectsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_prefix):
            query['projectPrefix'] = request.project_prefix
        if not UtilClient.is_unset(request.recent_days):
            query['recentDays'] = request.recent_days
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStorageProjectsInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projectsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStorageProjectsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_projects_info_with_options_async(
        self,
        request: max_compute_20220104_models.ListStorageProjectsInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStorageProjectsInfoResponse:
        """
        @param request: ListStorageProjectsInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStorageProjectsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_prefix):
            query['projectPrefix'] = request.project_prefix
        if not UtilClient.is_unset(request.recent_days):
            query['recentDays'] = request.recent_days
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStorageProjectsInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projectsInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStorageProjectsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_projects_info(
        self,
        request: max_compute_20220104_models.ListStorageProjectsInfoRequest,
    ) -> max_compute_20220104_models.ListStorageProjectsInfoResponse:
        """
        @param request: ListStorageProjectsInfoRequest
        @return: ListStorageProjectsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_storage_projects_info_with_options(request, headers, runtime)

    async def list_storage_projects_info_async(
        self,
        request: max_compute_20220104_models.ListStorageProjectsInfoRequest,
    ) -> max_compute_20220104_models.ListStorageProjectsInfoResponse:
        """
        @param request: ListStorageProjectsInfoRequest
        @return: ListStorageProjectsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_storage_projects_info_with_options_async(request, headers, runtime)

    def list_storage_tables_info_with_options(
        self,
        project: str,
        tmp_req: max_compute_20220104_models.ListStorageTablesInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStorageTablesInfoResponse:
        """
        @summary Queries the table storage details of a MaxCompute project.
        
        @param tmp_req: ListStorageTablesInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStorageTablesInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListStorageTablesInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'types', 'simple')
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.recent_days):
            query['recentDays'] = request.recent_days
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.schema):
            query['schema'] = request.schema
        if not UtilClient.is_unset(request.table_prefix):
            query['tablePrefix'] = request.table_prefix
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStorageTablesInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projects/{OpenApiUtilClient.get_encode_param(project)}/tablesInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStorageTablesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_tables_info_with_options_async(
        self,
        project: str,
        tmp_req: max_compute_20220104_models.ListStorageTablesInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListStorageTablesInfoResponse:
        """
        @summary Queries the table storage details of a MaxCompute project.
        
        @param tmp_req: ListStorageTablesInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStorageTablesInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = max_compute_20220104_models.ListStorageTablesInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'types', 'simple')
        query = {}
        if not UtilClient.is_unset(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.date):
            query['date'] = request.date
        if not UtilClient.is_unset(request.order_column):
            query['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.recent_days):
            query['recentDays'] = request.recent_days
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.schema):
            query['schema'] = request.schema
        if not UtilClient.is_unset(request.table_prefix):
            query['tablePrefix'] = request.table_prefix
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStorageTablesInfo',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/analysis/storage/projects/{OpenApiUtilClient.get_encode_param(project)}/tablesInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListStorageTablesInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_tables_info(
        self,
        project: str,
        request: max_compute_20220104_models.ListStorageTablesInfoRequest,
    ) -> max_compute_20220104_models.ListStorageTablesInfoResponse:
        """
        @summary Queries the table storage details of a MaxCompute project.
        
        @param request: ListStorageTablesInfoRequest
        @return: ListStorageTablesInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_storage_tables_info_with_options(project, request, headers, runtime)

    async def list_storage_tables_info_async(
        self,
        project: str,
        request: max_compute_20220104_models.ListStorageTablesInfoRequest,
    ) -> max_compute_20220104_models.ListStorageTablesInfoResponse:
        """
        @summary Queries the table storage details of a MaxCompute project.
        
        @param request: ListStorageTablesInfoRequest
        @return: ListStorageTablesInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_storage_tables_info_with_options_async(project, request, headers, runtime)

    def list_tables_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTablesResponse:
        """
        @summary Obtains tables in a MaxCompute project.
        
        @param request: ListTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTablesResponse:
        """
        @summary Obtains tables in a MaxCompute project.
        
        @param request: ListTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['marker'] = request.marker
        if not UtilClient.is_unset(request.max_item):
            query['maxItem'] = request.max_item
        if not UtilClient.is_unset(request.prefix):
            query['prefix'] = request.prefix
        if not UtilClient.is_unset(request.schema_name):
            query['schemaName'] = request.schema_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
    ) -> max_compute_20220104_models.ListTablesResponse:
        """
        @summary Obtains tables in a MaxCompute project.
        
        @param request: ListTablesRequest
        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(project_name, request, headers, runtime)

    async def list_tables_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.ListTablesRequest,
    ) -> max_compute_20220104_models.ListTablesResponse:
        """
        @summary Obtains tables in a MaxCompute project.
        
        @param request: ListTablesRequest
        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(project_name, request, headers, runtime)

    def list_tunnel_quota_timer_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTunnelQuotaTimerResponse:
        """
        @summary Displays the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTunnelQuotaTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTunnelQuotaTimer',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/tunnel/{OpenApiUtilClient.get_encode_param(nickname)}/timers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTunnelQuotaTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tunnel_quota_timer_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListTunnelQuotaTimerResponse:
        """
        @summary Displays the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTunnelQuotaTimerResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTunnelQuotaTimer',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/tunnel/{OpenApiUtilClient.get_encode_param(nickname)}/timers',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListTunnelQuotaTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tunnel_quota_timer(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.ListTunnelQuotaTimerResponse:
        """
        @summary Displays the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @return: ListTunnelQuotaTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tunnel_quota_timer_with_options(nickname, headers, runtime)

    async def list_tunnel_quota_timer_async(
        self,
        nickname: str,
    ) -> max_compute_20220104_models.ListTunnelQuotaTimerResponse:
        """
        @summary Displays the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @return: ListTunnelQuotaTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tunnel_quota_timer_with_options_async(nickname, headers, runtime)

    def list_users_with_options(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersResponse:
        """
        @summary Queries a list of all users under a tenant.
        
        @param request: ListUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersResponse:
        """
        @summary Queries a list of all users under a tenant.
        
        @param request: ListUsersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
    ) -> max_compute_20220104_models.ListUsersResponse:
        """
        @summary Queries a list of all users under a tenant.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: max_compute_20220104_models.ListUsersRequest,
    ) -> max_compute_20220104_models.ListUsersResponse:
        """
        @summary Queries a list of all users under a tenant.
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def list_users_by_role_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        """
        @summary Obtains information about the users who are assigned a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersByRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsersByRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersByRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_by_role_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        """
        @summary Obtains information about the users who are assigned a project-level role.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersByRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListUsersByRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.ListUsersByRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_by_role(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        """
        @summary Obtains information about the users who are assigned a project-level role.
        
        @return: ListUsersByRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_by_role_with_options(project_name, role_name, headers, runtime)

    async def list_users_by_role_async(
        self,
        project_name: str,
        role_name: str,
    ) -> max_compute_20220104_models.ListUsersByRoleResponse:
        """
        @summary Obtains information about the users who are assigned a project-level role.
        
        @return: ListUsersByRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_by_role_with_options_async(project_name, role_name, headers, runtime)

    def query_quota_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.QueryQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryQuotaResponse:
        """
        @summary Queries the information about a specified level-1 quota group.
        
        @param request: QueryQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_quota_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.QueryQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryQuotaResponse:
        """
        @summary Queries the information about a specified level-1 quota group.
        
        @param request: QueryQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not UtilClient.is_unset(request.mock):
            query['mock'] = request.mock
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_quota(
        self,
        nickname: str,
        request: max_compute_20220104_models.QueryQuotaRequest,
    ) -> max_compute_20220104_models.QueryQuotaResponse:
        """
        @summary Queries the information about a specified level-1 quota group.
        
        @param request: QueryQuotaRequest
        @return: QueryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_quota_with_options(nickname, request, headers, runtime)

    async def query_quota_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.QueryQuotaRequest,
    ) -> max_compute_20220104_models.QueryQuotaResponse:
        """
        @summary Queries the information about a specified level-1 quota group.
        
        @param request: QueryQuotaRequest
        @return: QueryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_quota_with_options_async(nickname, request, headers, runtime)

    def query_quota_metric_with_options(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryQuotaMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryQuotaMetricResponse:
        """
        @summary 查询quota的资源使用信息
        
        @param request: QueryQuotaMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQuotaMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not UtilClient.is_unset(request.interval):
            body['interval'] = request.interval
        if not UtilClient.is_unset(request.nickname):
            body['nickname'] = request.nickname
        if not UtilClient.is_unset(request.sub_quota_nickname):
            body['subQuotaNickname'] = request.sub_quota_nickname
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryQuotaMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/quota/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryQuotaMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_quota_metric_with_options_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryQuotaMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryQuotaMetricResponse:
        """
        @summary 查询quota的资源使用信息
        
        @param request: QueryQuotaMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryQuotaMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not UtilClient.is_unset(request.interval):
            body['interval'] = request.interval
        if not UtilClient.is_unset(request.nickname):
            body['nickname'] = request.nickname
        if not UtilClient.is_unset(request.sub_quota_nickname):
            body['subQuotaNickname'] = request.sub_quota_nickname
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryQuotaMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/quota/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryQuotaMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_quota_metric(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryQuotaMetricRequest,
    ) -> max_compute_20220104_models.QueryQuotaMetricResponse:
        """
        @summary 查询quota的资源使用信息
        
        @param request: QueryQuotaMetricRequest
        @return: QueryQuotaMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_quota_metric_with_options(metric, request, headers, runtime)

    async def query_quota_metric_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryQuotaMetricRequest,
    ) -> max_compute_20220104_models.QueryQuotaMetricResponse:
        """
        @summary 查询quota的资源使用信息
        
        @param request: QueryQuotaMetricRequest
        @return: QueryQuotaMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_quota_metric_with_options_async(metric, request, headers, runtime)

    def query_storage_metric_with_options(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryStorageMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryStorageMetricResponse:
        """
        @summary 查看存储数据的时序指标
        
        @param request: QueryStorageMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStorageMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStorageMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/storage/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryStorageMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_storage_metric_with_options_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryStorageMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryStorageMetricResponse:
        """
        @summary 查看存储数据的时序指标
        
        @param request: QueryStorageMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStorageMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.project_list):
            body['projectList'] = request.project_list
        if not UtilClient.is_unset(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStorageMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/storage/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryStorageMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_storage_metric(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryStorageMetricRequest,
    ) -> max_compute_20220104_models.QueryStorageMetricResponse:
        """
        @summary 查看存储数据的时序指标
        
        @param request: QueryStorageMetricRequest
        @return: QueryStorageMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_storage_metric_with_options(metric, request, headers, runtime)

    async def query_storage_metric_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryStorageMetricRequest,
    ) -> max_compute_20220104_models.QueryStorageMetricResponse:
        """
        @summary 查看存储数据的时序指标
        
        @param request: QueryStorageMetricRequest
        @return: QueryStorageMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_storage_metric_with_options_async(metric, request, headers, runtime)

    def query_tunnel_metric_with_options(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryTunnelMetricResponse:
        """
        @summary 查询tunnel资源使用信息
        
        @param request: QueryTunnelMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTunnelMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not UtilClient.is_unset(request.code_list):
            body['codeList'] = request.code_list
        if not UtilClient.is_unset(request.group_list):
            body['groupList'] = request.group_list
        if not UtilClient.is_unset(request.operation_list):
            body['operationList'] = request.operation_list
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.table_list):
            body['tableList'] = request.table_list
        if not UtilClient.is_unset(request.top_n):
            body['topN'] = request.top_n
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTunnelMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/tunnel/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryTunnelMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tunnel_metric_with_options_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryTunnelMetricResponse:
        """
        @summary 查询tunnel资源使用信息
        
        @param request: QueryTunnelMetricRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTunnelMetricResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not UtilClient.is_unset(request.code_list):
            body['codeList'] = request.code_list
        if not UtilClient.is_unset(request.group_list):
            body['groupList'] = request.group_list
        if not UtilClient.is_unset(request.operation_list):
            body['operationList'] = request.operation_list
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.table_list):
            body['tableList'] = request.table_list
        if not UtilClient.is_unset(request.top_n):
            body['topN'] = request.top_n
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTunnelMetric',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/tunnel/{OpenApiUtilClient.get_encode_param(metric)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryTunnelMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tunnel_metric(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricRequest,
    ) -> max_compute_20220104_models.QueryTunnelMetricResponse:
        """
        @summary 查询tunnel资源使用信息
        
        @param request: QueryTunnelMetricRequest
        @return: QueryTunnelMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_tunnel_metric_with_options(metric, request, headers, runtime)

    async def query_tunnel_metric_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricRequest,
    ) -> max_compute_20220104_models.QueryTunnelMetricResponse:
        """
        @summary 查询tunnel资源使用信息
        
        @param request: QueryTunnelMetricRequest
        @return: QueryTunnelMetricResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_tunnel_metric_with_options_async(metric, request, headers, runtime)

    def query_tunnel_metric_detail_with_options(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryTunnelMetricDetailResponse:
        """
        @summary 查询tunnel资源使用详情
        
        @param request: QueryTunnelMetricDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTunnelMetricDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.asc_order):
            body['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.group_list):
            body['groupList'] = request.group_list
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.operation_list):
            body['operationList'] = request.operation_list
        if not UtilClient.is_unset(request.order_column):
            body['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.table_list):
            body['tableList'] = request.table_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTunnelMetricDetail',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/tunnel/{OpenApiUtilClient.get_encode_param(metric)}/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryTunnelMetricDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tunnel_metric_detail_with_options_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.QueryTunnelMetricDetailResponse:
        """
        @summary 查询tunnel资源使用详情
        
        @param request: QueryTunnelMetricDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryTunnelMetricDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not UtilClient.is_unset(request.asc_order):
            body['ascOrder'] = request.asc_order
        if not UtilClient.is_unset(request.group_list):
            body['groupList'] = request.group_list
        if not UtilClient.is_unset(request.limit):
            body['limit'] = request.limit
        if not UtilClient.is_unset(request.operation_list):
            body['operationList'] = request.operation_list
        if not UtilClient.is_unset(request.order_column):
            body['orderColumn'] = request.order_column
        if not UtilClient.is_unset(request.project):
            body['project'] = request.project
        if not UtilClient.is_unset(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not UtilClient.is_unset(request.table_list):
            body['tableList'] = request.table_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTunnelMetricDetail',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/observations/tunnel/{OpenApiUtilClient.get_encode_param(metric)}/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.QueryTunnelMetricDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tunnel_metric_detail(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricDetailRequest,
    ) -> max_compute_20220104_models.QueryTunnelMetricDetailResponse:
        """
        @summary 查询tunnel资源使用详情
        
        @param request: QueryTunnelMetricDetailRequest
        @return: QueryTunnelMetricDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_tunnel_metric_detail_with_options(metric, request, headers, runtime)

    async def query_tunnel_metric_detail_async(
        self,
        metric: str,
        request: max_compute_20220104_models.QueryTunnelMetricDetailRequest,
    ) -> max_compute_20220104_models.QueryTunnelMetricDetailResponse:
        """
        @summary 查询tunnel资源使用详情
        
        @param request: QueryTunnelMetricDetailRequest
        @return: QueryTunnelMetricDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_tunnel_metric_detail_with_options_async(metric, request, headers, runtime)

    def retry_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.RetryMmsJobResponse:
        """
        @summary RetryMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/retry',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.RetryMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.RetryMmsJobResponse:
        """
        @summary RetryMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RetryMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/retry',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.RetryMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.RetryMmsJobResponse:
        """
        @summary RetryMmsJob
        
        @return: RetryMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.retry_mms_job_with_options(source_id, job_id, headers, runtime)

    async def retry_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.RetryMmsJobResponse:
        """
        @summary RetryMmsJob
        
        @return: RetryMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.retry_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def start_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.StartMmsJobResponse:
        """
        @summary StartMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.StartMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.StartMmsJobResponse:
        """
        @summary StartMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/start',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.StartMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.StartMmsJobResponse:
        """
        @summary StartMmsJob
        
        @return: StartMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_mms_job_with_options(source_id, job_id, headers, runtime)

    async def start_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.StartMmsJobResponse:
        """
        @summary StartMmsJob
        
        @return: StartMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def stop_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.StopMmsJobResponse:
        """
        @summary StopMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.StopMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.StopMmsJobResponse:
        """
        @summary StopMmsJob
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopMmsJobResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopMmsJob',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/stop',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.StopMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.StopMmsJobResponse:
        """
        @summary StopMmsJob
        
        @return: StopMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_mms_job_with_options(source_id, job_id, headers, runtime)

    async def stop_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> max_compute_20220104_models.StopMmsJobResponse:
        """
        @summary StopMmsJob
        
        @return: StopMmsJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def sum_storage_metrics_by_date_with_options(
        self,
        request: max_compute_20220104_models.SumStorageMetricsByDateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.SumStorageMetricsByDateResponse:
        """
        @param request: SumStorageMetricsByDateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SumStorageMetricsByDateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.project_names):
            body['projectNames'] = request.project_names
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.stats_type):
            body['statsType'] = request.stats_type
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SumStorageMetricsByDate',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/storageMetrics/sumByDate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.SumStorageMetricsByDateResponse(),
            self.call_api(params, req, runtime)
        )

    async def sum_storage_metrics_by_date_with_options_async(
        self,
        request: max_compute_20220104_models.SumStorageMetricsByDateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.SumStorageMetricsByDateResponse:
        """
        @param request: SumStorageMetricsByDateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SumStorageMetricsByDateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['endDate'] = request.end_date
        if not UtilClient.is_unset(request.project_names):
            body['projectNames'] = request.project_names
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.start_date):
            body['startDate'] = request.start_date
        if not UtilClient.is_unset(request.stats_type):
            body['statsType'] = request.stats_type
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SumStorageMetricsByDate',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/storageMetrics/sumByDate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.SumStorageMetricsByDateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sum_storage_metrics_by_date(
        self,
        request: max_compute_20220104_models.SumStorageMetricsByDateRequest,
    ) -> max_compute_20220104_models.SumStorageMetricsByDateResponse:
        """
        @param request: SumStorageMetricsByDateRequest
        @return: SumStorageMetricsByDateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sum_storage_metrics_by_date_with_options(request, headers, runtime)

    async def sum_storage_metrics_by_date_async(
        self,
        request: max_compute_20220104_models.SumStorageMetricsByDateRequest,
    ) -> max_compute_20220104_models.SumStorageMetricsByDateResponse:
        """
        @param request: SumStorageMetricsByDateRequest
        @return: SumStorageMetricsByDateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sum_storage_metrics_by_date_with_options_async(request, headers, runtime)

    def update_compute_quota_plan_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeQuotaPlanResponse:
        """
        @summary Update the ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeQuotaPlanResponse:
        """
        @summary Update the ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComputeQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaPlan',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_quota_plan(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateComputeQuotaPlanResponse:
        """
        @summary Update the ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaPlanRequest
        @return: UpdateComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_compute_quota_plan_with_options(nickname, request, headers, runtime)

    async def update_compute_quota_plan_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateComputeQuotaPlanResponse:
        """
        @summary Update the ComputeQuotaPlan.
        
        @description Please ensure that before using this interface, you have fully understood the <props="china">[Pricing and Charges](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Charges](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaPlanRequest
        @return: UpdateComputeQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_compute_quota_plan_with_options_async(nickname, request, headers, runtime)

    def update_compute_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeQuotaScheduleResponse:
        """
        @summary Update the time-based plan for computing quota.
        
        @description Please ensure that before using this interface, you have fully understood the<props="china">[Pricing and Billing](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Billing](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schedule_timezone):
            query['scheduleTimezone'] = request.schedule_timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateComputeQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaSchedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeQuotaScheduleResponse:
        """
        @summary Update the time-based plan for computing quota.
        
        @description Please ensure that before using this interface, you have fully understood the<props="china">[Pricing and Billing](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Billing](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schedule_timezone):
            query['scheduleTimezone'] = request.schedule_timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateComputeQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeQuotaSchedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateComputeQuotaScheduleResponse:
        """
        @summary Update the time-based plan for computing quota.
        
        @description Please ensure that before using this interface, you have fully understood the<props="china">[Pricing and Billing](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Billing](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaScheduleRequest
        @return: UpdateComputeQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_compute_quota_schedule_with_options(nickname, request, headers, runtime)

    async def update_compute_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateComputeQuotaScheduleResponse:
        """
        @summary Update the time-based plan for computing quota.
        
        @description Please ensure that before using this interface, you have fully understood the<props="china">[Pricing and Billing](https://help.aliyun.com/zh/maxcompute/product-overview/computing-pricing-1)
        <props="intl">[Pricing and Billing](https://www.alibabacloud.com/help/maxcompute/product-overview/computing-pricing-1) of MaxCompute Elastic Reserved CU.
        
        @param request: UpdateComputeQuotaScheduleRequest
        @return: UpdateComputeQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_compute_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def update_compute_sub_quota_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeSubQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeSubQuotaResponse:
        """
        @summary Update the basic configuration of the calculation quota, including adding or deleting the sub quota, modifying the basic properties of the secondary quota, and the CU configuration of the effective quota plan.
        
        @param request: UpdateComputeSubQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeSubQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_quota_info_list):
            body['subQuotaInfoList'] = request.sub_quota_info_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComputeSubQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeSubQuota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeSubQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_sub_quota_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeSubQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateComputeSubQuotaResponse:
        """
        @summary Update the basic configuration of the calculation quota, including adding or deleting the sub quota, modifying the basic properties of the secondary quota, and the CU configuration of the effective quota plan.
        
        @param request: UpdateComputeSubQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateComputeSubQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_quota_info_list):
            body['subQuotaInfoList'] = request.sub_quota_info_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateComputeSubQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/computeSubQuota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateComputeSubQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_sub_quota(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeSubQuotaRequest,
    ) -> max_compute_20220104_models.UpdateComputeSubQuotaResponse:
        """
        @summary Update the basic configuration of the calculation quota, including adding or deleting the sub quota, modifying the basic properties of the secondary quota, and the CU configuration of the effective quota plan.
        
        @param request: UpdateComputeSubQuotaRequest
        @return: UpdateComputeSubQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_compute_sub_quota_with_options(nickname, request, headers, runtime)

    async def update_compute_sub_quota_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateComputeSubQuotaRequest,
    ) -> max_compute_20220104_models.UpdateComputeSubQuotaResponse:
        """
        @summary Update the basic configuration of the calculation quota, including adding or deleting the sub quota, modifying the basic properties of the secondary quota, and the CU configuration of the effective quota plan.
        
        @param request: UpdateComputeSubQuotaRequest
        @return: UpdateComputeSubQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_compute_sub_quota_with_options_async(nickname, request, headers, runtime)

    def update_mms_data_source_with_options(
        self,
        source_id: str,
        request: max_compute_20220104_models.UpdateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateMmsDataSourceResponse:
        """
        @summary 更新数据源配置、名称，启/停数据源实例
        
        @param request: UpdateMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.test):
            body['test'] = request.test
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mms_data_source_with_options_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.UpdateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateMmsDataSourceResponse:
        """
        @summary 更新数据源配置、名称，启/停数据源实例
        
        @param request: UpdateMmsDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMmsDataSourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.test):
            body['test'] = request.test
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMmsDataSource',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/mms/datasources/{OpenApiUtilClient.get_encode_param(source_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mms_data_source(
        self,
        source_id: str,
        request: max_compute_20220104_models.UpdateMmsDataSourceRequest,
    ) -> max_compute_20220104_models.UpdateMmsDataSourceResponse:
        """
        @summary 更新数据源配置、名称，启/停数据源实例
        
        @param request: UpdateMmsDataSourceRequest
        @return: UpdateMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_mms_data_source_with_options(source_id, request, headers, runtime)

    async def update_mms_data_source_async(
        self,
        source_id: str,
        request: max_compute_20220104_models.UpdateMmsDataSourceRequest,
    ) -> max_compute_20220104_models.UpdateMmsDataSourceResponse:
        """
        @summary 更新数据源配置、名称，启/停数据源实例
        
        @param request: UpdateMmsDataSourceRequest
        @return: UpdateMmsDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_mms_data_source_with_options_async(source_id, request, headers, runtime)

    def update_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        """
        @summary Updates the objects in a package and projects in which the package can be installed.
        
        @param request: UpdatePackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePackageResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        """
        @summary Updates the objects in a package and projects in which the package can be installed.
        
        @param request: UpdatePackageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePackageResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdatePackage',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/packages/{OpenApiUtilClient.get_encode_param(package_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_package(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        """
        @summary Updates the objects in a package and projects in which the package can be installed.
        
        @param request: UpdatePackageRequest
        @return: UpdatePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_package_with_options(project_name, package_name, request, headers, runtime)

    async def update_package_async(
        self,
        project_name: str,
        package_name: str,
        request: max_compute_20220104_models.UpdatePackageRequest,
    ) -> max_compute_20220104_models.UpdatePackageResponse:
        """
        @summary Updates the objects in a package and projects in which the package can be installed.
        
        @param request: UpdatePackageRequest
        @return: UpdatePackageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_package_with_options_async(project_name, package_name, request, headers, runtime)

    def update_project_basic_meta_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectBasicMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectBasicMetaResponse:
        """
        @summary Update Project Basic Information
        
        @param request: UpdateProjectBasicMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectBasicMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectBasicMeta',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/meta',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectBasicMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_basic_meta_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectBasicMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectBasicMetaResponse:
        """
        @summary Update Project Basic Information
        
        @param request: UpdateProjectBasicMetaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectBasicMetaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.properties):
            body['properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectBasicMeta',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/meta',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectBasicMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_basic_meta(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectBasicMetaRequest,
    ) -> max_compute_20220104_models.UpdateProjectBasicMetaResponse:
        """
        @summary Update Project Basic Information
        
        @param request: UpdateProjectBasicMetaRequest
        @return: UpdateProjectBasicMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_basic_meta_with_options(project_name, request, headers, runtime)

    async def update_project_basic_meta_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectBasicMetaRequest,
    ) -> max_compute_20220104_models.UpdateProjectBasicMetaResponse:
        """
        @summary Update Project Basic Information
        
        @param request: UpdateProjectBasicMetaRequest
        @return: UpdateProjectBasicMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_basic_meta_with_options_async(project_name, request, headers, runtime)

    def update_project_default_quota_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectDefaultQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectDefaultQuotaResponse:
        """
        @summary Modify Default Project Compute Quota
        
        @param request: UpdateProjectDefaultQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectDefaultQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectDefaultQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/quota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectDefaultQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_default_quota_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectDefaultQuotaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectDefaultQuotaResponse:
        """
        @summary Modify Default Project Compute Quota
        
        @param request: UpdateProjectDefaultQuotaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectDefaultQuotaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.quota):
            body['quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProjectDefaultQuota',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/quota',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectDefaultQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_default_quota(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectDefaultQuotaRequest,
    ) -> max_compute_20220104_models.UpdateProjectDefaultQuotaResponse:
        """
        @summary Modify Default Project Compute Quota
        
        @param request: UpdateProjectDefaultQuotaRequest
        @return: UpdateProjectDefaultQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_default_quota_with_options(project_name, request, headers, runtime)

    async def update_project_default_quota_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectDefaultQuotaRequest,
    ) -> max_compute_20220104_models.UpdateProjectDefaultQuotaResponse:
        """
        @summary Modify Default Project Compute Quota
        
        @param request: UpdateProjectDefaultQuotaRequest
        @return: UpdateProjectDefaultQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_default_quota_with_options_async(project_name, request, headers, runtime)

    def update_project_ip_white_list_with_options(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of a MaxCompute project.
        
        @param request: UpdateProjectIpWhiteListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateProjectIpWhiteList',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/ipWhiteList',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_ip_white_list_with_options_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of a MaxCompute project.
        
        @param request: UpdateProjectIpWhiteListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectIpWhiteListResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateProjectIpWhiteList',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/ipWhiteList',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateProjectIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_ip_white_list(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of a MaxCompute project.
        
        @param request: UpdateProjectIpWhiteListRequest
        @return: UpdateProjectIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_ip_white_list_with_options(project_name, request, headers, runtime)

    async def update_project_ip_white_list_async(
        self,
        project_name: str,
        request: max_compute_20220104_models.UpdateProjectIpWhiteListRequest,
    ) -> max_compute_20220104_models.UpdateProjectIpWhiteListResponse:
        """
        @summary Modifies the IP address whitelist of a MaxCompute project.
        
        @param request: UpdateProjectIpWhiteListRequest
        @return: UpdateProjectIpWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_ip_white_list_with_options_async(project_name, request, headers, runtime)

    def update_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        """
        @summary Updates a quota plan.
        
        @param request: UpdateQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        """
        @summary Updates a quota plan.
        
        @param request: UpdateQuotaPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaPlan',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/plans/{OpenApiUtilClient.get_encode_param(plan_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        """
        @summary Updates a quota plan.
        
        @param request: UpdateQuotaPlanRequest
        @return: UpdateQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def update_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: max_compute_20220104_models.UpdateQuotaPlanRequest,
    ) -> max_compute_20220104_models.UpdateQuotaPlanResponse:
        """
        @summary Updates a quota plan.
        
        @param request: UpdateQuotaPlanRequest
        @return: UpdateQuotaPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def update_quota_schedule_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        """
        @summary Updates the scheduling plan for a quota plan.
        
        @param request: UpdateQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        """
        @summary Updates the scheduling plan for a quota plan.
        
        @param request: UpdateQuotaScheduleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQuotaScheduleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateQuotaSchedule',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/quotas/{OpenApiUtilClient.get_encode_param(nickname)}/schedule',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_schedule(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        """
        @summary Updates the scheduling plan for a quota plan.
        
        @param request: UpdateQuotaScheduleRequest
        @return: UpdateQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_quota_schedule_with_options(nickname, request, headers, runtime)

    async def update_quota_schedule_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateQuotaScheduleRequest,
    ) -> max_compute_20220104_models.UpdateQuotaScheduleResponse:
        """
        @summary Updates the scheduling plan for a quota plan.
        
        @param request: UpdateQuotaScheduleRequest
        @return: UpdateQuotaScheduleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def update_tunnel_quota_timer_with_options(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateTunnelQuotaTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateTunnelQuotaTimerResponse:
        """
        @summary Updates the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @description Before you call this operation, make sure that you are familiar with the [billing and prices](https://www.alibabacloud.com/help/maxcompute/product-overview/data-transfer-fees-hourly-billing) of Tunnel quotas and elastically reserved computing resources.
        
        @param request: UpdateTunnelQuotaTimerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTunnelQuotaTimerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.timezone):
            query['timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTunnelQuotaTimer',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/tunnel/{OpenApiUtilClient.get_encode_param(nickname)}/timers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateTunnelQuotaTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tunnel_quota_timer_with_options_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateTunnelQuotaTimerRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateTunnelQuotaTimerResponse:
        """
        @summary Updates the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @description Before you call this operation, make sure that you are familiar with the [billing and prices](https://www.alibabacloud.com/help/maxcompute/product-overview/data-transfer-fees-hourly-billing) of Tunnel quotas and elastically reserved computing resources.
        
        @param request: UpdateTunnelQuotaTimerRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTunnelQuotaTimerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.timezone):
            query['timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='UpdateTunnelQuotaTimer',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/tunnel/{OpenApiUtilClient.get_encode_param(nickname)}/timers',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateTunnelQuotaTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tunnel_quota_timer(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateTunnelQuotaTimerRequest,
    ) -> max_compute_20220104_models.UpdateTunnelQuotaTimerResponse:
        """
        @summary Updates the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @description Before you call this operation, make sure that you are familiar with the [billing and prices](https://www.alibabacloud.com/help/maxcompute/product-overview/data-transfer-fees-hourly-billing) of Tunnel quotas and elastically reserved computing resources.
        
        @param request: UpdateTunnelQuotaTimerRequest
        @return: UpdateTunnelQuotaTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_tunnel_quota_timer_with_options(nickname, request, headers, runtime)

    async def update_tunnel_quota_timer_async(
        self,
        nickname: str,
        request: max_compute_20220104_models.UpdateTunnelQuotaTimerRequest,
    ) -> max_compute_20220104_models.UpdateTunnelQuotaTimerResponse:
        """
        @summary Updates the time-specific configuration of an exclusive resource group for Tunnel (referred to as Tunnel quota).
        
        @description Before you call this operation, make sure that you are familiar with the [billing and prices](https://www.alibabacloud.com/help/maxcompute/product-overview/data-transfer-fees-hourly-billing) of Tunnel quotas and elastically reserved computing resources.
        
        @param request: UpdateTunnelQuotaTimerRequest
        @return: UpdateTunnelQuotaTimerResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_tunnel_quota_timer_with_options_async(nickname, request, headers, runtime)

    def update_users_to_role_with_options(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.UpdateUsersToRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateUsersToRoleResponse:
        """
        @summary Add or remove users from a project role.
        
        @param request: UpdateUsersToRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUsersToRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add):
            body['add'] = request.add
        if not UtilClient.is_unset(request.remove):
            body['remove'] = request.remove
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUsersToRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateUsersToRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_users_to_role_with_options_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.UpdateUsersToRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> max_compute_20220104_models.UpdateUsersToRoleResponse:
        """
        @summary Add or remove users from a project role.
        
        @param request: UpdateUsersToRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUsersToRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.add):
            body['add'] = request.add
        if not UtilClient.is_unset(request.remove):
            body['remove'] = request.remove
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUsersToRole',
            version='2022-01-04',
            protocol='HTTPS',
            pathname=f'/api/v1/projects/{OpenApiUtilClient.get_encode_param(project_name)}/roles/{OpenApiUtilClient.get_encode_param(role_name)}/users',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            max_compute_20220104_models.UpdateUsersToRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_users_to_role(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.UpdateUsersToRoleRequest,
    ) -> max_compute_20220104_models.UpdateUsersToRoleResponse:
        """
        @summary Add or remove users from a project role.
        
        @param request: UpdateUsersToRoleRequest
        @return: UpdateUsersToRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_users_to_role_with_options(project_name, role_name, request, headers, runtime)

    async def update_users_to_role_async(
        self,
        project_name: str,
        role_name: str,
        request: max_compute_20220104_models.UpdateUsersToRoleRequest,
    ) -> max_compute_20220104_models.UpdateUsersToRoleResponse:
        """
        @summary Add or remove users from a project role.
        
        @param request: UpdateUsersToRoleRequest
        @return: UpdateUsersToRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_users_to_role_with_options_async(project_name, role_name, request, headers, runtime)
