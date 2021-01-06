# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore
from typing import Dict

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_resourcemanager20200331 import models as resource_manager_20200331_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(
        self, 
        config: rpc_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('resourcemanager', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def create_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateServiceLinkedRoleResponse().from_map(
            self.do_request('CreateServiceLinkedRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateServiceLinkedRoleResponse().from_map(
            await self.do_request_async('CreateServiceLinkedRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_service_linked_role_deletion_status_with_options(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse().from_map(
            self.do_request('GetServiceLinkedRoleDeletionStatus', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_service_linked_role_deletion_status_with_options_async(
        self,
        request: resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse().from_map(
            await self.do_request_async('GetServiceLinkedRoleDeletionStatus', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_trusted_service_status_with_options(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListTrustedServiceStatusResponse().from_map(
            self.do_request('ListTrustedServiceStatus', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_trusted_service_status_with_options_async(
        self,
        request: resource_manager_20200331_models.ListTrustedServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListTrustedServiceStatusResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListTrustedServiceStatusResponse().from_map(
            await self.do_request_async('ListTrustedServiceStatus', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_service_linked_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteServiceLinkedRoleResponse().from_map(
            self.do_request('DeleteServiceLinkedRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_service_linked_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteServiceLinkedRoleResponse().from_map(
            await self.do_request_async('DeleteServiceLinkedRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def update_role_with_options(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateRoleResponse().from_map(
            self.do_request('UpdateRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_role_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateRoleResponse().from_map(
            await self.do_request_async('UpdateRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_resources_with_options(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListResourcesResponse().from_map(
            self.do_request('ListResources', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourcesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListResourcesResponse().from_map(
            await self.do_request_async('ListResources', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateCloudAccountResponse().from_map(
            self.do_request('CreateCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateCloudAccountResponse().from_map(
            await self.do_request_async('CreateCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_role_with_options(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteRoleResponse().from_map(
            self.do_request('DeleteRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteRoleResponse().from_map(
            await self.do_request_async('DeleteRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_role_with_options(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetRoleResponse().from_map(
            self.do_request('GetRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_role_with_options_async(
        self,
        request: resource_manager_20200331_models.GetRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetRoleResponse().from_map(
            await self.do_request_async('GetRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_roles_with_options(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListRolesResponse().from_map(
            self.do_request('ListRoles', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: resource_manager_20200331_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListRolesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListRolesResponse().from_map(
            await self.do_request_async('ListRoles', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_role_with_options(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateRoleResponse().from_map(
            self.do_request('CreateRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_role_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateRoleResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateRoleResponse().from_map(
            await self.do_request_async('CreateRole', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_policy_attachments_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPolicyAttachmentsResponse().from_map(
            self.do_request('ListPolicyAttachments', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_policy_attachments_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyAttachmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyAttachmentsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPolicyAttachmentsResponse().from_map(
            await self.do_request_async('ListPolicyAttachments', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def detach_policy_with_options(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DetachPolicyResponse().from_map(
            self.do_request('DetachPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def detach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DetachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DetachPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DetachPolicyResponse().from_map(
            await self.do_request_async('DetachPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def attach_policy_with_options(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.AttachPolicyResponse().from_map(
            self.do_request('AttachPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def attach_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.AttachPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.AttachPolicyResponse().from_map(
            await self.do_request_async('AttachPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPolicyVersionResponse().from_map(
            self.do_request('GetPolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPolicyVersionResponse().from_map(
            await self.do_request_async('GetPolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def set_default_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.SetDefaultPolicyVersionResponse().from_map(
            self.do_request('SetDefaultPolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def set_default_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.SetDefaultPolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.SetDefaultPolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.SetDefaultPolicyVersionResponse().from_map(
            await self.do_request_async('SetDefaultPolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteResourceGroupResponse().from_map(
            self.do_request('DeleteResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteResourceGroupResponse().from_map(
            await self.do_request_async('DeleteResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_policy_with_options(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPolicyResponse().from_map(
            self.do_request('GetPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPolicyResponse().from_map(
            await self.do_request_async('GetPolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def update_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateResourceGroupResponse().from_map(
            self.do_request('UpdateResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateResourceGroupResponse().from_map(
            await self.do_request_async('UpdateResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_resource_groups_with_options(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListResourceGroupsResponse().from_map(
            self.do_request('ListResourceGroups', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: resource_manager_20200331_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListResourceGroupsResponse().from_map(
            await self.do_request_async('ListResourceGroups', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_policies_with_options(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPoliciesResponse().from_map(
            self.do_request('ListPolicies', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPoliciesResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPoliciesResponse().from_map(
            await self.do_request_async('ListPolicies', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_policy_versions_with_options(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPolicyVersionsResponse().from_map(
            self.do_request('ListPolicyVersions', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_policy_versions_with_options_async(
        self,
        request: resource_manager_20200331_models.ListPolicyVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListPolicyVersionsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListPolicyVersionsResponse().from_map(
            await self.do_request_async('ListPolicyVersions', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateResourceAccountResponse().from_map(
            self.do_request('CreateResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateResourceAccountResponse().from_map(
            await self.do_request_async('CreateResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_handshakes_for_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse().from_map(
            self.do_request('ListHandshakesForResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_handshakes_for_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse().from_map(
            await self.do_request_async('ListHandshakesForResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def destroy_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.DestroyResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DestroyResourceDirectoryResponse().from_map(
            self.do_request('DestroyResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def destroy_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.DestroyResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DestroyResourceDirectoryResponse().from_map(
            await self.do_request_async('DestroyResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def destroy_resource_directory(
        self,
        request: resource_manager_20200331_models.DestroyResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(request, runtime)

    async def destroy_resource_directory_async(
        self,
        request: resource_manager_20200331_models.DestroyResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.DestroyResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_resource_directory_with_options_async(request, runtime)

    def create_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreatePolicyVersionResponse().from_map(
            self.do_request('CreatePolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreatePolicyVersionResponse().from_map(
            await self.do_request_async('CreatePolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_policy_version_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeletePolicyVersionResponse().from_map(
            self.do_request('DeletePolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_policy_version_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyVersionResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeletePolicyVersionResponse().from_map(
            await self.do_request_async('DeletePolicyVersion', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetResourceGroupResponse().from_map(
            self.do_request('GetResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.GetResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetResourceGroupResponse().from_map(
            await self.do_request_async('GetResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def init_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.InitResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.InitResourceDirectoryResponse().from_map(
            self.do_request('InitResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def init_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.InitResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.InitResourceDirectoryResponse().from_map(
            await self.do_request_async('InitResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def init_resource_directory(
        self,
        request: resource_manager_20200331_models.InitResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(request, runtime)

    async def init_resource_directory_async(
        self,
        request: resource_manager_20200331_models.InitResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.InitResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_resource_directory_with_options_async(request, runtime)

    def get_handshake_with_options(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetHandshakeResponse().from_map(
            self.do_request('GetHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.GetHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetHandshakeResponse().from_map(
            await self.do_request_async('GetHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def cancel_handshake_with_options(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelHandshakeResponse().from_map(
            self.do_request('CancelHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelHandshakeResponse().from_map(
            await self.do_request_async('CancelHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_policy_with_options(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreatePolicyResponse().from_map(
            self.do_request('CreatePolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreatePolicyResponse().from_map(
            await self.do_request_async('CreatePolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def decline_handshake_with_options(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeclineHandshakeResponse().from_map(
            self.do_request('DeclineHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def decline_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.DeclineHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeclineHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeclineHandshakeResponse().from_map(
            await self.do_request_async('DeclineHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_policy_with_options(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeletePolicyResponse().from_map(
            self.do_request('DeletePolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_policy_with_options_async(
        self,
        request: resource_manager_20200331_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeletePolicyResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeletePolicyResponse().from_map(
            await self.do_request_async('DeletePolicy', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_handshakes_for_account_with_options(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListHandshakesForAccountResponse().from_map(
            self.do_request('ListHandshakesForAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_handshakes_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.ListHandshakesForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListHandshakesForAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListHandshakesForAccountResponse().from_map(
            await self.do_request_async('ListHandshakesForAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def invite_account_to_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse().from_map(
            self.do_request('InviteAccountToResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def invite_account_to_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.InviteAccountToResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse().from_map(
            await self.do_request_async('InviteAccountToResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def accept_handshake_with_options(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.AcceptHandshakeResponse().from_map(
            self.do_request('AcceptHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def accept_handshake_with_options_async(
        self,
        request: resource_manager_20200331_models.AcceptHandshakeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.AcceptHandshakeResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.AcceptHandshakeResponse().from_map(
            await self.do_request_async('AcceptHandshake', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def update_account_with_options(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateAccountResponse().from_map(
            self.do_request('UpdateAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_account_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateAccountResponse().from_map(
            await self.do_request_async('UpdateAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_folder_with_options(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetFolderResponse().from_map(
            self.do_request('GetFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetFolderResponse().from_map(
            await self.do_request_async('GetFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_accounts_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAccountsForParentResponse().from_map(
            self.do_request('ListAccountsForParent', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_accounts_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsForParentResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAccountsForParentResponse().from_map(
            await self.do_request_async('ListAccountsForParent', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_resource_group_with_options(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateResourceGroupResponse().from_map(
            self.do_request('CreateResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_resource_group_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateResourceGroupResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateResourceGroupResponse().from_map(
            await self.do_request_async('CreateResourceGroup', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.PromoteResourceAccountResponse().from_map(
            self.do_request('PromoteResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.PromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.PromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.PromoteResourceAccountResponse().from_map(
            await self.do_request_async('PromoteResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_accounts_with_options(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAccountsResponse().from_map(
            self.do_request('ListAccounts', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_accounts_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAccountsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAccountsResponse().from_map(
            await self.do_request_async('ListAccounts', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def cancel_promote_resource_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelPromoteResourceAccountResponse().from_map(
            self.do_request('CancelPromoteResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_promote_resource_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelPromoteResourceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelPromoteResourceAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelPromoteResourceAccountResponse().from_map(
            await self.do_request_async('CancelPromoteResourceAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def create_folder_with_options(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateFolderResponse().from_map(
            self.do_request('CreateFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CreateFolderResponse().from_map(
            await self.do_request_async('CreateFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def delete_folder_with_options(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteFolderResponse().from_map(
            self.do_request('DeleteFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.DeleteFolderResponse().from_map(
            await self.do_request_async('DeleteFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_account_with_options(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetAccountResponse().from_map(
            self.do_request('GetAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetAccountResponse().from_map(
            await self.do_request_async('GetAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_resource_directory_with_options(
        self,
        request: resource_manager_20200331_models.GetResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetResourceDirectoryResponse().from_map(
            self.do_request('GetResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_resource_directory_with_options_async(
        self,
        request: resource_manager_20200331_models.GetResourceDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetResourceDirectoryResponse().from_map(
            await self.do_request_async('GetResourceDirectory', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_resource_directory(
        self,
        request: resource_manager_20200331_models.GetResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(request, runtime)

    async def get_resource_directory_async(
        self,
        request: resource_manager_20200331_models.GetResourceDirectoryRequest,
    ) -> resource_manager_20200331_models.GetResourceDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_directory_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateFolderResponse().from_map(
            self.do_request('UpdateFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: resource_manager_20200331_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.UpdateFolderResponse().from_map(
            await self.do_request_async('UpdateFolder', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def move_account_with_options(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.MoveAccountResponse().from_map(
            self.do_request('MoveAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def move_account_with_options_async(
        self,
        request: resource_manager_20200331_models.MoveAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.MoveAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.MoveAccountResponse().from_map(
            await self.do_request_async('MoveAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_ancestors_with_options(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAncestorsResponse().from_map(
            self.do_request('ListAncestors', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_ancestors_with_options_async(
        self,
        request: resource_manager_20200331_models.ListAncestorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListAncestorsResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListAncestorsResponse().from_map(
            await self.do_request_async('ListAncestors', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def resend_create_cloud_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse().from_map(
            self.do_request('ResendCreateCloudAccountEmail', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def resend_create_cloud_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendCreateCloudAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse().from_map(
            await self.do_request_async('ResendCreateCloudAccountEmail', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def get_payer_for_account_with_options(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPayerForAccountResponse().from_map(
            self.do_request('GetPayerForAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def get_payer_for_account_with_options_async(
        self,
        request: resource_manager_20200331_models.GetPayerForAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.GetPayerForAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.GetPayerForAccountResponse().from_map(
            await self.do_request_async('GetPayerForAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def resend_promote_resource_account_email_with_options(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse().from_map(
            self.do_request('ResendPromoteResourceAccountEmail', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def resend_promote_resource_account_email_with_options_async(
        self,
        request: resource_manager_20200331_models.ResendPromoteResourceAccountEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse().from_map(
            await self.do_request_async('ResendPromoteResourceAccountEmail', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def list_folders_for_parent_with_options(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListFoldersForParentResponse().from_map(
            self.do_request('ListFoldersForParent', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def list_folders_for_parent_with_options_async(
        self,
        request: resource_manager_20200331_models.ListFoldersForParentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.ListFoldersForParentResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.ListFoldersForParentResponse().from_map(
            await self.do_request_async('ListFoldersForParent', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def remove_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.RemoveCloudAccountResponse().from_map(
            self.do_request('RemoveCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def remove_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.RemoveCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.RemoveCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.RemoveCloudAccountResponse().from_map(
            await self.do_request_async('RemoveCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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

    def cancel_create_cloud_account_with_options(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelCreateCloudAccountResponse().from_map(
            self.do_request('CancelCreateCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
        )

    async def cancel_create_cloud_account_with_options_async(
        self,
        request: resource_manager_20200331_models.CancelCreateCloudAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> resource_manager_20200331_models.CancelCreateCloudAccountResponse:
        UtilClient.validate_model(request)
        return resource_manager_20200331_models.CancelCreateCloudAccountResponse().from_map(
            await self.do_request_async('CancelCreateCloudAccount', 'HTTPS', 'POST', '2020-03-31', 'AK', None, TeaCore.to_map(request), runtime)
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
