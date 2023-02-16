# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcedirectorymaster20220419 import models as resource_directory_master_20220419_models
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
        self._endpoint = self.get_endpoint('resourcedirectorymaster', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: resource_directory_master_20220419_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AcceptHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def accept_handshake_with_options_async(
        self,
        request: resource_directory_master_20220419_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AcceptHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def accept_handshake(
        self,
        request: resource_directory_master_20220419_models.AcceptHandshakeRequest,
    ) -> resource_directory_master_20220419_models.AcceptHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    async def accept_handshake_async(
        self,
        request: resource_directory_master_20220419_models.AcceptHandshakeRequest,
    ) -> resource_directory_master_20220419_models.AcceptHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_handshake_with_options_async(request, runtime)

    def attach_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.AttachControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AttachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.AttachControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AttachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_control_policy(
        self,
        request: resource_directory_master_20220419_models.AttachControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.AttachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    async def attach_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.AttachControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.AttachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_control_policy_with_options_async(request, runtime)

    def bind_secure_mobile_phone_with_options(
        self,
        request: resource_directory_master_20220419_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.BindSecureMobilePhoneResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.BindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_directory_master_20220419_models.BindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.BindSecureMobilePhoneResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.BindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_secure_mobile_phone(
        self,
        request: resource_directory_master_20220419_models.BindSecureMobilePhoneRequest,
    ) -> resource_directory_master_20220419_models.BindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    async def bind_secure_mobile_phone_async(
        self,
        request: resource_directory_master_20220419_models.BindSecureMobilePhoneRequest,
    ) -> resource_directory_master_20220419_models.BindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_secure_mobile_phone_with_options_async(request, runtime)

    def cancel_change_account_email_with_options(
        self,
        request: resource_directory_master_20220419_models.CancelChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CancelChangeAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_change_account_email_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CancelChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CancelChangeAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_change_account_email(
        self,
        request: resource_directory_master_20220419_models.CancelChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.CancelChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_change_account_email_with_options(request, runtime)

    async def cancel_change_account_email_async(
        self,
        request: resource_directory_master_20220419_models.CancelChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.CancelChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_change_account_email_with_options_async(request, runtime)

    def cancel_handshake_with_options(
        self,
        request: resource_directory_master_20220419_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_handshake_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_handshake(
        self,
        request: resource_directory_master_20220419_models.CancelHandshakeRequest,
    ) -> resource_directory_master_20220419_models.CancelHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    async def cancel_handshake_async(
        self,
        request: resource_directory_master_20220419_models.CancelHandshakeRequest,
    ) -> resource_directory_master_20220419_models.CancelHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_handshake_with_options_async(request, runtime)

    def change_account_email_with_options(
        self,
        request: resource_directory_master_20220419_models.ChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ChangeAccountEmailResponse:
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
            action='ChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_account_email_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ChangeAccountEmailResponse:
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
            action='ChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_account_email(
        self,
        request: resource_directory_master_20220419_models.ChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.ChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_account_email_with_options(request, runtime)

    async def change_account_email_async(
        self,
        request: resource_directory_master_20220419_models.ChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.ChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_account_email_with_options_async(request, runtime)

    def check_account_delete_with_options(
        self,
        request: resource_directory_master_20220419_models.CheckAccountDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CheckAccountDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountDelete',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CheckAccountDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_delete_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CheckAccountDeleteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CheckAccountDeleteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountDelete',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CheckAccountDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_delete(
        self,
        request: resource_directory_master_20220419_models.CheckAccountDeleteRequest,
    ) -> resource_directory_master_20220419_models.CheckAccountDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_account_delete_with_options(request, runtime)

    async def check_account_delete_async(
        self,
        request: resource_directory_master_20220419_models.CheckAccountDeleteRequest,
    ) -> resource_directory_master_20220419_models.CheckAccountDeleteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_account_delete_with_options_async(request, runtime)

    def create_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_control_policy(
        self,
        request: resource_directory_master_20220419_models.CreateControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.CreateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    async def create_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.CreateControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.CreateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_control_policy_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: resource_directory_master_20220419_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateFolderResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateFolderResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        request: resource_directory_master_20220419_models.CreateFolderRequest,
    ) -> resource_directory_master_20220419_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: resource_directory_master_20220419_models.CreateFolderRequest,
    ) -> resource_directory_master_20220419_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_resource_account_with_options(
        self,
        request: resource_directory_master_20220419_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateResourceAccountResponse:
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
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.CreateResourceAccountResponse:
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
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateResourceAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_account(
        self,
        request: resource_directory_master_20220419_models.CreateResourceAccountRequest,
    ) -> resource_directory_master_20220419_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    async def create_resource_account_async(
        self,
        request: resource_directory_master_20220419_models.CreateResourceAccountRequest,
    ) -> resource_directory_master_20220419_models.CreateResourceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_account_with_options_async(request, runtime)

    def decline_handshake_with_options(
        self,
        request: resource_directory_master_20220419_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeclineHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def decline_handshake_with_options_async(
        self,
        request: resource_directory_master_20220419_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeclineHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decline_handshake(
        self,
        request: resource_directory_master_20220419_models.DeclineHandshakeRequest,
    ) -> resource_directory_master_20220419_models.DeclineHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    async def decline_handshake_async(
        self,
        request: resource_directory_master_20220419_models.DeclineHandshakeRequest,
    ) -> resource_directory_master_20220419_models.DeclineHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decline_handshake_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        tmp_req: resource_directory_master_20220419_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteAccountResponse:
        UtilClient.validate_model(tmp_req)
        request = resource_directory_master_20220419_models.DeleteAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not UtilClient.is_unset(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        tmp_req: resource_directory_master_20220419_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteAccountResponse:
        UtilClient.validate_model(tmp_req)
        request = resource_directory_master_20220419_models.DeleteAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not UtilClient.is_unset(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: resource_directory_master_20220419_models.DeleteAccountRequest,
    ) -> resource_directory_master_20220419_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: resource_directory_master_20220419_models.DeleteAccountRequest,
    ) -> resource_directory_master_20220419_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_control_policy(
        self,
        request: resource_directory_master_20220419_models.DeleteControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    async def delete_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.DeleteControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.DeleteControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_control_policy_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: resource_directory_master_20220419_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: resource_directory_master_20220419_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        request: resource_directory_master_20220419_models.DeleteFolderRequest,
    ) -> resource_directory_master_20220419_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: resource_directory_master_20220419_models.DeleteFolderRequest,
    ) -> resource_directory_master_20220419_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def deregister_delegated_administrator_with_options(
        self,
        request: resource_directory_master_20220419_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_delegated_administrator_with_options_async(
        self,
        request: resource_directory_master_20220419_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_delegated_administrator(
        self,
        request: resource_directory_master_20220419_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    async def deregister_delegated_administrator_async(
        self,
        request: resource_directory_master_20220419_models.DeregisterDelegatedAdministratorRequest,
    ) -> resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_delegated_administrator_with_options_async(request, runtime)

    def destroy_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DestroyResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_resource_directory(self) -> resource_directory_master_20220419_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    async def destroy_resource_directory_async(self) -> resource_directory_master_20220419_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(runtime)

    def detach_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DetachControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DetachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DetachControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DetachControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_control_policy(
        self,
        request: resource_directory_master_20220419_models.DetachControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.DetachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    async def detach_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.DetachControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.DetachControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_control_policy_with_options_async(request, runtime)

    def disable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DisableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DisableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.DisableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DisableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_control_policy(self) -> resource_directory_master_20220419_models.DisableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    async def disable_control_policy_async(self) -> resource_directory_master_20220419_models.DisableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_control_policy_with_options_async(runtime)

    def enable_control_policy_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.EnableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.EnableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_control_policy(self) -> resource_directory_master_20220419_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    async def enable_control_policy_async(self) -> resource_directory_master_20220419_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_control_policy_with_options_async(runtime)

    def enable_resource_directory_with_options(
        self,
        request: resource_directory_master_20220419_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.EnableResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_directory_with_options_async(
        self,
        request: resource_directory_master_20220419_models.EnableResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.EnableResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_directory(
        self,
        request: resource_directory_master_20220419_models.EnableResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.EnableResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    async def enable_resource_directory_async(
        self,
        request: resource_directory_master_20220419_models.EnableResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.EnableResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_resource_directory_with_options_async(request, runtime)

    def get_account_with_options(
        self,
        request: resource_directory_master_20220419_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account(
        self,
        request: resource_directory_master_20220419_models.GetAccountRequest,
    ) -> resource_directory_master_20220419_models.GetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    async def get_account_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountRequest,
    ) -> resource_directory_master_20220419_models.GetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_with_options_async(request, runtime)

    def get_account_deletion_check_result_with_options(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionCheckResult',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_deletion_check_result_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionCheckResult',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_deletion_check_result(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionCheckResultRequest,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_check_result_with_options(request, runtime)

    async def get_account_deletion_check_result_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionCheckResultRequest,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_deletion_check_result_with_options_async(request, runtime)

    def get_account_deletion_status_with_options(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_deletion_status_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_deletion_status(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionStatusRequest,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_status_with_options(request, runtime)

    async def get_account_deletion_status_async(
        self,
        request: resource_directory_master_20220419_models.GetAccountDeletionStatusRequest,
    ) -> resource_directory_master_20220419_models.GetAccountDeletionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_deletion_status_with_options_async(request, runtime)

    def get_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy(
        self,
        request: resource_directory_master_20220419_models.GetControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.GetControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    async def get_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.GetControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.GetControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_with_options_async(request, runtime)

    def get_control_policy_enablement_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_control_policy_enablement_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_control_policy_enablement_status(self) -> resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    async def get_control_policy_enablement_status_async(self) -> resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_control_policy_enablement_status_with_options_async(runtime)

    def get_folder_with_options(
        self,
        request: resource_directory_master_20220419_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetFolderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_folder(
        self,
        request: resource_directory_master_20220419_models.GetFolderRequest,
    ) -> resource_directory_master_20220419_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: resource_directory_master_20220419_models.GetFolderRequest,
    ) -> resource_directory_master_20220419_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_handshake_with_options(
        self,
        request: resource_directory_master_20220419_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_handshake_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetHandshakeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_handshake(
        self,
        request: resource_directory_master_20220419_models.GetHandshakeRequest,
    ) -> resource_directory_master_20220419_models.GetHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    async def get_handshake_async(
        self,
        request: resource_directory_master_20220419_models.GetHandshakeRequest,
    ) -> resource_directory_master_20220419_models.GetHandshakeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_handshake_with_options_async(request, runtime)

    def get_payer_for_account_with_options(
        self,
        request: resource_directory_master_20220419_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetPayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_payer_for_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetPayerForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_payer_for_account(
        self,
        request: resource_directory_master_20220419_models.GetPayerForAccountRequest,
    ) -> resource_directory_master_20220419_models.GetPayerForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    async def get_payer_for_account_async(
        self,
        request: resource_directory_master_20220419_models.GetPayerForAccountRequest,
    ) -> resource_directory_master_20220419_models.GetPayerForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_payer_for_account_with_options_async(request, runtime)

    def get_resource_directory_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_directory(self) -> resource_directory_master_20220419_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    async def get_resource_directory_async(self) -> resource_directory_master_20220419_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_with_options_async(runtime)

    def invite_account_to_resource_directory_with_options(
        self,
        request: resource_directory_master_20220419_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: resource_directory_master_20220419_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_account_to_resource_directory(
        self,
        request: resource_directory_master_20220419_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    async def invite_account_to_resource_directory_async(
        self,
        request: resource_directory_master_20220419_models.InviteAccountToResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invite_account_to_resource_directory_with_options_async(request, runtime)

    def list_accounts_with_options(
        self,
        request: resource_directory_master_20220419_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts(
        self,
        request: resource_directory_master_20220419_models.ListAccountsRequest,
    ) -> resource_directory_master_20220419_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    async def list_accounts_async(
        self,
        request: resource_directory_master_20220419_models.ListAccountsRequest,
    ) -> resource_directory_master_20220419_models.ListAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_with_options_async(request, runtime)

    def list_accounts_for_parent_with_options(
        self,
        request: resource_directory_master_20220419_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAccountsForParentResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAccountsForParentResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_accounts_for_parent(
        self,
        request: resource_directory_master_20220419_models.ListAccountsForParentRequest,
    ) -> resource_directory_master_20220419_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    async def list_accounts_for_parent_async(
        self,
        request: resource_directory_master_20220419_models.ListAccountsForParentRequest,
    ) -> resource_directory_master_20220419_models.ListAccountsForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_accounts_for_parent_with_options_async(request, runtime)

    def list_ancestors_with_options(
        self,
        request: resource_directory_master_20220419_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAncestorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAncestorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ancestors(
        self,
        request: resource_directory_master_20220419_models.ListAncestorsRequest,
    ) -> resource_directory_master_20220419_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    async def list_ancestors_async(
        self,
        request: resource_directory_master_20220419_models.ListAncestorsRequest,
    ) -> resource_directory_master_20220419_models.ListAncestorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ancestors_with_options_async(request, runtime)

    def list_control_policies_with_options(
        self,
        request: resource_directory_master_20220419_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListControlPoliciesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policies_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListControlPoliciesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policies(
        self,
        request: resource_directory_master_20220419_models.ListControlPoliciesRequest,
    ) -> resource_directory_master_20220419_models.ListControlPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    async def list_control_policies_async(
        self,
        request: resource_directory_master_20220419_models.ListControlPoliciesRequest,
    ) -> resource_directory_master_20220419_models.ListControlPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policies_with_options_async(request, runtime)

    def list_control_policy_attachments_for_target_with_options(
        self,
        request: resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_control_policy_attachments_for_target_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_control_policy_attachments_for_target(
        self,
        request: resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    async def list_control_policy_attachments_for_target_async(
        self,
        request: resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetRequest,
    ) -> resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_control_policy_attachments_for_target_with_options_async(request, runtime)

    def list_delegated_administrators_with_options(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_administrators_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_administrators(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedAdministratorsRequest,
    ) -> resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    async def list_delegated_administrators_async(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedAdministratorsRequest,
    ) -> resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_administrators_with_options_async(request, runtime)

    def list_delegated_services_for_account_with_options(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delegated_services_for_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delegated_services_for_account(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    async def list_delegated_services_for_account_async(
        self,
        request: resource_directory_master_20220419_models.ListDelegatedServicesForAccountRequest,
    ) -> resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_delegated_services_for_account_with_options_async(request, runtime)

    def list_folders_for_parent_with_options(
        self,
        request: resource_directory_master_20220419_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListFoldersForParentResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListFoldersForParentResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListFoldersForParentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_folders_for_parent(
        self,
        request: resource_directory_master_20220419_models.ListFoldersForParentRequest,
    ) -> resource_directory_master_20220419_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    async def list_folders_for_parent_async(
        self,
        request: resource_directory_master_20220419_models.ListFoldersForParentRequest,
    ) -> resource_directory_master_20220419_models.ListFoldersForParentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_folders_for_parent_with_options_async(request, runtime)

    def list_handshakes_for_account_with_options(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListHandshakesForAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListHandshakesForAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_account(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForAccountRequest,
    ) -> resource_directory_master_20220419_models.ListHandshakesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    async def list_handshakes_for_account_async(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForAccountRequest,
    ) -> resource_directory_master_20220419_models.ListHandshakesForAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_account_with_options_async(request, runtime)

    def list_handshakes_for_resource_directory_with_options(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_handshakes_for_resource_directory(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    async def list_handshakes_for_resource_directory_async(
        self,
        request: resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryRequest,
    ) -> resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_handshakes_for_resource_directory_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: resource_directory_master_20220419_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: resource_directory_master_20220419_models.ListTagResourcesRequest,
    ) -> resource_directory_master_20220419_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: resource_directory_master_20220419_models.ListTagResourcesRequest,
    ) -> resource_directory_master_20220419_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_target_attachments_for_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_target_attachments_for_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_target_attachments_for_control_policy(
        self,
        request: resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    async def list_target_attachments_for_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_target_attachments_for_control_policy_with_options_async(request, runtime)

    def list_trusted_service_status_with_options(
        self,
        request: resource_directory_master_20220419_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTrustedServiceStatusResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_directory_master_20220419_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.ListTrustedServiceStatusResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTrustedServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trusted_service_status(
        self,
        request: resource_directory_master_20220419_models.ListTrustedServiceStatusRequest,
    ) -> resource_directory_master_20220419_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    async def list_trusted_service_status_async(
        self,
        request: resource_directory_master_20220419_models.ListTrustedServiceStatusRequest,
    ) -> resource_directory_master_20220419_models.ListTrustedServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trusted_service_status_with_options_async(request, runtime)

    def move_account_with_options(
        self,
        request: resource_directory_master_20220419_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.MoveAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.MoveAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.MoveAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_account(
        self,
        request: resource_directory_master_20220419_models.MoveAccountRequest,
    ) -> resource_directory_master_20220419_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    async def move_account_async(
        self,
        request: resource_directory_master_20220419_models.MoveAccountRequest,
    ) -> resource_directory_master_20220419_models.MoveAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_account_with_options_async(request, runtime)

    def register_delegated_administrator_with_options(
        self,
        request: resource_directory_master_20220419_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_delegated_administrator_with_options_async(
        self,
        request: resource_directory_master_20220419_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_delegated_administrator(
        self,
        request: resource_directory_master_20220419_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    async def register_delegated_administrator_async(
        self,
        request: resource_directory_master_20220419_models.RegisterDelegatedAdministratorRequest,
    ) -> resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_delegated_administrator_with_options_async(request, runtime)

    def remove_cloud_account_with_options(
        self,
        request: resource_directory_master_20220419_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RemoveCloudAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cloud_account(
        self,
        request: resource_directory_master_20220419_models.RemoveCloudAccountRequest,
    ) -> resource_directory_master_20220419_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    async def remove_cloud_account_async(
        self,
        request: resource_directory_master_20220419_models.RemoveCloudAccountRequest,
    ) -> resource_directory_master_20220419_models.RemoveCloudAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cloud_account_with_options_async(request, runtime)

    def retry_change_account_email_with_options(
        self,
        request: resource_directory_master_20220419_models.RetryChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RetryChangeAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RetryChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_change_account_email_with_options_async(
        self,
        request: resource_directory_master_20220419_models.RetryChangeAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.RetryChangeAccountEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RetryChangeAccountEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_change_account_email(
        self,
        request: resource_directory_master_20220419_models.RetryChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.RetryChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_change_account_email_with_options(request, runtime)

    async def retry_change_account_email_async(
        self,
        request: resource_directory_master_20220419_models.RetryChangeAccountEmailRequest,
    ) -> resource_directory_master_20220419_models.RetryChangeAccountEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_change_account_email_with_options_async(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_bind_secure_mobile_phone_with_options_async(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_bind_secure_mobile_phone(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    async def send_verification_code_for_bind_secure_mobile_phone_async(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneRequest,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_bind_secure_mobile_phone_with_options_async(request, runtime)

    def send_verification_code_for_enable_rdwith_options(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_verification_code_for_enable_rdwith_options_async(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForEnableRDRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_verification_code_for_enable_rd(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    async def send_verification_code_for_enable_rd_async(
        self,
        request: resource_directory_master_20220419_models.SendVerificationCodeForEnableRDRequest,
    ) -> resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_verification_code_for_enable_rdwith_options_async(request, runtime)

    def set_member_deletion_permission_with_options(
        self,
        request: resource_directory_master_20220419_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_member_deletion_permission_with_options_async(
        self,
        request: resource_directory_master_20220419_models.SetMemberDeletionPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_member_deletion_permission(
        self,
        request: resource_directory_master_20220419_models.SetMemberDeletionPermissionRequest,
    ) -> resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_member_deletion_permission_with_options(request, runtime)

    async def set_member_deletion_permission_async(
        self,
        request: resource_directory_master_20220419_models.SetMemberDeletionPermissionRequest,
    ) -> resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_member_deletion_permission_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: resource_directory_master_20220419_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.TagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: resource_directory_master_20220419_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.TagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: resource_directory_master_20220419_models.TagResourcesRequest,
    ) -> resource_directory_master_20220419_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: resource_directory_master_20220419_models.TagResourcesRequest,
    ) -> resource_directory_master_20220419_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: resource_directory_master_20220419_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UntagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: resource_directory_master_20220419_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UntagResourcesResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: resource_directory_master_20220419_models.UntagResourcesRequest,
    ) -> resource_directory_master_20220419_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: resource_directory_master_20220419_models.UntagResourcesRequest,
    ) -> resource_directory_master_20220419_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_account_with_options(
        self,
        request: resource_directory_master_20220419_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_with_options_async(
        self,
        request: resource_directory_master_20220419_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateAccountResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account(
        self,
        request: resource_directory_master_20220419_models.UpdateAccountRequest,
    ) -> resource_directory_master_20220419_models.UpdateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    async def update_account_async(
        self,
        request: resource_directory_master_20220419_models.UpdateAccountRequest,
    ) -> resource_directory_master_20220419_models.UpdateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_account_with_options_async(request, runtime)

    def update_control_policy_with_options(
        self,
        request: resource_directory_master_20220419_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_policy_with_options_async(
        self,
        request: resource_directory_master_20220419_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateControlPolicyResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateControlPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_policy(
        self,
        request: resource_directory_master_20220419_models.UpdateControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.UpdateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    async def update_control_policy_async(
        self,
        request: resource_directory_master_20220419_models.UpdateControlPolicyRequest,
    ) -> resource_directory_master_20220419_models.UpdateControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_control_policy_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: resource_directory_master_20220419_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateFolderResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: resource_directory_master_20220419_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_directory_master_20220419_models.UpdateFolderResponse:
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_folder(
        self,
        request: resource_directory_master_20220419_models.UpdateFolderRequest,
    ) -> resource_directory_master_20220419_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: resource_directory_master_20220419_models.UpdateFolderRequest,
    ) -> resource_directory_master_20220419_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)
