# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_advisor20180120 import models as advisor_20180120_models
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
        self._endpoint = self.get_endpoint('advisor', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_advices_with_options(
        self,
        request: advisor_20180120_models.DescribeAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesResponse:
        """
        @summary 根据多个维度获取用户最新的巡检结果，全量返回-openApi
        
        @param request: DescribeAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.exclude_advice_id):
            query['ExcludeAdviceId'] = request.exclude_advice_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advices_with_options_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesResponse:
        """
        @summary 根据多个维度获取用户最新的巡检结果，全量返回-openApi
        
        @param request: DescribeAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.exclude_advice_id):
            query['ExcludeAdviceId'] = request.exclude_advice_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advices(
        self,
        request: advisor_20180120_models.DescribeAdvicesRequest,
    ) -> advisor_20180120_models.DescribeAdvicesResponse:
        """
        @summary 根据多个维度获取用户最新的巡检结果，全量返回-openApi
        
        @param request: DescribeAdvicesRequest
        @return: DescribeAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_with_options(request, runtime)

    async def describe_advices_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesRequest,
    ) -> advisor_20180120_models.DescribeAdvicesResponse:
        """
        @summary 根据多个维度获取用户最新的巡检结果，全量返回-openApi
        
        @param request: DescribeAdvicesRequest
        @return: DescribeAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advices_with_options_async(request, runtime)

    def describe_advices_flat_page_with_options(
        self,
        request: advisor_20180120_models.DescribeAdvicesFlatPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesFlatPageResponse:
        """
        @summary DescribeAdvicesFlat分页
        
        @param request: DescribeAdvicesFlatPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesFlatPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesFlatPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesFlatPageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesFlatPageResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advices_flat_page_with_options_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesFlatPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesFlatPageResponse:
        """
        @summary DescribeAdvicesFlat分页
        
        @param request: DescribeAdvicesFlatPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesFlatPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesFlatPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesFlatPageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesFlatPageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advices_flat_page(
        self,
        request: advisor_20180120_models.DescribeAdvicesFlatPageRequest,
    ) -> advisor_20180120_models.DescribeAdvicesFlatPageResponse:
        """
        @summary DescribeAdvicesFlat分页
        
        @param request: DescribeAdvicesFlatPageRequest
        @return: DescribeAdvicesFlatPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_flat_page_with_options(request, runtime)

    async def describe_advices_flat_page_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesFlatPageRequest,
    ) -> advisor_20180120_models.DescribeAdvicesFlatPageResponse:
        """
        @summary DescribeAdvicesFlat分页
        
        @param request: DescribeAdvicesFlatPageRequest
        @return: DescribeAdvicesFlatPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advices_flat_page_with_options_async(request, runtime)

    def describe_advices_page_with_options(
        self,
        request: advisor_20180120_models.DescribeAdvicesPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesPageResponse:
        """
        @summary DescribeAdvices分页
        
        @param request: DescribeAdvicesPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesPageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesPageResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advices_page_with_options_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvicesPageResponse:
        """
        @summary DescribeAdvices分页
        
        @param request: DescribeAdvicesPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvicesPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advice_id):
            query['AdviceId'] = request.advice_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvicesPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesPageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvicesPageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advices_page(
        self,
        request: advisor_20180120_models.DescribeAdvicesPageRequest,
    ) -> advisor_20180120_models.DescribeAdvicesPageResponse:
        """
        @summary DescribeAdvices分页
        
        @param request: DescribeAdvicesPageRequest
        @return: DescribeAdvicesPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advices_page_with_options(request, runtime)

    async def describe_advices_page_async(
        self,
        request: advisor_20180120_models.DescribeAdvicesPageRequest,
    ) -> advisor_20180120_models.DescribeAdvicesPageResponse:
        """
        @summary DescribeAdvices分页
        
        @param request: DescribeAdvicesPageRequest
        @return: DescribeAdvicesPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advices_page_with_options_async(request, runtime)

    def describe_advisor_checks_with_options(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorChecksResponse:
        """
        @param request: DescribeAdvisorChecksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorChecksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorChecks',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advisor_checks_with_options_async(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorChecksResponse:
        """
        @param request: DescribeAdvisorChecksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorChecksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorChecks',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advisor_checks(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksRequest,
    ) -> advisor_20180120_models.DescribeAdvisorChecksResponse:
        """
        @param request: DescribeAdvisorChecksRequest
        @return: DescribeAdvisorChecksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_checks_with_options(request, runtime)

    async def describe_advisor_checks_async(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksRequest,
    ) -> advisor_20180120_models.DescribeAdvisorChecksResponse:
        """
        @param request: DescribeAdvisorChecksRequest
        @return: DescribeAdvisorChecksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advisor_checks_with_options_async(request, runtime)

    def describe_advisor_checks_fo_pages_with_options(
        self,
        tmp_req: advisor_20180120_models.DescribeAdvisorChecksFoPagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse:
        """
        @summary 巡检项设置-分页
        
        @param tmp_req: DescribeAdvisorChecksFoPagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorChecksFoPagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeAdvisorChecksFoPagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_types):
            request.check_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_types, 'CheckTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.biz_category):
            query['BizCategory'] = request.biz_category
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.check_types_shrink):
            query['CheckTypes'] = request.check_types_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorChecksFoPages',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advisor_checks_fo_pages_with_options_async(
        self,
        tmp_req: advisor_20180120_models.DescribeAdvisorChecksFoPagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse:
        """
        @summary 巡检项设置-分页
        
        @param tmp_req: DescribeAdvisorChecksFoPagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorChecksFoPagesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeAdvisorChecksFoPagesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.check_types):
            request.check_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_types, 'CheckTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.biz_category):
            query['BizCategory'] = request.biz_category
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.check_types_shrink):
            query['CheckTypes'] = request.check_types_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorChecksFoPages',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advisor_checks_fo_pages(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksFoPagesRequest,
    ) -> advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse:
        """
        @summary 巡检项设置-分页
        
        @param request: DescribeAdvisorChecksFoPagesRequest
        @return: DescribeAdvisorChecksFoPagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_checks_fo_pages_with_options(request, runtime)

    async def describe_advisor_checks_fo_pages_async(
        self,
        request: advisor_20180120_models.DescribeAdvisorChecksFoPagesRequest,
    ) -> advisor_20180120_models.DescribeAdvisorChecksFoPagesResponse:
        """
        @summary 巡检项设置-分页
        
        @param request: DescribeAdvisorChecksFoPagesRequest
        @return: DescribeAdvisorChecksFoPagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advisor_checks_fo_pages_with_options_async(request, runtime)

    def describe_advisor_resources_with_options(
        self,
        request: advisor_20180120_models.DescribeAdvisorResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorResourcesResponse:
        """
        @param request: DescribeAdvisorResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorResources',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_advisor_resources_with_options_async(
        self,
        request: advisor_20180120_models.DescribeAdvisorResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeAdvisorResourcesResponse:
        """
        @param request: DescribeAdvisorResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAdvisorResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdvisorResources',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeAdvisorResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_advisor_resources(
        self,
        request: advisor_20180120_models.DescribeAdvisorResourcesRequest,
    ) -> advisor_20180120_models.DescribeAdvisorResourcesResponse:
        """
        @param request: DescribeAdvisorResourcesRequest
        @return: DescribeAdvisorResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_advisor_resources_with_options(request, runtime)

    async def describe_advisor_resources_async(
        self,
        request: advisor_20180120_models.DescribeAdvisorResourcesRequest,
    ) -> advisor_20180120_models.DescribeAdvisorResourcesResponse:
        """
        @param request: DescribeAdvisorResourcesRequest
        @return: DescribeAdvisorResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_advisor_resources_with_options_async(request, runtime)

    def describe_cost_check_advices_with_options(
        self,
        tmp_req: advisor_20180120_models.DescribeCostCheckAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostCheckAdvicesResponse:
        """
        @summary 查询成本优化结果详情
        
        @param tmp_req: DescribeCostCheckAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostCheckAdvicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckAdvicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_values):
            request.tag_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckAdvicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckAdvicesResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cost_check_advices_with_options_async(
        self,
        tmp_req: advisor_20180120_models.DescribeCostCheckAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostCheckAdvicesResponse:
        """
        @summary 查询成本优化结果详情
        
        @param tmp_req: DescribeCostCheckAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostCheckAdvicesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckAdvicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_values):
            request.tag_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckAdvicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckAdvicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cost_check_advices(
        self,
        request: advisor_20180120_models.DescribeCostCheckAdvicesRequest,
    ) -> advisor_20180120_models.DescribeCostCheckAdvicesResponse:
        """
        @summary 查询成本优化结果详情
        
        @param request: DescribeCostCheckAdvicesRequest
        @return: DescribeCostCheckAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_check_advices_with_options(request, runtime)

    async def describe_cost_check_advices_async(
        self,
        request: advisor_20180120_models.DescribeCostCheckAdvicesRequest,
    ) -> advisor_20180120_models.DescribeCostCheckAdvicesResponse:
        """
        @summary 查询成本优化结果详情
        
        @param request: DescribeCostCheckAdvicesRequest
        @return: DescribeCostCheckAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cost_check_advices_with_options_async(request, runtime)

    def describe_cost_check_results_with_options(
        self,
        tmp_req: advisor_20180120_models.DescribeCostCheckResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostCheckResultsResponse:
        """
        @summary 查询巡检项聚合成本优化结果概览
        
        @param tmp_req: DescribeCostCheckResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostCheckResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.check_ids):
            request.check_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_values):
            request.tag_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckResults',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckResultsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckResultsResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cost_check_results_with_options_async(
        self,
        tmp_req: advisor_20180120_models.DescribeCostCheckResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostCheckResultsResponse:
        """
        @summary 查询巡检项聚合成本优化结果概览
        
        @param tmp_req: DescribeCostCheckResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostCheckResultsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostCheckResultsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.check_ids):
            request.check_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_group_id_list):
            request.resource_group_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_group_id_list, 'ResourceGroupIdList', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        if not UtilClient.is_unset(tmp_req.tag_list):
            request.tag_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_list, 'TagList', 'json')
        if not UtilClient.is_unset(tmp_req.tag_values):
            request.tag_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_values, 'TagValues', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_group_id_list_shrink):
            query['ResourceGroupIdList'] = request.resource_group_id_list_shrink
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        if not UtilClient.is_unset(request.tag_list_shrink):
            query['TagList'] = request.tag_list_shrink
        if not UtilClient.is_unset(request.tag_values_shrink):
            query['TagValues'] = request.tag_values_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostCheckResults',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckResultsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostCheckResultsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cost_check_results(
        self,
        request: advisor_20180120_models.DescribeCostCheckResultsRequest,
    ) -> advisor_20180120_models.DescribeCostCheckResultsResponse:
        """
        @summary 查询巡检项聚合成本优化结果概览
        
        @param request: DescribeCostCheckResultsRequest
        @return: DescribeCostCheckResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_check_results_with_options(request, runtime)

    async def describe_cost_check_results_async(
        self,
        request: advisor_20180120_models.DescribeCostCheckResultsRequest,
    ) -> advisor_20180120_models.DescribeCostCheckResultsResponse:
        """
        @summary 查询巡检项聚合成本优化结果概览
        
        @param request: DescribeCostCheckResultsRequest
        @return: DescribeCostCheckResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cost_check_results_with_options_async(request, runtime)

    def describe_cost_optimization_overview_with_options(
        self,
        tmp_req: advisor_20180120_models.DescribeCostOptimizationOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostOptimizationOverviewResponse:
        """
        @summary 成本优化-概览
        
        @param tmp_req: DescribeCostOptimizationOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostOptimizationOverviewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostOptimizationOverviewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostOptimizationOverview',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostOptimizationOverviewResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostOptimizationOverviewResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_cost_optimization_overview_with_options_async(
        self,
        tmp_req: advisor_20180120_models.DescribeCostOptimizationOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.DescribeCostOptimizationOverviewResponse:
        """
        @summary 成本优化-概览
        
        @param tmp_req: DescribeCostOptimizationOverviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostOptimizationOverviewResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.DescribeCostOptimizationOverviewShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostOptimizationOverview',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostOptimizationOverviewResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.DescribeCostOptimizationOverviewResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_cost_optimization_overview(
        self,
        request: advisor_20180120_models.DescribeCostOptimizationOverviewRequest,
    ) -> advisor_20180120_models.DescribeCostOptimizationOverviewResponse:
        """
        @summary 成本优化-概览
        
        @param request: DescribeCostOptimizationOverviewRequest
        @return: DescribeCostOptimizationOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_optimization_overview_with_options(request, runtime)

    async def describe_cost_optimization_overview_async(
        self,
        request: advisor_20180120_models.DescribeCostOptimizationOverviewRequest,
    ) -> advisor_20180120_models.DescribeCostOptimizationOverviewResponse:
        """
        @summary 成本优化-概览
        
        @param request: DescribeCostOptimizationOverviewRequest
        @return: DescribeCostOptimizationOverviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cost_optimization_overview_with_options_async(request, runtime)

    def get_history_advices_with_options(
        self,
        request: advisor_20180120_models.GetHistoryAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetHistoryAdvicesResponse:
        """
        @param request: GetHistoryAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoryAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetHistoryAdvicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetHistoryAdvicesResponse(),
                self.execute(params, req, runtime)
            )

    async def get_history_advices_with_options_async(
        self,
        request: advisor_20180120_models.GetHistoryAdvicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetHistoryAdvicesResponse:
        """
        @param request: GetHistoryAdvicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetHistoryAdvicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHistoryAdvices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetHistoryAdvicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetHistoryAdvicesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_history_advices(
        self,
        request: advisor_20180120_models.GetHistoryAdvicesRequest,
    ) -> advisor_20180120_models.GetHistoryAdvicesResponse:
        """
        @param request: GetHistoryAdvicesRequest
        @return: GetHistoryAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_history_advices_with_options(request, runtime)

    async def get_history_advices_async(
        self,
        request: advisor_20180120_models.GetHistoryAdvicesRequest,
    ) -> advisor_20180120_models.GetHistoryAdvicesResponse:
        """
        @param request: GetHistoryAdvicesRequest
        @return: GetHistoryAdvicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_history_advices_with_options_async(request, runtime)

    def get_inspect_progress_with_options(
        self,
        request: advisor_20180120_models.GetInspectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetInspectProgressResponse:
        """
        @summary 获取任务执行进度(普通用户、RD单账号)
        
        @param request: GetInspectProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInspectProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInspectProgress',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetInspectProgressResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetInspectProgressResponse(),
                self.execute(params, req, runtime)
            )

    async def get_inspect_progress_with_options_async(
        self,
        request: advisor_20180120_models.GetInspectProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetInspectProgressResponse:
        """
        @summary 获取任务执行进度(普通用户、RD单账号)
        
        @param request: GetInspectProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInspectProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInspectProgress',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetInspectProgressResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetInspectProgressResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_inspect_progress(
        self,
        request: advisor_20180120_models.GetInspectProgressRequest,
    ) -> advisor_20180120_models.GetInspectProgressResponse:
        """
        @summary 获取任务执行进度(普通用户、RD单账号)
        
        @param request: GetInspectProgressRequest
        @return: GetInspectProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_inspect_progress_with_options(request, runtime)

    async def get_inspect_progress_async(
        self,
        request: advisor_20180120_models.GetInspectProgressRequest,
    ) -> advisor_20180120_models.GetInspectProgressResponse:
        """
        @summary 获取任务执行进度(普通用户、RD单账号)
        
        @param request: GetInspectProgressRequest
        @return: GetInspectProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_inspect_progress_with_options_async(request, runtime)

    def get_product_list_with_options(
        self,
        request: advisor_20180120_models.GetProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetProductListResponse:
        """
        @summary 获取云产品的列表
        
        @param request: GetProductListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetProductListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetProductListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_product_list_with_options_async(
        self,
        request: advisor_20180120_models.GetProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetProductListResponse:
        """
        @summary 获取云产品的列表
        
        @param request: GetProductListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProductListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProductList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetProductListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetProductListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_product_list(
        self,
        request: advisor_20180120_models.GetProductListRequest,
    ) -> advisor_20180120_models.GetProductListResponse:
        """
        @summary 获取云产品的列表
        
        @param request: GetProductListRequest
        @return: GetProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_product_list_with_options(request, runtime)

    async def get_product_list_async(
        self,
        request: advisor_20180120_models.GetProductListRequest,
    ) -> advisor_20180120_models.GetProductListResponse:
        """
        @summary 获取云产品的列表
        
        @param request: GetProductListRequest
        @return: GetProductListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_product_list_with_options_async(request, runtime)

    def get_task_status_by_id_with_options(
        self,
        request: advisor_20180120_models.GetTaskStatusByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetTaskStatusByIdResponse:
        """
        @summary 根据id获取任务状态
        
        @param request: GetTaskStatusByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusByIdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatusById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetTaskStatusByIdResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetTaskStatusByIdResponse(),
                self.execute(params, req, runtime)
            )

    async def get_task_status_by_id_with_options_async(
        self,
        request: advisor_20180120_models.GetTaskStatusByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.GetTaskStatusByIdResponse:
        """
        @summary 根据id获取任务状态
        
        @param request: GetTaskStatusByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskStatusByIdResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTaskStatusById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.GetTaskStatusByIdResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.GetTaskStatusByIdResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_task_status_by_id(
        self,
        request: advisor_20180120_models.GetTaskStatusByIdRequest,
    ) -> advisor_20180120_models.GetTaskStatusByIdResponse:
        """
        @summary 根据id获取任务状态
        
        @param request: GetTaskStatusByIdRequest
        @return: GetTaskStatusByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_by_id_with_options(request, runtime)

    async def get_task_status_by_id_async(
        self,
        request: advisor_20180120_models.GetTaskStatusByIdRequest,
    ) -> advisor_20180120_models.GetTaskStatusByIdResponse:
        """
        @summary 根据id获取任务状态
        
        @param request: GetTaskStatusByIdRequest
        @return: GetTaskStatusByIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_by_id_with_options_async(request, runtime)

    def refresh_advisor_check_with_options(
        self,
        tmp_req: advisor_20180120_models.RefreshAdvisorCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorCheckResponse:
        """
        @summary 触发立即巡检
        
        @param tmp_req: RefreshAdvisorCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.RefreshAdvisorCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_dimension_list):
            request.resource_dimension_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_dimension_list, 'ResourceDimensionList', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        body = {}
        if not UtilClient.is_unset(request.resource_dimension_list_shrink):
            body['ResourceDimensionList'] = request.resource_dimension_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorCheck',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def refresh_advisor_check_with_options_async(
        self,
        tmp_req: advisor_20180120_models.RefreshAdvisorCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorCheckResponse:
        """
        @summary 触发立即巡检
        
        @param tmp_req: RefreshAdvisorCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.RefreshAdvisorCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_dimension_list):
            request.resource_dimension_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_dimension_list, 'ResourceDimensionList', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id):
            query['AssumeAliyunId'] = request.assume_aliyun_id
        if not UtilClient.is_unset(request.check_id):
            query['CheckId'] = request.check_id
        if not UtilClient.is_unset(request.check_plan_id):
            query['CheckPlanId'] = request.check_plan_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        body = {}
        if not UtilClient.is_unset(request.resource_dimension_list_shrink):
            body['ResourceDimensionList'] = request.resource_dimension_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorCheck',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def refresh_advisor_check(
        self,
        request: advisor_20180120_models.RefreshAdvisorCheckRequest,
    ) -> advisor_20180120_models.RefreshAdvisorCheckResponse:
        """
        @summary 触发立即巡检
        
        @param request: RefreshAdvisorCheckRequest
        @return: RefreshAdvisorCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_advisor_check_with_options(request, runtime)

    async def refresh_advisor_check_async(
        self,
        request: advisor_20180120_models.RefreshAdvisorCheckRequest,
    ) -> advisor_20180120_models.RefreshAdvisorCheckResponse:
        """
        @summary 触发立即巡检
        
        @param request: RefreshAdvisorCheckRequest
        @return: RefreshAdvisorCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_advisor_check_with_options_async(request, runtime)

    def refresh_advisor_cost_check_with_options(
        self,
        tmp_req: advisor_20180120_models.RefreshAdvisorCostCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorCostCheckResponse:
        """
        @summary 发起成本优化巡检
        
        @param tmp_req: RefreshAdvisorCostCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorCostCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.RefreshAdvisorCostCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.check_ids):
            request.check_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.refresh_resource):
            query['RefreshResource'] = request.refresh_resource
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorCostCheck',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCostCheckResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCostCheckResponse(),
                self.execute(params, req, runtime)
            )

    async def refresh_advisor_cost_check_with_options_async(
        self,
        tmp_req: advisor_20180120_models.RefreshAdvisorCostCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorCostCheckResponse:
        """
        @summary 发起成本优化巡检
        
        @param tmp_req: RefreshAdvisorCostCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorCostCheckResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.RefreshAdvisorCostCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_aliyun_id_list):
            request.assume_aliyun_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.assume_aliyun_id_list, 'AssumeAliyunIdList', 'json')
        if not UtilClient.is_unset(tmp_req.check_ids):
            request.check_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.check_ids, 'CheckIds', 'json')
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.assume_aliyun_id_list_shrink):
            query['AssumeAliyunIdList'] = request.assume_aliyun_id_list_shrink
        if not UtilClient.is_unset(request.check_ids_shrink):
            query['CheckIds'] = request.check_ids_shrink
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.refresh_resource):
            query['RefreshResource'] = request.refresh_resource
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorCostCheck',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCostCheckResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorCostCheckResponse(),
                await self.execute_async(params, req, runtime)
            )

    def refresh_advisor_cost_check(
        self,
        request: advisor_20180120_models.RefreshAdvisorCostCheckRequest,
    ) -> advisor_20180120_models.RefreshAdvisorCostCheckResponse:
        """
        @summary 发起成本优化巡检
        
        @param request: RefreshAdvisorCostCheckRequest
        @return: RefreshAdvisorCostCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_advisor_cost_check_with_options(request, runtime)

    async def refresh_advisor_cost_check_async(
        self,
        request: advisor_20180120_models.RefreshAdvisorCostCheckRequest,
    ) -> advisor_20180120_models.RefreshAdvisorCostCheckResponse:
        """
        @summary 发起成本优化巡检
        
        @param request: RefreshAdvisorCostCheckRequest
        @return: RefreshAdvisorCostCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_advisor_cost_check_with_options_async(request, runtime)

    def refresh_advisor_resource_with_options(
        self,
        request: advisor_20180120_models.RefreshAdvisorResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorResourceResponse:
        """
        @param request: RefreshAdvisorResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorResource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorResourceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorResourceResponse(),
                self.execute(params, req, runtime)
            )

    async def refresh_advisor_resource_with_options_async(
        self,
        request: advisor_20180120_models.RefreshAdvisorResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.RefreshAdvisorResourceResponse:
        """
        @param request: RefreshAdvisorResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshAdvisorResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshAdvisorResource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorResourceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.RefreshAdvisorResourceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def refresh_advisor_resource(
        self,
        request: advisor_20180120_models.RefreshAdvisorResourceRequest,
    ) -> advisor_20180120_models.RefreshAdvisorResourceResponse:
        """
        @param request: RefreshAdvisorResourceRequest
        @return: RefreshAdvisorResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_advisor_resource_with_options(request, runtime)

    async def refresh_advisor_resource_async(
        self,
        request: advisor_20180120_models.RefreshAdvisorResourceRequest,
    ) -> advisor_20180120_models.RefreshAdvisorResourceResponse:
        """
        @param request: RefreshAdvisorResourceRequest
        @return: RefreshAdvisorResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_advisor_resource_with_options_async(request, runtime)

    def report_biz_alert_info_with_options(
        self,
        tmp_req: advisor_20180120_models.ReportBizAlertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.ReportBizAlertInfoResponse:
        """
        @summary 上报用户业务报警信息
        
        @param tmp_req: ReportBizAlertInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportBizAlertInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.ReportBizAlertInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_uid):
            request.alert_uid_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_uid, 'AlertUid', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_description):
            query['AlertDescription'] = request.alert_description
        if not UtilClient.is_unset(request.alert_detail):
            query['AlertDetail'] = request.alert_detail
        if not UtilClient.is_unset(request.alert_grade):
            query['AlertGrade'] = request.alert_grade
        if not UtilClient.is_unset(request.alert_labels):
            query['AlertLabels'] = request.alert_labels
        if not UtilClient.is_unset(request.alert_scene):
            query['AlertScene'] = request.alert_scene
        if not UtilClient.is_unset(request.alert_token):
            query['AlertToken'] = request.alert_token
        if not UtilClient.is_unset(request.alert_uid_shrink):
            query['AlertUid'] = request.alert_uid_shrink
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportBizAlertInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.ReportBizAlertInfoResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.ReportBizAlertInfoResponse(),
                self.execute(params, req, runtime)
            )

    async def report_biz_alert_info_with_options_async(
        self,
        tmp_req: advisor_20180120_models.ReportBizAlertInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> advisor_20180120_models.ReportBizAlertInfoResponse:
        """
        @summary 上报用户业务报警信息
        
        @param tmp_req: ReportBizAlertInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReportBizAlertInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = advisor_20180120_models.ReportBizAlertInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_uid):
            request.alert_uid_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_uid, 'AlertUid', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_description):
            query['AlertDescription'] = request.alert_description
        if not UtilClient.is_unset(request.alert_detail):
            query['AlertDetail'] = request.alert_detail
        if not UtilClient.is_unset(request.alert_grade):
            query['AlertGrade'] = request.alert_grade
        if not UtilClient.is_unset(request.alert_labels):
            query['AlertLabels'] = request.alert_labels
        if not UtilClient.is_unset(request.alert_scene):
            query['AlertScene'] = request.alert_scene
        if not UtilClient.is_unset(request.alert_token):
            query['AlertToken'] = request.alert_token
        if not UtilClient.is_unset(request.alert_uid_shrink):
            query['AlertUid'] = request.alert_uid_shrink
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReportBizAlertInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                advisor_20180120_models.ReportBizAlertInfoResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                advisor_20180120_models.ReportBizAlertInfoResponse(),
                await self.execute_async(params, req, runtime)
            )

    def report_biz_alert_info(
        self,
        request: advisor_20180120_models.ReportBizAlertInfoRequest,
    ) -> advisor_20180120_models.ReportBizAlertInfoResponse:
        """
        @summary 上报用户业务报警信息
        
        @param request: ReportBizAlertInfoRequest
        @return: ReportBizAlertInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.report_biz_alert_info_with_options(request, runtime)

    async def report_biz_alert_info_async(
        self,
        request: advisor_20180120_models.ReportBizAlertInfoRequest,
    ) -> advisor_20180120_models.ReportBizAlertInfoResponse:
        """
        @summary 上报用户业务报警信息
        
        @param request: ReportBizAlertInfoRequest
        @return: ReportBizAlertInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.report_biz_alert_info_with_options_async(request, runtime)
