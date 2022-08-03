# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcemanager20200331 import models as resource_manager_20200331_models
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

    def accept_handshake_with_options(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_handshake(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    async def accept_handshake_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_handshake_with_options_async(request, runtime)

    def attach_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_control_policy(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    async def attach_control_policy_async(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_control_policy_with_options_async(request, runtime)

    def attach_policy_with_options(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_policy(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    async def attach_policy_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_policy_with_options_async(request, runtime)

    def bind_secure_mobile_phone_with_options(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_secure_mobile_phone(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    async def bind_secure_mobile_phone_async(
        self,
        request: resource_manager_20200331_models.BindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.BindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_secure_mobile_phone_with_options_async(request, runtime)

    def cancel_create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_create_cloud_account(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    async def cancel_create_cloud_account_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_create_cloud_account_with_options_async(request, runtime)

    def cancel_handshake_with_options(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_handshake(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    async def cancel_handshake_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_handshake_with_options_async(request, runtime)

    def cancel_promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_promote_resource_account(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    async def cancel_promote_resource_account_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_promote_resource_account_with_options_async(request, runtime)

    def create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cloud_account(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    async def create_cloud_account_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cloud_account_with_options_async(request, runtime)

    def create_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_control_policy(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    async def create_control_policy_async(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_control_policy_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_name):
            query['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_name):
            query['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_version(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    async def create_policy_version_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_version_with_options_async(request, runtime)

    def create_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_account(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    async def create_resource_account_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_account_with_options_async(request, runtime)

    def create_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_group(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    async def create_resource_group_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_group_with_options_async(request, runtime)

    def create_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    async def create_role_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_role_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def decline_handshake_with_options(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def decline_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decline_handshake(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    async def decline_handshake_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decline_handshake_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_version(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    async def delete_policy_version_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_version_with_options_async(request, runtime)

    def delete_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_group(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    async def delete_resource_group_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_group_with_options_async(request, runtime)

    def delete_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    async def delete_role_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_role_with_options_async(request, runtime)

    def delete_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_linked_role(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    async def delete_service_linked_role_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_linked_role_with_options_async(request, runtime)

    def deregister_delegated_administrator_with_options(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_delegated_administrator(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    async def deregister_delegated_administrator_async(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_delegated_administrator_with_options_async(request, runtime)

    def destroy_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_resource_directory(self) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    async def destroy_resource_directory_async(self) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(runtime)

    def detach_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_control_policy(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    async def detach_control_policy_async(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_control_policy_with_options_async(request, runtime)

    def detach_policy_with_options(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_policy(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    async def detach_policy_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_policy_with_options_async(request, runtime)

    def disable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_control_policy(self) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    async def disable_control_policy_async(self) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_control_policy_with_options_async(runtime)

    def enable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_control_policy(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    async def enable_control_policy_async(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_control_policy_with_options_async(runtime)

    def enable_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not UtilClient.is_unset(request.maname):
            query['MAName'] = request.maname
        if not UtilClient.is_unset(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not UtilClient.is_unset(request.maname):
            query['MAName'] = request.maname
        if not UtilClient.is_unset(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_directory(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    async def enable_resource_directory_async(
        self,
        request: resource_manager_20200331_models.EnableResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.EnableResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_resource_directory_with_options_async(request, runtime)

    def get_account_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    async def get_account_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_with_options_async(request, runtime)

    def get_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    async def get_control_policy_async(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_with_options_async(request, runtime)

    def get_control_policy_enablement_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_enablement_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy_enablement_status(self) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    async def get_control_policy_enablement_status_async(self) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_enablement_status_with_options_async(runtime)

    def get_folder_with_options(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_handshake_with_options(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_handshake(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    async def get_handshake_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_handshake_with_options_async(request, runtime)

    def get_payer_for_account_with_options(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_payer_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_payer_for_account(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    async def get_payer_for_account_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_payer_for_account_with_options_async(request, runtime)

    def get_policy_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    async def get_policy_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_with_options_async(request, runtime)

    def get_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_version(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    async def get_policy_version_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_version_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_directory(self) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    async def get_resource_directory_async(self) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_with_options_async(runtime)

    def get_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    async def get_resource_group_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_group_with_options_async(request, runtime)

    def get_resource_group_list_acl_mode_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupListAclModeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceGroupListAclMode',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupListAclModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_list_acl_mode_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupListAclModeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceGroupListAclMode',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupListAclModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_list_acl_mode(self) -> resource_manager_20200331_models.GetResourceGroupListAclModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_list_acl_mode_with_options(runtime)

    async def get_resource_group_list_acl_mode_async(self) -> resource_manager_20200331_models.GetResourceGroupListAclModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_group_list_acl_mode_with_options_async(runtime)

    def get_role_with_options(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    async def get_role_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_role_with_options_async(request, runtime)

    def get_service_linked_role_deletion_status_with_options(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_linked_role_deletion_status(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    async def get_service_linked_role_deletion_status_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_linked_role_deletion_status_with_options_async(request, runtime)

    def init_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_resource_directory(self) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    async def init_resource_directory_async(self) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_resource_directory_with_options_async(runtime)

    def invite_account_to_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_account_to_resource_directory(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    async def invite_account_to_resource_directory_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invite_account_to_resource_directory_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_accounts_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_for_parent(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    async def list_accounts_for_parent_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_for_parent_with_options_async(request, runtime)

    def list_ancestors_with_options(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ancestors(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    async def list_ancestors_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ancestors_with_options_async(request, runtime)

    def list_control_policies_with_options(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
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
            action='ListControlPolicies',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
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
            action='ListControlPolicies',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policies(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    async def list_control_policies_async(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policies_with_options_async(request, runtime)

    def list_control_policy_attachments_for_target_with_options(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicyAttachmentsForTarget',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policy_attachments_for_target_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicyAttachmentsForTarget',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policy_attachments_for_target(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    async def list_control_policy_attachments_for_target_async(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policy_attachments_for_target_with_options_async(request, runtime)

    def list_delegated_administrators_with_options(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedAdministrators',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_administrators_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedAdministrators',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_administrators(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    async def list_delegated_administrators_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_administrators_with_options_async(request, runtime)

    def list_delegated_services_for_account_with_options(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_services_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_services_for_account(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    async def list_delegated_services_for_account_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_services_for_account_with_options_async(request, runtime)

    def list_folders_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_folders_for_parent(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    async def list_folders_for_parent_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_folders_for_parent_with_options_async(request, runtime)

    def list_handshakes_for_account_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
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
            action='ListHandshakesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
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
            action='ListHandshakesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_account(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    async def list_handshakes_for_account_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_account_with_options_async(request, runtime)

    def list_handshakes_for_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
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
            action='ListHandshakesForResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
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
            action='ListHandshakesForResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_resource_directory(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    async def list_handshakes_for_resource_directory_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_resource_directory_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_policy_attachments_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_attachments_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        query = {}
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_attachments(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    async def list_policy_attachments_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_attachments_with_options_async(request, runtime)

    def list_policy_versions_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy_versions(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    async def list_policy_versions_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_versions_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_resources_with_options(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='ListResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='ListResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    async def list_resources_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resources_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: resource_manager_20200331_models.ListTagKeysRequest,
    ) -> resource_manager_20200331_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: resource_manager_20200331_models.ListTagResourcesRequest,
    ) -> resource_manager_20200331_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: resource_manager_20200331_models.ListTagValuesRequest,
    ) -> resource_manager_20200331_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_target_attachments_for_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetAttachmentsForControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_target_attachments_for_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetAttachmentsForControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_target_attachments_for_control_policy(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    async def list_target_attachments_for_control_policy_async(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_target_attachments_for_control_policy_with_options_async(request, runtime)

    def list_trusted_service_status_with_options(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trusted_service_status(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    async def list_trusted_service_status_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trusted_service_status_with_options_async(request, runtime)

    def move_account_with_options(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_account_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_account(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    async def move_account_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_account_with_options_async(request, runtime)

    def move_resources_with_options(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resources(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resources_with_options(request, runtime)

    async def move_resources_async(
        self,
        request: resource_manager_20200331_models.MoveResourcesRequest,
    ) -> resource_manager_20200331_models.MoveResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resources_with_options_async(request, runtime)

    def promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def promote_resource_account(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    async def promote_resource_account_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.promote_resource_account_with_options_async(request, runtime)

    def register_delegated_administrator_with_options(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_delegated_administrator(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    async def register_delegated_administrator_async(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_delegated_administrator_with_options_async(request, runtime)

    def remove_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cloud_account(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    async def remove_cloud_account_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cloud_account_with_options_async(request, runtime)

    def resend_create_cloud_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_create_cloud_account_email(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    async def resend_create_cloud_account_email_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_create_cloud_account_email_with_options_async(request, runtime)

    def resend_promote_resource_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_promote_resource_account_email(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    async def resend_promote_resource_account_email_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_promote_resource_account_email_with_options_async(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForBindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForBindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_bind_secure_mobile_phone(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    async def send_verification_code_for_bind_secure_mobile_phone_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_bind_secure_mobile_phone_with_options_async(request, runtime)

    def send_verification_code_for_enable_rdwith_options(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_enable_rdwith_options_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_enable_rd(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    async def send_verification_code_for_enable_rd_async(
        self,
        request: resource_manager_20200331_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_enable_rdwith_options_async(request, runtime)

    def set_default_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_policy_version(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    async def set_default_policy_version_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_policy_version_with_options_async(request, runtime)

    def set_member_deletion_permission_with_options(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_member_deletion_permission_with_options_async(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_member_deletion_permission(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_member_deletion_permission_with_options(request, runtime)

    async def set_member_deletion_permission_async(
        self,
        request: resource_manager_20200331_models.SetMemberDeletionPermissionRequest,
    ) -> resource_manager_20200331_models.SetMemberDeletionPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_member_deletion_permission_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: resource_manager_20200331_models.TagResourcesRequest,
    ) -> resource_manager_20200331_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: resource_manager_20200331_models.UntagResourcesRequest,
    ) -> resource_manager_20200331_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_account_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    async def update_account_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_account_with_options_async(request, runtime)

    def update_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not UtilClient.is_unset(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not UtilClient.is_unset(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_policy(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    async def update_control_policy_async(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_control_policy_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_group(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    async def update_resource_group_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_with_options_async(request, runtime)

    def update_role_with_options(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
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
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)

    async def update_role_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_role_with_options_async(request, runtime)
