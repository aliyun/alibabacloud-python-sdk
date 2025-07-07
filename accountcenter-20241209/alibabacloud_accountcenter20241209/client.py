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

    def enterprise_account_change_login_password_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse:
        """
        @summary 修改登录密码
        
        @param request: EnterpriseAccountChangeLoginPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeLoginPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeLoginPassword',
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
            account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_login_password_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeLoginPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse:
        """
        @summary 修改登录密码
        
        @param request: EnterpriseAccountChangeLoginPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeLoginPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_password):
            query['EncryptPassword'] = request.encrypt_password
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeLoginPassword',
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
            account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_login_password(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeLoginPasswordRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse:
        """
        @summary 修改登录密码
        
        @param request: EnterpriseAccountChangeLoginPasswordRequest
        @return: EnterpriseAccountChangeLoginPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_change_login_password_with_options(request, runtime)

    async def enterprise_account_change_login_password_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeLoginPasswordRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeLoginPasswordResponse:
        """
        @summary 修改登录密码
        
        @param request: EnterpriseAccountChangeLoginPasswordRequest
        @return: EnterpriseAccountChangeLoginPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_change_login_password_with_options_async(request, runtime)

    def enterprise_account_change_security_email_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse:
        """
        @summary 修改安全邮箱
        
        @param request: EnterpriseAccountChangeSecurityEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeSecurityEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.security_email):
            query['SecurityEmail'] = request.security_email
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeSecurityEmail',
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
            account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_security_email_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse:
        """
        @summary 修改安全邮箱
        
        @param request: EnterpriseAccountChangeSecurityEmailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeSecurityEmailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.security_email):
            query['SecurityEmail'] = request.security_email
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeSecurityEmail',
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
            account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_security_email(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityEmailRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse:
        """
        @summary 修改安全邮箱
        
        @param request: EnterpriseAccountChangeSecurityEmailRequest
        @return: EnterpriseAccountChangeSecurityEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_change_security_email_with_options(request, runtime)

    async def enterprise_account_change_security_email_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityEmailRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityEmailResponse:
        """
        @summary 修改安全邮箱
        
        @param request: EnterpriseAccountChangeSecurityEmailRequest
        @return: EnterpriseAccountChangeSecurityEmailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_change_security_email_with_options_async(request, runtime)

    def enterprise_account_change_security_mobile_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse:
        """
        @summary 修改成员账号安全手机号
        
        @param request: EnterpriseAccountChangeSecurityMobileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeSecurityMobileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.new_mobile):
            query['NewMobile'] = request.new_mobile
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeSecurityMobile',
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
            account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_change_security_mobile_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityMobileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse:
        """
        @summary 修改成员账号安全手机号
        
        @param request: EnterpriseAccountChangeSecurityMobileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountChangeSecurityMobileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.new_mobile):
            query['NewMobile'] = request.new_mobile
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountChangeSecurityMobile',
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
            account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_change_security_mobile(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityMobileRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse:
        """
        @summary 修改成员账号安全手机号
        
        @param request: EnterpriseAccountChangeSecurityMobileRequest
        @return: EnterpriseAccountChangeSecurityMobileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_change_security_mobile_with_options(request, runtime)

    async def enterprise_account_change_security_mobile_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountChangeSecurityMobileRequest,
    ) -> account_center_20241209_models.EnterpriseAccountChangeSecurityMobileResponse:
        """
        @summary 修改成员账号安全手机号
        
        @param request: EnterpriseAccountChangeSecurityMobileRequest
        @return: EnterpriseAccountChangeSecurityMobileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_change_security_mobile_with_options_async(request, runtime)

    def enterprise_account_query_account_granted_roles_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        """
        @summary 查询纳管账号授权角色
        
        @param request: EnterpriseAccountQueryAccountGrantedRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryAccountGrantedRolesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.pk):
            body['Pk'] = request.pk
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryAccountGrantedRoles',
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
            account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_account_granted_roles_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        """
        @summary 查询纳管账号授权角色
        
        @param request: EnterpriseAccountQueryAccountGrantedRolesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryAccountGrantedRolesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.pk):
            body['Pk'] = request.pk
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryAccountGrantedRoles',
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
            account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_account_granted_roles(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        """
        @summary 查询纳管账号授权角色
        
        @param request: EnterpriseAccountQueryAccountGrantedRolesRequest
        @return: EnterpriseAccountQueryAccountGrantedRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_query_account_granted_roles_with_options(request, runtime)

    async def enterprise_account_query_account_granted_roles_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountGrantedRolesResponse:
        """
        @summary 查询纳管账号授权角色
        
        @param request: EnterpriseAccountQueryAccountGrantedRolesRequest
        @return: EnterpriseAccountQueryAccountGrantedRolesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_query_account_granted_roles_with_options_async(request, runtime)

    def enterprise_account_query_accounts_info_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse:
        """
        @summary 批量查询纳管账号信息
        
        @param request: EnterpriseAccountQueryAccountsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryAccountsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pks_json):
            query['PksJson'] = request.pks_json
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryAccountsInfo',
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
            account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_accounts_info_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse:
        """
        @summary 批量查询纳管账号信息
        
        @param request: EnterpriseAccountQueryAccountsInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryAccountsInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pks_json):
            query['PksJson'] = request.pks_json
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryAccountsInfo',
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
            account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_accounts_info(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountsInfoRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse:
        """
        @summary 批量查询纳管账号信息
        
        @param request: EnterpriseAccountQueryAccountsInfoRequest
        @return: EnterpriseAccountQueryAccountsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_query_accounts_info_with_options(request, runtime)

    async def enterprise_account_query_accounts_info_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryAccountsInfoRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryAccountsInfoResponse:
        """
        @summary 批量查询纳管账号信息
        
        @param request: EnterpriseAccountQueryAccountsInfoRequest
        @return: EnterpriseAccountQueryAccountsInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_query_accounts_info_with_options_async(request, runtime)

    def enterprise_account_query_login_settings_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryLoginSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse:
        """
        @summary 查询纳管账号登录设置
        
        @param request: EnterpriseAccountQueryLoginSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryLoginSettingsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.pk):
            body['Pk'] = request.pk
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryLoginSettings',
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
            account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_query_login_settings_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryLoginSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse:
        """
        @summary 查询纳管账号登录设置
        
        @param request: EnterpriseAccountQueryLoginSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountQueryLoginSettingsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.is_open_api):
            body['IsOpenApi'] = request.is_open_api
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.pk):
            body['Pk'] = request.pk
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountQueryLoginSettings',
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
            account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_query_login_settings(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryLoginSettingsRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse:
        """
        @summary 查询纳管账号登录设置
        
        @param request: EnterpriseAccountQueryLoginSettingsRequest
        @return: EnterpriseAccountQueryLoginSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_query_login_settings_with_options(request, runtime)

    async def enterprise_account_query_login_settings_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountQueryLoginSettingsRequest,
    ) -> account_center_20241209_models.EnterpriseAccountQueryLoginSettingsResponse:
        """
        @summary 查询纳管账号登录设置
        
        @param request: EnterpriseAccountQueryLoginSettingsRequest
        @return: EnterpriseAccountQueryLoginSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_query_login_settings_with_options_async(request, runtime)

    def enterprise_account_remove_mfa_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountRemoveMfaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountRemoveMfaResponse:
        """
        @summary 移除mfa
        
        @param request: EnterpriseAccountRemoveMfaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountRemoveMfaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountRemoveMfa',
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
            account_center_20241209_models.EnterpriseAccountRemoveMfaResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_remove_mfa_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountRemoveMfaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountRemoveMfaResponse:
        """
        @summary 移除mfa
        
        @param request: EnterpriseAccountRemoveMfaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountRemoveMfaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountRemoveMfa',
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
            account_center_20241209_models.EnterpriseAccountRemoveMfaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_remove_mfa(
        self,
        request: account_center_20241209_models.EnterpriseAccountRemoveMfaRequest,
    ) -> account_center_20241209_models.EnterpriseAccountRemoveMfaResponse:
        """
        @summary 移除mfa
        
        @param request: EnterpriseAccountRemoveMfaRequest
        @return: EnterpriseAccountRemoveMfaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_remove_mfa_with_options(request, runtime)

    async def enterprise_account_remove_mfa_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountRemoveMfaRequest,
    ) -> account_center_20241209_models.EnterpriseAccountRemoveMfaResponse:
        """
        @summary 移除mfa
        
        @param request: EnterpriseAccountRemoveMfaRequest
        @return: EnterpriseAccountRemoveMfaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_remove_mfa_with_options_async(request, runtime)

    def enterprise_account_separate_ea_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountSeparateEaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountSeparateEaResponse:
        """
        @summary 脱离ea
        
        @param request: EnterpriseAccountSeparateEaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountSeparateEaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
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
            action='EnterpriseAccountSeparateEa',
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
            account_center_20241209_models.EnterpriseAccountSeparateEaResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_separate_ea_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountSeparateEaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountSeparateEaResponse:
        """
        @summary 脱离ea
        
        @param request: EnterpriseAccountSeparateEaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountSeparateEaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
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
            action='EnterpriseAccountSeparateEa',
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
            account_center_20241209_models.EnterpriseAccountSeparateEaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_separate_ea(
        self,
        request: account_center_20241209_models.EnterpriseAccountSeparateEaRequest,
    ) -> account_center_20241209_models.EnterpriseAccountSeparateEaResponse:
        """
        @summary 脱离ea
        
        @param request: EnterpriseAccountSeparateEaRequest
        @return: EnterpriseAccountSeparateEaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_separate_ea_with_options(request, runtime)

    async def enterprise_account_separate_ea_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountSeparateEaRequest,
    ) -> account_center_20241209_models.EnterpriseAccountSeparateEaResponse:
        """
        @summary 脱离ea
        
        @param request: EnterpriseAccountSeparateEaRequest
        @return: EnterpriseAccountSeparateEaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_separate_ea_with_options_async(request, runtime)

    def enterprise_account_update_account_alias_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse:
        """
        @summary 更新账号企业多账号中的别名
        
        @param request: EnterpriseAccountUpdateAccountAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateAccountAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateAccountAlias',
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
            account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_account_alias_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountAliasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse:
        """
        @summary 更新账号企业多账号中的别名
        
        @param request: EnterpriseAccountUpdateAccountAliasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateAccountAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateAccountAlias',
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
            account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_account_alias(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountAliasRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse:
        """
        @summary 更新账号企业多账号中的别名
        
        @param request: EnterpriseAccountUpdateAccountAliasRequest
        @return: EnterpriseAccountUpdateAccountAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_account_alias_with_options(request, runtime)

    async def enterprise_account_update_account_alias_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountAliasRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountAliasResponse:
        """
        @summary 更新账号企业多账号中的别名
        
        @param request: EnterpriseAccountUpdateAccountAliasRequest
        @return: EnterpriseAccountUpdateAccountAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_account_alias_with_options_async(request, runtime)

    def enterprise_account_update_account_biz_role_grant_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        """
        @summary 更新账号授权
        
        @param request: EnterpriseAccountUpdateAccountBizRoleGrantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateAccountBizRoleGrantResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code_list_json):
            query['BizRoleCodeListJson'] = request.biz_role_code_list_json
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
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
            action='EnterpriseAccountUpdateAccountBizRoleGrant',
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
            account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_account_biz_role_grant_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        """
        @summary 更新账号授权
        
        @param request: EnterpriseAccountUpdateAccountBizRoleGrantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateAccountBizRoleGrantResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code_list_json):
            query['BizRoleCodeListJson'] = request.biz_role_code_list_json
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
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
            action='EnterpriseAccountUpdateAccountBizRoleGrant',
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
            account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_account_biz_role_grant(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        """
        @summary 更新账号授权
        
        @param request: EnterpriseAccountUpdateAccountBizRoleGrantRequest
        @return: EnterpriseAccountUpdateAccountBizRoleGrantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_account_biz_role_grant_with_options(request, runtime)

    async def enterprise_account_update_account_biz_role_grant_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateAccountBizRoleGrantResponse:
        """
        @summary 更新账号授权
        
        @param request: EnterpriseAccountUpdateAccountBizRoleGrantRequest
        @return: EnterpriseAccountUpdateAccountBizRoleGrantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_account_biz_role_grant_with_options_async(request, runtime)

    def enterprise_account_update_ip_mask_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateIpMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse:
        """
        @summary 设置Ip掩码
        
        @param request: EnterpriseAccountUpdateIpMaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateIpMaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_masks_json):
            query['IpMasksJson'] = request.ip_masks_json
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateIpMask',
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
            account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_ip_mask_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateIpMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse:
        """
        @summary 设置Ip掩码
        
        @param request: EnterpriseAccountUpdateIpMaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateIpMaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ip_masks_json):
            query['IpMasksJson'] = request.ip_masks_json
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateIpMask',
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
            account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_ip_mask(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateIpMaskRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse:
        """
        @summary 设置Ip掩码
        
        @param request: EnterpriseAccountUpdateIpMaskRequest
        @return: EnterpriseAccountUpdateIpMaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_ip_mask_with_options(request, runtime)

    async def enterprise_account_update_ip_mask_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateIpMaskRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateIpMaskResponse:
        """
        @summary 设置Ip掩码
        
        @param request: EnterpriseAccountUpdateIpMaskRequest
        @return: EnterpriseAccountUpdateIpMaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_ip_mask_with_options_async(request, runtime)

    def enterprise_account_update_operate_risk_control_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        """
        @summary 更新操作风控
        
        @param request: EnterpriseAccountUpdateOperateRiskControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateOperateRiskControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.product_level):
            query['ProductLevel'] = request.product_level
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateOperateRiskControl',
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
            account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_operate_risk_control_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        """
        @summary 更新操作风控
        
        @param request: EnterpriseAccountUpdateOperateRiskControlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateOperateRiskControlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.product_level):
            query['ProductLevel'] = request.product_level
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateOperateRiskControl',
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
            account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_operate_risk_control(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        """
        @summary 更新操作风控
        
        @param request: EnterpriseAccountUpdateOperateRiskControlRequest
        @return: EnterpriseAccountUpdateOperateRiskControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_operate_risk_control_with_options(request, runtime)

    async def enterprise_account_update_operate_risk_control_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateOperateRiskControlResponse:
        """
        @summary 更新操作风控
        
        @param request: EnterpriseAccountUpdateOperateRiskControlRequest
        @return: EnterpriseAccountUpdateOperateRiskControlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_operate_risk_control_with_options_async(request, runtime)

    def enterprise_account_update_security_mobile_login_status_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        """
        @summary 修改安全手机启用状态
        
        @param request: EnterpriseAccountUpdateSecurityMobileLoginStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateSecurityMobileLoginStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateSecurityMobileLoginStatus',
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
            account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_security_mobile_login_status_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        """
        @summary 修改安全手机启用状态
        
        @param request: EnterpriseAccountUpdateSecurityMobileLoginStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateSecurityMobileLoginStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateSecurityMobileLoginStatus',
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
            account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_security_mobile_login_status(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        """
        @summary 修改安全手机启用状态
        
        @param request: EnterpriseAccountUpdateSecurityMobileLoginStatusRequest
        @return: EnterpriseAccountUpdateSecurityMobileLoginStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_security_mobile_login_status_with_options(request, runtime)

    async def enterprise_account_update_security_mobile_login_status_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSecurityMobileLoginStatusResponse:
        """
        @summary 修改安全手机启用状态
        
        @param request: EnterpriseAccountUpdateSecurityMobileLoginStatusRequest
        @return: EnterpriseAccountUpdateSecurityMobileLoginStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_security_mobile_login_status_with_options_async(request, runtime)

    def enterprise_account_update_session_expire_time_with_options(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        """
        @summary 更新过期时间
        
        @param request: EnterpriseAccountUpdateSessionExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateSessionExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.session_expire_time):
            query['SessionExpireTime'] = request.session_expire_time
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateSessionExpireTime',
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
            account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_account_update_session_expire_time_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        """
        @summary 更新过期时间
        
        @param request: EnterpriseAccountUpdateSessionExpireTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseAccountUpdateSessionExpireTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.pk):
            query['Pk'] = request.pk
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.session_expire_time):
            query['SessionExpireTime'] = request.session_expire_time
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseAccountUpdateSessionExpireTime',
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
            account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_account_update_session_expire_time(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        """
        @summary 更新过期时间
        
        @param request: EnterpriseAccountUpdateSessionExpireTimeRequest
        @return: EnterpriseAccountUpdateSessionExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_account_update_session_expire_time_with_options(request, runtime)

    async def enterprise_account_update_session_expire_time_async(
        self,
        request: account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeRequest,
    ) -> account_center_20241209_models.EnterpriseAccountUpdateSessionExpireTimeResponse:
        """
        @summary 更新过期时间
        
        @param request: EnterpriseAccountUpdateSessionExpireTimeRequest
        @return: EnterpriseAccountUpdateSessionExpireTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_account_update_session_expire_time_with_options_async(request, runtime)

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

    def enterprise_role_create_biz_role_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleCreateBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse:
        """
        @summary 创建业务角色
        
        @param request: EnterpriseRoleCreateBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleCreateBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not UtilClient.is_unset(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not UtilClient.is_unset(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
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
            action='EnterpriseRoleCreateBizRole',
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
            account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_create_biz_role_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleCreateBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse:
        """
        @summary 创建业务角色
        
        @param request: EnterpriseRoleCreateBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleCreateBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not UtilClient.is_unset(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not UtilClient.is_unset(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
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
            action='EnterpriseRoleCreateBizRole',
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
            account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_create_biz_role(
        self,
        request: account_center_20241209_models.EnterpriseRoleCreateBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse:
        """
        @summary 创建业务角色
        
        @param request: EnterpriseRoleCreateBizRoleRequest
        @return: EnterpriseRoleCreateBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_create_biz_role_with_options(request, runtime)

    async def enterprise_role_create_biz_role_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleCreateBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleCreateBizRoleResponse:
        """
        @summary 创建业务角色
        
        @param request: EnterpriseRoleCreateBizRoleRequest
        @return: EnterpriseRoleCreateBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_create_biz_role_with_options_async(request, runtime)

    def enterprise_role_delete_biz_role_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleDeleteBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse:
        """
        @summary 删除业务角色
        
        @param request: EnterpriseRoleDeleteBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleDeleteBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleDeleteBizRole',
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
            account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_delete_biz_role_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleDeleteBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse:
        """
        @summary 删除业务角色
        
        @param request: EnterpriseRoleDeleteBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleDeleteBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleDeleteBizRole',
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
            account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_delete_biz_role(
        self,
        request: account_center_20241209_models.EnterpriseRoleDeleteBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse:
        """
        @summary 删除业务角色
        
        @param request: EnterpriseRoleDeleteBizRoleRequest
        @return: EnterpriseRoleDeleteBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_delete_biz_role_with_options(request, runtime)

    async def enterprise_role_delete_biz_role_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleDeleteBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleDeleteBizRoleResponse:
        """
        @summary 删除业务角色
        
        @param request: EnterpriseRoleDeleteBizRoleRequest
        @return: EnterpriseRoleDeleteBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_delete_biz_role_with_options_async(request, runtime)

    def enterprise_role_query_account_for_role_grant_by_page_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        """
        @summary 角色授权场景下分页查询账号
        
        @param request: EnterpriseRoleQueryAccountForRoleGrantByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryAccountForRoleGrantByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
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
            action='EnterpriseRoleQueryAccountForRoleGrantByPage',
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
            account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_account_for_role_grant_by_page_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        """
        @summary 角色授权场景下分页查询账号
        
        @param request: EnterpriseRoleQueryAccountForRoleGrantByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryAccountForRoleGrantByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.show_complete_info):
            query['ShowCompleteInfo'] = request.show_complete_info
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
            action='EnterpriseRoleQueryAccountForRoleGrantByPage',
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
            account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_account_for_role_grant_by_page(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        """
        @summary 角色授权场景下分页查询账号
        
        @param request: EnterpriseRoleQueryAccountForRoleGrantByPageRequest
        @return: EnterpriseRoleQueryAccountForRoleGrantByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_query_account_for_role_grant_by_page_with_options(request, runtime)

    async def enterprise_role_query_account_for_role_grant_by_page_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryAccountForRoleGrantByPageResponse:
        """
        @summary 角色授权场景下分页查询账号
        
        @param request: EnterpriseRoleQueryAccountForRoleGrantByPageRequest
        @return: EnterpriseRoleQueryAccountForRoleGrantByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_query_account_for_role_grant_by_page_with_options_async(request, runtime)

    def enterprise_role_query_biz_role_by_page_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse:
        """
        @summary 分页查询业务角色
        
        @param request: EnterpriseRoleQueryBizRoleByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryBizRoleByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseRoleQueryBizRoleByPage',
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
            account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_biz_role_by_page_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse:
        """
        @summary 分页查询业务角色
        
        @param request: EnterpriseRoleQueryBizRoleByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryBizRoleByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.oriented_le_id):
            query['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        body = {}
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseRoleQueryBizRoleByPage',
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
            account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_biz_role_by_page(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse:
        """
        @summary 分页查询业务角色
        
        @param request: EnterpriseRoleQueryBizRoleByPageRequest
        @return: EnterpriseRoleQueryBizRoleByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_query_biz_role_by_page_with_options(request, runtime)

    async def enterprise_role_query_biz_role_by_page_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleByPageResponse:
        """
        @summary 分页查询业务角色
        
        @param request: EnterpriseRoleQueryBizRoleByPageRequest
        @return: EnterpriseRoleQueryBizRoleByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_query_biz_role_by_page_with_options_async(request, runtime)

    def enterprise_role_query_biz_role_detail_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse:
        """
        @summary 查询业务角色详情
        
        @param request: EnterpriseRoleQueryBizRoleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryBizRoleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleQueryBizRoleDetail',
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
            account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_query_biz_role_detail_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse:
        """
        @summary 查询业务角色详情
        
        @param request: EnterpriseRoleQueryBizRoleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleQueryBizRoleDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleQueryBizRoleDetail',
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
            account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_query_biz_role_detail(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse:
        """
        @summary 查询业务角色详情
        
        @param request: EnterpriseRoleQueryBizRoleDetailRequest
        @return: EnterpriseRoleQueryBizRoleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_query_biz_role_detail_with_options(request, runtime)

    async def enterprise_role_query_biz_role_detail_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailRequest,
    ) -> account_center_20241209_models.EnterpriseRoleQueryBizRoleDetailResponse:
        """
        @summary 查询业务角色详情
        
        @param request: EnterpriseRoleQueryBizRoleDetailRequest
        @return: EnterpriseRoleQueryBizRoleDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_query_biz_role_detail_with_options_async(request, runtime)

    def enterprise_role_update_biz_role_with_options(
        self,
        request: account_center_20241209_models.EnterpriseRoleUpdateBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse:
        """
        @summary 更新业务角色
        
        @param request: EnterpriseRoleUpdateBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleUpdateBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not UtilClient.is_unset(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleUpdateBizRole',
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
            account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_role_update_biz_role_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleUpdateBizRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse:
        """
        @summary 更新业务角色
        
        @param request: EnterpriseRoleUpdateBizRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseRoleUpdateBizRoleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_permission_code_list_json):
            query['BizPermissionCodeListJson'] = request.biz_permission_code_list_json
        if not UtilClient.is_unset(request.biz_role_code):
            query['BizRoleCode'] = request.biz_role_code
        if not UtilClient.is_unset(request.biz_role_desc):
            query['BizRoleDesc'] = request.biz_role_desc
        if not UtilClient.is_unset(request.biz_role_name):
            query['BizRoleName'] = request.biz_role_name
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
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
            action='EnterpriseRoleUpdateBizRole',
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
            account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_role_update_biz_role(
        self,
        request: account_center_20241209_models.EnterpriseRoleUpdateBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse:
        """
        @summary 更新业务角色
        
        @param request: EnterpriseRoleUpdateBizRoleRequest
        @return: EnterpriseRoleUpdateBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_role_update_biz_role_with_options(request, runtime)

    async def enterprise_role_update_biz_role_async(
        self,
        request: account_center_20241209_models.EnterpriseRoleUpdateBizRoleRequest,
    ) -> account_center_20241209_models.EnterpriseRoleUpdateBizRoleResponse:
        """
        @summary 更新业务角色
        
        @param request: EnterpriseRoleUpdateBizRoleRequest
        @return: EnterpriseRoleUpdateBizRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_role_update_biz_role_with_options_async(request, runtime)

    def enterprise_todo_deal_account_todo_with_options(
        self,
        request: account_center_20241209_models.EnterpriseTodoDealAccountTodoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse:
        """
        @summary 处理待办项
        
        @param request: EnterpriseTodoDealAccountTodoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoDealAccountTodoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_id):
            body['TodoId'] = request.todo_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoDealAccountTodo',
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
            account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_deal_account_todo_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoDealAccountTodoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse:
        """
        @summary 处理待办项
        
        @param request: EnterpriseTodoDealAccountTodoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoDealAccountTodoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_id):
            body['TodoId'] = request.todo_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoDealAccountTodo',
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
            account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_deal_account_todo(
        self,
        request: account_center_20241209_models.EnterpriseTodoDealAccountTodoRequest,
    ) -> account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse:
        """
        @summary 处理待办项
        
        @param request: EnterpriseTodoDealAccountTodoRequest
        @return: EnterpriseTodoDealAccountTodoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_todo_deal_account_todo_with_options(request, runtime)

    async def enterprise_todo_deal_account_todo_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoDealAccountTodoRequest,
    ) -> account_center_20241209_models.EnterpriseTodoDealAccountTodoResponse:
        """
        @summary 处理待办项
        
        @param request: EnterpriseTodoDealAccountTodoRequest
        @return: EnterpriseTodoDealAccountTodoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_todo_deal_account_todo_with_options_async(request, runtime)

    def enterprise_todo_query_account_todo_list_with_options(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse:
        """
        @summary 查询当前登录用户处理的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoQueryAccountTodoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoQueryAccountTodoList',
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
            account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_query_account_todo_list_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse:
        """
        @summary 查询当前登录用户处理的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoQueryAccountTodoListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoQueryAccountTodoList',
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
            account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_query_account_todo_list(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListRequest,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse:
        """
        @summary 查询当前登录用户处理的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListRequest
        @return: EnterpriseTodoQueryAccountTodoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_todo_query_account_todo_list_with_options(request, runtime)

    async def enterprise_todo_query_account_todo_list_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListRequest,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListResponse:
        """
        @summary 查询当前登录用户处理的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListRequest
        @return: EnterpriseTodoQueryAccountTodoListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_todo_query_account_todo_list_with_options_async(request, runtime)

    def enterprise_todo_query_account_todo_list_by_applicant_with_options(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        """
        @summary 查询当前登录用户发起的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListByApplicantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoQueryAccountTodoListByApplicantResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoQueryAccountTodoListByApplicant',
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
            account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_todo_query_account_todo_list_by_applicant_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        """
        @summary 查询当前登录用户发起的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListByApplicantRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseTodoQueryAccountTodoListByApplicantResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.operate_pk):
            body['OperatePk'] = request.operate_pk
        if not UtilClient.is_unset(request.oriented_ec_id):
            body['OrientedEcId'] = request.oriented_ec_id
        if not UtilClient.is_unset(request.oriented_le_id):
            body['OrientedLeId'] = request.oriented_le_id
        if not UtilClient.is_unset(request.oriented_nb_id):
            body['OrientedNbId'] = request.oriented_nb_id
        if not UtilClient.is_unset(request.page):
            body['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_complete_info):
            body['ShowCompleteInfo'] = request.show_complete_info
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.todo_type):
            body['TodoType'] = request.todo_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnterpriseTodoQueryAccountTodoListByApplicant',
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
            account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_todo_query_account_todo_list_by_applicant(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        """
        @summary 查询当前登录用户发起的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListByApplicantRequest
        @return: EnterpriseTodoQueryAccountTodoListByApplicantResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_todo_query_account_todo_list_by_applicant_with_options(request, runtime)

    async def enterprise_todo_query_account_todo_list_by_applicant_async(
        self,
        request: account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantRequest,
    ) -> account_center_20241209_models.EnterpriseTodoQueryAccountTodoListByApplicantResponse:
        """
        @summary 查询当前登录用户发起的待办项列表
        
        @param request: EnterpriseTodoQueryAccountTodoListByApplicantRequest
        @return: EnterpriseTodoQueryAccountTodoListByApplicantResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_todo_query_account_todo_list_by_applicant_with_options_async(request, runtime)

    def enterprise_uninvited_admin_invite_join_enterprise_with_options(
        self,
        request: account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        """
        @summary 管理员邀请纳管
        
        @param request: EnterpriseUninvitedAdminInviteJoinEnterpriseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseUninvitedAdminInviteJoinEnterpriseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id):
            query['EcId'] = request.ec_id
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.invitee_pk):
            query['InviteePk'] = request.invitee_pk
        if not UtilClient.is_unset(request.le_id):
            query['LeId'] = request.le_id
        if not UtilClient.is_unset(request.nb_id):
            query['NbId'] = request.nb_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnterpriseUninvitedAdminInviteJoinEnterprise',
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
            account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def enterprise_uninvited_admin_invite_join_enterprise_with_options_async(
        self,
        request: account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        """
        @summary 管理员邀请纳管
        
        @param request: EnterpriseUninvitedAdminInviteJoinEnterpriseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterpriseUninvitedAdminInviteJoinEnterpriseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id):
            query['EcId'] = request.ec_id
        if not UtilClient.is_unset(request.encrypt_ticket):
            query['EncryptTicket'] = request.encrypt_ticket
        if not UtilClient.is_unset(request.invitee_pk):
            query['InviteePk'] = request.invitee_pk
        if not UtilClient.is_unset(request.le_id):
            query['LeId'] = request.le_id
        if not UtilClient.is_unset(request.nb_id):
            query['NbId'] = request.nb_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnterpriseUninvitedAdminInviteJoinEnterprise',
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
            account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enterprise_uninvited_admin_invite_join_enterprise(
        self,
        request: account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
    ) -> account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        """
        @summary 管理员邀请纳管
        
        @param request: EnterpriseUninvitedAdminInviteJoinEnterpriseRequest
        @return: EnterpriseUninvitedAdminInviteJoinEnterpriseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enterprise_uninvited_admin_invite_join_enterprise_with_options(request, runtime)

    async def enterprise_uninvited_admin_invite_join_enterprise_async(
        self,
        request: account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseRequest,
    ) -> account_center_20241209_models.EnterpriseUninvitedAdminInviteJoinEnterpriseResponse:
        """
        @summary 管理员邀请纳管
        
        @param request: EnterpriseUninvitedAdminInviteJoinEnterpriseRequest
        @return: EnterpriseUninvitedAdminInviteJoinEnterpriseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enterprise_uninvited_admin_invite_join_enterprise_with_options_async(request, runtime)
