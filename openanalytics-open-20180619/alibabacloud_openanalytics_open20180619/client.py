# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_openanalytics_open20180619 import models as openanalytics_open_20180619_models
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
        self._endpoint_map = {
            'cn-beijing': 'openanalytics.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'openanalytics.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'openanalytics.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'openanalytics.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'openanalytics.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'openanalytics.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'openanalytics.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'datalakeanalytics.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'openanalytics.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'datalakeanalytics.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'openanalytics.eu-west-1.aliyuncs.com',
            'us-west-1': 'openanalytics.us-west-1.aliyuncs.com',
            'us-east-1': 'datalakeanalytics.us-east-1.aliyuncs.com',
            'eu-central-1': 'datalakeanalytics.eu-central-1.aliyuncs.com',
            'ap-south-1': 'openanalytics.ap-south-1.aliyuncs.com',
            'ap-northeast-2-pop': 'openanalytics.ap-northeast-1.aliyuncs.com',
            'ap-southeast-5': 'openanalytics.ap-southeast-5.aliyuncs.com',
            'cn-beijing-finance-1': 'openanalytics.aliyuncs.com',
            'cn-beijing-finance-pop': 'openanalytics.aliyuncs.com',
            'cn-beijing-gov-1': 'openanalytics.aliyuncs.com',
            'cn-beijing-nu16-b01': 'openanalytics.aliyuncs.com',
            'cn-chengdu': 'openanalytics.aliyuncs.com',
            'cn-edge-1': 'openanalytics.aliyuncs.com',
            'cn-fujian': 'openanalytics.aliyuncs.com',
            'cn-haidian-cm12-c01': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-finance': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'openanalytics.aliyuncs.com',
            'cn-hangzhou-test-306': 'openanalytics.aliyuncs.com',
            'cn-hongkong-finance-pop': 'openanalytics.aliyuncs.com',
            'cn-huhehaote': 'openanalytics.cn-huhehaote.aliyuncs.com',
            'cn-north-2-gov-1': 'openanalytics.aliyuncs.com',
            'cn-qingdao': 'openanalytics.cn-qingdao.aliyuncs.com',
            'cn-qingdao-nebula': 'openanalytics.aliyuncs.com',
            'cn-shanghai-et15-b01': 'openanalytics.aliyuncs.com',
            'cn-shanghai-et2-b01': 'openanalytics.aliyuncs.com',
            'cn-shanghai-finance-1': 'openanalytics.aliyuncs.com',
            'cn-shanghai-inner': 'openanalytics.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-finance-1': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-inner': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'openanalytics.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'openanalytics.aliyuncs.com',
            'cn-wuhan': 'openanalytics.aliyuncs.com',
            'cn-yushanfang': 'openanalytics.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'openanalytics.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'openanalytics.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'openanalytics.aliyuncs.com',
            'eu-west-1-oxs': 'openanalytics.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'openanalytics.me-east-1.aliyuncs.com',
            'rus-west-1-pop': 'openanalytics.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('openanalytics-open', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_spark_statement_with_options(
        self,
        request: openanalytics_open_20180619_models.CancelSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.CancelSparkStatementResponse:
        """
        @param request: CancelSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.CancelSparkStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_spark_statement_with_options_async(
        self,
        request: openanalytics_open_20180619_models.CancelSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.CancelSparkStatementResponse:
        """
        @param request: CancelSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.CancelSparkStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_spark_statement(
        self,
        request: openanalytics_open_20180619_models.CancelSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.CancelSparkStatementResponse:
        """
        @param request: CancelSparkStatementRequest
        @return: CancelSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_spark_statement_with_options(request, runtime)

    async def cancel_spark_statement_async(
        self,
        request: openanalytics_open_20180619_models.CancelSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.CancelSparkStatementResponse:
        """
        @param request: CancelSparkStatementRequest
        @return: CancelSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_spark_statement_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: openanalytics_open_20180619_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.component):
            body['Component'] = request.component
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: openanalytics_open_20180619_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.component):
            body['Component'] = request.component
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: openanalytics_open_20180619_models.CreateInstanceRequest,
    ) -> openanalytics_open_20180619_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: openanalytics_open_20180619_models.CreateInstanceRequest,
    ) -> openanalytics_open_20180619_models.CreateInstanceResponse:
        """
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def execute_spark_statement_with_options(
        self,
        request: openanalytics_open_20180619_models.ExecuteSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ExecuteSparkStatementResponse:
        """
        @param request: ExecuteSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ExecuteSparkStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_spark_statement_with_options_async(
        self,
        request: openanalytics_open_20180619_models.ExecuteSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ExecuteSparkStatementResponse:
        """
        @param request: ExecuteSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code):
            body['Code'] = request.code
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ExecuteSparkStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_spark_statement(
        self,
        request: openanalytics_open_20180619_models.ExecuteSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.ExecuteSparkStatementResponse:
        """
        @param request: ExecuteSparkStatementRequest
        @return: ExecuteSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_spark_statement_with_options(request, runtime)

    async def execute_spark_statement_async(
        self,
        request: openanalytics_open_20180619_models.ExecuteSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.ExecuteSparkStatementResponse:
        """
        @param request: ExecuteSparkStatementRequest
        @return: ExecuteSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_spark_statement_with_options_async(request, runtime)

    def get_job_attempt_log_with_options(
        self,
        request: openanalytics_open_20180619_models.GetJobAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobAttemptLogResponse:
        """
        @param request: GetJobAttemptLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobAttemptLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_attempt_id):
            body['JobAttemptId'] = request.job_attempt_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobAttemptLog',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobAttemptLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_attempt_log_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetJobAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobAttemptLogResponse:
        """
        @param request: GetJobAttemptLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobAttemptLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_attempt_id):
            body['JobAttemptId'] = request.job_attempt_id
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobAttemptLog',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobAttemptLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_attempt_log(
        self,
        request: openanalytics_open_20180619_models.GetJobAttemptLogRequest,
    ) -> openanalytics_open_20180619_models.GetJobAttemptLogResponse:
        """
        @param request: GetJobAttemptLogRequest
        @return: GetJobAttemptLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_attempt_log_with_options(request, runtime)

    async def get_job_attempt_log_async(
        self,
        request: openanalytics_open_20180619_models.GetJobAttemptLogRequest,
    ) -> openanalytics_open_20180619_models.GetJobAttemptLogResponse:
        """
        @param request: GetJobAttemptLogRequest
        @return: GetJobAttemptLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_attempt_log_with_options_async(request, runtime)

    def get_job_detail_with_options(
        self,
        request: openanalytics_open_20180619_models.GetJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobDetailResponse:
        """
        @param request: GetJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobDetail',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_detail_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobDetailResponse:
        """
        @param request: GetJobDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobDetail',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_detail(
        self,
        request: openanalytics_open_20180619_models.GetJobDetailRequest,
    ) -> openanalytics_open_20180619_models.GetJobDetailResponse:
        """
        @param request: GetJobDetailRequest
        @return: GetJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_detail_with_options(request, runtime)

    async def get_job_detail_async(
        self,
        request: openanalytics_open_20180619_models.GetJobDetailRequest,
    ) -> openanalytics_open_20180619_models.GetJobDetailResponse:
        """
        @param request: GetJobDetailRequest
        @return: GetJobDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_detail_with_options_async(request, runtime)

    def get_job_log_with_options(
        self,
        request: openanalytics_open_20180619_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobLogResponse:
        """
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_log_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobLogResponse:
        """
        @param request: GetJobLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobLogResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobLog',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_log(
        self,
        request: openanalytics_open_20180619_models.GetJobLogRequest,
    ) -> openanalytics_open_20180619_models.GetJobLogResponse:
        """
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_log_with_options(request, runtime)

    async def get_job_log_async(
        self,
        request: openanalytics_open_20180619_models.GetJobLogRequest,
    ) -> openanalytics_open_20180619_models.GetJobLogResponse:
        """
        @param request: GetJobLogRequest
        @return: GetJobLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_log_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: openanalytics_open_20180619_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobStatusResponse:
        """
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetJobStatusResponse:
        """
        @param request: GetJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetJobStatus',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_status(
        self,
        request: openanalytics_open_20180619_models.GetJobStatusRequest,
    ) -> openanalytics_open_20180619_models.GetJobStatusResponse:
        """
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: openanalytics_open_20180619_models.GetJobStatusRequest,
    ) -> openanalytics_open_20180619_models.GetJobStatusResponse:
        """
        @param request: GetJobStatusRequest
        @return: GetJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_spark_session_state_with_options(
        self,
        request: openanalytics_open_20180619_models.GetSparkSessionStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetSparkSessionStateResponse:
        """
        @param request: GetSparkSessionStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSessionStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSessionState',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetSparkSessionStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_session_state_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetSparkSessionStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetSparkSessionStateResponse:
        """
        @param request: GetSparkSessionStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkSessionStateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSessionState',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetSparkSessionStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_session_state(
        self,
        request: openanalytics_open_20180619_models.GetSparkSessionStateRequest,
    ) -> openanalytics_open_20180619_models.GetSparkSessionStateResponse:
        """
        @param request: GetSparkSessionStateRequest
        @return: GetSparkSessionStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_session_state_with_options(request, runtime)

    async def get_spark_session_state_async(
        self,
        request: openanalytics_open_20180619_models.GetSparkSessionStateRequest,
    ) -> openanalytics_open_20180619_models.GetSparkSessionStateResponse:
        """
        @param request: GetSparkSessionStateRequest
        @return: GetSparkSessionStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_session_state_with_options_async(request, runtime)

    def get_spark_statement_with_options(
        self,
        request: openanalytics_open_20180619_models.GetSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetSparkStatementResponse:
        """
        @param request: GetSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetSparkStatementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_statement_with_options_async(
        self,
        request: openanalytics_open_20180619_models.GetSparkStatementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.GetSparkStatementResponse:
        """
        @param request: GetSparkStatementRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSparkStatementResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.statement_id):
            body['StatementId'] = request.statement_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkStatement',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.GetSparkStatementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_statement(
        self,
        request: openanalytics_open_20180619_models.GetSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.GetSparkStatementResponse:
        """
        @param request: GetSparkStatementRequest
        @return: GetSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_spark_statement_with_options(request, runtime)

    async def get_spark_statement_async(
        self,
        request: openanalytics_open_20180619_models.GetSparkStatementRequest,
    ) -> openanalytics_open_20180619_models.GetSparkStatementResponse:
        """
        @param request: GetSparkStatementRequest
        @return: GetSparkStatementResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_statement_with_options_async(request, runtime)

    def kill_spark_job_with_options(
        self,
        request: openanalytics_open_20180619_models.KillSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.KillSparkJobResponse:
        """
        @param request: KillSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.KillSparkJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_job_with_options_async(
        self,
        request: openanalytics_open_20180619_models.KillSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.KillSparkJobResponse:
        """
        @param request: KillSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillSparkJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.KillSparkJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_job(
        self,
        request: openanalytics_open_20180619_models.KillSparkJobRequest,
    ) -> openanalytics_open_20180619_models.KillSparkJobResponse:
        """
        @param request: KillSparkJobRequest
        @return: KillSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_job_with_options(request, runtime)

    async def kill_spark_job_async(
        self,
        request: openanalytics_open_20180619_models.KillSparkJobRequest,
    ) -> openanalytics_open_20180619_models.KillSparkJobResponse:
        """
        @param request: KillSparkJobRequest
        @return: KillSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_job_with_options_async(request, runtime)

    def list_spark_job_with_options(
        self,
        tmp_req: openanalytics_open_20180619_models.ListSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkJobResponse:
        """
        @param tmp_req: ListSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20180619_models.ListSparkJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vc_name):
            query['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_job_with_options_async(
        self,
        tmp_req: openanalytics_open_20180619_models.ListSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkJobResponse:
        """
        @param tmp_req: ListSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkJobResponse
        """
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20180619_models.ListSparkJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vc_name):
            query['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_job(
        self,
        request: openanalytics_open_20180619_models.ListSparkJobRequest,
    ) -> openanalytics_open_20180619_models.ListSparkJobResponse:
        """
        @param request: ListSparkJobRequest
        @return: ListSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_job_with_options(request, runtime)

    async def list_spark_job_async(
        self,
        request: openanalytics_open_20180619_models.ListSparkJobRequest,
    ) -> openanalytics_open_20180619_models.ListSparkJobResponse:
        """
        @param request: ListSparkJobRequest
        @return: ListSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_job_with_options_async(request, runtime)

    def list_spark_job_attempt_with_options(
        self,
        tmp_req: openanalytics_open_20180619_models.ListSparkJobAttemptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkJobAttemptResponse:
        """
        @param tmp_req: ListSparkJobAttemptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkJobAttemptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20180619_models.ListSparkJobAttemptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vc_name):
            query['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkJobAttempt',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkJobAttemptResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_job_attempt_with_options_async(
        self,
        tmp_req: openanalytics_open_20180619_models.ListSparkJobAttemptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkJobAttemptResponse:
        """
        @param tmp_req: ListSparkJobAttemptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkJobAttemptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = openanalytics_open_20180619_models.ListSparkJobAttemptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vc_name):
            query['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkJobAttempt',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkJobAttemptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_job_attempt(
        self,
        request: openanalytics_open_20180619_models.ListSparkJobAttemptRequest,
    ) -> openanalytics_open_20180619_models.ListSparkJobAttemptResponse:
        """
        @param request: ListSparkJobAttemptRequest
        @return: ListSparkJobAttemptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_job_attempt_with_options(request, runtime)

    async def list_spark_job_attempt_async(
        self,
        request: openanalytics_open_20180619_models.ListSparkJobAttemptRequest,
    ) -> openanalytics_open_20180619_models.ListSparkJobAttemptResponse:
        """
        @param request: ListSparkJobAttemptRequest
        @return: ListSparkJobAttemptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_job_attempt_with_options_async(request, runtime)

    def list_spark_statements_with_options(
        self,
        request: openanalytics_open_20180619_models.ListSparkStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkStatementsResponse:
        """
        @param request: ListSparkStatementsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkStatementsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkStatements',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkStatementsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_statements_with_options_async(
        self,
        request: openanalytics_open_20180619_models.ListSparkStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ListSparkStatementsResponse:
        """
        @param request: ListSparkStatementsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSparkStatementsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkStatements',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ListSparkStatementsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_statements(
        self,
        request: openanalytics_open_20180619_models.ListSparkStatementsRequest,
    ) -> openanalytics_open_20180619_models.ListSparkStatementsResponse:
        """
        @param request: ListSparkStatementsRequest
        @return: ListSparkStatementsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_spark_statements_with_options(request, runtime)

    async def list_spark_statements_async(
        self,
        request: openanalytics_open_20180619_models.ListSparkStatementsRequest,
    ) -> openanalytics_open_20180619_models.ListSparkStatementsResponse:
        """
        @param request: ListSparkStatementsRequest
        @return: ListSparkStatementsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_statements_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: openanalytics_open_20180619_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: openanalytics_open_20180619_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: openanalytics_open_20180619_models.ReleaseInstanceRequest,
    ) -> openanalytics_open_20180619_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: openanalytics_open_20180619_models.ReleaseInstanceRequest,
    ) -> openanalytics_open_20180619_models.ReleaseInstanceResponse:
        """
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def submit_spark_job_with_options(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.SubmitSparkJobResponse:
        """
        @param request: SubmitSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_json):
            body['ConfigJson'] = request.config_json
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.SubmitSparkJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_job_with_options_async(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.SubmitSparkJobResponse:
        """
        @param request: SubmitSparkJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config_json):
            body['ConfigJson'] = request.config_json
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkJob',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.SubmitSparkJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_job(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkJobRequest,
    ) -> openanalytics_open_20180619_models.SubmitSparkJobResponse:
        """
        @param request: SubmitSparkJobRequest
        @return: SubmitSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_job_with_options(request, runtime)

    async def submit_spark_job_async(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkJobRequest,
    ) -> openanalytics_open_20180619_models.SubmitSparkJobResponse:
        """
        @param request: SubmitSparkJobRequest
        @return: SubmitSparkJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_job_with_options_async(request, runtime)

    def submit_spark_sqlwith_options(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.SubmitSparkSQLResponse:
        """
        @param request: SubmitSparkSQLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkSQLResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkSQL',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.SubmitSparkSQLResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_sqlwith_options_async(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkSQLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.SubmitSparkSQLResponse:
        """
        @param request: SubmitSparkSQLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitSparkSQLResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sql):
            body['Sql'] = request.sql
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkSQL',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.SubmitSparkSQLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_sql(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkSQLRequest,
    ) -> openanalytics_open_20180619_models.SubmitSparkSQLResponse:
        """
        @param request: SubmitSparkSQLRequest
        @return: SubmitSparkSQLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_sqlwith_options(request, runtime)

    async def submit_spark_sql_async(
        self,
        request: openanalytics_open_20180619_models.SubmitSparkSQLRequest,
    ) -> openanalytics_open_20180619_models.SubmitSparkSQLResponse:
        """
        @param request: SubmitSparkSQLRequest
        @return: SubmitSparkSQLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_sqlwith_options_async(request, runtime)

    def validate_virtual_cluster_name_with_options(
        self,
        request: openanalytics_open_20180619_models.ValidateVirtualClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse:
        """
        @param request: ValidateVirtualClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateVirtualClusterNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateVirtualClusterName',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_virtual_cluster_name_with_options_async(
        self,
        request: openanalytics_open_20180619_models.ValidateVirtualClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse:
        """
        @param request: ValidateVirtualClusterNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateVirtualClusterNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vc_name):
            body['VcName'] = request.vc_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateVirtualClusterName',
            version='2018-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_virtual_cluster_name(
        self,
        request: openanalytics_open_20180619_models.ValidateVirtualClusterNameRequest,
    ) -> openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse:
        """
        @param request: ValidateVirtualClusterNameRequest
        @return: ValidateVirtualClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_virtual_cluster_name_with_options(request, runtime)

    async def validate_virtual_cluster_name_async(
        self,
        request: openanalytics_open_20180619_models.ValidateVirtualClusterNameRequest,
    ) -> openanalytics_open_20180619_models.ValidateVirtualClusterNameResponse:
        """
        @param request: ValidateVirtualClusterNameRequest
        @return: ValidateVirtualClusterNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_virtual_cluster_name_with_options_async(request, runtime)
