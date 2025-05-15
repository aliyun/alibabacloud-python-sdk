# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_governance20210120 import models as governance_20210120_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('governance', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_enroll_accounts_with_options(
        self,
        request: governance_20210120_models.BatchEnrollAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.BatchEnrollAccountsResponse:
        """
        @summary Applies an account baseline to multiple existing resource accounts at a time.
        
        @description You can call this operation to apply an account baseline to existing resource accounts.
        Accounts are enrolled in the account factory in asynchronous mode. After a resource account is created, an account baseline is applied to the account. You can call the [GetEnrolledAccount](https://help.aliyun.com/document_detail/609062.html) operation to query the details of the account enrolled in the account factory and check whether the account baseline is applied to the account.
        
        @param request: BatchEnrollAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchEnrollAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accounts):
            query['Accounts'] = request.accounts
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchEnrollAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.BatchEnrollAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_enroll_accounts_with_options_async(
        self,
        request: governance_20210120_models.BatchEnrollAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.BatchEnrollAccountsResponse:
        """
        @summary Applies an account baseline to multiple existing resource accounts at a time.
        
        @description You can call this operation to apply an account baseline to existing resource accounts.
        Accounts are enrolled in the account factory in asynchronous mode. After a resource account is created, an account baseline is applied to the account. You can call the [GetEnrolledAccount](https://help.aliyun.com/document_detail/609062.html) operation to query the details of the account enrolled in the account factory and check whether the account baseline is applied to the account.
        
        @param request: BatchEnrollAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchEnrollAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accounts):
            query['Accounts'] = request.accounts
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchEnrollAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.BatchEnrollAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_enroll_accounts(
        self,
        request: governance_20210120_models.BatchEnrollAccountsRequest,
    ) -> governance_20210120_models.BatchEnrollAccountsResponse:
        """
        @summary Applies an account baseline to multiple existing resource accounts at a time.
        
        @description You can call this operation to apply an account baseline to existing resource accounts.
        Accounts are enrolled in the account factory in asynchronous mode. After a resource account is created, an account baseline is applied to the account. You can call the [GetEnrolledAccount](https://help.aliyun.com/document_detail/609062.html) operation to query the details of the account enrolled in the account factory and check whether the account baseline is applied to the account.
        
        @param request: BatchEnrollAccountsRequest
        @return: BatchEnrollAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_enroll_accounts_with_options(request, runtime)

    async def batch_enroll_accounts_async(
        self,
        request: governance_20210120_models.BatchEnrollAccountsRequest,
    ) -> governance_20210120_models.BatchEnrollAccountsResponse:
        """
        @summary Applies an account baseline to multiple existing resource accounts at a time.
        
        @description You can call this operation to apply an account baseline to existing resource accounts.
        Accounts are enrolled in the account factory in asynchronous mode. After a resource account is created, an account baseline is applied to the account. You can call the [GetEnrolledAccount](https://help.aliyun.com/document_detail/609062.html) operation to query the details of the account enrolled in the account factory and check whether the account baseline is applied to the account.
        
        @param request: BatchEnrollAccountsRequest
        @return: BatchEnrollAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_enroll_accounts_with_options_async(request, runtime)

    def create_account_factory_baseline_with_options(
        self,
        request: governance_20210120_models.CreateAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.CreateAccountFactoryBaselineResponse:
        """
        @summary Creates a baseline of the account factory.
        
        @param request: CreateAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.CreateAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_factory_baseline_with_options_async(
        self,
        request: governance_20210120_models.CreateAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.CreateAccountFactoryBaselineResponse:
        """
        @summary Creates a baseline of the account factory.
        
        @param request: CreateAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.CreateAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_factory_baseline(
        self,
        request: governance_20210120_models.CreateAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.CreateAccountFactoryBaselineResponse:
        """
        @summary Creates a baseline of the account factory.
        
        @param request: CreateAccountFactoryBaselineRequest
        @return: CreateAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_factory_baseline_with_options(request, runtime)

    async def create_account_factory_baseline_async(
        self,
        request: governance_20210120_models.CreateAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.CreateAccountFactoryBaselineResponse:
        """
        @summary Creates a baseline of the account factory.
        
        @param request: CreateAccountFactoryBaselineRequest
        @return: CreateAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_factory_baseline_with_options_async(request, runtime)

    def delete_account_factory_baseline_with_options(
        self,
        request: governance_20210120_models.DeleteAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.DeleteAccountFactoryBaselineResponse:
        """
        @summary Deletes an account factory baseline.
        
        @param request: DeleteAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.DeleteAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_factory_baseline_with_options_async(
        self,
        request: governance_20210120_models.DeleteAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.DeleteAccountFactoryBaselineResponse:
        """
        @summary Deletes an account factory baseline.
        
        @param request: DeleteAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.DeleteAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account_factory_baseline(
        self,
        request: governance_20210120_models.DeleteAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.DeleteAccountFactoryBaselineResponse:
        """
        @summary Deletes an account factory baseline.
        
        @param request: DeleteAccountFactoryBaselineRequest
        @return: DeleteAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_factory_baseline_with_options(request, runtime)

    async def delete_account_factory_baseline_async(
        self,
        request: governance_20210120_models.DeleteAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.DeleteAccountFactoryBaselineResponse:
        """
        @summary Deletes an account factory baseline.
        
        @param request: DeleteAccountFactoryBaselineRequest
        @return: DeleteAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_factory_baseline_with_options_async(request, runtime)

    def enroll_account_with_options(
        self,
        tmp_req: governance_20210120_models.EnrollAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.EnrollAccountResponse:
        """
        @summary Enrolls an account. You can create a new account or manage an existing account in the account factory.
        
        @description You can call this API operation to create a new account or manage an existing account and apply the account baseline to the account.
        Accounts are created in asynchronous mode. After you create an account, you can apply the account baseline to the account. You can call the [GetEnrolledAccount API](~~GetEnrolledAccount~~) operation to view the details about the account to obtain the result of applying the account baseline to the account.
        
        @param tmp_req: EnrollAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnrollAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = governance_20210120_models.EnrollAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnrollAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.EnrollAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enroll_account_with_options_async(
        self,
        tmp_req: governance_20210120_models.EnrollAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.EnrollAccountResponse:
        """
        @summary Enrolls an account. You can create a new account or manage an existing account in the account factory.
        
        @description You can call this API operation to create a new account or manage an existing account and apply the account baseline to the account.
        Accounts are created in asynchronous mode. After you create an account, you can apply the account baseline to the account. You can call the [GetEnrolledAccount API](~~GetEnrolledAccount~~) operation to view the details about the account to obtain the result of applying the account baseline to the account.
        
        @param tmp_req: EnrollAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnrollAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = governance_20210120_models.EnrollAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnrollAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.EnrollAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enroll_account(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
    ) -> governance_20210120_models.EnrollAccountResponse:
        """
        @summary Enrolls an account. You can create a new account or manage an existing account in the account factory.
        
        @description You can call this API operation to create a new account or manage an existing account and apply the account baseline to the account.
        Accounts are created in asynchronous mode. After you create an account, you can apply the account baseline to the account. You can call the [GetEnrolledAccount API](~~GetEnrolledAccount~~) operation to view the details about the account to obtain the result of applying the account baseline to the account.
        
        @param request: EnrollAccountRequest
        @return: EnrollAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enroll_account_with_options(request, runtime)

    async def enroll_account_async(
        self,
        request: governance_20210120_models.EnrollAccountRequest,
    ) -> governance_20210120_models.EnrollAccountResponse:
        """
        @summary Enrolls an account. You can create a new account or manage an existing account in the account factory.
        
        @description You can call this API operation to create a new account or manage an existing account and apply the account baseline to the account.
        Accounts are created in asynchronous mode. After you create an account, you can apply the account baseline to the account. You can call the [GetEnrolledAccount API](~~GetEnrolledAccount~~) operation to view the details about the account to obtain the result of applying the account baseline to the account.
        
        @param request: EnrollAccountRequest
        @return: EnrollAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enroll_account_with_options_async(request, runtime)

    def get_account_factory_baseline_with_options(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        """
        @summary Obtains the details of an account factory baseline.
        
        @param request: GetAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_factory_baseline_with_options_async(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        """
        @summary Obtains the details of an account factory baseline.
        
        @param request: GetAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_factory_baseline(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        """
        @summary Obtains the details of an account factory baseline.
        
        @param request: GetAccountFactoryBaselineRequest
        @return: GetAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_factory_baseline_with_options(request, runtime)

    async def get_account_factory_baseline_async(
        self,
        request: governance_20210120_models.GetAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.GetAccountFactoryBaselineResponse:
        """
        @summary Obtains the details of an account factory baseline.
        
        @param request: GetAccountFactoryBaselineRequest
        @return: GetAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_account_factory_baseline_with_options_async(request, runtime)

    def get_enrolled_account_with_options(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        """
        @summary Queries the details about an account that is enrolled in the account factory.
        
        @param request: GetEnrolledAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnrolledAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnrolledAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetEnrolledAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enrolled_account_with_options_async(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        """
        @summary Queries the details about an account that is enrolled in the account factory.
        
        @param request: GetEnrolledAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEnrolledAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEnrolledAccount',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.GetEnrolledAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enrolled_account(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        """
        @summary Queries the details about an account that is enrolled in the account factory.
        
        @param request: GetEnrolledAccountRequest
        @return: GetEnrolledAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_enrolled_account_with_options(request, runtime)

    async def get_enrolled_account_async(
        self,
        request: governance_20210120_models.GetEnrolledAccountRequest,
    ) -> governance_20210120_models.GetEnrolledAccountResponse:
        """
        @summary Queries the details about an account that is enrolled in the account factory.
        
        @param request: GetEnrolledAccountRequest
        @return: GetEnrolledAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_enrolled_account_with_options_async(request, runtime)

    def list_account_factory_baseline_items_with_options(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselineItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselineItemsResponse:
        """
        @summary Queries a list of baseline items that are supported by the account factory of Cloud Governance Center (CGC).
        
        @param request: ListAccountFactoryBaselineItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountFactoryBaselineItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.versions):
            query['Versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselineItems',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselineItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_factory_baseline_items_with_options_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselineItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselineItemsResponse:
        """
        @summary Queries a list of baseline items that are supported by the account factory of Cloud Governance Center (CGC).
        
        @param request: ListAccountFactoryBaselineItemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountFactoryBaselineItemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.names):
            query['Names'] = request.names
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.versions):
            query['Versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselineItems',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselineItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_factory_baseline_items(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselineItemsRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselineItemsResponse:
        """
        @summary Queries a list of baseline items that are supported by the account factory of Cloud Governance Center (CGC).
        
        @param request: ListAccountFactoryBaselineItemsRequest
        @return: ListAccountFactoryBaselineItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_account_factory_baseline_items_with_options(request, runtime)

    async def list_account_factory_baseline_items_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselineItemsRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselineItemsResponse:
        """
        @summary Queries a list of baseline items that are supported by the account factory of Cloud Governance Center (CGC).
        
        @param request: ListAccountFactoryBaselineItemsRequest
        @return: ListAccountFactoryBaselineItemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_account_factory_baseline_items_with_options_async(request, runtime)

    def list_account_factory_baselines_with_options(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        """
        @summary Obtains a list of baselines in the account factory.
        
        @param request: ListAccountFactoryBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountFactoryBaselinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselines',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_factory_baselines_with_options_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        """
        @summary Obtains a list of baselines in the account factory.
        
        @param request: ListAccountFactoryBaselinesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAccountFactoryBaselinesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountFactoryBaselines',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListAccountFactoryBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_factory_baselines(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        """
        @summary Obtains a list of baselines in the account factory.
        
        @param request: ListAccountFactoryBaselinesRequest
        @return: ListAccountFactoryBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_account_factory_baselines_with_options(request, runtime)

    async def list_account_factory_baselines_async(
        self,
        request: governance_20210120_models.ListAccountFactoryBaselinesRequest,
    ) -> governance_20210120_models.ListAccountFactoryBaselinesResponse:
        """
        @summary Obtains a list of baselines in the account factory.
        
        @param request: ListAccountFactoryBaselinesRequest
        @return: ListAccountFactoryBaselinesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_account_factory_baselines_with_options_async(request, runtime)

    def list_enrolled_accounts_with_options(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        """
        @summary Queries a list of accounts that are enrolled in the account factory.
        
        @param request: ListEnrolledAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnrolledAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnrolledAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEnrolledAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enrolled_accounts_with_options_async(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        """
        @summary Queries a list of accounts that are enrolled in the account factory.
        
        @param request: ListEnrolledAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEnrolledAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnrolledAccounts',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEnrolledAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enrolled_accounts(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        """
        @summary Queries a list of accounts that are enrolled in the account factory.
        
        @param request: ListEnrolledAccountsRequest
        @return: ListEnrolledAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_enrolled_accounts_with_options(request, runtime)

    async def list_enrolled_accounts_async(
        self,
        request: governance_20210120_models.ListEnrolledAccountsRequest,
    ) -> governance_20210120_models.ListEnrolledAccountsResponse:
        """
        @summary Queries a list of accounts that are enrolled in the account factory.
        
        @param request: ListEnrolledAccountsRequest
        @return: ListEnrolledAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_enrolled_accounts_with_options_async(request, runtime)

    def list_evaluation_metadata_with_options(
        self,
        request: governance_20210120_models.ListEvaluationMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationMetadataResponse:
        """
        @summary Queries all available information about check items in a governance maturity check, including the name, ID, description, stage, resource metadata, and fixing guide.
        
        @param request: ListEvaluationMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lens_code):
            query['LensCode'] = request.lens_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationMetadata',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_metadata_with_options_async(
        self,
        request: governance_20210120_models.ListEvaluationMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationMetadataResponse:
        """
        @summary Queries all available information about check items in a governance maturity check, including the name, ID, description, stage, resource metadata, and fixing guide.
        
        @param request: ListEvaluationMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationMetadataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.lens_code):
            query['LensCode'] = request.lens_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationMetadata',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_metadata(
        self,
        request: governance_20210120_models.ListEvaluationMetadataRequest,
    ) -> governance_20210120_models.ListEvaluationMetadataResponse:
        """
        @summary Queries all available information about check items in a governance maturity check, including the name, ID, description, stage, resource metadata, and fixing guide.
        
        @param request: ListEvaluationMetadataRequest
        @return: ListEvaluationMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_evaluation_metadata_with_options(request, runtime)

    async def list_evaluation_metadata_async(
        self,
        request: governance_20210120_models.ListEvaluationMetadataRequest,
    ) -> governance_20210120_models.ListEvaluationMetadataResponse:
        """
        @summary Queries all available information about check items in a governance maturity check, including the name, ID, description, stage, resource metadata, and fixing guide.
        
        @param request: ListEvaluationMetadataRequest
        @return: ListEvaluationMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_evaluation_metadata_with_options_async(request, runtime)

    def list_evaluation_metric_details_with_options(
        self,
        request: governance_20210120_models.ListEvaluationMetricDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationMetricDetailsResponse:
        """
        @summary Queries the non-compliant resource information of a check item, including the name, ID, category, type, region, and related metadata of non-compliant resources.
        
        @param request: ListEvaluationMetricDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationMetricDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationMetricDetails',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationMetricDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_metric_details_with_options_async(
        self,
        request: governance_20210120_models.ListEvaluationMetricDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationMetricDetailsResponse:
        """
        @summary Queries the non-compliant resource information of a check item, including the name, ID, category, type, region, and related metadata of non-compliant resources.
        
        @param request: ListEvaluationMetricDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationMetricDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationMetricDetails',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationMetricDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_metric_details(
        self,
        request: governance_20210120_models.ListEvaluationMetricDetailsRequest,
    ) -> governance_20210120_models.ListEvaluationMetricDetailsResponse:
        """
        @summary Queries the non-compliant resource information of a check item, including the name, ID, category, type, region, and related metadata of non-compliant resources.
        
        @param request: ListEvaluationMetricDetailsRequest
        @return: ListEvaluationMetricDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_evaluation_metric_details_with_options(request, runtime)

    async def list_evaluation_metric_details_async(
        self,
        request: governance_20210120_models.ListEvaluationMetricDetailsRequest,
    ) -> governance_20210120_models.ListEvaluationMetricDetailsResponse:
        """
        @summary Queries the non-compliant resource information of a check item, including the name, ID, category, type, region, and related metadata of non-compliant resources.
        
        @param request: ListEvaluationMetricDetailsRequest
        @return: ListEvaluationMetricDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_evaluation_metric_details_with_options_async(request, runtime)

    def list_evaluation_results_with_options(
        self,
        request: governance_20210120_models.ListEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationResultsResponse:
        """
        @summary Queries the result and status of a governance check.
        
        @param request: ListEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.lens_code):
            query['LensCode'] = request.lens_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationResults',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_results_with_options_async(
        self,
        request: governance_20210120_models.ListEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationResultsResponse:
        """
        @summary Queries the result and status of a governance check.
        
        @param request: ListEvaluationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.lens_code):
            query['LensCode'] = request.lens_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationResults',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_results(
        self,
        request: governance_20210120_models.ListEvaluationResultsRequest,
    ) -> governance_20210120_models.ListEvaluationResultsResponse:
        """
        @summary Queries the result and status of a governance check.
        
        @param request: ListEvaluationResultsRequest
        @return: ListEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_evaluation_results_with_options(request, runtime)

    async def list_evaluation_results_async(
        self,
        request: governance_20210120_models.ListEvaluationResultsRequest,
    ) -> governance_20210120_models.ListEvaluationResultsResponse:
        """
        @summary Queries the result and status of a governance check.
        
        @param request: ListEvaluationResultsRequest
        @return: ListEvaluationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_evaluation_results_with_options_async(request, runtime)

    def list_evaluation_score_history_with_options(
        self,
        request: governance_20210120_models.ListEvaluationScoreHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationScoreHistoryResponse:
        """
        @summary Queries the historical scores of a governance maturity check.
        
        @param request: ListEvaluationScoreHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationScoreHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationScoreHistory',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationScoreHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_score_history_with_options_async(
        self,
        request: governance_20210120_models.ListEvaluationScoreHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.ListEvaluationScoreHistoryResponse:
        """
        @summary Queries the historical scores of a governance maturity check.
        
        @param request: ListEvaluationScoreHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEvaluationScoreHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEvaluationScoreHistory',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.ListEvaluationScoreHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_score_history(
        self,
        request: governance_20210120_models.ListEvaluationScoreHistoryRequest,
    ) -> governance_20210120_models.ListEvaluationScoreHistoryResponse:
        """
        @summary Queries the historical scores of a governance maturity check.
        
        @param request: ListEvaluationScoreHistoryRequest
        @return: ListEvaluationScoreHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_evaluation_score_history_with_options(request, runtime)

    async def list_evaluation_score_history_async(
        self,
        request: governance_20210120_models.ListEvaluationScoreHistoryRequest,
    ) -> governance_20210120_models.ListEvaluationScoreHistoryResponse:
        """
        @summary Queries the historical scores of a governance maturity check.
        
        @param request: ListEvaluationScoreHistoryRequest
        @return: ListEvaluationScoreHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_evaluation_score_history_with_options_async(request, runtime)

    def run_evaluation_with_options(
        self,
        tmp_req: governance_20210120_models.RunEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.RunEvaluationResponse:
        """
        @summary Performs a governance maturity check.
        
        @param tmp_req: RunEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEvaluationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = governance_20210120_models.RunEvaluationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_ids):
            request.metric_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_ids, 'MetricIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.metric_ids_shrink):
            query['MetricIds'] = request.metric_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunEvaluation',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.RunEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_evaluation_with_options_async(
        self,
        tmp_req: governance_20210120_models.RunEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.RunEvaluationResponse:
        """
        @summary Performs a governance maturity check.
        
        @param tmp_req: RunEvaluationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunEvaluationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = governance_20210120_models.RunEvaluationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_ids):
            request.metric_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_ids, 'MetricIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.metric_ids_shrink):
            query['MetricIds'] = request.metric_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunEvaluation',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.RunEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_evaluation(
        self,
        request: governance_20210120_models.RunEvaluationRequest,
    ) -> governance_20210120_models.RunEvaluationResponse:
        """
        @summary Performs a governance maturity check.
        
        @param request: RunEvaluationRequest
        @return: RunEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_evaluation_with_options(request, runtime)

    async def run_evaluation_async(
        self,
        request: governance_20210120_models.RunEvaluationRequest,
    ) -> governance_20210120_models.RunEvaluationResponse:
        """
        @summary Performs a governance maturity check.
        
        @param request: RunEvaluationRequest
        @return: RunEvaluationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_evaluation_with_options_async(request, runtime)

    def update_account_factory_baseline_with_options(
        self,
        request: governance_20210120_models.UpdateAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.UpdateAccountFactoryBaselineResponse:
        """
        @summary Updates a baseline of the account factory.
        
        @param request: UpdateAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.UpdateAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_factory_baseline_with_options_async(
        self,
        request: governance_20210120_models.UpdateAccountFactoryBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> governance_20210120_models.UpdateAccountFactoryBaselineResponse:
        """
        @summary Updates a baseline of the account factory.
        
        @param request: UpdateAccountFactoryBaselineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccountFactoryBaselineResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not UtilClient.is_unset(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not UtilClient.is_unset(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountFactoryBaseline',
            version='2021-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            governance_20210120_models.UpdateAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_factory_baseline(
        self,
        request: governance_20210120_models.UpdateAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.UpdateAccountFactoryBaselineResponse:
        """
        @summary Updates a baseline of the account factory.
        
        @param request: UpdateAccountFactoryBaselineRequest
        @return: UpdateAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_account_factory_baseline_with_options(request, runtime)

    async def update_account_factory_baseline_async(
        self,
        request: governance_20210120_models.UpdateAccountFactoryBaselineRequest,
    ) -> governance_20210120_models.UpdateAccountFactoryBaselineResponse:
        """
        @summary Updates a baseline of the account factory.
        
        @param request: UpdateAccountFactoryBaselineRequest
        @return: UpdateAccountFactoryBaselineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_account_factory_baseline_with_options_async(request, runtime)
