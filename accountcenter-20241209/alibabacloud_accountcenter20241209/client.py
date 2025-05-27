# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_accountcenter20241209 import models as account_center_20241209_models
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
        self._endpoint = self.get_endpoint('accountcenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def enterprise_org_query_load_tree_with_options(
        self,
        request: account_center_20241209_models.EnterpriseOrgQueryLoadTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse:
        """
        @summary 组织目录树查询
        
        @param request: EnterpriseOrgQueryLoadTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseOrgQueryLoadTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.load_org_only):
            query['LoadOrgOnly'] = request.load_org_only
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseOrgQueryLoadTree',
            version='2024-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_org_query_load_tree_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseOrgQueryLoadTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse:
        """
        @summary 组织目录树查询
        
        @param request: EnterpriseOrgQueryLoadTreeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseOrgQueryLoadTreeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.load_org_only):
            query['LoadOrgOnly'] = request.load_org_only
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseOrgQueryLoadTree',
            version='2024-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_org_query_load_tree(
        self,
        request: account_center_20241209_models.EnterpriseOrgQueryLoadTreeRequest,
    ) -> account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse:
        """
        @summary 组织目录树查询
        
        @param request: EnterpriseOrgQueryLoadTreeRequest
        @return: EnterpriseOrgQueryLoadTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_org_query_load_tree_with_options(request, runtime)

    async def enterprise_org_query_load_tree_async(
        self,
        request: account_center_20241209_models.EnterpriseOrgQueryLoadTreeRequest,
    ) -> account_center_20241209_models.EnterpriseOrgQueryLoadTreeResponse:
        """
        @summary 组织目录树查询
        
        @param request: EnterpriseOrgQueryLoadTreeRequest
        @return: EnterpriseOrgQueryLoadTreeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_org_query_load_tree_with_options_async(request, runtime)

    def enterprise_register_account_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRegisterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRegisterAccountResponse:
        """
        @summary 创建成员账号
        
        @param request: EnterpriseRegisterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRegisterAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.site_nick):
            query['SiteNick'] = request.site_nick
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseRegisterAccount',
            version='2024-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            account_center_20241209_models.EnterpriseRegisterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_register_account_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRegisterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRegisterAccountResponse:
        """
        @summary 创建成员账号
        
        @param request: EnterpriseRegisterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRegisterAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.organization_id):
            query['OrganizationId'] = request.organization_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.site_nick):
            query['SiteNick'] = request.site_nick
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseRegisterAccount',
            version='2024-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            account_center_20241209_models.EnterpriseRegisterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_register_account(
        self,
        request: account_center_20241209_models.EnterpriseRegisterAccountRequest,
    ) -> account_center_20241209_models.EnterpriseRegisterAccountResponse:
        """
        @summary 创建成员账号
        
        @param request: EnterpriseRegisterAccountRequest
        @return: EnterpriseRegisterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_register_account_with_options(request, runtime)

    async def enterprise_register_account_async(
        self,
        request: account_center_20241209_models.EnterpriseRegisterAccountRequest,
    ) -> account_center_20241209_models.EnterpriseRegisterAccountResponse:
        """
        @summary 创建成员账号
        
        @param request: EnterpriseRegisterAccountRequest
        @return: EnterpriseRegisterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_register_account_with_options_async(request, runtime)
