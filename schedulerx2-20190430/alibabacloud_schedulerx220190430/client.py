# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_schedulerx220190430 import models as schedulerx_220190430_models
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
            'cn-beijing': 'schedulerx.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'schedulerx.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'schedulerx.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'schedulerx.cn-shenzhen.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('schedulerx2', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_delete_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        """
        @summary Deletes multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        """
        @summary Deletes multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDeleteJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_jobs(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        """
        @summary Deletes multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDeleteJobsRequest
        @return: BatchDeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_jobs_with_options(request, runtime)

    async def batch_delete_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteJobsRequest,
    ) -> schedulerx_220190430_models.BatchDeleteJobsResponse:
        """
        @summary Deletes multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDeleteJobsRequest
        @return: BatchDeleteJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_jobs_with_options_async(request, runtime)

    def batch_delete_route_strategy_with_options(
        self,
        request: schedulerx_220190430_models.BatchDeleteRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteRouteStrategyResponse:
        """
        @summary The additional information that is returned.
        
        @param request: BatchDeleteRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_route_strategy_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDeleteRouteStrategyResponse:
        """
        @summary The additional information that is returned.
        
        @param request: BatchDeleteRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDeleteRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_route_strategy(
        self,
        request: schedulerx_220190430_models.BatchDeleteRouteStrategyRequest,
    ) -> schedulerx_220190430_models.BatchDeleteRouteStrategyResponse:
        """
        @summary The additional information that is returned.
        
        @param request: BatchDeleteRouteStrategyRequest
        @return: BatchDeleteRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_route_strategy_with_options(request, runtime)

    async def batch_delete_route_strategy_async(
        self,
        request: schedulerx_220190430_models.BatchDeleteRouteStrategyRequest,
    ) -> schedulerx_220190430_models.BatchDeleteRouteStrategyResponse:
        """
        @summary The additional information that is returned.
        
        @param request: BatchDeleteRouteStrategyRequest
        @return: BatchDeleteRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_route_strategy_with_options_async(request, runtime)

    def batch_disable_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        """
        @summary Disables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDisableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDisableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDisableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDisableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_disable_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        """
        @summary Disables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDisableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDisableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDisableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchDisableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_disable_jobs(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        """
        @summary Disables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDisableJobsRequest
        @return: BatchDisableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_disable_jobs_with_options(request, runtime)

    async def batch_disable_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchDisableJobsRequest,
    ) -> schedulerx_220190430_models.BatchDisableJobsResponse:
        """
        @summary Disables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchDisableJobsRequest
        @return: BatchDisableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_disable_jobs_with_options_async(request, runtime)

    def batch_enable_jobs_with_options(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        """
        @summary Enables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchEnableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchEnableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchEnableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchEnableJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_enable_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        """
        @summary Enables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchEnableJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchEnableJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.job_id_list):
            body['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchEnableJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.BatchEnableJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_enable_jobs(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        """
        @summary Enables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchEnableJobsRequest
        @return: BatchEnableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_enable_jobs_with_options(request, runtime)

    async def batch_enable_jobs_async(
        self,
        request: schedulerx_220190430_models.BatchEnableJobsRequest,
    ) -> schedulerx_220190430_models.BatchEnableJobsResponse:
        """
        @summary Enables multiple jobs at a time.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.4</version>
        </dependency>
        ```
        
        @param request: BatchEnableJobsRequest
        @return: BatchEnableJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_enable_jobs_with_options_async(request, runtime)

    def create_app_group_with_options(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        """
        @summary Creates an application group. The AppKey is returned.
        
        @param request: CreateAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        """
        @summary Creates an application group. The AppKey is returned.
        
        @param request: CreateAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        """
        @summary Creates an application group. The AppKey is returned.
        
        @param request: CreateAppGroupRequest
        @return: CreateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    async def create_app_group_async(
        self,
        request: schedulerx_220190430_models.CreateAppGroupRequest,
    ) -> schedulerx_220190430_models.CreateAppGroupResponse:
        """
        @summary Creates an application group. The AppKey is returned.
        
        @param request: CreateAppGroupRequest
        @return: CreateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_group_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        """
        @summary Creates a job and obtains the job ID.
        
        @param request: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        """
        @summary Creates a job and obtains the job ID.
        
        @param request: CreateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            body['JobType'] = request.job_type
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        """
        @summary Creates a job and obtains the job ID.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: schedulerx_220190430_models.CreateJobRequest,
    ) -> schedulerx_220190430_models.CreateJobResponse:
        """
        @summary Creates a job and obtains the job ID.
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        """
        @summary Creates a namespace.
        
        @param request: CreateNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        """
        @summary Creates a namespace.
        
        @param request: CreateNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNamespace',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        """
        @summary Creates a namespace.
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: schedulerx_220190430_models.CreateNamespaceRequest,
    ) -> schedulerx_220190430_models.CreateNamespaceResponse:
        """
        @summary Creates a namespace.
        
        @param request: CreateNamespaceRequest
        @return: CreateNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_route_strategy_with_options(
        self,
        request: schedulerx_220190430_models.CreateRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateRouteStrategyResponse:
        """
        @summary Creates a routing policy.
        
        @param request: CreateRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.strategy_content):
            query['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_route_strategy_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateRouteStrategyResponse:
        """
        @summary Creates a routing policy.
        
        @param request: CreateRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.strategy_content):
            query['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_route_strategy(
        self,
        request: schedulerx_220190430_models.CreateRouteStrategyRequest,
    ) -> schedulerx_220190430_models.CreateRouteStrategyResponse:
        """
        @summary Creates a routing policy.
        
        @param request: CreateRouteStrategyRequest
        @return: CreateRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_route_strategy_with_options(request, runtime)

    async def create_route_strategy_async(
        self,
        request: schedulerx_220190430_models.CreateRouteStrategyRequest,
    ) -> schedulerx_220190430_models.CreateRouteStrategyResponse:
        """
        @summary Creates a routing policy.
        
        @param request: CreateRouteStrategyRequest
        @return: CreateRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_route_strategy_with_options_async(request, runtime)

    def create_workflow_with_options(
        self,
        request: schedulerx_220190430_models.CreateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateWorkflowResponse:
        """
        @summary Creates a workflow. By default, the created workflow is disabled. After you update the directed acyclic graph (DAG) of the workflow, you must manually or call the corresponding operation to enable the workflow. You can call this operation only in the professional edition.
        
        @param request: CreateWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.CreateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.CreateWorkflowResponse:
        """
        @summary Creates a workflow. By default, the created workflow is disabled. After you update the directed acyclic graph (DAG) of the workflow, you must manually or call the corresponding operation to enable the workflow. You can call this operation only in the professional edition.
        
        @param request: CreateWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.CreateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workflow(
        self,
        request: schedulerx_220190430_models.CreateWorkflowRequest,
    ) -> schedulerx_220190430_models.CreateWorkflowResponse:
        """
        @summary Creates a workflow. By default, the created workflow is disabled. After you update the directed acyclic graph (DAG) of the workflow, you must manually or call the corresponding operation to enable the workflow. You can call this operation only in the professional edition.
        
        @param request: CreateWorkflowRequest
        @return: CreateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_workflow_with_options(request, runtime)

    async def create_workflow_async(
        self,
        request: schedulerx_220190430_models.CreateWorkflowRequest,
    ) -> schedulerx_220190430_models.CreateWorkflowResponse:
        """
        @summary Creates a workflow. By default, the created workflow is disabled. After you update the directed acyclic graph (DAG) of the workflow, you must manually or call the corresponding operation to enable the workflow. You can call this operation only in the professional edition.
        
        @param request: CreateWorkflowRequest
        @return: CreateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_workflow_with_options_async(request, runtime)

    def delete_app_group_with_options(
        self,
        request: schedulerx_220190430_models.DeleteAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: DeleteAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_jobs):
            query['DeleteJobs'] = request.delete_jobs
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_group_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: DeleteAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_jobs):
            query['DeleteJobs'] = request.delete_jobs
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_group(
        self,
        request: schedulerx_220190430_models.DeleteAppGroupRequest,
    ) -> schedulerx_220190430_models.DeleteAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: DeleteAppGroupRequest
        @return: DeleteAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_group_with_options(request, runtime)

    async def delete_app_group_async(
        self,
        request: schedulerx_220190430_models.DeleteAppGroupRequest,
    ) -> schedulerx_220190430_models.DeleteAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: DeleteAppGroupRequest
        @return: DeleteAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_group_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        """
        @summary Deletes a specified job.
        
        @param request: DeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        """
        @summary Deletes a specified job.
        
        @param request: DeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        """
        @summary Deletes a specified job.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: schedulerx_220190430_models.DeleteJobRequest,
    ) -> schedulerx_220190430_models.DeleteJobResponse:
        """
        @summary Deletes a specified job.
        
        @param request: DeleteJobRequest
        @return: DeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_route_strategy_with_options(
        self,
        request: schedulerx_220190430_models.DeleteRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteRouteStrategyResponse:
        """
        @summary Deletes a routing policy.
        
        @param request: DeleteRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteRouteStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_strategy_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteRouteStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteRouteStrategyResponse:
        """
        @summary Deletes a routing policy.
        
        @param request: DeleteRouteStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRouteStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRouteStrategy',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteRouteStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_strategy(
        self,
        request: schedulerx_220190430_models.DeleteRouteStrategyRequest,
    ) -> schedulerx_220190430_models.DeleteRouteStrategyResponse:
        """
        @summary Deletes a routing policy.
        
        @param request: DeleteRouteStrategyRequest
        @return: DeleteRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_route_strategy_with_options(request, runtime)

    async def delete_route_strategy_async(
        self,
        request: schedulerx_220190430_models.DeleteRouteStrategyRequest,
    ) -> schedulerx_220190430_models.DeleteRouteStrategyResponse:
        """
        @summary Deletes a routing policy.
        
        @param request: DeleteRouteStrategyRequest
        @return: DeleteRouteStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_strategy_with_options_async(request, runtime)

    def delete_workflow_with_options(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        """
        @summary Deletes a workflow.
        
        @param request: DeleteWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        """
        @summary Deletes a workflow.
        
        @param request: DeleteWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DeleteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workflow(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        """
        @summary Deletes a workflow.
        
        @param request: DeleteWorkflowRequest
        @return: DeleteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_workflow_with_options(request, runtime)

    async def delete_workflow_async(
        self,
        request: schedulerx_220190430_models.DeleteWorkflowRequest,
    ) -> schedulerx_220190430_models.DeleteWorkflowResponse:
        """
        @summary Deletes a workflow.
        
        @param request: DeleteWorkflowRequest
        @return: DeleteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_workflow_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: schedulerx_220190430_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        """
        @summary Returns available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: schedulerx_220190430_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        """
        @summary Returns available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: schedulerx_220190430_models.DescribeRegionsRequest,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        """
        @summary Returns available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: schedulerx_220190430_models.DescribeRegionsRequest,
    ) -> schedulerx_220190430_models.DescribeRegionsResponse:
        """
        @summary Returns available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def designate_workers_with_options(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        """
        @summary Designates machines.
        
        @param request: DesignateWorkersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DesignateWorkersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesignateWorkers',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DesignateWorkersResponse(),
            self.call_api(params, req, runtime)
        )

    async def designate_workers_with_options_async(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        """
        @summary Designates machines.
        
        @param request: DesignateWorkersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DesignateWorkersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DesignateWorkers',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DesignateWorkersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def designate_workers(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        """
        @summary Designates machines.
        
        @param request: DesignateWorkersRequest
        @return: DesignateWorkersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.designate_workers_with_options(request, runtime)

    async def designate_workers_async(
        self,
        request: schedulerx_220190430_models.DesignateWorkersRequest,
    ) -> schedulerx_220190430_models.DesignateWorkersResponse:
        """
        @summary Designates machines.
        
        @param request: DesignateWorkersRequest
        @return: DesignateWorkersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.designate_workers_with_options_async(request, runtime)

    def disable_job_with_options(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        """
        @summary Disables a job.
        
        @param request: DisableJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_job_with_options_async(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        """
        @summary Disables a job.
        
        @param request: DisableJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_job(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        """
        @summary Disables a job.
        
        @param request: DisableJobRequest
        @return: DisableJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_job_with_options(request, runtime)

    async def disable_job_async(
        self,
        request: schedulerx_220190430_models.DisableJobRequest,
    ) -> schedulerx_220190430_models.DisableJobResponse:
        """
        @summary Disables a job.
        
        @param request: DisableJobRequest
        @return: DisableJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_job_with_options_async(request, runtime)

    def disable_workflow_with_options(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        """
        @summary Disables a specified workflow.
        
        @param request: DisableWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        """
        @summary Disables a specified workflow.
        
        @param request: DisableWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.DisableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_workflow(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        """
        @summary Disables a specified workflow.
        
        @param request: DisableWorkflowRequest
        @return: DisableWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_workflow_with_options(request, runtime)

    async def disable_workflow_async(
        self,
        request: schedulerx_220190430_models.DisableWorkflowRequest,
    ) -> schedulerx_220190430_models.DisableWorkflowResponse:
        """
        @summary Disables a specified workflow.
        
        @param request: DisableWorkflowRequest
        @return: DisableWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_workflow_with_options_async(request, runtime)

    def enable_job_with_options(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        """
        @summary Enables a job.
        
        @param request: EnableJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_job_with_options_async(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        """
        @summary Enables a job.
        
        @param request: EnableJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_job(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        """
        @summary Enables a job.
        
        @param request: EnableJobRequest
        @return: EnableJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_job_with_options(request, runtime)

    async def enable_job_async(
        self,
        request: schedulerx_220190430_models.EnableJobRequest,
    ) -> schedulerx_220190430_models.EnableJobResponse:
        """
        @summary Enables a job.
        
        @param request: EnableJobRequest
        @return: EnableJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_job_with_options_async(request, runtime)

    def enable_workflow_with_options(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        """
        @summary Enables a specified workflow.
        
        @param request: EnableWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        """
        @summary Enables a specified workflow.
        
        @param request: EnableWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.EnableWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_workflow(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        """
        @summary Enables a specified workflow.
        
        @param request: EnableWorkflowRequest
        @return: EnableWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_workflow_with_options(request, runtime)

    async def enable_workflow_async(
        self,
        request: schedulerx_220190430_models.EnableWorkflowRequest,
    ) -> schedulerx_220190430_models.EnableWorkflowResponse:
        """
        @summary Enables a specified workflow.
        
        @param request: EnableWorkflowRequest
        @return: EnableWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_workflow_with_options_async(request, runtime)

    def execute_job_with_options(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        """
        @summary Triggers a job to immediately run once.
        
        @description > The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        
        @param request: ExecuteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_job_with_options_async(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        """
        @summary Triggers a job to immediately run once.
        
        @description > The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        
        @param request: ExecuteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_job(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        """
        @summary Triggers a job to immediately run once.
        
        @description > The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        
        @param request: ExecuteJobRequest
        @return: ExecuteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_job_with_options(request, runtime)

    async def execute_job_async(
        self,
        request: schedulerx_220190430_models.ExecuteJobRequest,
    ) -> schedulerx_220190430_models.ExecuteJobResponse:
        """
        @summary Triggers a job to immediately run once.
        
        @description > The combination of the `JobID` and `ScheduleTime` parameters serves as a unique index. Therefore, after the ExecuteJob operation is called to run a job once, a sleep for one second is required before the ExecuteJob operation is called to run the job again. Otherwise, the job may fail.
        
        @param request: ExecuteJobRequest
        @return: ExecuteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_job_with_options_async(request, runtime)

    def execute_workflow_with_options(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        """
        @summary Immediately triggers a workflow.
        
        @param request: ExecuteWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        """
        @summary Immediately triggers a workflow.
        
        @param request: ExecuteWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ExecuteWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_workflow(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        """
        @summary Immediately triggers a workflow.
        
        @param request: ExecuteWorkflowRequest
        @return: ExecuteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_workflow_with_options(request, runtime)

    async def execute_workflow_async(
        self,
        request: schedulerx_220190430_models.ExecuteWorkflowRequest,
    ) -> schedulerx_220190430_models.ExecuteWorkflowResponse:
        """
        @summary Immediately triggers a workflow.
        
        @param request: ExecuteWorkflowRequest
        @return: ExecuteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_workflow_with_options_async(request, runtime)

    def get_app_group_with_options(
        self,
        request: schedulerx_220190430_models.GetAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetAppGroupResponse:
        """
        @summary The configuration of the alert. The value is a JSON string. For more information, see \\\\*the additional information about response parameters below this table\\*\\*.
        
        @param request: GetAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_group_with_options_async(
        self,
        request: schedulerx_220190430_models.GetAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetAppGroupResponse:
        """
        @summary The configuration of the alert. The value is a JSON string. For more information, see \\\\*the additional information about response parameters below this table\\*\\*.
        
        @param request: GetAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_group(
        self,
        request: schedulerx_220190430_models.GetAppGroupRequest,
    ) -> schedulerx_220190430_models.GetAppGroupResponse:
        """
        @summary The configuration of the alert. The value is a JSON string. For more information, see \\\\*the additional information about response parameters below this table\\*\\*.
        
        @param request: GetAppGroupRequest
        @return: GetAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_app_group_with_options(request, runtime)

    async def get_app_group_async(
        self,
        request: schedulerx_220190430_models.GetAppGroupRequest,
    ) -> schedulerx_220190430_models.GetAppGroupResponse:
        """
        @summary The configuration of the alert. The value is a JSON string. For more information, see \\\\*the additional information about response parameters below this table\\*\\*.
        
        @param request: GetAppGroupRequest
        @return: GetAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_app_group_with_options_async(request, runtime)

    def get_job_info_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        """
        @summary Queries the details of a job based on the job ID. In most cases, the obtained information is used to update jobs.
        
        @param request: GetJobInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        """
        @summary Queries the details of a job based on the job ID. In most cases, the obtained information is used to update jobs.
        
        @param request: GetJobInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInfo',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        """
        @summary Queries the details of a job based on the job ID. In most cases, the obtained information is used to update jobs.
        
        @param request: GetJobInfoRequest
        @return: GetJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_info_with_options(request, runtime)

    async def get_job_info_async(
        self,
        request: schedulerx_220190430_models.GetJobInfoRequest,
    ) -> schedulerx_220190430_models.GetJobInfoResponse:
        """
        @summary Queries the details of a job based on the job ID. In most cases, the obtained information is used to update jobs.
        
        @param request: GetJobInfoRequest
        @return: GetJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_info_with_options_async(request, runtime)

    def get_job_instance_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        """
        @summary Queries the information about a job instance. You can view the status and progress of the job instance.
        
        @param request: GetJobInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        """
        @summary Queries the information about a job instance. You can view the status and progress of the job instance.
        
        @param request: GetJobInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        """
        @summary Queries the information about a job instance. You can view the status and progress of the job instance.
        
        @param request: GetJobInstanceRequest
        @return: GetJobInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_with_options(request, runtime)

    async def get_job_instance_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceResponse:
        """
        @summary Queries the information about a job instance. You can view the status and progress of the job instance.
        
        @param request: GetJobInstanceRequest
        @return: GetJobInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_instance_with_options_async(request, runtime)

    def get_job_instance_list_with_options(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        """
        @summary Queries the most recent 10 execution instances of a job.
        
        @param request: GetJobInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstanceList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_instance_list_with_options_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        """
        @summary Queries the most recent 10 execution instances of a job.
        
        @param request: GetJobInstanceListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobInstanceListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobInstanceList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetJobInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_instance_list(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        """
        @summary Queries the most recent 10 execution instances of a job.
        
        @param request: GetJobInstanceListRequest
        @return: GetJobInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_instance_list_with_options(request, runtime)

    async def get_job_instance_list_async(
        self,
        request: schedulerx_220190430_models.GetJobInstanceListRequest,
    ) -> schedulerx_220190430_models.GetJobInstanceListResponse:
        """
        @summary Queries the most recent 10 execution instances of a job.
        
        @param request: GetJobInstanceListRequest
        @return: GetJobInstanceListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_instance_list_with_options_async(request, runtime)

    def get_log_with_options(
        self,
        request: schedulerx_220190430_models.GetLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetLogResponse:
        """
        @summary Queries the operational logs of a job. You can call this operation only in the professional edition.
        
        @param request: GetLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLog',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_with_options_async(
        self,
        request: schedulerx_220190430_models.GetLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetLogResponse:
        """
        @summary Queries the operational logs of a job. You can call this operation only in the professional edition.
        
        @param request: GetLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLog',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log(
        self,
        request: schedulerx_220190430_models.GetLogRequest,
    ) -> schedulerx_220190430_models.GetLogResponse:
        """
        @summary Queries the operational logs of a job. You can call this operation only in the professional edition.
        
        @param request: GetLogRequest
        @return: GetLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_log_with_options(request, runtime)

    async def get_log_async(
        self,
        request: schedulerx_220190430_models.GetLogRequest,
    ) -> schedulerx_220190430_models.GetLogResponse:
        """
        @summary Queries the operational logs of a job. You can call this operation only in the professional edition.
        
        @param request: GetLogRequest
        @return: GetLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_log_with_options_async(request, runtime)

    def get_overview_with_options(
        self,
        request: schedulerx_220190430_models.GetOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetOverviewResponse:
        """
        @summary 查询概览数据信息
        
        @param request: GetOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.operate):
            query['Operate'] = request.operate
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOverview',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_overview_with_options_async(
        self,
        request: schedulerx_220190430_models.GetOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetOverviewResponse:
        """
        @summary 查询概览数据信息
        
        @param request: GetOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOverviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.operate):
            query['Operate'] = request.operate
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOverview',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_overview(
        self,
        request: schedulerx_220190430_models.GetOverviewRequest,
    ) -> schedulerx_220190430_models.GetOverviewResponse:
        """
        @summary 查询概览数据信息
        
        @param request: GetOverviewRequest
        @return: GetOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    async def get_overview_async(
        self,
        request: schedulerx_220190430_models.GetOverviewRequest,
    ) -> schedulerx_220190430_models.GetOverviewResponse:
        """
        @summary 查询概览数据信息
        
        @param request: GetOverviewRequest
        @return: GetOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_overview_with_options_async(request, runtime)

    def get_work_flow_with_options(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        """
        @summary Obtains the information about a workflow.
        
        @param request: GetWorkFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkFlowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkFlow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_work_flow_with_options_async(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        """
        @summary Obtains the information about a workflow.
        
        @param request: GetWorkFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkFlowResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkFlow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_work_flow(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        """
        @summary Obtains the information about a workflow.
        
        @param request: GetWorkFlowRequest
        @return: GetWorkFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_work_flow_with_options(request, runtime)

    async def get_work_flow_async(
        self,
        request: schedulerx_220190430_models.GetWorkFlowRequest,
    ) -> schedulerx_220190430_models.GetWorkFlowResponse:
        """
        @summary Obtains the information about a workflow.
        
        @param request: GetWorkFlowRequest
        @return: GetWorkFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_work_flow_with_options_async(request, runtime)

    def get_worker_list_with_options(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        """
        @summary Obtains the list of workers that are connected to an application.
        
        @param request: GetWorkerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkerListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkerList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_worker_list_with_options_async(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        """
        @summary Obtains the list of workers that are connected to an application.
        
        @param request: GetWorkerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkerListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkerList',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_worker_list(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        """
        @summary Obtains the list of workers that are connected to an application.
        
        @param request: GetWorkerListRequest
        @return: GetWorkerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_worker_list_with_options(request, runtime)

    async def get_worker_list_async(
        self,
        request: schedulerx_220190430_models.GetWorkerListRequest,
    ) -> schedulerx_220190430_models.GetWorkerListResponse:
        """
        @summary Obtains the list of workers that are connected to an application.
        
        @param request: GetWorkerListRequest
        @return: GetWorkerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_worker_list_with_options_async(request, runtime)

    def get_workflow_instance_with_options(
        self,
        request: schedulerx_220190430_models.GetWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkflowInstanceResponse:
        """
        @summary Queries the details of a specified workflow instance, including the state of the workflow instance, the state of each job instance, and the dependencies between job instances. You can call this operation only in the professional edition.
        
        @param request: GetWorkflowInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.GetWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GetWorkflowInstanceResponse:
        """
        @summary Queries the details of a specified workflow instance, including the state of the workflow instance, the state of each job instance, and the dependencies between job instances. You can call this operation only in the professional edition.
        
        @param request: GetWorkflowInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GetWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_instance(
        self,
        request: schedulerx_220190430_models.GetWorkflowInstanceRequest,
    ) -> schedulerx_220190430_models.GetWorkflowInstanceResponse:
        """
        @summary Queries the details of a specified workflow instance, including the state of the workflow instance, the state of each job instance, and the dependencies between job instances. You can call this operation only in the professional edition.
        
        @param request: GetWorkflowInstanceRequest
        @return: GetWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_instance_with_options(request, runtime)

    async def get_workflow_instance_async(
        self,
        request: schedulerx_220190430_models.GetWorkflowInstanceRequest,
    ) -> schedulerx_220190430_models.GetWorkflowInstanceResponse:
        """
        @summary Queries the details of a specified workflow instance, including the state of the workflow instance, the state of each job instance, and the dependencies between job instances. You can call this operation only in the professional edition.
        
        @param request: GetWorkflowInstanceRequest
        @return: GetWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_workflow_instance_with_options_async(request, runtime)

    def grant_permission_with_options(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        """
        @summary Grants permissions to an application group.
        
        @param request: GrantPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantPermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GrantPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_permission_with_options_async(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        """
        @summary Grants permissions to an application group.
        
        @param request: GrantPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grant_option):
            query['GrantOption'] = request.grant_option
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantPermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.GrantPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_permission(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        """
        @summary Grants permissions to an application group.
        
        @param request: GrantPermissionRequest
        @return: GrantPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_permission_with_options(request, runtime)

    async def grant_permission_async(
        self,
        request: schedulerx_220190430_models.GrantPermissionRequest,
    ) -> schedulerx_220190430_models.GrantPermissionResponse:
        """
        @summary Grants permissions to an application group.
        
        @param request: GrantPermissionRequest
        @return: GrantPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_permission_with_options_async(request, runtime)

    def list_groups_with_options(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        """
        @summary Queries a list of applications.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        ```
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_group_name):
            query['AppGroupName'] = request.app_group_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_groups_with_options_async(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        """
        @summary Queries a list of applications.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        ```
        
        @param request: ListGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_group_name):
            query['AppGroupName'] = request.app_group_name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroups',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_groups(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        """
        @summary Queries a list of applications.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        ```
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_groups_with_options(request, runtime)

    async def list_groups_async(
        self,
        request: schedulerx_220190430_models.ListGroupsRequest,
    ) -> schedulerx_220190430_models.ListGroupsResponse:
        """
        @summary Queries a list of applications.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        ```xml
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        ```
        
        @param request: ListGroupsRequest
        @return: ListGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_groups_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        """
        @summary Queries jobs.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        """
        @summary Queries jobs.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        """
        @summary Queries jobs.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: schedulerx_220190430_models.ListJobsRequest,
    ) -> schedulerx_220190430_models.ListJobsResponse:
        """
        @summary Queries jobs.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        """
        @summary Queries namespaces.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        """
        @summary Queries namespaces.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNamespaces',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        """
        @summary Queries namespaces.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListNamespacesRequest
        @return: ListNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: schedulerx_220190430_models.ListNamespacesRequest,
    ) -> schedulerx_220190430_models.ListNamespacesResponse:
        """
        @summary Queries namespaces.
        
        @description Before you call this operation, you must add the following dependency to the pom.xml file:
        <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-schedulerx2</artifactId>
        <version>1.0.5</version>
        </dependency>
        
        @param request: ListNamespacesRequest
        @return: ListNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_workflow_instance_with_options(
        self,
        request: schedulerx_220190430_models.ListWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListWorkflowInstanceResponse:
        """
        @summary Queries the execution history of a workflow. You can call this operation only in the professional edition.
        
        @param request: ListWorkflowInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.ListWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.ListWorkflowInstanceResponse:
        """
        @summary Queries the execution history of a workflow. You can call this operation only in the professional edition.
        
        @param request: ListWorkflowInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.ListWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_instance(
        self,
        request: schedulerx_220190430_models.ListWorkflowInstanceRequest,
    ) -> schedulerx_220190430_models.ListWorkflowInstanceResponse:
        """
        @summary Queries the execution history of a workflow. You can call this operation only in the professional edition.
        
        @param request: ListWorkflowInstanceRequest
        @return: ListWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_instance_with_options(request, runtime)

    async def list_workflow_instance_async(
        self,
        request: schedulerx_220190430_models.ListWorkflowInstanceRequest,
    ) -> schedulerx_220190430_models.ListWorkflowInstanceResponse:
        """
        @summary Queries the execution history of a workflow. You can call this operation only in the professional edition.
        
        @param request: ListWorkflowInstanceRequest
        @return: ListWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workflow_instance_with_options_async(request, runtime)

    def rerun_job_with_options(
        self,
        request: schedulerx_220190430_models.RerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RerunJobResponse:
        """
        @summary Reruns a job to obtain the historical data of the job. You can call this operation only in the professional edition.
        
        @param request: RerunJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_time):
            body['DataTime'] = request.data_time
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RerunJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_job_with_options_async(
        self,
        request: schedulerx_220190430_models.RerunJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RerunJobResponse:
        """
        @summary Reruns a job to obtain the historical data of the job. You can call this operation only in the professional edition.
        
        @param request: RerunJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RerunJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_time):
            body['DataTime'] = request.data_time
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RerunJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RerunJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rerun_job(
        self,
        request: schedulerx_220190430_models.RerunJobRequest,
    ) -> schedulerx_220190430_models.RerunJobResponse:
        """
        @summary Reruns a job to obtain the historical data of the job. You can call this operation only in the professional edition.
        
        @param request: RerunJobRequest
        @return: RerunJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    async def rerun_job_async(
        self,
        request: schedulerx_220190430_models.RerunJobRequest,
    ) -> schedulerx_220190430_models.RerunJobResponse:
        """
        @summary Reruns a job to obtain the historical data of the job. You can call this operation only in the professional edition.
        
        @param request: RerunJobRequest
        @return: RerunJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rerun_job_with_options_async(request, runtime)

    def retry_job_instance_with_options(
        self,
        request: schedulerx_220190430_models.RetryJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RetryJobInstanceResponse:
        """
        @summary Reruns a successful or failed job instance. You can call this operation only in the professional edition.
        
        @param request: RetryJobInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryJobInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RetryJobInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_job_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.RetryJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RetryJobInstanceResponse:
        """
        @summary Reruns a successful or failed job instance. You can call this operation only in the professional edition.
        
        @param request: RetryJobInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryJobInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryJobInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RetryJobInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_job_instance(
        self,
        request: schedulerx_220190430_models.RetryJobInstanceRequest,
    ) -> schedulerx_220190430_models.RetryJobInstanceResponse:
        """
        @summary Reruns a successful or failed job instance. You can call this operation only in the professional edition.
        
        @param request: RetryJobInstanceRequest
        @return: RetryJobInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_job_instance_with_options(request, runtime)

    async def retry_job_instance_async(
        self,
        request: schedulerx_220190430_models.RetryJobInstanceRequest,
    ) -> schedulerx_220190430_models.RetryJobInstanceResponse:
        """
        @summary Reruns a successful or failed job instance. You can call this operation only in the professional edition.
        
        @param request: RetryJobInstanceRequest
        @return: RetryJobInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_job_instance_with_options_async(request, runtime)

    def revoke_permission_with_options(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        """
        @summary Revokes the permissions that are granted to an Alibaba Cloud Resource Access Management (RAM) user.
        
        @param request: RevokePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokePermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RevokePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_permission_with_options_async(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        """
        @summary Revokes the permissions that are granted to an Alibaba Cloud Resource Access Management (RAM) user.
        
        @param request: RevokePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokePermission',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.RevokePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_permission(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        """
        @summary Revokes the permissions that are granted to an Alibaba Cloud Resource Access Management (RAM) user.
        
        @param request: RevokePermissionRequest
        @return: RevokePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_permission_with_options(request, runtime)

    async def revoke_permission_async(
        self,
        request: schedulerx_220190430_models.RevokePermissionRequest,
    ) -> schedulerx_220190430_models.RevokePermissionResponse:
        """
        @summary Revokes the permissions that are granted to an Alibaba Cloud Resource Access Management (RAM) user.
        
        @param request: RevokePermissionRequest
        @return: RevokePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_permission_with_options_async(request, runtime)

    def set_job_instance_success_with_options(
        self,
        request: schedulerx_220190430_models.SetJobInstanceSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.SetJobInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a job instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetJobInstanceSuccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetJobInstanceSuccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetJobInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetJobInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_job_instance_success_with_options_async(
        self,
        request: schedulerx_220190430_models.SetJobInstanceSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.SetJobInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a job instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetJobInstanceSuccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetJobInstanceSuccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetJobInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetJobInstanceSuccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_job_instance_success(
        self,
        request: schedulerx_220190430_models.SetJobInstanceSuccessRequest,
    ) -> schedulerx_220190430_models.SetJobInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a job instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetJobInstanceSuccessRequest
        @return: SetJobInstanceSuccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_job_instance_success_with_options(request, runtime)

    async def set_job_instance_success_async(
        self,
        request: schedulerx_220190430_models.SetJobInstanceSuccessRequest,
    ) -> schedulerx_220190430_models.SetJobInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a job instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetJobInstanceSuccessRequest
        @return: SetJobInstanceSuccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_job_instance_success_with_options_async(request, runtime)

    def set_wf_instance_success_with_options(
        self,
        request: schedulerx_220190430_models.SetWfInstanceSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.SetWfInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a workflow instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetWfInstanceSuccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetWfInstanceSuccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wf_instance_id):
            query['WfInstanceId'] = request.wf_instance_id
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWfInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetWfInstanceSuccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_wf_instance_success_with_options_async(
        self,
        request: schedulerx_220190430_models.SetWfInstanceSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.SetWfInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a workflow instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetWfInstanceSuccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetWfInstanceSuccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            query['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.wf_instance_id):
            query['WfInstanceId'] = request.wf_instance_id
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWfInstanceSuccess',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.SetWfInstanceSuccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_wf_instance_success(
        self,
        request: schedulerx_220190430_models.SetWfInstanceSuccessRequest,
    ) -> schedulerx_220190430_models.SetWfInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a workflow instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetWfInstanceSuccessRequest
        @return: SetWfInstanceSuccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_wf_instance_success_with_options(request, runtime)

    async def set_wf_instance_success_async(
        self,
        request: schedulerx_220190430_models.SetWfInstanceSuccessRequest,
    ) -> schedulerx_220190430_models.SetWfInstanceSuccessResponse:
        """
        @summary Forcibly sets the state of a workflow instance to successful. You can call this operation only in the professional edition.
        
        @param request: SetWfInstanceSuccessRequest
        @return: SetWfInstanceSuccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_wf_instance_success_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        """
        @summary Stops a job instance in the running state.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        """
        @summary Stops a job instance in the running state.
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        """
        @summary Stops a job instance in the running state.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: schedulerx_220190430_models.StopInstanceRequest,
    ) -> schedulerx_220190430_models.StopInstanceResponse:
        """
        @summary Stops a job instance in the running state.
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def update_app_group_with_options(
        self,
        request: schedulerx_220190430_models.UpdateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: UpdateAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_group_with_options_async(
        self,
        request: schedulerx_220190430_models.UpdateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: UpdateAppGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.max_concurrency):
            query['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAppGroup',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_group(
        self,
        request: schedulerx_220190430_models.UpdateAppGroupRequest,
    ) -> schedulerx_220190430_models.UpdateAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: UpdateAppGroupRequest
        @return: UpdateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_app_group_with_options(request, runtime)

    async def update_app_group_async(
        self,
        request: schedulerx_220190430_models.UpdateAppGroupRequest,
    ) -> schedulerx_220190430_models.UpdateAppGroupResponse:
        """
        @summary The additional information that is returned.
        
        @param request: UpdateAppGroupRequest
        @return: UpdateAppGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_app_group_with_options_async(request, runtime)

    def update_job_with_options(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        """
        @summary Updates the configuration information about a job. By default, you need to call the GetJobInfo operation to obtain the original configuration of the job before you call this operation to modify the configuration as required.
        
        @param request: UpdateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_dispatch_mode):
            body['TaskDispatchMode'] = request.task_dispatch_mode
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.template):
            body['Template'] = request.template
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_with_options_async(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        """
        @summary Updates the configuration information about a job. By default, you need to call the GetJobInfo operation to obtain the original configuration of the job before you call this operation to modify the configuration as required.
        
        @param request: UpdateJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.attempt_interval):
            body['AttemptInterval'] = request.attempt_interval
        if not UtilClient.is_unset(request.calendar):
            body['Calendar'] = request.calendar
        if not UtilClient.is_unset(request.class_name):
            body['ClassName'] = request.class_name
        if not UtilClient.is_unset(request.consumer_size):
            body['ConsumerSize'] = request.consumer_size
        if not UtilClient.is_unset(request.contact_info):
            body['ContactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.data_offset):
            body['DataOffset'] = request.data_offset
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dispatcher_size):
            body['DispatcherSize'] = request.dispatcher_size
        if not UtilClient.is_unset(request.execute_mode):
            body['ExecuteMode'] = request.execute_mode
        if not UtilClient.is_unset(request.fail_enable):
            body['FailEnable'] = request.fail_enable
        if not UtilClient.is_unset(request.fail_times):
            body['FailTimes'] = request.fail_times
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.max_attempt):
            body['MaxAttempt'] = request.max_attempt
        if not UtilClient.is_unset(request.max_concurrency):
            body['MaxConcurrency'] = request.max_concurrency
        if not UtilClient.is_unset(request.miss_worker_enable):
            body['MissWorkerEnable'] = request.miss_worker_enable
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parameters):
            body['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.queue_size):
            body['QueueSize'] = request.queue_size
        if not UtilClient.is_unset(request.send_channel):
            body['SendChannel'] = request.send_channel
        if not UtilClient.is_unset(request.success_notice_enable):
            body['SuccessNoticeEnable'] = request.success_notice_enable
        if not UtilClient.is_unset(request.task_attempt_interval):
            body['TaskAttemptInterval'] = request.task_attempt_interval
        if not UtilClient.is_unset(request.task_dispatch_mode):
            body['TaskDispatchMode'] = request.task_dispatch_mode
        if not UtilClient.is_unset(request.task_max_attempt):
            body['TaskMaxAttempt'] = request.task_max_attempt
        if not UtilClient.is_unset(request.template):
            body['Template'] = request.template
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.timeout_enable):
            body['TimeoutEnable'] = request.timeout_enable
        if not UtilClient.is_unset(request.timeout_kill_enable):
            body['TimeoutKillEnable'] = request.timeout_kill_enable
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.xattrs):
            body['XAttrs'] = request.xattrs
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        """
        @summary Updates the configuration information about a job. By default, you need to call the GetJobInfo operation to obtain the original configuration of the job before you call this operation to modify the configuration as required.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    async def update_job_async(
        self,
        request: schedulerx_220190430_models.UpdateJobRequest,
    ) -> schedulerx_220190430_models.UpdateJobResponse:
        """
        @summary Updates the configuration information about a job. By default, you need to call the GetJobInfo operation to obtain the original configuration of the job before you call this operation to modify the configuration as required.
        
        @param request: UpdateJobRequest
        @return: UpdateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_job_with_options_async(request, runtime)

    def update_workflow_with_options(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateWorkflowResponse:
        """
        @summary Updates the basic information about a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_with_options_async(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateWorkflowResponse:
        """
        @summary Updates the basic information about a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.time_expression):
            body['TimeExpression'] = request.time_expression
        if not UtilClient.is_unset(request.time_type):
            body['TimeType'] = request.time_type
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflow',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowRequest,
    ) -> schedulerx_220190430_models.UpdateWorkflowResponse:
        """
        @summary Updates the basic information about a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowRequest
        @return: UpdateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_with_options(request, runtime)

    async def update_workflow_async(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowRequest,
    ) -> schedulerx_220190430_models.UpdateWorkflowResponse:
        """
        @summary Updates the basic information about a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowRequest
        @return: UpdateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workflow_with_options_async(request, runtime)

    def update_workflow_dag_with_options(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateWorkflowDagResponse:
        """
        @summary Modifies the nodes and dependencies of a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowDagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.dag_json):
            body['DagJson'] = request.dag_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDag',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowDagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workflow_dag_with_options_async(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> schedulerx_220190430_models.UpdateWorkflowDagResponse:
        """
        @summary Modifies the nodes and dependencies of a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowDagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowDagResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.dag_json):
            body['DagJson'] = request.dag_json
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.namespace_source):
            body['NamespaceSource'] = request.namespace_source
        if not UtilClient.is_unset(request.workflow_id):
            body['WorkflowId'] = request.workflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflowDag',
            version='2019-04-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            schedulerx_220190430_models.UpdateWorkflowDagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workflow_dag(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowDagRequest,
    ) -> schedulerx_220190430_models.UpdateWorkflowDagResponse:
        """
        @summary Modifies the nodes and dependencies of a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowDagRequest
        @return: UpdateWorkflowDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_workflow_dag_with_options(request, runtime)

    async def update_workflow_dag_async(
        self,
        request: schedulerx_220190430_models.UpdateWorkflowDagRequest,
    ) -> schedulerx_220190430_models.UpdateWorkflowDagResponse:
        """
        @summary Modifies the nodes and dependencies of a workflow. You can call this operation only in the professional edition.
        
        @param request: UpdateWorkflowDagRequest
        @return: UpdateWorkflowDagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_workflow_dag_with_options_async(request, runtime)
