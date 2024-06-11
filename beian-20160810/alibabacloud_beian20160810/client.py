# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_beian20160810 import models as beian_20160810_models
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
        self._endpoint = self.get_endpoint('beian', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def delete_unbeian_ip_check_type_with_options(
        self,
        request: beian_20160810_models.DeleteUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.DeleteUnbeianIpCheckTypeResponse:
        """
        @param request: DeleteUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.DeleteUnbeianIpCheckTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_unbeian_ip_check_type_with_options_async(
        self,
        request: beian_20160810_models.DeleteUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.DeleteUnbeianIpCheckTypeResponse:
        """
        @param request: DeleteUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.DeleteUnbeianIpCheckTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_unbeian_ip_check_type(
        self,
        request: beian_20160810_models.DeleteUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.DeleteUnbeianIpCheckTypeResponse:
        """
        @param request: DeleteUnbeianIpCheckTypeRequest
        @return: DeleteUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_unbeian_ip_check_type_with_options(request, runtime)

    async def delete_unbeian_ip_check_type_async(
        self,
        request: beian_20160810_models.DeleteUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.DeleteUnbeianIpCheckTypeResponse:
        """
        @param request: DeleteUnbeianIpCheckTypeRequest
        @return: DeleteUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_unbeian_ip_check_type_with_options_async(request, runtime)

    def get_main_domain_with_options(
        self,
        request: beian_20160810_models.GetMainDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.GetMainDomainResponse:
        """
        @summary 获取主域名接口
        
        @param request: GetMainDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMainDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.GetMainDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_main_domain_with_options_async(
        self,
        request: beian_20160810_models.GetMainDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.GetMainDomainResponse:
        """
        @summary 获取主域名接口
        
        @param request: GetMainDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMainDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMainDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.GetMainDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_main_domain(
        self,
        request: beian_20160810_models.GetMainDomainRequest,
    ) -> beian_20160810_models.GetMainDomainResponse:
        """
        @summary 获取主域名接口
        
        @param request: GetMainDomainRequest
        @return: GetMainDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_main_domain_with_options(request, runtime)

    async def get_main_domain_async(
        self,
        request: beian_20160810_models.GetMainDomainRequest,
    ) -> beian_20160810_models.GetMainDomainResponse:
        """
        @summary 获取主域名接口
        
        @param request: GetMainDomainRequest
        @return: GetMainDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_main_domain_with_options_async(request, runtime)

    def insert_unbeian_ip_check_type_with_options(
        self,
        request: beian_20160810_models.InsertUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.InsertUnbeianIpCheckTypeResponse:
        """
        @param request: InsertUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.InsertUnbeianIpCheckTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_unbeian_ip_check_type_with_options_async(
        self,
        request: beian_20160810_models.InsertUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.InsertUnbeianIpCheckTypeResponse:
        """
        @param request: InsertUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InsertUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.InsertUnbeianIpCheckTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_unbeian_ip_check_type(
        self,
        request: beian_20160810_models.InsertUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.InsertUnbeianIpCheckTypeResponse:
        """
        @param request: InsertUnbeianIpCheckTypeRequest
        @return: InsertUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.insert_unbeian_ip_check_type_with_options(request, runtime)

    async def insert_unbeian_ip_check_type_async(
        self,
        request: beian_20160810_models.InsertUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.InsertUnbeianIpCheckTypeResponse:
        """
        @param request: InsertUnbeianIpCheckTypeRequest
        @return: InsertUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.insert_unbeian_ip_check_type_with_options_async(request, runtime)

    def list_unbeian_ip_check_type_with_options(
        self,
        request: beian_20160810_models.ListUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ListUnbeianIpCheckTypeResponse:
        """
        @param request: ListUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ListUnbeianIpCheckTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_unbeian_ip_check_type_with_options_async(
        self,
        request: beian_20160810_models.ListUnbeianIpCheckTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ListUnbeianIpCheckTypeResponse:
        """
        @param request: ListUnbeianIpCheckTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUnbeianIpCheckTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.check_type):
            query['CheckType'] = request.check_type
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUnbeianIpCheckType',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ListUnbeianIpCheckTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_unbeian_ip_check_type(
        self,
        request: beian_20160810_models.ListUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.ListUnbeianIpCheckTypeResponse:
        """
        @param request: ListUnbeianIpCheckTypeRequest
        @return: ListUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_unbeian_ip_check_type_with_options(request, runtime)

    async def list_unbeian_ip_check_type_async(
        self,
        request: beian_20160810_models.ListUnbeianIpCheckTypeRequest,
    ) -> beian_20160810_models.ListUnbeianIpCheckTypeResponse:
        """
        @param request: ListUnbeianIpCheckTypeRequest
        @return: ListUnbeianIpCheckTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_unbeian_ip_check_type_with_options_async(request, runtime)

    def manage_accessor_domain_with_options(
        self,
        request: beian_20160810_models.ManageAccessorDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorDomainResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: ManageAccessorDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_accessor_domain_with_options_async(
        self,
        request: beian_20160810_models.ManageAccessorDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorDomainResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: ManageAccessorDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_accessor_domain(
        self,
        request: beian_20160810_models.ManageAccessorDomainRequest,
    ) -> beian_20160810_models.ManageAccessorDomainResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: ManageAccessorDomainRequest
        @return: ManageAccessorDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manage_accessor_domain_with_options(request, runtime)

    async def manage_accessor_domain_async(
        self,
        request: beian_20160810_models.ManageAccessorDomainRequest,
    ) -> beian_20160810_models.ManageAccessorDomainResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: ManageAccessorDomainRequest
        @return: ManageAccessorDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manage_accessor_domain_with_options_async(request, runtime)

    def manage_accessor_domain_white_list_with_options(
        self,
        request: beian_20160810_models.ManageAccessorDomainWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报接口
        
        @param request: ManageAccessorDomainWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorDomainWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorDomainWhiteList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorDomainWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_accessor_domain_white_list_with_options_async(
        self,
        request: beian_20160810_models.ManageAccessorDomainWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报接口
        
        @param request: ManageAccessorDomainWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorDomainWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorDomainWhiteList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorDomainWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_accessor_domain_white_list(
        self,
        request: beian_20160810_models.ManageAccessorDomainWhiteListRequest,
    ) -> beian_20160810_models.ManageAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报接口
        
        @param request: ManageAccessorDomainWhiteListRequest
        @return: ManageAccessorDomainWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manage_accessor_domain_white_list_with_options(request, runtime)

    async def manage_accessor_domain_white_list_async(
        self,
        request: beian_20160810_models.ManageAccessorDomainWhiteListRequest,
    ) -> beian_20160810_models.ManageAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报接口
        
        @param request: ManageAccessorDomainWhiteListRequest
        @return: ManageAccessorDomainWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manage_accessor_domain_white_list_with_options_async(request, runtime)

    def manage_accessor_ip_with_options(
        self,
        request: beian_20160810_models.ManageAccessorIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorIpResponse:
        """
        @summary 接入方管控IP上报接口
        
        @param request: ManageAccessorIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorIp',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_accessor_ip_with_options_async(
        self,
        request: beian_20160810_models.ManageAccessorIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.ManageAccessorIpResponse:
        """
        @summary 接入方管控IP上报接口
        
        @param request: ManageAccessorIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ManageAccessorIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageAccessorIp',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.ManageAccessorIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_accessor_ip(
        self,
        request: beian_20160810_models.ManageAccessorIpRequest,
    ) -> beian_20160810_models.ManageAccessorIpResponse:
        """
        @summary 接入方管控IP上报接口
        
        @param request: ManageAccessorIpRequest
        @return: ManageAccessorIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.manage_accessor_ip_with_options(request, runtime)

    async def manage_accessor_ip_async(
        self,
        request: beian_20160810_models.ManageAccessorIpRequest,
    ) -> beian_20160810_models.ManageAccessorIpResponse:
        """
        @summary 接入方管控IP上报接口
        
        @param request: ManageAccessorIpRequest
        @return: ManageAccessorIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.manage_accessor_ip_with_options_async(request, runtime)

    def query_accessor_domain_with_options(
        self,
        request: beian_20160810_models.QueryAccessorDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainResponse:
        """
        @summary 接入方服务域名是否上报查询接口
        
        @param request: QueryAccessorDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_domain_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainResponse:
        """
        @summary 接入方服务域名是否上报查询接口
        
        @param request: QueryAccessorDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomain',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_domain(
        self,
        request: beian_20160810_models.QueryAccessorDomainRequest,
    ) -> beian_20160810_models.QueryAccessorDomainResponse:
        """
        @summary 接入方服务域名是否上报查询接口
        
        @param request: QueryAccessorDomainRequest
        @return: QueryAccessorDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_domain_with_options(request, runtime)

    async def query_accessor_domain_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainRequest,
    ) -> beian_20160810_models.QueryAccessorDomainResponse:
        """
        @summary 接入方服务域名是否上报查询接口
        
        @param request: QueryAccessorDomainRequest
        @return: QueryAccessorDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_domain_with_options_async(request, runtime)

    def query_accessor_domain_list_with_options(
        self,
        request: beian_20160810_models.QueryAccessorDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainListResponse:
        """
        @summary 接入方查询服务域名列表接口
        
        @param request: QueryAccessorDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_domain_list_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainListResponse:
        """
        @summary 接入方查询服务域名列表接口
        
        @param request: QueryAccessorDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_domain_list(
        self,
        request: beian_20160810_models.QueryAccessorDomainListRequest,
    ) -> beian_20160810_models.QueryAccessorDomainListResponse:
        """
        @summary 接入方查询服务域名列表接口
        
        @param request: QueryAccessorDomainListRequest
        @return: QueryAccessorDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_domain_list_with_options(request, runtime)

    async def query_accessor_domain_list_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainListRequest,
    ) -> beian_20160810_models.QueryAccessorDomainListResponse:
        """
        @summary 接入方查询服务域名列表接口
        
        @param request: QueryAccessorDomainListRequest
        @return: QueryAccessorDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_domain_list_with_options_async(request, runtime)

    def query_accessor_domain_status_with_options(
        self,
        request: beian_20160810_models.QueryAccessorDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainStatusResponse:
        """
        @summary 接入方域名状态查询接口
        
        @param request: QueryAccessorDomainStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainStatus',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_domain_status_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainStatusResponse:
        """
        @summary 接入方域名状态查询接口
        
        @param request: QueryAccessorDomainStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainStatus',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_domain_status(
        self,
        request: beian_20160810_models.QueryAccessorDomainStatusRequest,
    ) -> beian_20160810_models.QueryAccessorDomainStatusResponse:
        """
        @summary 接入方域名状态查询接口
        
        @param request: QueryAccessorDomainStatusRequest
        @return: QueryAccessorDomainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_domain_status_with_options(request, runtime)

    async def query_accessor_domain_status_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainStatusRequest,
    ) -> beian_20160810_models.QueryAccessorDomainStatusResponse:
        """
        @summary 接入方域名状态查询接口
        
        @param request: QueryAccessorDomainStatusRequest
        @return: QueryAccessorDomainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_domain_status_with_options_async(request, runtime)

    def query_accessor_domain_white_list_with_options(
        self,
        request: beian_20160810_models.QueryAccessorDomainWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报查询接口
        
        @param request: QueryAccessorDomainWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainWhiteList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_domain_white_list_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报查询接口
        
        @param request: QueryAccessorDomainWhiteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainWhiteListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainWhiteList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_domain_white_list(
        self,
        request: beian_20160810_models.QueryAccessorDomainWhiteListRequest,
    ) -> beian_20160810_models.QueryAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报查询接口
        
        @param request: QueryAccessorDomainWhiteListRequest
        @return: QueryAccessorDomainWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_domain_white_list_with_options(request, runtime)

    async def query_accessor_domain_white_list_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainWhiteListRequest,
    ) -> beian_20160810_models.QueryAccessorDomainWhiteListResponse:
        """
        @summary 接入方域名白名单上报查询接口
        
        @param request: QueryAccessorDomainWhiteListRequest
        @return: QueryAccessorDomainWhiteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_domain_white_list_with_options_async(request, runtime)

    def query_accessor_domains_status_with_options(
        self,
        request: beian_20160810_models.QueryAccessorDomainsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainsStatusResponse:
        """
        @summary 接入方域名状态批量查询接口
        
        @param request: QueryAccessorDomainsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainsStatus',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_domains_status_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorDomainsStatusResponse:
        """
        @summary 接入方域名状态批量查询接口
        
        @param request: QueryAccessorDomainsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorDomainsStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorDomainsStatus',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorDomainsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_domains_status(
        self,
        request: beian_20160810_models.QueryAccessorDomainsStatusRequest,
    ) -> beian_20160810_models.QueryAccessorDomainsStatusResponse:
        """
        @summary 接入方域名状态批量查询接口
        
        @param request: QueryAccessorDomainsStatusRequest
        @return: QueryAccessorDomainsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_domains_status_with_options(request, runtime)

    async def query_accessor_domains_status_async(
        self,
        request: beian_20160810_models.QueryAccessorDomainsStatusRequest,
    ) -> beian_20160810_models.QueryAccessorDomainsStatusResponse:
        """
        @summary 接入方域名状态批量查询接口
        
        @param request: QueryAccessorDomainsStatusRequest
        @return: QueryAccessorDomainsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_domains_status_with_options_async(request, runtime)

    def query_accessor_ip_with_options(
        self,
        request: beian_20160810_models.QueryAccessorIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorIpResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: QueryAccessorIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorIp',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_accessor_ip_with_options_async(
        self,
        request: beian_20160810_models.QueryAccessorIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.QueryAccessorIpResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: QueryAccessorIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccessorIpResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccessorIp',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.QueryAccessorIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_accessor_ip(
        self,
        request: beian_20160810_models.QueryAccessorIpRequest,
    ) -> beian_20160810_models.QueryAccessorIpResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: QueryAccessorIpRequest
        @return: QueryAccessorIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_accessor_ip_with_options(request, runtime)

    async def query_accessor_ip_async(
        self,
        request: beian_20160810_models.QueryAccessorIpRequest,
    ) -> beian_20160810_models.QueryAccessorIpResponse:
        """
        @summary 接入方服务域名上报接口
        
        @param request: QueryAccessorIpRequest
        @return: QueryAccessorIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_accessor_ip_with_options_async(request, runtime)

    def submit_accessor_full_domains_oss_list_with_options(
        self,
        request: beian_20160810_models.SubmitAccessorFullDomainsOssListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.SubmitAccessorFullDomainsOssListResponse:
        """
        @summary 接入方服务域名全量上报接口
        
        @param request: SubmitAccessorFullDomainsOssListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAccessorFullDomainsOssListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.oss_list):
            query['OssList'] = request.oss_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAccessorFullDomainsOssList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.SubmitAccessorFullDomainsOssListResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_accessor_full_domains_oss_list_with_options_async(
        self,
        request: beian_20160810_models.SubmitAccessorFullDomainsOssListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> beian_20160810_models.SubmitAccessorFullDomainsOssListResponse:
        """
        @summary 接入方服务域名全量上报接口
        
        @param request: SubmitAccessorFullDomainsOssListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitAccessorFullDomainsOssListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller):
            query['Caller'] = request.caller
        if not UtilClient.is_unset(request.oss_list):
            query['OssList'] = request.oss_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAccessorFullDomainsOssList',
            version='2016-08-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            beian_20160810_models.SubmitAccessorFullDomainsOssListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_accessor_full_domains_oss_list(
        self,
        request: beian_20160810_models.SubmitAccessorFullDomainsOssListRequest,
    ) -> beian_20160810_models.SubmitAccessorFullDomainsOssListResponse:
        """
        @summary 接入方服务域名全量上报接口
        
        @param request: SubmitAccessorFullDomainsOssListRequest
        @return: SubmitAccessorFullDomainsOssListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_accessor_full_domains_oss_list_with_options(request, runtime)

    async def submit_accessor_full_domains_oss_list_async(
        self,
        request: beian_20160810_models.SubmitAccessorFullDomainsOssListRequest,
    ) -> beian_20160810_models.SubmitAccessorFullDomainsOssListResponse:
        """
        @summary 接入方服务域名全量上报接口
        
        @param request: SubmitAccessorFullDomainsOssListRequest
        @return: SubmitAccessorFullDomainsOssListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_accessor_full_domains_oss_list_with_options_async(request, runtime)
