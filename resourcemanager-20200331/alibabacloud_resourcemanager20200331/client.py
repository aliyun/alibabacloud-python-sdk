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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            self.do_rpcrequest('AcceptHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            await self.do_rpcrequest_async('AcceptHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            self.do_rpcrequest('AttachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            await self.do_rpcrequest_async('AttachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            self.do_rpcrequest('AttachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            await self.do_rpcrequest_async('AttachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def cancel_create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            self.do_rpcrequest('CancelCreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            await self.do_rpcrequest_async('CancelCreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            self.do_rpcrequest('CancelHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            await self.do_rpcrequest_async('CancelHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            self.do_rpcrequest('CancelPromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            await self.do_rpcrequest_async('CancelPromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            self.do_rpcrequest('CreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            await self.do_rpcrequest_async('CreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            self.do_rpcrequest('CreateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            await self.do_rpcrequest_async('CreateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            self.do_rpcrequest('CreateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            await self.do_rpcrequest_async('CreateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            self.do_rpcrequest('CreatePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            await self.do_rpcrequest_async('CreatePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            self.do_rpcrequest('CreatePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            await self.do_rpcrequest_async('CreatePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            self.do_rpcrequest('CreateResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            await self.do_rpcrequest_async('CreateResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            self.do_rpcrequest('CreateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            await self.do_rpcrequest_async('CreateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            self.do_rpcrequest('CreateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            await self.do_rpcrequest_async('CreateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            self.do_rpcrequest('DeclineHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def decline_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            await self.do_rpcrequest_async('DeclineHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            self.do_rpcrequest('DeleteControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            await self.do_rpcrequest_async('DeleteControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            self.do_rpcrequest('DeleteFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            await self.do_rpcrequest_async('DeleteFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            self.do_rpcrequest('DeletePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            await self.do_rpcrequest_async('DeletePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            self.do_rpcrequest('DeletePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            await self.do_rpcrequest_async('DeletePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            self.do_rpcrequest('DeleteResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            await self.do_rpcrequest_async('DeleteResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            self.do_rpcrequest('DeleteRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            await self.do_rpcrequest_async('DeleteRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            self.do_rpcrequest('DeleteServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('DeleteServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            self.do_rpcrequest('DeregisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deregister_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.DeregisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            await self.do_rpcrequest_async('DeregisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            self.do_rpcrequest('DestroyResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            await self.do_rpcrequest_async('DestroyResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            self.do_rpcrequest('DetachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            await self.do_rpcrequest_async('DetachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            self.do_rpcrequest('DetachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            await self.do_rpcrequest_async('DetachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            self.do_rpcrequest('DisableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DisableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            await self.do_rpcrequest_async('DisableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            self.do_rpcrequest('EnableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_control_policy_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            await self.do_rpcrequest_async('EnableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_control_policy(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    async def enable_control_policy_async(self) -> resource_manager_20200331_models.EnableControlPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_control_policy_with_options_async(runtime)

    def get_account_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            self.do_rpcrequest('GetAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            await self.do_rpcrequest_async('GetAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            self.do_rpcrequest('GetControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            await self.do_rpcrequest_async('GetControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            self.do_rpcrequest('GetControlPolicyEnablementStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_control_policy_enablement_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            await self.do_rpcrequest_async('GetControlPolicyEnablementStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            self.do_rpcrequest('GetFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            await self.do_rpcrequest_async('GetFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            self.do_rpcrequest('GetHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            await self.do_rpcrequest_async('GetHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            self.do_rpcrequest('GetPayerForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_payer_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            await self.do_rpcrequest_async('GetPayerForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            self.do_rpcrequest('GetPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            await self.do_rpcrequest_async('GetPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            self.do_rpcrequest('GetPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            await self.do_rpcrequest_async('GetPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            self.do_rpcrequest('GetResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            await self.do_rpcrequest_async('GetResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            self.do_rpcrequest('GetResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            await self.do_rpcrequest_async('GetResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_role_with_options(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            self.do_rpcrequest('GetRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_role_with_options_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            await self.do_rpcrequest_async('GetRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.do_rpcrequest('GetServiceLinkedRoleDeletionStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            await self.do_rpcrequest_async('GetServiceLinkedRoleDeletionStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            self.do_rpcrequest('InitResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_resource_directory_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            await self.do_rpcrequest_async('InitResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            self.do_rpcrequest('InviteAccountToResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            await self.do_rpcrequest_async('InviteAccountToResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            self.do_rpcrequest('ListAccounts', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            await self.do_rpcrequest_async('ListAccounts', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            self.do_rpcrequest('ListAccountsForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            await self.do_rpcrequest_async('ListAccountsForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            self.do_rpcrequest('ListAncestors', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            await self.do_rpcrequest_async('ListAncestors', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            self.do_rpcrequest('ListControlPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_control_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            await self.do_rpcrequest_async('ListControlPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.do_rpcrequest('ListControlPolicyAttachmentsForTarget', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_control_policy_attachments_for_target_with_options_async(
        self,
        request: resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            await self.do_rpcrequest_async('ListControlPolicyAttachmentsForTarget', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            self.do_rpcrequest('ListDelegatedAdministrators', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_delegated_administrators_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedAdministratorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedAdministratorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            await self.do_rpcrequest_async('ListDelegatedAdministrators', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            self.do_rpcrequest('ListDelegatedServicesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_delegated_services_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListDelegatedServicesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListDelegatedServicesForAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            await self.do_rpcrequest_async('ListDelegatedServicesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            self.do_rpcrequest('ListFoldersForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            await self.do_rpcrequest_async('ListFoldersForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            self.do_rpcrequest('ListHandshakesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            await self.do_rpcrequest_async('ListHandshakesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            self.do_rpcrequest('ListHandshakesForResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            await self.do_rpcrequest_async('ListHandshakesForResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            self.do_rpcrequest('ListPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            await self.do_rpcrequest_async('ListPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            self.do_rpcrequest('ListPolicyAttachments', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policy_attachments_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            await self.do_rpcrequest_async('ListPolicyAttachments', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            self.do_rpcrequest('ListPolicyVersions', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            await self.do_rpcrequest_async('ListPolicyVersions', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            self.do_rpcrequest('ListResourceGroups', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            await self.do_rpcrequest_async('ListResourceGroups', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            self.do_rpcrequest('ListResources', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            await self.do_rpcrequest_async('ListResources', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            await self.do_rpcrequest_async('ListRoles', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_target_attachments_for_control_policy_with_options(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.do_rpcrequest('ListTargetAttachmentsForControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_target_attachments_for_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            await self.do_rpcrequest_async('ListTargetAttachmentsForControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            self.do_rpcrequest('ListTrustedServiceStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            await self.do_rpcrequest_async('ListTrustedServiceStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            self.do_rpcrequest('MoveAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_account_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            await self.do_rpcrequest_async('MoveAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            self.do_rpcrequest('PromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            await self.do_rpcrequest_async('PromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            self.do_rpcrequest('RegisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_delegated_administrator_with_options_async(
        self,
        request: resource_manager_20200331_models.RegisterDelegatedAdministratorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RegisterDelegatedAdministratorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            await self.do_rpcrequest_async('RegisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            self.do_rpcrequest('RemoveCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            await self.do_rpcrequest_async('RemoveCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            self.do_rpcrequest('ResendCreateCloudAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            await self.do_rpcrequest_async('ResendCreateCloudAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            self.do_rpcrequest('ResendPromoteResourceAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            await self.do_rpcrequest_async('ResendPromoteResourceAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_default_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            self.do_rpcrequest('SetDefaultPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            await self.do_rpcrequest_async('SetDefaultPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_account_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            self.do_rpcrequest('UpdateAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_account_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            await self.do_rpcrequest_async('UpdateAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            self.do_rpcrequest('UpdateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_control_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateControlPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateControlPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            await self.do_rpcrequest_async('UpdateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            self.do_rpcrequest('UpdateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            await self.do_rpcrequest_async('UpdateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            self.do_rpcrequest('UpdateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            await self.do_rpcrequest_async('UpdateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            self.do_rpcrequest('UpdateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            await self.do_rpcrequest_async('UpdateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
