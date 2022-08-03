# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcemanager20161111 import models as resource_manager_20161111_models
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
            'ap-northeast-1': 'resourcemanager.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'resourcemanager.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'resourcemanager.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'resourcemanager.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'resourcemanager.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'resourcemanager.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'resourcemanager.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'resourcemanager.cn-chengdu.aliyuncs.com',
            'cn-hangzhou-finance': 'resourcemanager.cn-hangzhou-finance.aliyuncs.com',
            'cn-hongkong': 'resourcemanager.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'resourcemanager.cn-huhehaote.aliyuncs.com',
            'cn-north-2-gov-1': 'resourcemanager.cn-north-2-gov-1.aliyuncs.com',
            'cn-qingdao': 'resourcemanager.cn-qingdao.aliyuncs.com',
            'cn-shanghai-finance-1': 'resourcemanager.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shenzhen': 'resourcemanager.cn-shenzhen.aliyuncs.com',
            'cn-shenzhen-finance-1': 'resourcemanager.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-wulanchabu': 'resourcemanager.cn-wulanchabu.aliyuncs.com',
            'cn-zhangjiakou': 'resourcemanager.cn-zhangjiakou.aliyuncs.com',
            'eu-central-1': 'resourcemanager.eu-central-1.aliyuncs.com',
            'eu-west-1': 'resourcemanager.eu-west-1.aliyuncs.com',
            'me-east-1': 'resourcemanager.me-east-1.aliyuncs.com',
            'us-east-1': 'resourcemanager.us-east-1.aliyuncs.com',
            'us-west-1': 'resourcemanager.us-west-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcemanager', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_policy_with_options(
        self,
        request: resource_manager_20161111_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: resource_manager_20161111_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.AttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy(
        self,
        request: resource_manager_20161111_models.AttachPolicyRequest,
    ) -> resource_manager_20161111_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: resource_manager_20161111_models.AttachPolicyRequest,
    ) -> resource_manager_20161111_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def cancel_create_cloud_account_with_options(
        self,
        request: resource_manager_20161111_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CancelCreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: resource_manager_20161111_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CancelCreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_create_cloud_account(
        self,
        request: resource_manager_20161111_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20161111_models.CancelCreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    async def cancel_create_cloud_account_async(
        self,
        request: resource_manager_20161111_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20161111_models.CancelCreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_create_cloud_account_with_options_async(request, runtime)

    def cancel_promote_resource_account_with_options(
        self,
        request: resource_manager_20161111_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CancelPromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: resource_manager_20161111_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CancelPromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_promote_resource_account(
        self,
        request: resource_manager_20161111_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20161111_models.CancelPromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    async def cancel_promote_resource_account_async(
        self,
        request: resource_manager_20161111_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20161111_models.CancelPromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_promote_resource_account_with_options_async(request, runtime)

    def create_cloud_account_with_options(
        self,
        request: resource_manager_20161111_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.enable_consolidated_billing):
            query['EnableConsolidatedBilling'] = request.enable_consolidated_billing
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.enable_consolidated_billing):
            query['EnableConsolidatedBilling'] = request.enable_consolidated_billing
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_account(
        self,
        request: resource_manager_20161111_models.CreateCloudAccountRequest,
    ) -> resource_manager_20161111_models.CreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    async def create_cloud_account_async(
        self,
        request: resource_manager_20161111_models.CreateCloudAccountRequest,
    ) -> resource_manager_20161111_models.CreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_account_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: resource_manager_20161111_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        request: resource_manager_20161111_models.CreateFolderRequest,
    ) -> resource_manager_20161111_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: resource_manager_20161111_models.CreateFolderRequest,
    ) -> resource_manager_20161111_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: resource_manager_20161111_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: resource_manager_20161111_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: resource_manager_20161111_models.CreatePolicyRequest,
    ) -> resource_manager_20161111_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: resource_manager_20161111_models.CreatePolicyRequest,
    ) -> resource_manager_20161111_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: resource_manager_20161111_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreatePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: resource_manager_20161111_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreatePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_version(
        self,
        request: resource_manager_20161111_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20161111_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    async def create_policy_version_async(
        self,
        request: resource_manager_20161111_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20161111_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_version_with_options_async(request, runtime)

    def create_resource_account_with_options(
        self,
        request: resource_manager_20161111_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.enable_consolidated_billing):
            query['EnableConsolidatedBilling'] = request.enable_consolidated_billing
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.enable_consolidated_billing):
            query['EnableConsolidatedBilling'] = request.enable_consolidated_billing
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_account(
        self,
        request: resource_manager_20161111_models.CreateResourceAccountRequest,
    ) -> resource_manager_20161111_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    async def create_resource_account_async(
        self,
        request: resource_manager_20161111_models.CreateResourceAccountRequest,
    ) -> resource_manager_20161111_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_account_with_options_async(request, runtime)

    def create_resource_group_with_options(
        self,
        request: resource_manager_20161111_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: resource_manager_20161111_models.CreateResourceGroupRequest,
    ) -> resource_manager_20161111_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: resource_manager_20161111_models.CreateResourceGroupRequest,
    ) -> resource_manager_20161111_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: resource_manager_20161111_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: resource_manager_20161111_models.CreateRoleRequest,
    ) -> resource_manager_20161111_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: resource_manager_20161111_models.CreateRoleRequest,
    ) -> resource_manager_20161111_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: resource_manager_20161111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: resource_manager_20161111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: resource_manager_20161111_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20161111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: resource_manager_20161111_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20161111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: resource_manager_20161111_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: resource_manager_20161111_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: resource_manager_20161111_models.DeleteFolderRequest,
    ) -> resource_manager_20161111_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: resource_manager_20161111_models.DeleteFolderRequest,
    ) -> resource_manager_20161111_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_invalid_cloud_account_record_with_options(
        self,
        request: resource_manager_20161111_models.DeleteInvalidCloudAccountRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvalidCloudAccountRecord',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_invalid_cloud_account_record_with_options_async(
        self,
        request: resource_manager_20161111_models.DeleteInvalidCloudAccountRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInvalidCloudAccountRecord',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_invalid_cloud_account_record(
        self,
        request: resource_manager_20161111_models.DeleteInvalidCloudAccountRecordRequest,
    ) -> resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_invalid_cloud_account_record_with_options(request, runtime)

    async def delete_invalid_cloud_account_record_async(
        self,
        request: resource_manager_20161111_models.DeleteInvalidCloudAccountRecordRequest,
    ) -> resource_manager_20161111_models.DeleteInvalidCloudAccountRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_invalid_cloud_account_record_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: resource_manager_20161111_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: resource_manager_20161111_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: resource_manager_20161111_models.DeletePolicyRequest,
    ) -> resource_manager_20161111_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: resource_manager_20161111_models.DeletePolicyRequest,
    ) -> resource_manager_20161111_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_version_with_options(
        self,
        request: resource_manager_20161111_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeletePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: resource_manager_20161111_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeletePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_version(
        self,
        request: resource_manager_20161111_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20161111_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    async def delete_policy_version_async(
        self,
        request: resource_manager_20161111_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20161111_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_version_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: resource_manager_20161111_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: resource_manager_20161111_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: resource_manager_20161111_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20161111_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: resource_manager_20161111_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20161111_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: resource_manager_20161111_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: resource_manager_20161111_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: resource_manager_20161111_models.DeleteRoleRequest,
    ) -> resource_manager_20161111_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: resource_manager_20161111_models.DeleteRoleRequest,
    ) -> resource_manager_20161111_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_service_linked_role_with_options(
        self,
        request: resource_manager_20161111_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_linked_role_with_options_async(
        self,
        request: resource_manager_20161111_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DeleteServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_linked_role(
        self,
        request: resource_manager_20161111_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20161111_models.DeleteServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    async def delete_service_linked_role_async(
        self,
        request: resource_manager_20161111_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20161111_models.DeleteServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_linked_role_with_options_async(request, runtime)

    def destory_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DestoryResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestoryResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DestoryResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def destory_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DestoryResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestoryResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DestoryResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destory_resource_directory(self) -> resource_manager_20161111_models.DestoryResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.destory_resource_directory_with_options(runtime)

    async def destory_resource_directory_async(self) -> resource_manager_20161111_models.DestoryResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destory_resource_directory_with_options_async(runtime)

    def destroy_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DestroyResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_resource_directory(self) -> resource_manager_20161111_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    async def destroy_resource_directory_async(self) -> resource_manager_20161111_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(runtime)

    def detach_policy_with_options(
        self,
        request: resource_manager_20161111_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: resource_manager_20161111_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.DetachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy(
        self,
        request: resource_manager_20161111_models.DetachPolicyRequest,
    ) -> resource_manager_20161111_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: resource_manager_20161111_models.DetachPolicyRequest,
    ) -> resource_manager_20161111_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def get_account_summary_with_options(
        self,
        request: resource_manager_20161111_models.GetAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetAccountSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountSummary',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetAccountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_summary_with_options_async(
        self,
        request: resource_manager_20161111_models.GetAccountSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetAccountSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountSummary',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetAccountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_summary(
        self,
        request: resource_manager_20161111_models.GetAccountSummaryRequest,
    ) -> resource_manager_20161111_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_summary_with_options(request, runtime)

    async def get_account_summary_async(
        self,
        request: resource_manager_20161111_models.GetAccountSummaryRequest,
    ) -> resource_manager_20161111_models.GetAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_summary_with_options_async(request, runtime)

    def get_folder_with_options(
        self,
        request: resource_manager_20161111_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: resource_manager_20161111_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        request: resource_manager_20161111_models.GetFolderRequest,
    ) -> resource_manager_20161111_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: resource_manager_20161111_models.GetFolderRequest,
    ) -> resource_manager_20161111_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: resource_manager_20161111_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: resource_manager_20161111_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: resource_manager_20161111_models.GetPolicyRequest,
    ) -> resource_manager_20161111_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: resource_manager_20161111_models.GetPolicyRequest,
    ) -> resource_manager_20161111_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_version_with_options(
        self,
        request: resource_manager_20161111_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: resource_manager_20161111_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_version(
        self,
        request: resource_manager_20161111_models.GetPolicyVersionRequest,
    ) -> resource_manager_20161111_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    async def get_policy_version_async(
        self,
        request: resource_manager_20161111_models.GetPolicyVersionRequest,
    ) -> resource_manager_20161111_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_version_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_directory(self) -> resource_manager_20161111_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    async def get_resource_directory_async(self) -> resource_manager_20161111_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_with_options_async(runtime)

    def get_resource_directory_account_with_options(
        self,
        request: resource_manager_20161111_models.GetResourceDirectoryAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceDirectoryAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceDirectoryAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceDirectoryAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_directory_account_with_options_async(
        self,
        request: resource_manager_20161111_models.GetResourceDirectoryAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceDirectoryAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceDirectoryAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceDirectoryAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_directory_account(
        self,
        request: resource_manager_20161111_models.GetResourceDirectoryAccountRequest,
    ) -> resource_manager_20161111_models.GetResourceDirectoryAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_account_with_options(request, runtime)

    async def get_resource_directory_account_async(
        self,
        request: resource_manager_20161111_models.GetResourceDirectoryAccountRequest,
    ) -> resource_manager_20161111_models.GetResourceDirectoryAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_account_with_options_async(request, runtime)

    def get_resource_group_with_options(
        self,
        request: resource_manager_20161111_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: resource_manager_20161111_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        request: resource_manager_20161111_models.GetResourceGroupRequest,
    ) -> resource_manager_20161111_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: resource_manager_20161111_models.GetResourceGroupRequest,
    ) -> resource_manager_20161111_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_role_with_options(
        self,
        request: resource_manager_20161111_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: resource_manager_20161111_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: resource_manager_20161111_models.GetRoleRequest,
    ) -> resource_manager_20161111_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: resource_manager_20161111_models.GetRoleRequest,
    ) -> resource_manager_20161111_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_service_linked_role_deletion_status_with_options(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role_deletion_status(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    async def get_service_linked_role_deletion_status_async(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_deletion_status_with_options_async(request, runtime)

    def get_service_linked_role_template_with_options(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleTemplate',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_template_with_options_async(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleTemplate',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role_template(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleTemplateRequest,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_template_with_options(request, runtime)

    async def get_service_linked_role_template_async(
        self,
        request: resource_manager_20161111_models.GetServiceLinkedRoleTemplateRequest,
    ) -> resource_manager_20161111_models.GetServiceLinkedRoleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_template_with_options_async(request, runtime)

    def init_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.InitResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.InitResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.InitResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.InitResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_resource_directory(self) -> resource_manager_20161111_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    async def init_resource_directory_async(self) -> resource_manager_20161111_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_resource_directory_with_options_async(runtime)

    def list_account_records_for_parent_with_options(
        self,
        request: resource_manager_20161111_models.ListAccountRecordsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountRecordsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountRecordsForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountRecordsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_records_for_parent_with_options_async(
        self,
        request: resource_manager_20161111_models.ListAccountRecordsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountRecordsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountRecordsForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountRecordsForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_records_for_parent(
        self,
        request: resource_manager_20161111_models.ListAccountRecordsForParentRequest,
    ) -> resource_manager_20161111_models.ListAccountRecordsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_account_records_for_parent_with_options(request, runtime)

    async def list_account_records_for_parent_async(
        self,
        request: resource_manager_20161111_models.ListAccountRecordsForParentRequest,
    ) -> resource_manager_20161111_models.ListAccountRecordsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_account_records_for_parent_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: resource_manager_20161111_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: resource_manager_20161111_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: resource_manager_20161111_models.ListAccountsRequest,
    ) -> resource_manager_20161111_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: resource_manager_20161111_models.ListAccountsRequest,
    ) -> resource_manager_20161111_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_accounts_for_parent_with_options(
        self,
        request: resource_manager_20161111_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_manager_20161111_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAccountsForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_for_parent(
        self,
        request: resource_manager_20161111_models.ListAccountsForParentRequest,
    ) -> resource_manager_20161111_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    async def list_accounts_for_parent_async(
        self,
        request: resource_manager_20161111_models.ListAccountsForParentRequest,
    ) -> resource_manager_20161111_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_for_parent_with_options_async(request, runtime)

    def list_ancestors_with_options(
        self,
        request: resource_manager_20161111_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAncestorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: resource_manager_20161111_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListAncestorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ancestors(
        self,
        request: resource_manager_20161111_models.ListAncestorsRequest,
    ) -> resource_manager_20161111_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    async def list_ancestors_async(
        self,
        request: resource_manager_20161111_models.ListAncestorsRequest,
    ) -> resource_manager_20161111_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ancestors_with_options_async(request, runtime)

    def list_folders_for_parent_with_options(
        self,
        request: resource_manager_20161111_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListFoldersForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoldersForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_manager_20161111_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListFoldersForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoldersForParent',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListFoldersForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_folders_for_parent(
        self,
        request: resource_manager_20161111_models.ListFoldersForParentRequest,
    ) -> resource_manager_20161111_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    async def list_folders_for_parent_async(
        self,
        request: resource_manager_20161111_models.ListFoldersForParentRequest,
    ) -> resource_manager_20161111_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_folders_for_parent_with_options_async(request, runtime)

    def list_parents_with_options(
        self,
        request: resource_manager_20161111_models.ListParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListParentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParents',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListParentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parents_with_options_async(
        self,
        request: resource_manager_20161111_models.ListParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListParentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParents',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListParentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parents(
        self,
        request: resource_manager_20161111_models.ListParentsRequest,
    ) -> resource_manager_20161111_models.ListParentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_parents_with_options(request, runtime)

    async def list_parents_async(
        self,
        request: resource_manager_20161111_models.ListParentsRequest,
    ) -> resource_manager_20161111_models.ListParentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_parents_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: resource_manager_20161111_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: resource_manager_20161111_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: resource_manager_20161111_models.ListPoliciesRequest,
    ) -> resource_manager_20161111_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: resource_manager_20161111_models.ListPoliciesRequest,
    ) -> resource_manager_20161111_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policy_attachments_with_options(
        self,
        request: resource_manager_20161111_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachments',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPolicyAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_attachments_with_options_async(
        self,
        request: resource_manager_20161111_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachments',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPolicyAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_attachments(
        self,
        request: resource_manager_20161111_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20161111_models.ListPolicyAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    async def list_policy_attachments_async(
        self,
        request: resource_manager_20161111_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20161111_models.ListPolicyAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_attachments_with_options_async(request, runtime)

    def list_policy_versions_with_options(
        self,
        request: resource_manager_20161111_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPolicyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: resource_manager_20161111_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListPolicyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_versions(
        self,
        request: resource_manager_20161111_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20161111_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    async def list_policy_versions_async(
        self,
        request: resource_manager_20161111_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20161111_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_versions_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        request: resource_manager_20161111_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: resource_manager_20161111_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: resource_manager_20161111_models.ListResourceGroupsRequest,
    ) -> resource_manager_20161111_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: resource_manager_20161111_models.ListResourceGroupsRequest,
    ) -> resource_manager_20161111_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: resource_manager_20161111_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: resource_manager_20161111_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: resource_manager_20161111_models.ListRolesRequest,
    ) -> resource_manager_20161111_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: resource_manager_20161111_models.ListRolesRequest,
    ) -> resource_manager_20161111_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_roles_for_service_with_options(
        self,
        request: resource_manager_20161111_models.ListRolesForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListRolesForServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRolesForService',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListRolesForServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_for_service_with_options_async(
        self,
        request: resource_manager_20161111_models.ListRolesForServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListRolesForServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRolesForService',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListRolesForServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles_for_service(
        self,
        request: resource_manager_20161111_models.ListRolesForServiceRequest,
    ) -> resource_manager_20161111_models.ListRolesForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_for_service_with_options(request, runtime)

    async def list_roles_for_service_async(
        self,
        request: resource_manager_20161111_models.ListRolesForServiceRequest,
    ) -> resource_manager_20161111_models.ListRolesForServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_for_service_with_options_async(request, runtime)

    def list_trusted_service_status_with_options(
        self,
        request: resource_manager_20161111_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_manager_20161111_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ListTrustedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trusted_service_status(
        self,
        request: resource_manager_20161111_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20161111_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    async def list_trusted_service_status_async(
        self,
        request: resource_manager_20161111_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20161111_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trusted_service_status_with_options_async(request, runtime)

    def move_account_with_options(
        self,
        request: resource_manager_20161111_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.MoveAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_account_with_options_async(
        self,
        request: resource_manager_20161111_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.MoveAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.MoveAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_account(
        self,
        request: resource_manager_20161111_models.MoveAccountRequest,
    ) -> resource_manager_20161111_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    async def move_account_async(
        self,
        request: resource_manager_20161111_models.MoveAccountRequest,
    ) -> resource_manager_20161111_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_account_with_options_async(request, runtime)

    def promote_resource_account_with_options(
        self,
        request: resource_manager_20161111_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromoteResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.PromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def promote_resource_account_with_options_async(
        self,
        request: resource_manager_20161111_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromoteResourceAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.PromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def promote_resource_account(
        self,
        request: resource_manager_20161111_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20161111_models.PromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    async def promote_resource_account_async(
        self,
        request: resource_manager_20161111_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20161111_models.PromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.promote_resource_account_with_options_async(request, runtime)

    def query_resource_with_options(
        self,
        request: resource_manager_20161111_models.QueryResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.QueryResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResource',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.QueryResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_with_options_async(
        self,
        request: resource_manager_20161111_models.QueryResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.QueryResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResource',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.QueryResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource(
        self,
        request: resource_manager_20161111_models.QueryResourceRequest,
    ) -> resource_manager_20161111_models.QueryResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_resource_with_options(request, runtime)

    async def query_resource_async(
        self,
        request: resource_manager_20161111_models.QueryResourceRequest,
    ) -> resource_manager_20161111_models.QueryResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_resource_with_options_async(request, runtime)

    def remove_cloud_account_with_options(
        self,
        request: resource_manager_20161111_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_manager_20161111_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.RemoveCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cloud_account(
        self,
        request: resource_manager_20161111_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20161111_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    async def remove_cloud_account_async(
        self,
        request: resource_manager_20161111_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20161111_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cloud_account_with_options_async(request, runtime)

    def resend_create_cloud_account_email_with_options(
        self,
        request: resource_manager_20161111_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: resource_manager_20161111_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_create_cloud_account_email(
        self,
        request: resource_manager_20161111_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    async def resend_create_cloud_account_email_async(
        self,
        request: resource_manager_20161111_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20161111_models.ResendCreateCloudAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_create_cloud_account_email_with_options_async(request, runtime)

    def resend_promote_resource_account_email_with_options(
        self,
        request: resource_manager_20161111_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: resource_manager_20161111_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_promote_resource_account_email(
        self,
        request: resource_manager_20161111_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    async def resend_promote_resource_account_email_async(
        self,
        request: resource_manager_20161111_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20161111_models.ResendPromoteResourceAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_promote_resource_account_email_with_options_async(request, runtime)

    def set_default_policy_version_with_options(
        self,
        request: resource_manager_20161111_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.SetDefaultPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: resource_manager_20161111_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.SetDefaultPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_policy_version(
        self,
        request: resource_manager_20161111_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20161111_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    async def set_default_policy_version_async(
        self,
        request: resource_manager_20161111_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20161111_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_policy_version_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: resource_manager_20161111_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: resource_manager_20161111_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        request: resource_manager_20161111_models.UpdateFolderRequest,
    ) -> resource_manager_20161111_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: resource_manager_20161111_models.UpdateFolderRequest,
    ) -> resource_manager_20161111_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_resource_group_with_options(
        self,
        request: resource_manager_20161111_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: resource_manager_20161111_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        request: resource_manager_20161111_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20161111_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: resource_manager_20161111_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20161111_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: resource_manager_20161111_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: resource_manager_20161111_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20161111_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2016-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20161111_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: resource_manager_20161111_models.UpdateRoleRequest,
    ) -> resource_manager_20161111_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: resource_manager_20161111_models.UpdateRoleRequest,
    ) -> resource_manager_20161111_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)
