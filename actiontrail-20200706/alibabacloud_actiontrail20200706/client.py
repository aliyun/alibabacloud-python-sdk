# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_actiontrail20200706 import models as actiontrail_20200706_models
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
            'ap-northeast-2-pop': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-beijing-gov-1': 'actiontrail.aliyuncs.com',
            'cn-beijing-nu16-b01': 'actiontrail.aliyuncs.com',
            'cn-edge-1': 'actiontrail.aliyuncs.com',
            'cn-fujian': 'actiontrail.aliyuncs.com',
            'cn-haidian-cm12-c01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-finance': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'actiontrail.aliyuncs.com',
            'cn-hangzhou-test-306': 'actiontrail.aliyuncs.com',
            'cn-hongkong-finance-pop': 'actiontrail.aliyuncs.com',
            'cn-qingdao-nebula': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et15-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-et2-b01': 'actiontrail.aliyuncs.com',
            'cn-shanghai-inner': 'actiontrail.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-finance-1': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-inner': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'actiontrail.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'actiontrail.aliyuncs.com',
            'cn-wuhan': 'actiontrail.aliyuncs.com',
            'cn-yushanfang': 'actiontrail.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'actiontrail.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'actiontrail.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'actiontrail.aliyuncs.com',
            'eu-west-1-oxs': 'actiontrail.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'actiontrail.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('actiontrail', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_advanced_query_history_with_options(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse:
        """
        @summary 创建高级查询历史记录
        
        @param request: CreateAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedQueryHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_sql):
            query['QuerySql'] = request.query_sql
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_query_history_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse:
        """
        @summary 创建高级查询历史记录
        
        @param request: CreateAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedQueryHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_sql):
            query['QuerySql'] = request.query_sql
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_query_history(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryHistoryRequest,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse:
        """
        @summary 创建高级查询历史记录
        
        @param request: CreateAdvancedQueryHistoryRequest
        @return: CreateAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_advanced_query_history_with_options(request, runtime)

    async def create_advanced_query_history_async(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryHistoryRequest,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryHistoryResponse:
        """
        @summary 创建高级查询历史记录
        
        @param request: CreateAdvancedQueryHistoryRequest
        @return: CreateAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_advanced_query_history_with_options_async(request, runtime)

    def create_advanced_query_template_with_options(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse:
        """
        @summary 创建高级查询模板
        
        @param request: CreateAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_query_template_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse:
        """
        @summary 创建高级查询模板
        
        @param request: CreateAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_query_template(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse:
        """
        @summary 创建高级查询模板
        
        @param request: CreateAdvancedQueryTemplateRequest
        @return: CreateAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_advanced_query_template_with_options(request, runtime)

    async def create_advanced_query_template_async(
        self,
        request: actiontrail_20200706_models.CreateAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.CreateAdvancedQueryTemplateResponse:
        """
        @summary 创建高级查询模板
        
        @param request: CreateAdvancedQueryTemplateRequest
        @return: CreateAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_advanced_query_template_with_options_async(request, runtime)

    def create_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        """
        @summary Creates a data backfill task.
        
        @description Limits
        Make sure that you have created a single-account trail to deliver events to Simple Log Service by calling the [CreateTrail](https://help.aliyun.com/document_detail/212313.html) operation.
        Only one data backfill task can run at a time within an Alibaba Cloud account.
        This topic provides an example on how to create a data backfill task for a trail named `trail-name`.
        
        @param request: CreateDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        """
        @summary Creates a data backfill task.
        
        @description Limits
        Make sure that you have created a single-account trail to deliver events to Simple Log Service by calling the [CreateTrail](https://help.aliyun.com/document_detail/212313.html) operation.
        Only one data backfill task can run at a time within an Alibaba Cloud account.
        This topic provides an example on how to create a data backfill task for a trail named `trail-name`.
        
        @param request: CreateDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.trail_name):
            query['TrailName'] = request.trail_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_delivery_history_job(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        """
        @summary Creates a data backfill task.
        
        @description Limits
        Make sure that you have created a single-account trail to deliver events to Simple Log Service by calling the [CreateTrail](https://help.aliyun.com/document_detail/212313.html) operation.
        Only one data backfill task can run at a time within an Alibaba Cloud account.
        This topic provides an example on how to create a data backfill task for a trail named `trail-name`.
        
        @param request: CreateDeliveryHistoryJobRequest
        @return: CreateDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_delivery_history_job_with_options(request, runtime)

    async def create_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.CreateDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.CreateDeliveryHistoryJobResponse:
        """
        @summary Creates a data backfill task.
        
        @description Limits
        Make sure that you have created a single-account trail to deliver events to Simple Log Service by calling the [CreateTrail](https://help.aliyun.com/document_detail/212313.html) operation.
        Only one data backfill task can run at a time within an Alibaba Cloud account.
        This topic provides an example on how to create a data backfill task for a trail named `trail-name`.
        
        @param request: CreateDeliveryHistoryJobRequest
        @return: CreateDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_delivery_history_job_with_options_async(request, runtime)

    def create_trail_with_options(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        """
        @summary Creates a trail. By default, ActionTrail allows you to query events generated within your Alibaba Cloud account in the last 90 days. To query and analyze events generated more than 90 days ago, create a trail to deliver events to Object Storage Service (OSS), Simple Log Service, or MaxCompute.
        
        @description *Operation description**\
        >By default, a trail that is created by calling an operation is in the Disabled state. You must call the StartLogging operation to enable the trail. This way, ActionTrail can deliver events to the destination cloud service.
        *Prerequisites**\
        Before you create a trail, make sure that at least one of the following storage configurations is complete:
        - Deliver events to OSS
        - OSS is activated and a bucket is created.
        
        - Deliver events to Simple Log Service
        - Simple Log Service is activated and a project is created.
        >When a trail is created, ActionTrail automatically creates a Logstore named `actiontrail_<Trail name>` in the project. You cannot write data other than the audit data to the Logstore. This ensures the accuracy of the audit data.
        
        - Deliver events to MaxCompute
        - MaxCompute is activated.
        >When a trail is created, ActionTrail automatically creates a project named `actiontrail_<Account ID>` on the Projects page. You cannot write data other than the audit data to the project. This ensures the accuracy of the audit data.
        *Usage Notes**\
        This topic provides an example on how to create a single-account trail named `trail-test` to deliver events to an OSS bucket named `audit-log`.
        
        @param request: CreateTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not UtilClient.is_unset(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        """
        @summary Creates a trail. By default, ActionTrail allows you to query events generated within your Alibaba Cloud account in the last 90 days. To query and analyze events generated more than 90 days ago, create a trail to deliver events to Object Storage Service (OSS), Simple Log Service, or MaxCompute.
        
        @description *Operation description**\
        >By default, a trail that is created by calling an operation is in the Disabled state. You must call the StartLogging operation to enable the trail. This way, ActionTrail can deliver events to the destination cloud service.
        *Prerequisites**\
        Before you create a trail, make sure that at least one of the following storage configurations is complete:
        - Deliver events to OSS
        - OSS is activated and a bucket is created.
        
        - Deliver events to Simple Log Service
        - Simple Log Service is activated and a project is created.
        >When a trail is created, ActionTrail automatically creates a Logstore named `actiontrail_<Trail name>` in the project. You cannot write data other than the audit data to the Logstore. This ensures the accuracy of the audit data.
        
        - Deliver events to MaxCompute
        - MaxCompute is activated.
        >When a trail is created, ActionTrail automatically creates a project named `actiontrail_<Account ID>` on the Projects page. You cannot write data other than the audit data to the project. This ensures the accuracy of the audit data.
        *Usage Notes**\
        This topic provides an example on how to create a single-account trail named `trail-test` to deliver events to an OSS bucket named `audit-log`.
        
        @param request: CreateTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not UtilClient.is_unset(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.CreateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trail(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        """
        @summary Creates a trail. By default, ActionTrail allows you to query events generated within your Alibaba Cloud account in the last 90 days. To query and analyze events generated more than 90 days ago, create a trail to deliver events to Object Storage Service (OSS), Simple Log Service, or MaxCompute.
        
        @description *Operation description**\
        >By default, a trail that is created by calling an operation is in the Disabled state. You must call the StartLogging operation to enable the trail. This way, ActionTrail can deliver events to the destination cloud service.
        *Prerequisites**\
        Before you create a trail, make sure that at least one of the following storage configurations is complete:
        - Deliver events to OSS
        - OSS is activated and a bucket is created.
        
        - Deliver events to Simple Log Service
        - Simple Log Service is activated and a project is created.
        >When a trail is created, ActionTrail automatically creates a Logstore named `actiontrail_<Trail name>` in the project. You cannot write data other than the audit data to the Logstore. This ensures the accuracy of the audit data.
        
        - Deliver events to MaxCompute
        - MaxCompute is activated.
        >When a trail is created, ActionTrail automatically creates a project named `actiontrail_<Account ID>` on the Projects page. You cannot write data other than the audit data to the project. This ensures the accuracy of the audit data.
        *Usage Notes**\
        This topic provides an example on how to create a single-account trail named `trail-test` to deliver events to an OSS bucket named `audit-log`.
        
        @param request: CreateTrailRequest
        @return: CreateTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_trail_with_options(request, runtime)

    async def create_trail_async(
        self,
        request: actiontrail_20200706_models.CreateTrailRequest,
    ) -> actiontrail_20200706_models.CreateTrailResponse:
        """
        @summary Creates a trail. By default, ActionTrail allows you to query events generated within your Alibaba Cloud account in the last 90 days. To query and analyze events generated more than 90 days ago, create a trail to deliver events to Object Storage Service (OSS), Simple Log Service, or MaxCompute.
        
        @description *Operation description**\
        >By default, a trail that is created by calling an operation is in the Disabled state. You must call the StartLogging operation to enable the trail. This way, ActionTrail can deliver events to the destination cloud service.
        *Prerequisites**\
        Before you create a trail, make sure that at least one of the following storage configurations is complete:
        - Deliver events to OSS
        - OSS is activated and a bucket is created.
        
        - Deliver events to Simple Log Service
        - Simple Log Service is activated and a project is created.
        >When a trail is created, ActionTrail automatically creates a Logstore named `actiontrail_<Trail name>` in the project. You cannot write data other than the audit data to the Logstore. This ensures the accuracy of the audit data.
        
        - Deliver events to MaxCompute
        - MaxCompute is activated.
        >When a trail is created, ActionTrail automatically creates a project named `actiontrail_<Account ID>` on the Projects page. You cannot write data other than the audit data to the project. This ensures the accuracy of the audit data.
        *Usage Notes**\
        This topic provides an example on how to create a single-account trail named `trail-test` to deliver events to an OSS bucket named `audit-log`.
        
        @param request: CreateTrailRequest
        @return: CreateTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_trail_with_options_async(request, runtime)

    def delete_advanced_query_history_with_options(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse:
        """
        @summary 删除高级查询历史记录
        
        @param request: DeleteAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvancedQueryHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_advanced_query_history_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse:
        """
        @summary 删除高级查询历史记录
        
        @param request: DeleteAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvancedQueryHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_advanced_query_history(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryHistoryRequest,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse:
        """
        @summary 删除高级查询历史记录
        
        @param request: DeleteAdvancedQueryHistoryRequest
        @return: DeleteAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_advanced_query_history_with_options(request, runtime)

    async def delete_advanced_query_history_async(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryHistoryRequest,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryHistoryResponse:
        """
        @summary 删除高级查询历史记录
        
        @param request: DeleteAdvancedQueryHistoryRequest
        @return: DeleteAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_advanced_query_history_with_options_async(request, runtime)

    def delete_advanced_query_template_with_options(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse:
        """
        @summary 删除高级查询模板
        
        @param request: DeleteAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_advanced_query_template_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse:
        """
        @summary 删除高级查询模板
        
        @param request: DeleteAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_advanced_query_template(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse:
        """
        @summary 删除高级查询模板
        
        @param request: DeleteAdvancedQueryTemplateRequest
        @return: DeleteAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_advanced_query_template_with_options(request, runtime)

    async def delete_advanced_query_template_async(
        self,
        request: actiontrail_20200706_models.DeleteAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.DeleteAdvancedQueryTemplateResponse:
        """
        @summary 删除高级查询模板
        
        @param request: DeleteAdvancedQueryTemplateRequest
        @return: DeleteAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_advanced_query_template_with_options_async(request, runtime)

    def delete_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        """
        @summary Deletes a data backfill task.
        
        @description This topic describes how to delete a data backfill task whose ID is `16602`.
        
        @param request: DeleteDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        """
        @summary Deletes a data backfill task.
        
        @description This topic describes how to delete a data backfill task whose ID is `16602`.
        
        @param request: DeleteDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_history_job(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        """
        @summary Deletes a data backfill task.
        
        @description This topic describes how to delete a data backfill task whose ID is `16602`.
        
        @param request: DeleteDeliveryHistoryJobRequest
        @return: DeleteDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_delivery_history_job_with_options(request, runtime)

    async def delete_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.DeleteDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.DeleteDeliveryHistoryJobResponse:
        """
        @summary Deletes a data backfill task.
        
        @description This topic describes how to delete a data backfill task whose ID is `16602`.
        
        @param request: DeleteDeliveryHistoryJobRequest
        @return: DeleteDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_delivery_history_job_with_options_async(request, runtime)

    def delete_trail_with_options(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        """
        @summary Deletes a trail.
        
        @description This topic describes how to delete a sample trail named `trail-test`.
        
        @param request: DeleteTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        """
        @summary Deletes a trail.
        
        @description This topic describes how to delete a sample trail named `trail-test`.
        
        @param request: DeleteTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DeleteTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trail(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        """
        @summary Deletes a trail.
        
        @description This topic describes how to delete a sample trail named `trail-test`.
        
        @param request: DeleteTrailRequest
        @return: DeleteTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_trail_with_options(request, runtime)

    async def delete_trail_async(
        self,
        request: actiontrail_20200706_models.DeleteTrailRequest,
    ) -> actiontrail_20200706_models.DeleteTrailResponse:
        """
        @summary Deletes a trail.
        
        @description This topic describes how to delete a sample trail named `trail-test`.
        
        @param request: DeleteTrailRequest
        @return: DeleteTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_trail_with_options_async(request, runtime)

    def describe_advanced_query_history_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse:
        """
        @summary 查询高级查询历史记录
        
        @param request: DescribeAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvancedQueryHistoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advanced_query_history_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse:
        """
        @summary 查询高级查询历史记录
        
        @param request: DescribeAdvancedQueryHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvancedQueryHistoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeAdvancedQueryHistory',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advanced_query_history(self) -> actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse:
        """
        @summary 查询高级查询历史记录
        
        @return: DescribeAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advanced_query_history_with_options(runtime)

    async def describe_advanced_query_history_async(self) -> actiontrail_20200706_models.DescribeAdvancedQueryHistoryResponse:
        """
        @summary 查询高级查询历史记录
        
        @return: DescribeAdvancedQueryHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advanced_query_history_with_options_async(runtime)

    def describe_advanced_query_template_with_options(
        self,
        request: actiontrail_20200706_models.DescribeAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse:
        """
        @summary 查询高级查询模板
        
        @param request: DescribeAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_advanced_query_template_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse:
        """
        @summary 查询高级查询模板
        
        @param request: DescribeAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_advanced_query_template(
        self,
        request: actiontrail_20200706_models.DescribeAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse:
        """
        @summary 查询高级查询模板
        
        @param request: DescribeAdvancedQueryTemplateRequest
        @return: DescribeAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advanced_query_template_with_options(request, runtime)

    async def describe_advanced_query_template_async(
        self,
        request: actiontrail_20200706_models.DescribeAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.DescribeAdvancedQueryTemplateResponse:
        """
        @summary 查询高级查询模板
        
        @param request: DescribeAdvancedQueryTemplateRequest
        @return: DescribeAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advanced_query_template_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        """
        @summary Queries the Alibaba Cloud regions that are supported by ActionTrail.
        
        @description For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        """
        @summary Queries the Alibaba Cloud regions that are supported by ActionTrail.
        
        @description For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        """
        @summary Queries the Alibaba Cloud regions that are supported by ActionTrail.
        
        @description For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: actiontrail_20200706_models.DescribeRegionsRequest,
    ) -> actiontrail_20200706_models.DescribeRegionsResponse:
        """
        @summary Queries the Alibaba Cloud regions that are supported by ActionTrail.
        
        @description For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_resource_life_cycle_events_with_options(
        self,
        request: actiontrail_20200706_models.DescribeResourceLifeCycleEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse:
        """
        @summary 列举资源生命周期事件
        
        @param request: DescribeResourceLifeCycleEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLifeCycleEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLifeCycleEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_life_cycle_events_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeResourceLifeCycleEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse:
        """
        @summary 列举资源生命周期事件
        
        @param request: DescribeResourceLifeCycleEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceLifeCycleEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceLifeCycleEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_life_cycle_events(
        self,
        request: actiontrail_20200706_models.DescribeResourceLifeCycleEventsRequest,
    ) -> actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse:
        """
        @summary 列举资源生命周期事件
        
        @param request: DescribeResourceLifeCycleEventsRequest
        @return: DescribeResourceLifeCycleEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_life_cycle_events_with_options(request, runtime)

    async def describe_resource_life_cycle_events_async(
        self,
        request: actiontrail_20200706_models.DescribeResourceLifeCycleEventsRequest,
    ) -> actiontrail_20200706_models.DescribeResourceLifeCycleEventsResponse:
        """
        @summary 列举资源生命周期事件
        
        @param request: DescribeResourceLifeCycleEventsRequest
        @return: DescribeResourceLifeCycleEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_life_cycle_events_with_options_async(request, runtime)

    def describe_scenes_with_options(
        self,
        request: actiontrail_20200706_models.DescribeScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeScenesResponse:
        """
        @summary 查询所有场景
        
        @param request: DescribeScenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_code):
            query['SearchCode'] = request.search_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScenes',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeScenesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scenes_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeScenesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeScenesResponse:
        """
        @summary 查询所有场景
        
        @param request: DescribeScenesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScenesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_code):
            query['SearchCode'] = request.search_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScenes',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeScenesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scenes(
        self,
        request: actiontrail_20200706_models.DescribeScenesRequest,
    ) -> actiontrail_20200706_models.DescribeScenesResponse:
        """
        @summary 查询所有场景
        
        @param request: DescribeScenesRequest
        @return: DescribeScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scenes_with_options(request, runtime)

    async def describe_scenes_async(
        self,
        request: actiontrail_20200706_models.DescribeScenesRequest,
    ) -> actiontrail_20200706_models.DescribeScenesResponse:
        """
        @summary 查询所有场景
        
        @param request: DescribeScenesRequest
        @return: DescribeScenesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scenes_with_options_async(request, runtime)

    def describe_search_templates_with_options(
        self,
        request: actiontrail_20200706_models.DescribeSearchTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeSearchTemplatesResponse:
        """
        @summary 列举所有模版
        
        @param request: DescribeSearchTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSearchTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSearchTemplates',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeSearchTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_search_templates_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeSearchTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeSearchTemplatesResponse:
        """
        @summary 列举所有模版
        
        @param request: DescribeSearchTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSearchTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSearchTemplates',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeSearchTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_search_templates(
        self,
        request: actiontrail_20200706_models.DescribeSearchTemplatesRequest,
    ) -> actiontrail_20200706_models.DescribeSearchTemplatesResponse:
        """
        @summary 列举所有模版
        
        @param request: DescribeSearchTemplatesRequest
        @return: DescribeSearchTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_search_templates_with_options(request, runtime)

    async def describe_search_templates_async(
        self,
        request: actiontrail_20200706_models.DescribeSearchTemplatesRequest,
    ) -> actiontrail_20200706_models.DescribeSearchTemplatesResponse:
        """
        @summary 列举所有模版
        
        @param request: DescribeSearchTemplatesRequest
        @return: DescribeSearchTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_search_templates_with_options_async(request, runtime)

    def describe_trails_with_options(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        """
        @summary Queries created trails.
        
        @description This topic shows you how to query the information about the single-account trails within an Alibaba Cloud account. In this example, the information about a trail named `test-4` is returned.
        
        @param request: DescribeTrailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not UtilClient.is_unset(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not UtilClient.is_unset(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trails_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        """
        @summary Queries created trails.
        
        @description This topic shows you how to query the information about the single-account trails within an Alibaba Cloud account. In this example, the information about a trail named `test-4` is returned.
        
        @param request: DescribeTrailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTrailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_organization_trail):
            query['IncludeOrganizationTrail'] = request.include_organization_trail
        if not UtilClient.is_unset(request.include_shadow_trails):
            query['IncludeShadowTrails'] = request.include_shadow_trails
        if not UtilClient.is_unset(request.name_list):
            query['NameList'] = request.name_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTrails',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeTrailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trails(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        """
        @summary Queries created trails.
        
        @description This topic shows you how to query the information about the single-account trails within an Alibaba Cloud account. In this example, the information about a trail named `test-4` is returned.
        
        @param request: DescribeTrailsRequest
        @return: DescribeTrailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_trails_with_options(request, runtime)

    async def describe_trails_async(
        self,
        request: actiontrail_20200706_models.DescribeTrailsRequest,
    ) -> actiontrail_20200706_models.DescribeTrailsResponse:
        """
        @summary Queries created trails.
        
        @description This topic shows you how to query the information about the single-account trails within an Alibaba Cloud account. In this example, the information about a trail named `test-4` is returned.
        
        @param request: DescribeTrailsRequest
        @return: DescribeTrailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_trails_with_options_async(request, runtime)

    def describe_user_alert_count_with_options(
        self,
        request: actiontrail_20200706_models.DescribeUserAlertCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeUserAlertCountResponse:
        """
        @summary 查询用户告警量
        
        @param request: DescribeUserAlertCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAlertCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAlertCount',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeUserAlertCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_alert_count_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeUserAlertCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeUserAlertCountResponse:
        """
        @summary 查询用户告警量
        
        @param request: DescribeUserAlertCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserAlertCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserAlertCount',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeUserAlertCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_alert_count(
        self,
        request: actiontrail_20200706_models.DescribeUserAlertCountRequest,
    ) -> actiontrail_20200706_models.DescribeUserAlertCountResponse:
        """
        @summary 查询用户告警量
        
        @param request: DescribeUserAlertCountRequest
        @return: DescribeUserAlertCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_alert_count_with_options(request, runtime)

    async def describe_user_alert_count_async(
        self,
        request: actiontrail_20200706_models.DescribeUserAlertCountRequest,
    ) -> actiontrail_20200706_models.DescribeUserAlertCountResponse:
        """
        @summary 查询用户告警量
        
        @param request: DescribeUserAlertCountRequest
        @return: DescribeUserAlertCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_alert_count_with_options_async(request, runtime)

    def describe_user_log_count_with_options(
        self,
        request: actiontrail_20200706_models.DescribeUserLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeUserLogCountResponse:
        """
        @summary 查询用户日志量
        
        @param request: DescribeUserLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLogCount',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeUserLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_log_count_with_options_async(
        self,
        request: actiontrail_20200706_models.DescribeUserLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.DescribeUserLogCountResponse:
        """
        @summary 查询用户日志量
        
        @param request: DescribeUserLogCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserLogCountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserLogCount',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.DescribeUserLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_log_count(
        self,
        request: actiontrail_20200706_models.DescribeUserLogCountRequest,
    ) -> actiontrail_20200706_models.DescribeUserLogCountResponse:
        """
        @summary 查询用户日志量
        
        @param request: DescribeUserLogCountRequest
        @return: DescribeUserLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_log_count_with_options(request, runtime)

    async def describe_user_log_count_async(
        self,
        request: actiontrail_20200706_models.DescribeUserLogCountRequest,
    ) -> actiontrail_20200706_models.DescribeUserLogCountResponse:
        """
        @summary 查询用户日志量
        
        @param request: DescribeUserLogCountRequest
        @return: DescribeUserLogCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_log_count_with_options_async(request, runtime)

    def enable_insight_with_options(
        self,
        request: actiontrail_20200706_models.EnableInsightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.EnableInsightResponse:
        """
        @summary Enables the Insights feature
        
        @param request: EnableInsightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInsightResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInsight',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.EnableInsightResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_insight_with_options_async(
        self,
        request: actiontrail_20200706_models.EnableInsightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.EnableInsightResponse:
        """
        @summary Enables the Insights feature
        
        @param request: EnableInsightRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableInsightResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.insight_type):
            query['InsightType'] = request.insight_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInsight',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.EnableInsightResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_insight(
        self,
        request: actiontrail_20200706_models.EnableInsightRequest,
    ) -> actiontrail_20200706_models.EnableInsightResponse:
        """
        @summary Enables the Insights feature
        
        @param request: EnableInsightRequest
        @return: EnableInsightResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_insight_with_options(request, runtime)

    async def enable_insight_async(
        self,
        request: actiontrail_20200706_models.EnableInsightRequest,
    ) -> actiontrail_20200706_models.EnableInsightResponse:
        """
        @summary Enables the Insights feature
        
        @param request: EnableInsightRequest
        @return: EnableInsightResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_insight_with_options_async(request, runtime)

    def get_access_key_last_used_events_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        """
        @summary Queries the information about the most recent events that are generated when a specified AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the most recent events that are generated within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. For more information about supported events, see [Alibaba Cloud services and events that are supported by the AccessKey pair audit feature](https://help.aliyun.com/document_detail/419214.html). Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_events_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        """
        @summary Queries the information about the most recent events that are generated when a specified AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the most recent events that are generated within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. For more information about supported events, see [Alibaba Cloud services and events that are supported by the AccessKey pair audit feature](https://help.aliyun.com/document_detail/419214.html). Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_events(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        """
        @summary Queries the information about the most recent events that are generated when a specified AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the most recent events that are generated within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. For more information about supported events, see [Alibaba Cloud services and events that are supported by the AccessKey pair audit feature](https://help.aliyun.com/document_detail/419214.html). Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedEventsRequest
        @return: GetAccessKeyLastUsedEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_events_with_options(request, runtime)

    async def get_access_key_last_used_events_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedEventsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedEventsResponse:
        """
        @summary Queries the information about the most recent events that are generated when a specified AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the most recent events that are generated within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. For more information about supported events, see [Alibaba Cloud services and events that are supported by the AccessKey pair audit feature](https://help.aliyun.com/document_detail/419214.html). Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedEventsRequest
        @return: GetAccessKeyLastUsedEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_events_with_options_async(request, runtime)

    def get_access_key_last_used_info_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        """
        @summary Queries the information about the most recent call of a specified AccessKey pair.
        
        @description You can call this operation to query only the information about the most recent call of a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedInfo',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_info_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        """
        @summary Queries the information about the most recent call of a specified AccessKey pair.
        
        @description You can call this operation to query only the information about the most recent call of a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedInfo',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_info(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        """
        @summary Queries the information about the most recent call of a specified AccessKey pair.
        
        @description You can call this operation to query only the information about the most recent call of a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedInfoRequest
        @return: GetAccessKeyLastUsedInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_info_with_options(request, runtime)

    async def get_access_key_last_used_info_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedInfoRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedInfoResponse:
        """
        @summary Queries the information about the most recent call of a specified AccessKey pair.
        
        @description You can call this operation to query only the information about the most recent call of a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedInfoRequest
        @return: GetAccessKeyLastUsedInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_info_with_options_async(request, runtime)

    def get_access_key_last_used_ips_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        """
        @summary Queries the information about the IP addresses that are most recently used when an AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the IP addresses that are most recently used within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedIps',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_ips_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        """
        @summary Queries the information about the IP addresses that are most recently used when an AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the IP addresses that are most recently used within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedIpsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedIpsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedIps',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_ips(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        """
        @summary Queries the information about the IP addresses that are most recently used when an AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the IP addresses that are most recently used within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedIpsRequest
        @return: GetAccessKeyLastUsedIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_ips_with_options(request, runtime)

    async def get_access_key_last_used_ips_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedIpsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedIpsResponse:
        """
        @summary Queries the information about the IP addresses that are most recently used when an AccessKey pair is called to access Alibaba Cloud services.
        
        @description You can call this operation to query only the information about the IP addresses that are most recently used within 400 days after February 1, 2022 when a specified AccessKey pair is called to access Alibaba Cloud services. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedIpsRequest
        @return: GetAccessKeyLastUsedIpsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_ips_with_options_async(request, runtime)

    def get_access_key_last_used_products_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        """
        @summary Queries the information about the Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedProducts',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_products_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        """
        @summary Queries the information about the Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedProductsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedProducts',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_products(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        """
        @summary Queries the information about the Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedProductsRequest
        @return: GetAccessKeyLastUsedProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_products_with_options(request, runtime)

    async def get_access_key_last_used_products_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedProductsRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedProductsResponse:
        """
        @summary Queries the information about the Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about Alibaba Cloud services that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedProductsRequest
        @return: GetAccessKeyLastUsedProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_products_with_options_async(request, runtime)

    def get_access_key_last_used_resources_with_options(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        """
        @summary Queries the information about the resources that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about resources that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedResources',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_access_key_last_used_resources_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        """
        @summary Queries the information about the resources that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about resources that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccessKeyLastUsedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccessKeyLastUsedResources',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_access_key_last_used_resources(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        """
        @summary Queries the information about the resources that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about resources that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedResourcesRequest
        @return: GetAccessKeyLastUsedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_access_key_last_used_resources_with_options(request, runtime)

    async def get_access_key_last_used_resources_async(
        self,
        request: actiontrail_20200706_models.GetAccessKeyLastUsedResourcesRequest,
    ) -> actiontrail_20200706_models.GetAccessKeyLastUsedResourcesResponse:
        """
        @summary Queries the information about the resources that are most recently accessed by using a specified AccessKey pair.
        
        @description You can call this operation to query only the information about resources that are most recently accessed by using a specified AccessKey pair within 400 days after February 1, 2022. Data is updated at 1-hour intervals, which can cause query latency. We recommend that you do not change an AccessKey pair unless required.
        
        @param request: GetAccessKeyLastUsedResourcesRequest
        @return: GetAccessKeyLastUsedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_access_key_last_used_resources_with_options_async(request, runtime)

    def get_advanced_query_template_with_options(
        self,
        request: actiontrail_20200706_models.GetAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAdvancedQueryTemplateResponse:
        """
        @summary 查询单个高级查询模板
        
        @param request: GetAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advanced_query_template_with_options_async(
        self,
        request: actiontrail_20200706_models.GetAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetAdvancedQueryTemplateResponse:
        """
        @summary 查询单个高级查询模板
        
        @param request: GetAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advanced_query_template(
        self,
        request: actiontrail_20200706_models.GetAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.GetAdvancedQueryTemplateResponse:
        """
        @summary 查询单个高级查询模板
        
        @param request: GetAdvancedQueryTemplateRequest
        @return: GetAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_advanced_query_template_with_options(request, runtime)

    async def get_advanced_query_template_async(
        self,
        request: actiontrail_20200706_models.GetAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.GetAdvancedQueryTemplateResponse:
        """
        @summary 查询单个高级查询模板
        
        @param request: GetAdvancedQueryTemplateRequest
        @return: GetAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_advanced_query_template_with_options_async(request, runtime)

    def get_delivery_history_job_with_options(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        """
        @summary Queries the details of a data backfill task.
        
        @description This topic provides an example on how to query the details of a data backfill task whose ID is `16602`. The return result shows that historical events for a trail named `trail-name` are delivered to Simple Log Service and the task is complete.
        
        @param request: GetDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_delivery_history_job_with_options_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        """
        @summary Queries the details of a data backfill task.
        
        @description This topic provides an example on how to query the details of a data backfill task whose ID is `16602`. The return result shows that historical events for a trail named `trail-name` are delivered to Simple Log Service and the task is complete.
        
        @param request: GetDeliveryHistoryJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeliveryHistoryJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeliveryHistoryJob',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetDeliveryHistoryJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_delivery_history_job(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        """
        @summary Queries the details of a data backfill task.
        
        @description This topic provides an example on how to query the details of a data backfill task whose ID is `16602`. The return result shows that historical events for a trail named `trail-name` are delivered to Simple Log Service and the task is complete.
        
        @param request: GetDeliveryHistoryJobRequest
        @return: GetDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_delivery_history_job_with_options(request, runtime)

    async def get_delivery_history_job_async(
        self,
        request: actiontrail_20200706_models.GetDeliveryHistoryJobRequest,
    ) -> actiontrail_20200706_models.GetDeliveryHistoryJobResponse:
        """
        @summary Queries the details of a data backfill task.
        
        @description This topic provides an example on how to query the details of a data backfill task whose ID is `16602`. The return result shows that historical events for a trail named `trail-name` are delivered to Simple Log Service and the task is complete.
        
        @param request: GetDeliveryHistoryJobRequest
        @return: GetDeliveryHistoryJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_delivery_history_job_with_options_async(request, runtime)

    def get_global_events_storage_region_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse:
        """
        @summary Queries the region where global events are stored.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        
        @param request: GetGlobalEventsStorageRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGlobalEventsStorageRegionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGlobalEventsStorageRegion',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_global_events_storage_region_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse:
        """
        @summary Queries the region where global events are stored.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        
        @param request: GetGlobalEventsStorageRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGlobalEventsStorageRegionResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGlobalEventsStorageRegion',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_global_events_storage_region(self) -> actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse:
        """
        @summary Queries the region where global events are stored.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        
        @return: GetGlobalEventsStorageRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_global_events_storage_region_with_options(runtime)

    async def get_global_events_storage_region_async(self) -> actiontrail_20200706_models.GetGlobalEventsStorageRegionResponse:
        """
        @summary Queries the region where global events are stored.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        
        @return: GetGlobalEventsStorageRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_global_events_storage_region_with_options_async(runtime)

    def get_governance_metrics_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetGovernanceMetricsResponse:
        """
        @summary 操作审计成熟度查询接口
        
        @param request: GetGovernanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceMetricsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGovernanceMetrics',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetGovernanceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_metrics_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetGovernanceMetricsResponse:
        """
        @summary 操作审计成熟度查询接口
        
        @param request: GetGovernanceMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGovernanceMetricsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetGovernanceMetrics',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetGovernanceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_metrics(self) -> actiontrail_20200706_models.GetGovernanceMetricsResponse:
        """
        @summary 操作审计成熟度查询接口
        
        @return: GetGovernanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_governance_metrics_with_options(runtime)

    async def get_governance_metrics_async(self) -> actiontrail_20200706_models.GetGovernanceMetricsResponse:
        """
        @summary 操作审计成熟度查询接口
        
        @return: GetGovernanceMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_governance_metrics_with_options_async(runtime)

    def get_trail_status_with_options(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        """
        @summary Queries the status of a trail.
        
        @description This topic describes how to query the status of a sample single-account trail named `trail-test`.
        
        @param request: GetTrailStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrailStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trail_status_with_options_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        """
        @summary Queries the status of a trail.
        
        @description This topic describes how to query the status of a sample single-account trail named `trail-test`.
        
        @param request: GetTrailStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTrailStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_organization_trail):
            query['IsOrganizationTrail'] = request.is_organization_trail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrailStatus',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.GetTrailStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trail_status(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        """
        @summary Queries the status of a trail.
        
        @description This topic describes how to query the status of a sample single-account trail named `trail-test`.
        
        @param request: GetTrailStatusRequest
        @return: GetTrailStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trail_status_with_options(request, runtime)

    async def get_trail_status_async(
        self,
        request: actiontrail_20200706_models.GetTrailStatusRequest,
    ) -> actiontrail_20200706_models.GetTrailStatusResponse:
        """
        @summary Queries the status of a trail.
        
        @description This topic describes how to query the status of a sample single-account trail named `trail-test`.
        
        @param request: GetTrailStatusRequest
        @return: GetTrailStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_trail_status_with_options_async(request, runtime)

    def list_data_event_services_with_options(
        self,
        request: actiontrail_20200706_models.ListDataEventServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDataEventServicesResponse:
        """
        @summary 查询数据事件支持的服务与事件名称
        
        @param request: ListDataEventServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataEventServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataEventServices',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDataEventServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_event_services_with_options_async(
        self,
        request: actiontrail_20200706_models.ListDataEventServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDataEventServicesResponse:
        """
        @summary 查询数据事件支持的服务与事件名称
        
        @param request: ListDataEventServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataEventServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataEventServices',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDataEventServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_event_services(
        self,
        request: actiontrail_20200706_models.ListDataEventServicesRequest,
    ) -> actiontrail_20200706_models.ListDataEventServicesResponse:
        """
        @summary 查询数据事件支持的服务与事件名称
        
        @param request: ListDataEventServicesRequest
        @return: ListDataEventServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_event_services_with_options(request, runtime)

    async def list_data_event_services_async(
        self,
        request: actiontrail_20200706_models.ListDataEventServicesRequest,
    ) -> actiontrail_20200706_models.ListDataEventServicesResponse:
        """
        @summary 查询数据事件支持的服务与事件名称
        
        @param request: ListDataEventServicesRequest
        @return: ListDataEventServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_event_services_with_options_async(request, runtime)

    def list_delivery_history_jobs_with_options(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        """
        @summary Queries a list of data backfill tasks.
        
        @description This topic provides an example on how to query a list of data backfill tasks. The returned result shows that a data backfill task with the ID `16602` is used to deliver historical events for a trail named `trail-name` to Simple Log Service.
        
        @param request: ListDeliveryHistoryJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeliveryHistoryJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeliveryHistoryJobs',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_history_jobs_with_options_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        """
        @summary Queries a list of data backfill tasks.
        
        @description This topic provides an example on how to query a list of data backfill tasks. The returned result shows that a data backfill task with the ID `16602` is used to deliver historical events for a trail named `trail-name` to Simple Log Service.
        
        @param request: ListDeliveryHistoryJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeliveryHistoryJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeliveryHistoryJobs',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.ListDeliveryHistoryJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery_history_jobs(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        """
        @summary Queries a list of data backfill tasks.
        
        @description This topic provides an example on how to query a list of data backfill tasks. The returned result shows that a data backfill task with the ID `16602` is used to deliver historical events for a trail named `trail-name` to Simple Log Service.
        
        @param request: ListDeliveryHistoryJobsRequest
        @return: ListDeliveryHistoryJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delivery_history_jobs_with_options(request, runtime)

    async def list_delivery_history_jobs_async(
        self,
        request: actiontrail_20200706_models.ListDeliveryHistoryJobsRequest,
    ) -> actiontrail_20200706_models.ListDeliveryHistoryJobsResponse:
        """
        @summary Queries a list of data backfill tasks.
        
        @description This topic provides an example on how to query a list of data backfill tasks. The returned result shows that a data backfill task with the ID `16602` is used to deliver historical events for a trail named `trail-name` to Simple Log Service.
        
        @param request: ListDeliveryHistoryJobsRequest
        @return: ListDeliveryHistoryJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_delivery_history_jobs_with_options_async(request, runtime)

    def lookup_events_with_options(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        """
        @summary Queries event details.
        
        @description When you call this operation to query event details, you can query the event details at most twice per second.
        > Do not frequently call this operation. You can create a trail to deliver events to Log Service. Then, you can query event details in near real time by using the real-time log consumption feature of Log Service. For more information, see [Create a single-account trail](https://help.aliyun.com/document_detail/28810.html), [Create a multi-account trail](https://help.aliyun.com/document_detail/160661.html), and [Overview](https://help.aliyun.com/document_detail/28997.html).
        
        @param request: LookupEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_events_with_options_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        """
        @summary Queries event details.
        
        @description When you call this operation to query event details, you can query the event details at most twice per second.
        > Do not frequently call this operation. You can create a trail to deliver events to Log Service. Then, you can query event details in near real time by using the real-time log consumption feature of Log Service. For more information, see [Create a single-account trail](https://help.aliyun.com/document_detail/28810.html), [Create a multi-account trail](https://help.aliyun.com/document_detail/160661.html), and [Overview](https://help.aliyun.com/document_detail/28997.html).
        
        @param request: LookupEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lookup_attribute):
            query['LookupAttribute'] = request.lookup_attribute
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupEvents',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.LookupEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_events(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        """
        @summary Queries event details.
        
        @description When you call this operation to query event details, you can query the event details at most twice per second.
        > Do not frequently call this operation. You can create a trail to deliver events to Log Service. Then, you can query event details in near real time by using the real-time log consumption feature of Log Service. For more information, see [Create a single-account trail](https://help.aliyun.com/document_detail/28810.html), [Create a multi-account trail](https://help.aliyun.com/document_detail/160661.html), and [Overview](https://help.aliyun.com/document_detail/28997.html).
        
        @param request: LookupEventsRequest
        @return: LookupEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lookup_events_with_options(request, runtime)

    async def lookup_events_async(
        self,
        request: actiontrail_20200706_models.LookupEventsRequest,
    ) -> actiontrail_20200706_models.LookupEventsResponse:
        """
        @summary Queries event details.
        
        @description When you call this operation to query event details, you can query the event details at most twice per second.
        > Do not frequently call this operation. You can create a trail to deliver events to Log Service. Then, you can query event details in near real time by using the real-time log consumption feature of Log Service. For more information, see [Create a single-account trail](https://help.aliyun.com/document_detail/28810.html), [Create a multi-account trail](https://help.aliyun.com/document_detail/160661.html), and [Overview](https://help.aliyun.com/document_detail/28997.html).
        
        @param request: LookupEventsRequest
        @return: LookupEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lookup_events_with_options_async(request, runtime)

    def start_logging_with_options(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        """
        @summary Enables a trail to deliver events to an Object Storage Service (OSS) bucket or a Simple Log Service Logstore.
        
        @description This topic describes how to enable logging for a sample trail named `trail-test`.
        
        @param request: StartLoggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLoggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        """
        @summary Enables a trail to deliver events to an Object Storage Service (OSS) bucket or a Simple Log Service Logstore.
        
        @description This topic describes how to enable logging for a sample trail named `trail-test`.
        
        @param request: StartLoggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartLoggingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StartLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_logging(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        """
        @summary Enables a trail to deliver events to an Object Storage Service (OSS) bucket or a Simple Log Service Logstore.
        
        @description This topic describes how to enable logging for a sample trail named `trail-test`.
        
        @param request: StartLoggingRequest
        @return: StartLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_logging_with_options(request, runtime)

    async def start_logging_async(
        self,
        request: actiontrail_20200706_models.StartLoggingRequest,
    ) -> actiontrail_20200706_models.StartLoggingResponse:
        """
        @summary Enables a trail to deliver events to an Object Storage Service (OSS) bucket or a Simple Log Service Logstore.
        
        @description This topic describes how to enable logging for a sample trail named `trail-test`.
        
        @param request: StartLoggingRequest
        @return: StartLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_logging_with_options_async(request, runtime)

    def stop_logging_with_options(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        """
        @summary Disables a trail to stop the delivery of events to an Object Storage Service (OSS) bucket or a  Simple Log Service Logstore.
        
        @description This topic describes how to disable logging for a sample trail named `trail-test`.
        
        @param request: StopLoggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLoggingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_logging_with_options_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        """
        @summary Disables a trail to stop the delivery of events to an Object Storage Service (OSS) bucket or a  Simple Log Service Logstore.
        
        @description This topic describes how to disable logging for a sample trail named `trail-test`.
        
        @param request: StopLoggingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopLoggingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLogging',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.StopLoggingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_logging(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        """
        @summary Disables a trail to stop the delivery of events to an Object Storage Service (OSS) bucket or a  Simple Log Service Logstore.
        
        @description This topic describes how to disable logging for a sample trail named `trail-test`.
        
        @param request: StopLoggingRequest
        @return: StopLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_logging_with_options(request, runtime)

    async def stop_logging_async(
        self,
        request: actiontrail_20200706_models.StopLoggingRequest,
    ) -> actiontrail_20200706_models.StopLoggingResponse:
        """
        @summary Disables a trail to stop the delivery of events to an Object Storage Service (OSS) bucket or a  Simple Log Service Logstore.
        
        @description This topic describes how to disable logging for a sample trail named `trail-test`.
        
        @param request: StopLoggingRequest
        @return: StopLoggingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_logging_with_options_async(request, runtime)

    def update_advanced_query_template_with_options(
        self,
        request: actiontrail_20200706_models.UpdateAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse:
        """
        @summary 更新高级查询模板
        
        @param request: UpdateAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_advanced_query_template_with_options_async(
        self,
        request: actiontrail_20200706_models.UpdateAdvancedQueryTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse:
        """
        @summary 更新高级查询模板
        
        @param request: UpdateAdvancedQueryTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAdvancedQueryTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.simple_query):
            query['SimpleQuery'] = request.simple_query
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_sql):
            query['TemplateSql'] = request.template_sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAdvancedQueryTemplate',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_advanced_query_template(
        self,
        request: actiontrail_20200706_models.UpdateAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse:
        """
        @summary 更新高级查询模板
        
        @param request: UpdateAdvancedQueryTemplateRequest
        @return: UpdateAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_advanced_query_template_with_options(request, runtime)

    async def update_advanced_query_template_async(
        self,
        request: actiontrail_20200706_models.UpdateAdvancedQueryTemplateRequest,
    ) -> actiontrail_20200706_models.UpdateAdvancedQueryTemplateResponse:
        """
        @summary 更新高级查询模板
        
        @param request: UpdateAdvancedQueryTemplateRequest
        @return: UpdateAdvancedQueryTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_advanced_query_template_with_options_async(request, runtime)

    def update_global_events_storage_region_with_options(
        self,
        request: actiontrail_20200706_models.UpdateGlobalEventsStorageRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse:
        """
        @summary Specifies the region where you want to store global events.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        Only the China (Hangzhou) region (cn-hangzhou) and the Singapore region (ap-southeast-1) are supported.
        
        @param request: UpdateGlobalEventsStorageRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGlobalEventsStorageRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGlobalEventsStorageRegion',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_global_events_storage_region_with_options_async(
        self,
        request: actiontrail_20200706_models.UpdateGlobalEventsStorageRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse:
        """
        @summary Specifies the region where you want to store global events.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        Only the China (Hangzhou) region (cn-hangzhou) and the Singapore region (ap-southeast-1) are supported.
        
        @param request: UpdateGlobalEventsStorageRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGlobalEventsStorageRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGlobalEventsStorageRegion',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_global_events_storage_region(
        self,
        request: actiontrail_20200706_models.UpdateGlobalEventsStorageRegionRequest,
    ) -> actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse:
        """
        @summary Specifies the region where you want to store global events.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        Only the China (Hangzhou) region (cn-hangzhou) and the Singapore region (ap-southeast-1) are supported.
        
        @param request: UpdateGlobalEventsStorageRegionRequest
        @return: UpdateGlobalEventsStorageRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_global_events_storage_region_with_options(request, runtime)

    async def update_global_events_storage_region_async(
        self,
        request: actiontrail_20200706_models.UpdateGlobalEventsStorageRegionRequest,
    ) -> actiontrail_20200706_models.UpdateGlobalEventsStorageRegionResponse:
        """
        @summary Specifies the region where you want to store global events.
        
        @description By default, global events are stored in the Singapore region.
        To obtain the permissions to call the API operation, you must submit a ticket.
        Only the China (Hangzhou) region (cn-hangzhou) and the Singapore region (ap-southeast-1) are supported.
        
        @param request: UpdateGlobalEventsStorageRegionRequest
        @return: UpdateGlobalEventsStorageRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_global_events_storage_region_with_options_async(request, runtime)

    def update_trail_with_options(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        """
        @summary Updates the configurations of a trail.
        
        @description This topic shows you how to change the destination Object Storage Service (OSS) bucket of a sample trail named `trail-test` to `audit-log`.
        
        @param request: UpdateTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not UtilClient.is_unset(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trail_with_options_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        """
        @summary Updates the configurations of a trail.
        
        @description This topic shows you how to change the destination Object Storage Service (OSS) bucket of a sample trail named `trail-test` to `audit-log`.
        
        @param request: UpdateTrailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTrailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_rw):
            query['EventRW'] = request.event_rw
        if not UtilClient.is_unset(request.max_compute_project_arn):
            query['MaxComputeProjectArn'] = request.max_compute_project_arn
        if not UtilClient.is_unset(request.max_compute_write_role_arn):
            query['MaxComputeWriteRoleArn'] = request.max_compute_write_role_arn
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_key_prefix):
            query['OssKeyPrefix'] = request.oss_key_prefix
        if not UtilClient.is_unset(request.oss_write_role_arn):
            query['OssWriteRoleArn'] = request.oss_write_role_arn
        if not UtilClient.is_unset(request.sls_project_arn):
            query['SlsProjectArn'] = request.sls_project_arn
        if not UtilClient.is_unset(request.sls_write_role_arn):
            query['SlsWriteRoleArn'] = request.sls_write_role_arn
        if not UtilClient.is_unset(request.trail_region):
            query['TrailRegion'] = request.trail_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTrail',
            version='2020-07-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            actiontrail_20200706_models.UpdateTrailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trail(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        """
        @summary Updates the configurations of a trail.
        
        @description This topic shows you how to change the destination Object Storage Service (OSS) bucket of a sample trail named `trail-test` to `audit-log`.
        
        @param request: UpdateTrailRequest
        @return: UpdateTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_trail_with_options(request, runtime)

    async def update_trail_async(
        self,
        request: actiontrail_20200706_models.UpdateTrailRequest,
    ) -> actiontrail_20200706_models.UpdateTrailResponse:
        """
        @summary Updates the configurations of a trail.
        
        @description This topic shows you how to change the destination Object Storage Service (OSS) bucket of a sample trail named `trail-test` to `audit-log`.
        
        @param request: UpdateTrailRequest
        @return: UpdateTrailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_trail_with_options_async(request, runtime)
