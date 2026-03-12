# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_domain20160511 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('domain', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_domain_with_options(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_domain_with_options_async(
        self,
        request: main_models.CheckDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDomainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDomain',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_domain(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return self.check_domain_with_options(request, runtime)

    async def check_domain_async(
        self,
        request: main_models.CheckDomainRequest,
    ) -> main_models.CheckDomainResponse:
        runtime = RuntimeOptions()
        return await self.check_domain_with_options_async(request, runtime)

    def delete_contact_template_with_options(
        self,
        request: main_models.DeleteContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_template_with_options_async(
        self,
        request: main_models.DeleteContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_template(
        self,
        request: main_models.DeleteContactTemplateRequest,
    ) -> main_models.DeleteContactTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_template_with_options(request, runtime)

    async def delete_contact_template_async(
        self,
        request: main_models.DeleteContactTemplateRequest,
    ) -> main_models.DeleteContactTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_template_with_options_async(request, runtime)

    def query_batch_task_detail_list_with_options(
        self,
        request: main_models.QueryBatchTaskDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBatchTaskDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBatchTaskDetailList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBatchTaskDetailListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_batch_task_detail_list_with_options_async(
        self,
        request: main_models.QueryBatchTaskDetailListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBatchTaskDetailListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.task_no):
            query['TaskNo'] = request.task_no
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBatchTaskDetailList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBatchTaskDetailListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_batch_task_detail_list(
        self,
        request: main_models.QueryBatchTaskDetailListRequest,
    ) -> main_models.QueryBatchTaskDetailListResponse:
        runtime = RuntimeOptions()
        return self.query_batch_task_detail_list_with_options(request, runtime)

    async def query_batch_task_detail_list_async(
        self,
        request: main_models.QueryBatchTaskDetailListRequest,
    ) -> main_models.QueryBatchTaskDetailListResponse:
        runtime = RuntimeOptions()
        return await self.query_batch_task_detail_list_with_options_async(request, runtime)

    def query_batch_task_list_with_options(
        self,
        request: main_models.QueryBatchTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBatchTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBatchTaskList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBatchTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_batch_task_list_with_options_async(
        self,
        request: main_models.QueryBatchTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBatchTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_create_time):
            query['BeginCreateTime'] = request.begin_create_time
        if not DaraCore.is_null(request.end_create_time):
            query['EndCreateTime'] = request.end_create_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBatchTaskList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBatchTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_batch_task_list(
        self,
        request: main_models.QueryBatchTaskListRequest,
    ) -> main_models.QueryBatchTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_batch_task_list_with_options(request, runtime)

    async def query_batch_task_list_async(
        self,
        request: main_models.QueryBatchTaskListRequest,
    ) -> main_models.QueryBatchTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_batch_task_list_with_options_async(request, runtime)

    def query_contact_with_options(
        self,
        request: main_models.QueryContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContact',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contact_with_options_async(
        self,
        request: main_models.QueryContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContact',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contact(
        self,
        request: main_models.QueryContactRequest,
    ) -> main_models.QueryContactResponse:
        runtime = RuntimeOptions()
        return self.query_contact_with_options(request, runtime)

    async def query_contact_async(
        self,
        request: main_models.QueryContactRequest,
    ) -> main_models.QueryContactResponse:
        runtime = RuntimeOptions()
        return await self.query_contact_with_options_async(request, runtime)

    def query_contact_template_with_options(
        self,
        request: main_models.QueryContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.ccompany):
            query['CCompany'] = request.ccompany
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.default_template):
            query['DefaultTemplate'] = request.default_template
        if not DaraCore.is_null(request.ecompany):
            query['ECompany'] = request.ecompany
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_contact_template_with_options_async(
        self,
        request: main_models.QueryContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.ccompany):
            query['CCompany'] = request.ccompany
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.default_template):
            query['DefaultTemplate'] = request.default_template
        if not DaraCore.is_null(request.ecompany):
            query['ECompany'] = request.ecompany
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContactTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_contact_template(
        self,
        request: main_models.QueryContactTemplateRequest,
    ) -> main_models.QueryContactTemplateResponse:
        runtime = RuntimeOptions()
        return self.query_contact_template_with_options(request, runtime)

    async def query_contact_template_async(
        self,
        request: main_models.QueryContactTemplateRequest,
    ) -> main_models.QueryContactTemplateResponse:
        runtime = RuntimeOptions()
        return await self.query_contact_template_with_options_async(request, runtime)

    def query_domain_by_sale_id_with_options(
        self,
        request: main_models.QueryDomainBySaleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainBySaleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainBySaleId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainBySaleIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_by_sale_id_with_options_async(
        self,
        request: main_models.QueryDomainBySaleIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainBySaleIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainBySaleId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainBySaleIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_by_sale_id(
        self,
        request: main_models.QueryDomainBySaleIdRequest,
    ) -> main_models.QueryDomainBySaleIdResponse:
        runtime = RuntimeOptions()
        return self.query_domain_by_sale_id_with_options(request, runtime)

    async def query_domain_by_sale_id_async(
        self,
        request: main_models.QueryDomainBySaleIdRequest,
    ) -> main_models.QueryDomainBySaleIdResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_by_sale_id_with_options_async(request, runtime)

    def query_domain_list_with_options(
        self,
        request: main_models.QueryDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dead_end_date):
            query['DeadEndDate'] = request.dead_end_date
        if not DaraCore.is_null(request.dead_start_date):
            query['DeadStartDate'] = request.dead_start_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.reg_end_date):
            query['RegEndDate'] = request.reg_end_date
        if not DaraCore.is_null(request.reg_start_date):
            query['RegStartDate'] = request.reg_start_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_domain_list_with_options_async(
        self,
        request: main_models.QueryDomainListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDomainListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dead_end_date):
            query['DeadEndDate'] = request.dead_end_date
        if not DaraCore.is_null(request.dead_start_date):
            query['DeadStartDate'] = request.dead_start_date
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.domain_type):
            query['DomainType'] = request.domain_type
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.order_key_type):
            query['OrderKeyType'] = request.order_key_type
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_domain_type):
            query['ProductDomainType'] = request.product_domain_type
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.reg_end_date):
            query['RegEndDate'] = request.reg_end_date
        if not DaraCore.is_null(request.reg_start_date):
            query['RegStartDate'] = request.reg_start_date
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDomainList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_domain_list(
        self,
        request: main_models.QueryDomainListRequest,
    ) -> main_models.QueryDomainListResponse:
        runtime = RuntimeOptions()
        return self.query_domain_list_with_options(request, runtime)

    async def query_domain_list_async(
        self,
        request: main_models.QueryDomainListRequest,
    ) -> main_models.QueryDomainListResponse:
        runtime = RuntimeOptions()
        return await self.query_domain_list_with_options_async(request, runtime)

    def query_fail_reason_list_with_options(
        self,
        request: main_models.QueryFailReasonListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_fail_reason_list_with_options_async(
        self,
        request: main_models.QueryFailReasonListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFailReasonListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFailReasonList',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFailReasonListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_fail_reason_list(
        self,
        request: main_models.QueryFailReasonListRequest,
    ) -> main_models.QueryFailReasonListResponse:
        runtime = RuntimeOptions()
        return self.query_fail_reason_list_with_options(request, runtime)

    async def query_fail_reason_list_async(
        self,
        request: main_models.QueryFailReasonListRequest,
    ) -> main_models.QueryFailReasonListResponse:
        runtime = RuntimeOptions()
        return await self.query_fail_reason_list_with_options_async(request, runtime)

    def save_contact_template_with_options(
        self,
        request: main_models.SaveContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccity):
            query['CCity'] = request.ccity
        if not DaraCore.is_null(request.ccompany):
            query['CCompany'] = request.ccompany
        if not DaraCore.is_null(request.ccountry):
            query['CCountry'] = request.ccountry
        if not DaraCore.is_null(request.cname):
            query['CName'] = request.cname
        if not DaraCore.is_null(request.cprovince):
            query['CProvince'] = request.cprovince
        if not DaraCore.is_null(request.cvenu):
            query['CVenu'] = request.cvenu
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.default_template):
            query['DefaultTemplate'] = request.default_template
        if not DaraCore.is_null(request.ecity):
            query['ECity'] = request.ecity
        if not DaraCore.is_null(request.ecompany):
            query['ECompany'] = request.ecompany
        if not DaraCore.is_null(request.ename):
            query['EName'] = request.ename
        if not DaraCore.is_null(request.eprovince):
            query['EProvince'] = request.eprovince
        if not DaraCore.is_null(request.evenu):
            query['EVenu'] = request.evenu
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.tel_main):
            query['TelMain'] = request.tel_main
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_template_with_options_async(
        self,
        request: main_models.SaveContactTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ccity):
            query['CCity'] = request.ccity
        if not DaraCore.is_null(request.ccompany):
            query['CCompany'] = request.ccompany
        if not DaraCore.is_null(request.ccountry):
            query['CCountry'] = request.ccountry
        if not DaraCore.is_null(request.cname):
            query['CName'] = request.cname
        if not DaraCore.is_null(request.cprovince):
            query['CProvince'] = request.cprovince
        if not DaraCore.is_null(request.cvenu):
            query['CVenu'] = request.cvenu
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.default_template):
            query['DefaultTemplate'] = request.default_template
        if not DaraCore.is_null(request.ecity):
            query['ECity'] = request.ecity
        if not DaraCore.is_null(request.ecompany):
            query['ECompany'] = request.ecompany
        if not DaraCore.is_null(request.ename):
            query['EName'] = request.ename
        if not DaraCore.is_null(request.eprovince):
            query['EProvince'] = request.eprovince
        if not DaraCore.is_null(request.evenu):
            query['EVenu'] = request.evenu
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.postal_code):
            query['PostalCode'] = request.postal_code
        if not DaraCore.is_null(request.reg_type):
            query['RegType'] = request.reg_type
        if not DaraCore.is_null(request.tel_area):
            query['TelArea'] = request.tel_area
        if not DaraCore.is_null(request.tel_ext):
            query['TelExt'] = request.tel_ext
        if not DaraCore.is_null(request.tel_main):
            query['TelMain'] = request.tel_main
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactTemplate',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_template(
        self,
        request: main_models.SaveContactTemplateRequest,
    ) -> main_models.SaveContactTemplateResponse:
        runtime = RuntimeOptions()
        return self.save_contact_template_with_options(request, runtime)

    async def save_contact_template_async(
        self,
        request: main_models.SaveContactTemplateRequest,
    ) -> main_models.SaveContactTemplateResponse:
        runtime = RuntimeOptions()
        return await self.save_contact_template_with_options_async(request, runtime)

    def save_contact_template_credential_with_options(
        self,
        request: main_models.SaveContactTemplateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactTemplateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactTemplateCredential',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactTemplateCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_contact_template_credential_with_options_async(
        self,
        request: main_models.SaveContactTemplateCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveContactTemplateCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveContactTemplateCredential',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveContactTemplateCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_contact_template_credential(
        self,
        request: main_models.SaveContactTemplateCredentialRequest,
    ) -> main_models.SaveContactTemplateCredentialResponse:
        runtime = RuntimeOptions()
        return self.save_contact_template_credential_with_options(request, runtime)

    async def save_contact_template_credential_async(
        self,
        request: main_models.SaveContactTemplateCredentialRequest,
    ) -> main_models.SaveContactTemplateCredentialResponse:
        runtime = RuntimeOptions()
        return await self.save_contact_template_credential_with_options_async(request, runtime)

    def save_task_for_modifying_domain_dns_with_options(
        self,
        request: main_models.SaveTaskForModifyingDomainDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForModifyingDomainDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.dns_list):
            query['DnsList'] = request.dns_list
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForModifyingDomainDns',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForModifyingDomainDnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_modifying_domain_dns_with_options_async(
        self,
        request: main_models.SaveTaskForModifyingDomainDnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForModifyingDomainDnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_dns):
            query['AliyunDns'] = request.aliyun_dns
        if not DaraCore.is_null(request.dns_list):
            query['DnsList'] = request.dns_list
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForModifyingDomainDns',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForModifyingDomainDnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_modifying_domain_dns(
        self,
        request: main_models.SaveTaskForModifyingDomainDnsRequest,
    ) -> main_models.SaveTaskForModifyingDomainDnsResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_modifying_domain_dns_with_options(request, runtime)

    async def save_task_for_modifying_domain_dns_async(
        self,
        request: main_models.SaveTaskForModifyingDomainDnsRequest,
    ) -> main_models.SaveTaskForModifyingDomainDnsResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_modifying_domain_dns_with_options_async(request, runtime)

    def save_task_for_submitting_domain_name_credential_with_options(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainNameCredential',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainNameCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_name_credential_with_options_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credential):
            query['Credential'] = request.credential
        if not DaraCore.is_null(request.credential_no):
            query['CredentialNo'] = request.credential_no
        if not DaraCore.is_null(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainNameCredential',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainNameCredentialResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_name_credential(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialRequest,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_submitting_domain_name_credential_with_options(request, runtime)

    async def save_task_for_submitting_domain_name_credential_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialRequest,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_submitting_domain_name_credential_with_options_async(request, runtime)

    def save_task_for_submitting_domain_name_credential_by_template_id_with_options(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainNameCredentialByTemplateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_submitting_domain_name_credential_by_template_id_with_options_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForSubmittingDomainNameCredentialByTemplateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_submitting_domain_name_credential_by_template_id(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdRequest,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_submitting_domain_name_credential_by_template_id_with_options(request, runtime)

    async def save_task_for_submitting_domain_name_credential_by_template_id_async(
        self,
        request: main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdRequest,
    ) -> main_models.SaveTaskForSubmittingDomainNameCredentialByTemplateIdResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_submitting_domain_name_credential_by_template_id_with_options_async(request, runtime)

    def save_task_for_updating_contact_by_tempate_id_with_options(
        self,
        request: main_models.SaveTaskForUpdatingContactByTempateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingContactByTempateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingContactByTempateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingContactByTempateIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_contact_by_tempate_id_with_options_async(
        self,
        request: main_models.SaveTaskForUpdatingContactByTempateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingContactByTempateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingContactByTempateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingContactByTempateIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_contact_by_tempate_id(
        self,
        request: main_models.SaveTaskForUpdatingContactByTempateIdRequest,
    ) -> main_models.SaveTaskForUpdatingContactByTempateIdResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_updating_contact_by_tempate_id_with_options(request, runtime)

    async def save_task_for_updating_contact_by_tempate_id_async(
        self,
        request: main_models.SaveTaskForUpdatingContactByTempateIdRequest,
    ) -> main_models.SaveTaskForUpdatingContactByTempateIdResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_updating_contact_by_tempate_id_with_options_async(request, runtime)

    def save_task_for_updating_contact_by_template_id_with_options(
        self,
        request: main_models.SaveTaskForUpdatingContactByTemplateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingContactByTemplateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingContactByTemplateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingContactByTemplateIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_task_for_updating_contact_by_template_id_with_options_async(
        self,
        request: main_models.SaveTaskForUpdatingContactByTemplateIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTaskForUpdatingContactByTemplateIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_transfer_lock):
            query['AddTransferLock'] = request.add_transfer_lock
        if not DaraCore.is_null(request.contact_template_id):
            query['ContactTemplateId'] = request.contact_template_id
        if not DaraCore.is_null(request.contact_type):
            query['ContactType'] = request.contact_type
        if not DaraCore.is_null(request.domain_name):
            query['DomainName'] = request.domain_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTaskForUpdatingContactByTemplateId',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTaskForUpdatingContactByTemplateIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_task_for_updating_contact_by_template_id(
        self,
        request: main_models.SaveTaskForUpdatingContactByTemplateIdRequest,
    ) -> main_models.SaveTaskForUpdatingContactByTemplateIdResponse:
        runtime = RuntimeOptions()
        return self.save_task_for_updating_contact_by_template_id_with_options(request, runtime)

    async def save_task_for_updating_contact_by_template_id_async(
        self,
        request: main_models.SaveTaskForUpdatingContactByTemplateIdRequest,
    ) -> main_models.SaveTaskForUpdatingContactByTemplateIdResponse:
        runtime = RuntimeOptions()
        return await self.save_task_for_updating_contact_by_template_id_with_options_async(request, runtime)

    def whois_protection_with_options(
        self,
        request: main_models.WhoisProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WhoisProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_content):
            query['DataContent'] = request.data_content
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.whois_protect):
            query['WhoisProtect'] = request.whois_protect
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WhoisProtection',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WhoisProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def whois_protection_with_options_async(
        self,
        request: main_models.WhoisProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WhoisProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_content):
            query['DataContent'] = request.data_content
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.user_client_ip):
            query['UserClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.whois_protect):
            query['WhoisProtect'] = request.whois_protect
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WhoisProtection',
            version = '2016-05-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WhoisProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def whois_protection(
        self,
        request: main_models.WhoisProtectionRequest,
    ) -> main_models.WhoisProtectionResponse:
        runtime = RuntimeOptions()
        return self.whois_protection_with_options(request, runtime)

    async def whois_protection_async(
        self,
        request: main_models.WhoisProtectionRequest,
    ) -> main_models.WhoisProtectionResponse:
        runtime = RuntimeOptions()
        return await self.whois_protection_with_options_async(request, runtime)
