# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_websitebuild20250429 import models as website_build_20250429_models
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
        self._endpoint = self.get_endpoint('websitebuild', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def bind_app_domain_with_options(
        self,
        request: website_build_20250429_models.BindAppDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.BindAppDomainResponse:
        """
        @summary 绑定应用域名
        
        @param request: BindAppDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAppDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAppDomain',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.BindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_app_domain_with_options_async(
        self,
        request: website_build_20250429_models.BindAppDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.BindAppDomainResponse:
        """
        @summary 绑定应用域名
        
        @param request: BindAppDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BindAppDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAppDomain',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.BindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_app_domain(
        self,
        request: website_build_20250429_models.BindAppDomainRequest,
    ) -> website_build_20250429_models.BindAppDomainResponse:
        """
        @summary 绑定应用域名
        
        @param request: BindAppDomainRequest
        @return: BindAppDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_app_domain_with_options(request, runtime)

    async def bind_app_domain_async(
        self,
        request: website_build_20250429_models.BindAppDomainRequest,
    ) -> website_build_20250429_models.BindAppDomainResponse:
        """
        @summary 绑定应用域名
        
        @param request: BindAppDomainRequest
        @return: BindAppDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.bind_app_domain_with_options_async(request, runtime)

    def create_logo_task_with_options(
        self,
        request: website_build_20250429_models.CreateLogoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.CreateLogoTaskResponse:
        """
        @summary 提交创建Logo任务
        
        @param request: CreateLogoTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogoTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not UtilClient.is_unset(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogoTask',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.CreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logo_task_with_options_async(
        self,
        request: website_build_20250429_models.CreateLogoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.CreateLogoTaskResponse:
        """
        @summary 提交创建Logo任务
        
        @param request: CreateLogoTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogoTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not UtilClient.is_unset(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogoTask',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.CreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logo_task(
        self,
        request: website_build_20250429_models.CreateLogoTaskRequest,
    ) -> website_build_20250429_models.CreateLogoTaskResponse:
        """
        @summary 提交创建Logo任务
        
        @param request: CreateLogoTaskRequest
        @return: CreateLogoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_logo_task_with_options(request, runtime)

    async def create_logo_task_async(
        self,
        request: website_build_20250429_models.CreateLogoTaskRequest,
    ) -> website_build_20250429_models.CreateLogoTaskResponse:
        """
        @summary 提交创建Logo任务
        
        @param request: CreateLogoTaskRequest
        @return: CreateLogoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_logo_task_with_options_async(request, runtime)

    def delete_app_domain_certificate_with_options(
        self,
        request: website_build_20250429_models.DeleteAppDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DeleteAppDomainCertificateResponse:
        """
        @summary 删除域名的SSL证书
        
        @param request: DeleteAppDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDomainCertificate',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DeleteAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_certificate_with_options_async(
        self,
        request: website_build_20250429_models.DeleteAppDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DeleteAppDomainCertificateResponse:
        """
        @summary 删除域名的SSL证书
        
        @param request: DeleteAppDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDomainCertificate',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DeleteAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_certificate(
        self,
        request: website_build_20250429_models.DeleteAppDomainCertificateRequest,
    ) -> website_build_20250429_models.DeleteAppDomainCertificateResponse:
        """
        @summary 删除域名的SSL证书
        
        @param request: DeleteAppDomainCertificateRequest
        @return: DeleteAppDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_domain_certificate_with_options(request, runtime)

    async def delete_app_domain_certificate_async(
        self,
        request: website_build_20250429_models.DeleteAppDomainCertificateRequest,
    ) -> website_build_20250429_models.DeleteAppDomainCertificateResponse:
        """
        @summary 删除域名的SSL证书
        
        @param request: DeleteAppDomainCertificateRequest
        @return: DeleteAppDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_domain_certificate_with_options_async(request, runtime)

    def delete_app_domain_redirect_with_options(
        self,
        request: website_build_20250429_models.DeleteAppDomainRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DeleteAppDomainRedirectResponse:
        """
        @summary 删除域名的跳转规则
        
        @param request: DeleteAppDomainRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppDomainRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDomainRedirect',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DeleteAppDomainRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_redirect_with_options_async(
        self,
        request: website_build_20250429_models.DeleteAppDomainRedirectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DeleteAppDomainRedirectResponse:
        """
        @summary 删除域名的跳转规则
        
        @param request: DeleteAppDomainRedirectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppDomainRedirectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDomainRedirect',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DeleteAppDomainRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_redirect(
        self,
        request: website_build_20250429_models.DeleteAppDomainRedirectRequest,
    ) -> website_build_20250429_models.DeleteAppDomainRedirectResponse:
        """
        @summary 删除域名的跳转规则
        
        @param request: DeleteAppDomainRedirectRequest
        @return: DeleteAppDomainRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_domain_redirect_with_options(request, runtime)

    async def delete_app_domain_redirect_async(
        self,
        request: website_build_20250429_models.DeleteAppDomainRedirectRequest,
    ) -> website_build_20250429_models.DeleteAppDomainRedirectResponse:
        """
        @summary 删除域名的跳转规则
        
        @param request: DeleteAppDomainRedirectRequest
        @return: DeleteAppDomainRedirectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_domain_redirect_with_options_async(request, runtime)

    def describe_app_domain_dns_record_with_options(
        self,
        request: website_build_20250429_models.DescribeAppDomainDnsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DescribeAppDomainDnsRecordResponse:
        """
        @summary 查询域名的DNS解析记录
        
        @param request: DescribeAppDomainDnsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppDomainDnsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppDomainDnsRecord',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DescribeAppDomainDnsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_domain_dns_record_with_options_async(
        self,
        request: website_build_20250429_models.DescribeAppDomainDnsRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.DescribeAppDomainDnsRecordResponse:
        """
        @summary 查询域名的DNS解析记录
        
        @param request: DescribeAppDomainDnsRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppDomainDnsRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppDomainDnsRecord',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.DescribeAppDomainDnsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_domain_dns_record(
        self,
        request: website_build_20250429_models.DescribeAppDomainDnsRecordRequest,
    ) -> website_build_20250429_models.DescribeAppDomainDnsRecordResponse:
        """
        @summary 查询域名的DNS解析记录
        
        @param request: DescribeAppDomainDnsRecordRequest
        @return: DescribeAppDomainDnsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_domain_dns_record_with_options(request, runtime)

    async def describe_app_domain_dns_record_async(
        self,
        request: website_build_20250429_models.DescribeAppDomainDnsRecordRequest,
    ) -> website_build_20250429_models.DescribeAppDomainDnsRecordResponse:
        """
        @summary 查询域名的DNS解析记录
        
        @param request: DescribeAppDomainDnsRecordRequest
        @return: DescribeAppDomainDnsRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_domain_dns_record_with_options_async(request, runtime)

    def get_create_logo_task_with_options(
        self,
        request: website_build_20250429_models.GetCreateLogoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetCreateLogoTaskResponse:
        """
        @summary 查询Logo创建任务
        
        @param request: GetCreateLogoTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateLogoTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateLogoTask',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetCreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_logo_task_with_options_async(
        self,
        request: website_build_20250429_models.GetCreateLogoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetCreateLogoTaskResponse:
        """
        @summary 查询Logo创建任务
        
        @param request: GetCreateLogoTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCreateLogoTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreateLogoTask',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetCreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_logo_task(
        self,
        request: website_build_20250429_models.GetCreateLogoTaskRequest,
    ) -> website_build_20250429_models.GetCreateLogoTaskResponse:
        """
        @summary 查询Logo创建任务
        
        @param request: GetCreateLogoTaskRequest
        @return: GetCreateLogoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_create_logo_task_with_options(request, runtime)

    async def get_create_logo_task_async(
        self,
        request: website_build_20250429_models.GetCreateLogoTaskRequest,
    ) -> website_build_20250429_models.GetCreateLogoTaskResponse:
        """
        @summary 查询Logo创建任务
        
        @param request: GetCreateLogoTaskRequest
        @return: GetCreateLogoTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_create_logo_task_with_options_async(request, runtime)

    def get_domain_info_for_partner_with_options(
        self,
        request: website_build_20250429_models.GetDomainInfoForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetDomainInfoForPartnerResponse:
        """
        @summary 提供给服务商的域名查询接口
        
        @param request: GetDomainInfoForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainInfoForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainInfoForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetDomainInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_info_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.GetDomainInfoForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetDomainInfoForPartnerResponse:
        """
        @summary 提供给服务商的域名查询接口
        
        @param request: GetDomainInfoForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDomainInfoForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDomainInfoForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetDomainInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_info_for_partner(
        self,
        request: website_build_20250429_models.GetDomainInfoForPartnerRequest,
    ) -> website_build_20250429_models.GetDomainInfoForPartnerResponse:
        """
        @summary 提供给服务商的域名查询接口
        
        @param request: GetDomainInfoForPartnerRequest
        @return: GetDomainInfoForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_domain_info_for_partner_with_options(request, runtime)

    async def get_domain_info_for_partner_async(
        self,
        request: website_build_20250429_models.GetDomainInfoForPartnerRequest,
    ) -> website_build_20250429_models.GetDomainInfoForPartnerResponse:
        """
        @summary 提供给服务商的域名查询接口
        
        @param request: GetDomainInfoForPartnerRequest
        @return: GetDomainInfoForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_domain_info_for_partner_with_options_async(request, runtime)

    def get_icp_filing_info_for_partner_with_options(
        self,
        request: website_build_20250429_models.GetIcpFilingInfoForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetIcpFilingInfoForPartnerResponse:
        """
        @summary 查询域名备案信息
        
        @param request: GetIcpFilingInfoForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIcpFilingInfoForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIcpFilingInfoForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetIcpFilingInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_icp_filing_info_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.GetIcpFilingInfoForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetIcpFilingInfoForPartnerResponse:
        """
        @summary 查询域名备案信息
        
        @param request: GetIcpFilingInfoForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIcpFilingInfoForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIcpFilingInfoForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetIcpFilingInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_icp_filing_info_for_partner(
        self,
        request: website_build_20250429_models.GetIcpFilingInfoForPartnerRequest,
    ) -> website_build_20250429_models.GetIcpFilingInfoForPartnerResponse:
        """
        @summary 查询域名备案信息
        
        @param request: GetIcpFilingInfoForPartnerRequest
        @return: GetIcpFilingInfoForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_icp_filing_info_for_partner_with_options(request, runtime)

    async def get_icp_filing_info_for_partner_async(
        self,
        request: website_build_20250429_models.GetIcpFilingInfoForPartnerRequest,
    ) -> website_build_20250429_models.GetIcpFilingInfoForPartnerResponse:
        """
        @summary 查询域名备案信息
        
        @param request: GetIcpFilingInfoForPartnerRequest
        @return: GetIcpFilingInfoForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_icp_filing_info_for_partner_with_options_async(request, runtime)

    def get_user_tmp_identity_for_partner_with_options(
        self,
        request: website_build_20250429_models.GetUserTmpIdentityForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetUserTmpIdentityForPartnerResponse:
        """
        @summary 合作伙伴获取用户SLR角色授权临时凭证
        
        @param request: GetUserTmpIdentityForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserTmpIdentityForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTmpIdentityForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetUserTmpIdentityForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_tmp_identity_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.GetUserTmpIdentityForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.GetUserTmpIdentityForPartnerResponse:
        """
        @summary 合作伙伴获取用户SLR角色授权临时凭证
        
        @param request: GetUserTmpIdentityForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserTmpIdentityForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTmpIdentityForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.GetUserTmpIdentityForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_tmp_identity_for_partner(
        self,
        request: website_build_20250429_models.GetUserTmpIdentityForPartnerRequest,
    ) -> website_build_20250429_models.GetUserTmpIdentityForPartnerResponse:
        """
        @summary 合作伙伴获取用户SLR角色授权临时凭证
        
        @param request: GetUserTmpIdentityForPartnerRequest
        @return: GetUserTmpIdentityForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_tmp_identity_for_partner_with_options(request, runtime)

    async def get_user_tmp_identity_for_partner_async(
        self,
        request: website_build_20250429_models.GetUserTmpIdentityForPartnerRequest,
    ) -> website_build_20250429_models.GetUserTmpIdentityForPartnerResponse:
        """
        @summary 合作伙伴获取用户SLR角色授权临时凭证
        
        @param request: GetUserTmpIdentityForPartnerRequest
        @return: GetUserTmpIdentityForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_tmp_identity_for_partner_with_options_async(request, runtime)

    def list_app_domain_redirect_records_with_options(
        self,
        request: website_build_20250429_models.ListAppDomainRedirectRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.ListAppDomainRedirectRecordsResponse:
        """
        @summary 查询域名的跳转规则列表
        
        @param request: ListAppDomainRedirectRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppDomainRedirectRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppDomainRedirectRecords',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.ListAppDomainRedirectRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_domain_redirect_records_with_options_async(
        self,
        request: website_build_20250429_models.ListAppDomainRedirectRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.ListAppDomainRedirectRecordsResponse:
        """
        @summary 查询域名的跳转规则列表
        
        @param request: ListAppDomainRedirectRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppDomainRedirectRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppDomainRedirectRecords',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.ListAppDomainRedirectRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_domain_redirect_records(
        self,
        request: website_build_20250429_models.ListAppDomainRedirectRecordsRequest,
    ) -> website_build_20250429_models.ListAppDomainRedirectRecordsResponse:
        """
        @summary 查询域名的跳转规则列表
        
        @param request: ListAppDomainRedirectRecordsRequest
        @return: ListAppDomainRedirectRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_domain_redirect_records_with_options(request, runtime)

    async def list_app_domain_redirect_records_async(
        self,
        request: website_build_20250429_models.ListAppDomainRedirectRecordsRequest,
    ) -> website_build_20250429_models.ListAppDomainRedirectRecordsResponse:
        """
        @summary 查询域名的跳转规则列表
        
        @param request: ListAppDomainRedirectRecordsRequest
        @return: ListAppDomainRedirectRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_domain_redirect_records_with_options_async(request, runtime)

    def list_app_instance_domains_with_options(
        self,
        request: website_build_20250429_models.ListAppInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.ListAppInstanceDomainsResponse:
        """
        @summary 查询应用实例下的所有域名列表
        
        @param request: ListAppInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppInstanceDomains',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.ListAppInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_domains_with_options_async(
        self,
        request: website_build_20250429_models.ListAppInstanceDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.ListAppInstanceDomainsResponse:
        """
        @summary 查询应用实例下的所有域名列表
        
        @param request: ListAppInstanceDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppInstanceDomainsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppInstanceDomains',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.ListAppInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance_domains(
        self,
        request: website_build_20250429_models.ListAppInstanceDomainsRequest,
    ) -> website_build_20250429_models.ListAppInstanceDomainsResponse:
        """
        @summary 查询应用实例下的所有域名列表
        
        @param request: ListAppInstanceDomainsRequest
        @return: ListAppInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_app_instance_domains_with_options(request, runtime)

    async def list_app_instance_domains_async(
        self,
        request: website_build_20250429_models.ListAppInstanceDomainsRequest,
    ) -> website_build_20250429_models.ListAppInstanceDomainsResponse:
        """
        @summary 查询应用实例下的所有域名列表
        
        @param request: ListAppInstanceDomainsRequest
        @return: ListAppInstanceDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_app_instance_domains_with_options_async(request, runtime)

    def operate_app_instance_for_partner_with_options(
        self,
        request: website_build_20250429_models.OperateAppInstanceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴操作应用
        
        @param request: OperateAppInstanceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppInstanceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppInstanceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_instance_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.OperateAppInstanceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴操作应用
        
        @param request: OperateAppInstanceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppInstanceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppInstanceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_instance_for_partner(
        self,
        request: website_build_20250429_models.OperateAppInstanceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴操作应用
        
        @param request: OperateAppInstanceForPartnerRequest
        @return: OperateAppInstanceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_app_instance_for_partner_with_options(request, runtime)

    async def operate_app_instance_for_partner_async(
        self,
        request: website_build_20250429_models.OperateAppInstanceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴操作应用
        
        @param request: OperateAppInstanceForPartnerRequest
        @return: OperateAppInstanceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_app_instance_for_partner_with_options_async(request, runtime)

    def operate_app_service_for_partner_with_options(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppServiceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppServiceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppServiceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_service_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppServiceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppServiceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppServiceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_service_for_partner(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @return: OperateAppServiceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_app_service_for_partner_with_options(request, runtime)

    async def operate_app_service_for_partner_async(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @return: OperateAppServiceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_app_service_for_partner_with_options_async(request, runtime)

    def search_image_with_options(
        self,
        tmp_req: website_build_20250429_models.SearchImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SearchImageResponse:
        """
        @summary 图片检索
        
        @param tmp_req: SearchImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = website_build_20250429_models.SearchImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not UtilClient.is_unset(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not UtilClient.is_unset(request.has_person):
            query['HasPerson'] = request.has_person
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not UtilClient.is_unset(request.max_height):
            query['MaxHeight'] = request.max_height
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.max_width):
            query['MaxWidth'] = request.max_width
        if not UtilClient.is_unset(request.min_height):
            query['MinHeight'] = request.min_height
        if not UtilClient.is_unset(request.min_width):
            query['MinWidth'] = request.min_width
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImage',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SearchImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_with_options_async(
        self,
        tmp_req: website_build_20250429_models.SearchImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SearchImageResponse:
        """
        @summary 图片检索
        
        @param tmp_req: SearchImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = website_build_20250429_models.SearchImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not UtilClient.is_unset(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not UtilClient.is_unset(request.has_person):
            query['HasPerson'] = request.has_person
        if not UtilClient.is_unset(request.image_category):
            query['ImageCategory'] = request.image_category
        if not UtilClient.is_unset(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not UtilClient.is_unset(request.max_height):
            query['MaxHeight'] = request.max_height
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.max_width):
            query['MaxWidth'] = request.max_width
        if not UtilClient.is_unset(request.min_height):
            query['MinHeight'] = request.min_height
        if not UtilClient.is_unset(request.min_width):
            query['MinWidth'] = request.min_width
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oss_key):
            query['OssKey'] = request.oss_key
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImage',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SearchImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image(
        self,
        request: website_build_20250429_models.SearchImageRequest,
    ) -> website_build_20250429_models.SearchImageResponse:
        """
        @summary 图片检索
        
        @param request: SearchImageRequest
        @return: SearchImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_with_options(request, runtime)

    async def search_image_async(
        self,
        request: website_build_20250429_models.SearchImageRequest,
    ) -> website_build_20250429_models.SearchImageResponse:
        """
        @summary 图片检索
        
        @param request: SearchImageRequest
        @return: SearchImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_with_options_async(request, runtime)

    def set_app_domain_certificate_with_options(
        self,
        request: website_build_20250429_models.SetAppDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SetAppDomainCertificateResponse:
        """
        @summary 设置域名的SSL证书
        
        @param request: SetAppDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAppDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAppDomainCertificate',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SetAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_app_domain_certificate_with_options_async(
        self,
        request: website_build_20250429_models.SetAppDomainCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SetAppDomainCertificateResponse:
        """
        @summary 设置域名的SSL证书
        
        @param request: SetAppDomainCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetAppDomainCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAppDomainCertificate',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SetAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_app_domain_certificate(
        self,
        request: website_build_20250429_models.SetAppDomainCertificateRequest,
    ) -> website_build_20250429_models.SetAppDomainCertificateResponse:
        """
        @summary 设置域名的SSL证书
        
        @param request: SetAppDomainCertificateRequest
        @return: SetAppDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_app_domain_certificate_with_options(request, runtime)

    async def set_app_domain_certificate_async(
        self,
        request: website_build_20250429_models.SetAppDomainCertificateRequest,
    ) -> website_build_20250429_models.SetAppDomainCertificateResponse:
        """
        @summary 设置域名的SSL证书
        
        @param request: SetAppDomainCertificateRequest
        @return: SetAppDomainCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_app_domain_certificate_with_options_async(request, runtime)

    def sync_app_instance_for_partner_with_options(
        self,
        tmp_req: website_build_20250429_models.SyncAppInstanceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SyncAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴同步应用实例
        
        @param tmp_req: SyncAppInstanceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncAppInstanceForPartnerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = website_build_20250429_models.SyncAppInstanceForPartnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_instance):
            request.app_instance_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncAppInstanceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SyncAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_app_instance_for_partner_with_options_async(
        self,
        tmp_req: website_build_20250429_models.SyncAppInstanceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.SyncAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴同步应用实例
        
        @param tmp_req: SyncAppInstanceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncAppInstanceForPartnerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = website_build_20250429_models.SyncAppInstanceForPartnerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.app_instance):
            request.app_instance_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncAppInstanceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.SyncAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_app_instance_for_partner(
        self,
        request: website_build_20250429_models.SyncAppInstanceForPartnerRequest,
    ) -> website_build_20250429_models.SyncAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴同步应用实例
        
        @param request: SyncAppInstanceForPartnerRequest
        @return: SyncAppInstanceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_app_instance_for_partner_with_options(request, runtime)

    async def sync_app_instance_for_partner_async(
        self,
        request: website_build_20250429_models.SyncAppInstanceForPartnerRequest,
    ) -> website_build_20250429_models.SyncAppInstanceForPartnerResponse:
        """
        @summary 合作伙伴同步应用实例
        
        @param request: SyncAppInstanceForPartnerRequest
        @return: SyncAppInstanceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_app_instance_for_partner_with_options_async(request, runtime)

    def unbind_app_domain_with_options(
        self,
        request: website_build_20250429_models.UnbindAppDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.UnbindAppDomainResponse:
        """
        @summary 解绑应用域名
        
        @param request: UnbindAppDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAppDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAppDomain',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.UnbindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_app_domain_with_options_async(
        self,
        request: website_build_20250429_models.UnbindAppDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.UnbindAppDomainResponse:
        """
        @summary 解绑应用域名
        
        @param request: UnbindAppDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindAppDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAppDomain',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.UnbindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_app_domain(
        self,
        request: website_build_20250429_models.UnbindAppDomainRequest,
    ) -> website_build_20250429_models.UnbindAppDomainResponse:
        """
        @summary 解绑应用域名
        
        @param request: UnbindAppDomainRequest
        @return: UnbindAppDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_app_domain_with_options(request, runtime)

    async def unbind_app_domain_async(
        self,
        request: website_build_20250429_models.UnbindAppDomainRequest,
    ) -> website_build_20250429_models.UnbindAppDomainResponse:
        """
        @summary 解绑应用域名
        
        @param request: UnbindAppDomainRequest
        @return: UnbindAppDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_app_domain_with_options_async(request, runtime)
