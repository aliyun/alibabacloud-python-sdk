# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_app_domain_with_options(
        self,
        request: main_models.BindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_app_domain_with_options_async(
        self,
        request: main_models.BindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_app_domain(
        self,
        request: main_models.BindAppDomainRequest,
    ) -> main_models.BindAppDomainResponse:
        runtime = RuntimeOptions()
        return self.bind_app_domain_with_options(request, runtime)

    async def bind_app_domain_async(
        self,
        request: main_models.BindAppDomainRequest,
    ) -> main_models.BindAppDomainResponse:
        runtime = RuntimeOptions()
        return await self.bind_app_domain_with_options_async(request, runtime)

    def create_app_instance_with_options(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_with_options_async(
        self,
        tmp_req: main_models.CreateAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateAppInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance(
        self,
        request: main_models.CreateAppInstanceRequest,
    ) -> main_models.CreateAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_app_instance_with_options(request, runtime)

    async def create_app_instance_async(
        self,
        request: main_models.CreateAppInstanceRequest,
    ) -> main_models.CreateAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_app_instance_with_options_async(request, runtime)

    def create_app_instance_ticket_with_options(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_ticket_with_options_async(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAppInstanceTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance_ticket(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
    ) -> main_models.CreateAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return self.create_app_instance_ticket_with_options(request, runtime)

    async def create_app_instance_ticket_async(
        self,
        request: main_models.CreateAppInstanceTicketRequest,
    ) -> main_models.CreateAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return await self.create_app_instance_ticket_with_options_async(request, runtime)

    def create_logo_task_with_options(
        self,
        request: main_models.CreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_logo_task_with_options_async(
        self,
        request: main_models.CreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logo_version):
            query['LogoVersion'] = request.logo_version
        if not DaraCore.is_null(request.negative_prompt):
            query['NegativePrompt'] = request.negative_prompt
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_logo_task(
        self,
        request: main_models.CreateLogoTaskRequest,
    ) -> main_models.CreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return self.create_logo_task_with_options(request, runtime)

    async def create_logo_task_async(
        self,
        request: main_models.CreateLogoTaskRequest,
    ) -> main_models.CreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_logo_task_with_options_async(request, runtime)

    def delete_app_domain_certificate_with_options(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_certificate_with_options_async(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_certificate(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_app_domain_certificate_with_options(request, runtime)

    async def delete_app_domain_certificate_async(
        self,
        request: main_models.DeleteAppDomainCertificateRequest,
    ) -> main_models.DeleteAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_domain_certificate_with_options_async(request, runtime)

    def delete_app_domain_redirect_with_options(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainRedirect',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainRedirectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_domain_redirect_with_options_async(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppDomainRedirect',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppDomainRedirectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_domain_redirect(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        runtime = RuntimeOptions()
        return self.delete_app_domain_redirect_with_options(request, runtime)

    async def delete_app_domain_redirect_async(
        self,
        request: main_models.DeleteAppDomainRedirectRequest,
    ) -> main_models.DeleteAppDomainRedirectResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_domain_redirect_with_options_async(request, runtime)

    def describe_app_domain_dns_record_with_options(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppDomainDnsRecord',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppDomainDnsRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_domain_dns_record_with_options_async(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.purpose):
            query['Purpose'] = request.purpose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAppDomainDnsRecord',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAppDomainDnsRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_domain_dns_record(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        runtime = RuntimeOptions()
        return self.describe_app_domain_dns_record_with_options(request, runtime)

    async def describe_app_domain_dns_record_async(
        self,
        request: main_models.DescribeAppDomainDnsRecordRequest,
    ) -> main_models.DescribeAppDomainDnsRecordResponse:
        runtime = RuntimeOptions()
        return await self.describe_app_domain_dns_record_with_options_async(request, runtime)

    def dispatch_console_apifor_partner_with_options(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.live_token):
            query['LiveToken'] = request.live_token
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DispatchConsoleAPIForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DispatchConsoleAPIForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def dispatch_console_apifor_partner_with_options_async(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.live_token):
            query['LiveToken'] = request.live_token
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.params):
            query['Params'] = request.params
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DispatchConsoleAPIForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DispatchConsoleAPIForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dispatch_console_apifor_partner(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        runtime = RuntimeOptions()
        return self.dispatch_console_apifor_partner_with_options(request, runtime)

    async def dispatch_console_apifor_partner_async(
        self,
        request: main_models.DispatchConsoleAPIForPartnerRequest,
    ) -> main_models.DispatchConsoleAPIForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.dispatch_console_apifor_partner_with_options_async(request, runtime)

    def get_app_instance_with_options(
        self,
        request: main_models.GetAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_instance_with_options_async(
        self,
        request: main_models.GetAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_instance(
        self,
        request: main_models.GetAppInstanceRequest,
    ) -> main_models.GetAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_app_instance_with_options(request, runtime)

    async def get_app_instance_async(
        self,
        request: main_models.GetAppInstanceRequest,
    ) -> main_models.GetAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_app_instance_with_options_async(request, runtime)

    def get_create_logo_task_with_options(
        self,
        request: main_models.GetCreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateLogoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_logo_task_with_options_async(
        self,
        request: main_models.GetCreateLogoTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateLogoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateLogoTask',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateLogoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_logo_task(
        self,
        request: main_models.GetCreateLogoTaskRequest,
    ) -> main_models.GetCreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return self.get_create_logo_task_with_options(request, runtime)

    async def get_create_logo_task_async(
        self,
        request: main_models.GetCreateLogoTaskRequest,
    ) -> main_models.GetCreateLogoTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_create_logo_task_with_options_async(request, runtime)

    def get_domain_info_for_partner_with_options(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_domain_info_for_partner_with_options_async(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDomainInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDomainInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_domain_info_for_partner(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_domain_info_for_partner_with_options(request, runtime)

    async def get_domain_info_for_partner_async(
        self,
        request: main_models.GetDomainInfoForPartnerRequest,
    ) -> main_models.GetDomainInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_domain_info_for_partner_with_options_async(request, runtime)

    def get_icp_filing_info_for_partner_with_options(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIcpFilingInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcpFilingInfoForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_icp_filing_info_for_partner_with_options_async(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIcpFilingInfoForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcpFilingInfoForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_icp_filing_info_for_partner(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_icp_filing_info_for_partner_with_options(request, runtime)

    async def get_icp_filing_info_for_partner_async(
        self,
        request: main_models.GetIcpFilingInfoForPartnerRequest,
    ) -> main_models.GetIcpFilingInfoForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_icp_filing_info_for_partner_with_options_async(request, runtime)

    def get_user_access_token_for_partner_with_options(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAccessTokenForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAccessTokenForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_access_token_for_partner_with_options_async(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.site_host):
            query['SiteHost'] = request.site_host
        if not DaraCore.is_null(request.ticket):
            query['Ticket'] = request.ticket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAccessTokenForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAccessTokenForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_access_token_for_partner(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_user_access_token_for_partner_with_options(request, runtime)

    async def get_user_access_token_for_partner_async(
        self,
        request: main_models.GetUserAccessTokenForPartnerRequest,
    ) -> main_models.GetUserAccessTokenForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_user_access_token_for_partner_with_options_async(request, runtime)

    def get_user_tmp_identity_for_partner_with_options(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserTmpIdentityForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTmpIdentityForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_tmp_identity_for_partner_with_options_async(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_purpose):
            query['AuthPurpose'] = request.auth_purpose
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.service_linked_role):
            query['ServiceLinkedRole'] = request.service_linked_role
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserTmpIdentityForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTmpIdentityForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_tmp_identity_for_partner(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        runtime = RuntimeOptions()
        return self.get_user_tmp_identity_for_partner_with_options(request, runtime)

    async def get_user_tmp_identity_for_partner_async(
        self,
        request: main_models.GetUserTmpIdentityForPartnerRequest,
    ) -> main_models.GetUserTmpIdentityForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.get_user_tmp_identity_for_partner_with_options_async(request, runtime)

    def list_app_domain_redirect_records_with_options(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppDomainRedirectRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppDomainRedirectRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_domain_redirect_records_with_options_async(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppDomainRedirectRecords',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppDomainRedirectRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_domain_redirect_records(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_app_domain_redirect_records_with_options(request, runtime)

    async def list_app_domain_redirect_records_async(
        self,
        request: main_models.ListAppDomainRedirectRecordsRequest,
    ) -> main_models.ListAppDomainRedirectRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_domain_redirect_records_with_options_async(request, runtime)

    def list_app_instance_domains_with_options(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceDomains',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_domains_with_options_async(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstanceDomainsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstanceDomains',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstanceDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance_domains(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
    ) -> main_models.ListAppInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return self.list_app_instance_domains_with_options(request, runtime)

    async def list_app_instance_domains_async(
        self,
        request: main_models.ListAppInstanceDomainsRequest,
    ) -> main_models.ListAppInstanceDomainsResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instance_domains_with_options_async(request, runtime)

    def list_app_instances_with_options(
        self,
        tmp_req: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        tmp_req.validate()
        request = main_models.ListAppInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instances_with_options_async(
        self,
        tmp_req: main_models.ListAppInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAppInstancesResponse:
        tmp_req.validate()
        request = main_models.ListAppInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'StatusList', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.end_time_begin):
            query['EndTimeBegin'] = request.end_time_begin
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.status_list_shrink):
            query['StatusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAppInstances',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instances(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_app_instances_with_options(request, runtime)

    async def list_app_instances_async(
        self,
        request: main_models.ListAppInstancesRequest,
    ) -> main_models.ListAppInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_app_instances_with_options_async(request, runtime)

    def modify_app_instance_spec_with_options(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceSpec',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_app_instance_spec_with_options_async(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_area):
            query['DeployArea'] = request.deploy_area
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAppInstanceSpec',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAppInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_app_instance_spec(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_app_instance_spec_with_options(request, runtime)

    async def modify_app_instance_spec_async(
        self,
        request: main_models.ModifyAppInstanceSpecRequest,
    ) -> main_models.ModifyAppInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_app_instance_spec_with_options_async(request, runtime)

    def operate_app_instance_for_partner_with_options(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_instance_for_partner_with_options_async(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_instance_for_partner(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_app_instance_for_partner_with_options(request, runtime)

    async def operate_app_instance_for_partner_async(
        self,
        request: main_models.OperateAppInstanceForPartnerRequest,
    ) -> main_models.OperateAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_instance_for_partner_with_options_async(request, runtime)

    def operate_app_service_for_partner_with_options(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppServiceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppServiceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_service_for_partner_with_options_async(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateAppServiceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAppServiceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_service_for_partner(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.operate_app_service_for_partner_with_options(request, runtime)

    async def operate_app_service_for_partner_async(
        self,
        request: main_models.OperateAppServiceForPartnerRequest,
    ) -> main_models.OperateAppServiceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.operate_app_service_for_partner_with_options_async(request, runtime)

    def refresh_app_instance_ticket_with_options(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAppInstanceTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_app_instance_ticket_with_options_async(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshAppInstanceTicket',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshAppInstanceTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_app_instance_ticket(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return self.refresh_app_instance_ticket_with_options(request, runtime)

    async def refresh_app_instance_ticket_async(
        self,
        request: main_models.RefreshAppInstanceTicketRequest,
    ) -> main_models.RefreshAppInstanceTicketResponse:
        runtime = RuntimeOptions()
        return await self.refresh_app_instance_ticket_with_options_async(request, runtime)

    def refund_app_instance_for_partner_with_options(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.refund_reason):
            query['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_app_instance_for_partner_with_options_async(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.refund_reason):
            query['RefundReason'] = request.refund_reason
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_app_instance_for_partner(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.refund_app_instance_for_partner_with_options(request, runtime)

    async def refund_app_instance_for_partner_async(
        self,
        request: main_models.RefundAppInstanceForPartnerRequest,
    ) -> main_models.RefundAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.refund_app_instance_for_partner_with_options_async(request, runtime)

    def renew_app_instance_with_options(
        self,
        request: main_models.RenewAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_app_instance_with_options_async(
        self,
        request: main_models.RenewAppInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewAppInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.extend):
            query['Extend'] = request.extend
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewAppInstance',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_app_instance(
        self,
        request: main_models.RenewAppInstanceRequest,
    ) -> main_models.RenewAppInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_app_instance_with_options(request, runtime)

    async def renew_app_instance_async(
        self,
        request: main_models.RenewAppInstanceRequest,
    ) -> main_models.RenewAppInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_app_instance_with_options_async(request, runtime)

    def search_image_with_options(
        self,
        tmp_req: main_models.SearchImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageResponse:
        tmp_req.validate()
        request = main_models.SearchImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not DaraCore.is_null(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not DaraCore.is_null(request.has_person):
            query['HasPerson'] = request.has_person
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not DaraCore.is_null(request.max_height):
            query['MaxHeight'] = request.max_height
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.max_width):
            query['MaxWidth'] = request.max_width
        if not DaraCore.is_null(request.min_height):
            query['MinHeight'] = request.min_height
        if not DaraCore.is_null(request.min_width):
            query['MinWidth'] = request.min_width
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_with_options_async(
        self,
        tmp_req: main_models.SearchImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageResponse:
        tmp_req.validate()
        request = main_models.SearchImageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'simple')
        query = {}
        if not DaraCore.is_null(request.color_hex):
            query['ColorHex'] = request.color_hex
        if not DaraCore.is_null(request.has_person):
            query['HasPerson'] = request.has_person
        if not DaraCore.is_null(request.image_category):
            query['ImageCategory'] = request.image_category
        if not DaraCore.is_null(request.image_ratio):
            query['ImageRatio'] = request.image_ratio
        if not DaraCore.is_null(request.max_height):
            query['MaxHeight'] = request.max_height
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.max_width):
            query['MaxWidth'] = request.max_width
        if not DaraCore.is_null(request.min_height):
            query['MinHeight'] = request.min_height
        if not DaraCore.is_null(request.min_width):
            query['MinWidth'] = request.min_width
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oss_key):
            query['OssKey'] = request.oss_key
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.text):
            query['Text'] = request.text
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImage',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image(
        self,
        request: main_models.SearchImageRequest,
    ) -> main_models.SearchImageResponse:
        runtime = RuntimeOptions()
        return self.search_image_with_options(request, runtime)

    async def search_image_async(
        self,
        request: main_models.SearchImageRequest,
    ) -> main_models.SearchImageResponse:
        runtime = RuntimeOptions()
        return await self.search_image_with_options_async(request, runtime)

    def set_app_domain_certificate_with_options(
        self,
        request: main_models.SetAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_app_domain_certificate_with_options_async(
        self,
        request: main_models.SetAppDomainCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAppDomainCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not DaraCore.is_null(request.certificate_type):
            query['CertificateType'] = request.certificate_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.private_key):
            query['PrivateKey'] = request.private_key
        if not DaraCore.is_null(request.public_key):
            query['PublicKey'] = request.public_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAppDomainCertificate',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAppDomainCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_app_domain_certificate(
        self,
        request: main_models.SetAppDomainCertificateRequest,
    ) -> main_models.SetAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return self.set_app_domain_certificate_with_options(request, runtime)

    async def set_app_domain_certificate_async(
        self,
        request: main_models.SetAppDomainCertificateRequest,
    ) -> main_models.SetAppDomainCertificateResponse:
        runtime = RuntimeOptions()
        return await self.set_app_domain_certificate_with_options_async(request, runtime)

    def sync_app_instance_for_partner_with_options(
        self,
        tmp_req: main_models.SyncAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        tmp_req.validate()
        request = main_models.SyncAppInstanceForPartnerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_instance):
            request.app_instance_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAppInstanceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_app_instance_for_partner_with_options_async(
        self,
        tmp_req: main_models.SyncAppInstanceForPartnerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        tmp_req.validate()
        request = main_models.SyncAppInstanceForPartnerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.app_instance):
            request.app_instance_shrink = Utils.array_to_string_with_specified_style(tmp_req.app_instance, 'AppInstance', 'json')
        query = {}
        if not DaraCore.is_null(request.app_instance_shrink):
            query['AppInstance'] = request.app_instance_shrink
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.operator):
            query['Operator'] = request.operator
        if not DaraCore.is_null(request.source_biz_id):
            query['SourceBizId'] = request.source_biz_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncAppInstanceForPartner',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncAppInstanceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_app_instance_for_partner(
        self,
        request: main_models.SyncAppInstanceForPartnerRequest,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return self.sync_app_instance_for_partner_with_options(request, runtime)

    async def sync_app_instance_for_partner_async(
        self,
        request: main_models.SyncAppInstanceForPartnerRequest,
    ) -> main_models.SyncAppInstanceForPartnerResponse:
        runtime = RuntimeOptions()
        return await self.sync_app_instance_for_partner_with_options_async(request, runtime)

    def unbind_app_domain_with_options(
        self,
        request: main_models.UnbindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAppDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_app_domain_with_options_async(
        self,
        request: main_models.UnbindAppDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindAppDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_id):
            query['BizId'] = request.biz_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnbindAppDomain',
            version = '2025-04-29',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindAppDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_app_domain(
        self,
        request: main_models.UnbindAppDomainRequest,
    ) -> main_models.UnbindAppDomainResponse:
        runtime = RuntimeOptions()
        return self.unbind_app_domain_with_options(request, runtime)

    async def unbind_app_domain_async(
        self,
        request: main_models.UnbindAppDomainRequest,
    ) -> main_models.UnbindAppDomainResponse:
        runtime = RuntimeOptions()
        return await self.unbind_app_domain_with_options_async(request, runtime)
