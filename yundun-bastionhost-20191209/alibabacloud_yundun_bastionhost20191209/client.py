# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_bastionhost20191209 import models as yundun_bastionhost_20191209_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-bastionhost', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_hosts_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AddHostsToGroupResponse().from_map(
            self.do_rpcrequest('AddHostsToGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_hosts_to_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AddHostsToGroupResponse().from_map(
            await self.do_rpcrequest_async('AddHostsToGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hosts_to_group(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_hosts_to_group_with_options(request, runtime)

    async def add_hosts_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddHostsToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddHostsToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_hosts_to_group_with_options_async(request, runtime)

    def add_users_to_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AddUsersToGroupResponse().from_map(
            self.do_rpcrequest('AddUsersToGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_users_to_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AddUsersToGroupResponse().from_map(
            await self.do_rpcrequest_async('AddUsersToGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_users_to_group(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    async def add_users_to_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AddUsersToGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AddUsersToGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_users_to_group_with_options_async(request, runtime)

    def attach_host_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse().from_map(
            self.do_rpcrequest('AttachHostAccountsToUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_host_accounts_to_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse().from_map(
            await self.do_rpcrequest_async('AttachHostAccountsToUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_host_accounts_to_user(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_with_options(request, runtime)

    async def attach_host_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_user_with_options_async(request, runtime)

    def attach_host_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse().from_map(
            self.do_rpcrequest('AttachHostAccountsToUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_host_accounts_to_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse().from_map(
            await self.do_rpcrequest_async('AttachHostAccountsToUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_host_accounts_to_user_group(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_accounts_to_user_group_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse().from_map(
            self.do_rpcrequest('AttachHostGroupAccountsToUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_host_group_accounts_to_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse().from_map(
            await self.do_rpcrequest_async('AttachHostGroupAccountsToUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_host_group_accounts_to_user(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_with_options_async(request, runtime)

    def attach_host_group_accounts_to_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse().from_map(
            self.do_rpcrequest('AttachHostGroupAccountsToUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_host_group_accounts_to_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse().from_map(
            await self.do_rpcrequest_async('AttachHostGroupAccountsToUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_host_group_accounts_to_user_group(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_group_with_options(request, runtime)

    async def attach_host_group_accounts_to_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_host_group_accounts_to_user_group_with_options_async(request, runtime)

    def config_instance_security_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse().from_map(
            self.do_rpcrequest('ConfigInstanceSecurityGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_security_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('ConfigInstanceSecurityGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_security_groups(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_security_groups_with_options(request, runtime)

    async def config_instance_security_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_security_groups_with_options_async(request, runtime)

    def config_instance_white_list_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse().from_map(
            self.do_rpcrequest('ConfigInstanceWhiteList', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_instance_white_list_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse().from_map(
            await self.do_rpcrequest_async('ConfigInstanceWhiteList', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_instance_white_list(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    async def config_instance_white_list_async(
        self,
        request: yundun_bastionhost_20191209_models.ConfigInstanceWhiteListRequest,
    ) -> yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_instance_white_list_with_options_async(request, runtime)

    def create_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostResponse().from_map(
            self.do_rpcrequest('CreateHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostResponse().from_map(
            await self.do_rpcrequest_async('CreateHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_host(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_with_options(request, runtime)

    async def create_host_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_with_options_async(request, runtime)

    def create_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostAccountResponse().from_map(
            self.do_rpcrequest('CreateHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_host_account(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    async def create_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_account_with_options_async(request, runtime)

    def create_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostGroupResponse().from_map(
            self.do_rpcrequest('CreateHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateHostGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_host_group(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_group_with_options(request, runtime)

    async def create_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_group_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateUserResponse().from_map(
            await self.do_rpcrequest_async('CreateUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateUserGroupResponse().from_map(
            self.do_rpcrequest('CreateUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.CreateUserGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user_group(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.CreateUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.CreateUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def delete_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostResponse().from_map(
            self.do_rpcrequest('DeleteHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostResponse().from_map(
            await self.do_rpcrequest_async('DeleteHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_host(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_with_options(request, runtime)

    async def delete_host_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_with_options_async(request, runtime)

    def delete_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostAccountResponse().from_map(
            self.do_rpcrequest('DeleteHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_host_account(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    async def delete_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_account_with_options_async(request, runtime)

    def delete_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostGroupResponse().from_map(
            self.do_rpcrequest('DeleteHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteHostGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_host_group(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_group_with_options(request, runtime)

    async def delete_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_group_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteUserGroupResponse().from_map(
            self.do_rpcrequest('DeleteUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DeleteUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_group(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DeleteUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DeleteUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeInstancesRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: yundun_bastionhost_20191209_models.DescribeRegionsRequest,
    ) -> yundun_bastionhost_20191209_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detach_host_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse().from_map(
            self.do_rpcrequest('DetachHostAccountsFromUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_host_accounts_from_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse().from_map(
            await self.do_rpcrequest_async('DetachHostAccountsFromUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_host_accounts_from_user(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_with_options(request, runtime)

    async def detach_host_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_user_with_options_async(request, runtime)

    def detach_host_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse().from_map(
            self.do_rpcrequest('DetachHostAccountsFromUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_host_accounts_from_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DetachHostAccountsFromUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_host_accounts_from_user_group(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_accounts_from_user_group_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse().from_map(
            self.do_rpcrequest('DetachHostGroupAccountsFromUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_host_group_accounts_from_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse().from_map(
            await self.do_rpcrequest_async('DetachHostGroupAccountsFromUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_host_group_accounts_from_user(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_with_options_async(request, runtime)

    def detach_host_group_accounts_from_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse().from_map(
            self.do_rpcrequest('DetachHostGroupAccountsFromUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_host_group_accounts_from_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse().from_map(
            await self.do_rpcrequest_async('DetachHostGroupAccountsFromUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_host_group_accounts_from_user_group(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_group_with_options(request, runtime)

    async def detach_host_group_accounts_from_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_host_group_accounts_from_user_group_with_options_async(request, runtime)

    def disable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse().from_map(
            self.do_rpcrequest('DisableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse().from_map(
            await self.do_rpcrequest_async('DisableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_instance_public_access(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    async def disable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.DisableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_instance_public_access_with_options_async(request, runtime)

    def enable_instance_public_access_with_options(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse().from_map(
            self.do_rpcrequest('EnableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_instance_public_access_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse().from_map(
            await self.do_rpcrequest_async('EnableInstancePublicAccess', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_public_access(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    async def enable_instance_public_access_async(
        self,
        request: yundun_bastionhost_20191209_models.EnableInstancePublicAccessRequest,
    ) -> yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_public_access_with_options_async(request, runtime)

    def get_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostResponse().from_map(
            self.do_rpcrequest('GetHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostResponse().from_map(
            await self.do_rpcrequest_async('GetHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_host(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_host_with_options(request, runtime)

    async def get_host_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_host_with_options_async(request, runtime)

    def get_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostAccountResponse().from_map(
            self.do_rpcrequest('GetHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostAccountResponse().from_map(
            await self.do_rpcrequest_async('GetHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_host_account(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_host_account_with_options(request, runtime)

    async def get_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_host_account_with_options_async(request, runtime)

    def get_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostGroupResponse().from_map(
            self.do_rpcrequest('GetHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetHostGroupResponse().from_map(
            await self.do_rpcrequest_async('GetHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_host_group(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_host_group_with_options(request, runtime)

    async def get_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.GetHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_host_group_with_options_async(request, runtime)

    def get_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetUserResponse().from_map(
            self.do_rpcrequest('GetUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetUserResponse().from_map(
            await self.do_rpcrequest_async('GetUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    async def get_user_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetUserGroupResponse().from_map(
            self.do_rpcrequest('GetUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.GetUserGroupResponse().from_map(
            await self.do_rpcrequest_async('GetUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_group(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.GetUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.GetUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def list_host_accounts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsResponse().from_map(
            self.do_rpcrequest('ListHostAccounts', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_accounts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsResponse().from_map(
            await self.do_rpcrequest_async('ListHostAccounts', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_accounts(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_with_options(request, runtime)

    async def list_host_accounts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_with_options_async(request, runtime)

    def list_host_accounts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse().from_map(
            self.do_rpcrequest('ListHostAccountsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_accounts_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse().from_map(
            await self.do_rpcrequest_async('ListHostAccountsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_accounts_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_with_options(request, runtime)

    async def list_host_accounts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_user_with_options_async(request, runtime)

    def list_host_accounts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse().from_map(
            self.do_rpcrequest('ListHostAccountsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_accounts_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse().from_map(
            await self.do_rpcrequest_async('ListHostAccountsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_accounts_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_group_with_options(request, runtime)

    async def list_host_accounts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_accounts_for_user_group_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse().from_map(
            self.do_rpcrequest('ListHostGroupAccountNamesForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_group_account_names_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse().from_map(
            await self.do_rpcrequest_async('ListHostGroupAccountNamesForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_group_account_names_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_with_options(request, runtime)

    async def list_host_group_account_names_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_group_account_names_for_user_with_options_async(request, runtime)

    def list_host_group_account_names_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse().from_map(
            self.do_rpcrequest('ListHostGroupAccountNamesForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_group_account_names_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse().from_map(
            await self.do_rpcrequest_async('ListHostGroupAccountNamesForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_group_account_names_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_group_with_options(request, runtime)

    async def list_host_group_account_names_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_group_account_names_for_user_group_with_options_async(request, runtime)

    def list_host_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsResponse().from_map(
            self.do_rpcrequest('ListHostGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListHostGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_groups(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_with_options(request, runtime)

    async def list_host_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_with_options_async(request, runtime)

    def list_host_groups_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse().from_map(
            self.do_rpcrequest('ListHostGroupsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_groups_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse().from_map(
            await self.do_rpcrequest_async('ListHostGroupsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_groups_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_with_options(request, runtime)

    async def list_host_groups_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_for_user_with_options_async(request, runtime)

    def list_host_groups_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse().from_map(
            self.do_rpcrequest('ListHostGroupsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_host_groups_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse().from_map(
            await self.do_rpcrequest_async('ListHostGroupsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_groups_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_group_with_options(request, runtime)

    async def list_host_groups_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_host_groups_for_user_group_with_options_async(request, runtime)

    def list_hosts_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsResponse().from_map(
            self.do_rpcrequest('ListHosts', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hosts_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsResponse().from_map(
            await self.do_rpcrequest_async('ListHosts', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hosts(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_with_options(request, runtime)

    async def list_hosts_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_with_options_async(request, runtime)

    def list_hosts_for_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsForUserResponse().from_map(
            self.do_rpcrequest('ListHostsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hosts_for_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsForUserResponse().from_map(
            await self.do_rpcrequest_async('ListHostsForUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hosts_for_user(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_with_options(request, runtime)

    async def list_hosts_for_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_for_user_with_options_async(request, runtime)

    def list_hosts_for_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse().from_map(
            self.do_rpcrequest('ListHostsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hosts_for_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse().from_map(
            await self.do_rpcrequest_async('ListHostsForUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_hosts_for_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_group_with_options(request, runtime)

    async def list_hosts_for_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ListHostsForUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hosts_for_user_group_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagKeysRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.ListTagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListUserGroupsResponse().from_map(
            self.do_rpcrequest('ListUserGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListUserGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListUserGroups', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_groups(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUserGroupsRequest,
    ) -> yundun_bastionhost_20191209_models.ListUserGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: yundun_bastionhost_20191209_models.ListUsersRequest,
    ) -> yundun_bastionhost_20191209_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def lock_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.LockUsersResponse().from_map(
            self.do_rpcrequest('LockUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lock_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.LockUsersResponse().from_map(
            await self.do_rpcrequest_async('LockUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_users(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    async def lock_users_async(
        self,
        request: yundun_bastionhost_20191209_models.LockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.LockUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_users_with_options_async(request, runtime)

    def modify_host_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostResponse().from_map(
            self.do_rpcrequest('ModifyHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_host_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostResponse().from_map(
            await self.do_rpcrequest_async('ModifyHost', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_host(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_with_options(request, runtime)

    async def modify_host_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_with_options_async(request, runtime)

    def modify_host_account_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostAccountResponse().from_map(
            self.do_rpcrequest('ModifyHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_host_account_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostAccountResponse().from_map(
            await self.do_rpcrequest_async('ModifyHostAccount', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_host_account(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_account_with_options(request, runtime)

    async def modify_host_account_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostAccountRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_account_with_options_async(request, runtime)

    def modify_host_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostGroupResponse().from_map(
            self.do_rpcrequest('ModifyHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_host_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyHostGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_host_group(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_group_with_options(request, runtime)

    async def modify_host_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_group_with_options_async(request, runtime)

    def modify_hosts_active_address_type_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse().from_map(
            self.do_rpcrequest('ModifyHostsActiveAddressType', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hosts_active_address_type_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHostsActiveAddressType', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hosts_active_address_type(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_active_address_type_with_options(request, runtime)

    async def modify_hosts_active_address_type_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hosts_active_address_type_with_options_async(request, runtime)

    def modify_hosts_port_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostsPortResponse().from_map(
            self.do_rpcrequest('ModifyHostsPort', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hosts_port_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyHostsPortResponse().from_map(
            await self.do_rpcrequest_async('ModifyHostsPort', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hosts_port(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_port_with_options(request, runtime)

    async def modify_hosts_port_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyHostsPortRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyHostsPortResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hosts_port_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyInstanceAttributeRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_user_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyUserResponse().from_map(
            self.do_rpcrequest('ModifyUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyUserResponse().from_map(
            await self.do_rpcrequest_async('ModifyUser', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    async def modify_user_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_with_options_async(request, runtime)

    def modify_user_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyUserGroupResponse().from_map(
            self.do_rpcrequest('ModifyUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ModifyUserGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyUserGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_group(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_group_with_options(request, runtime)

    async def modify_user_group_async(
        self,
        request: yundun_bastionhost_20191209_models.ModifyUserGroupRequest,
    ) -> yundun_bastionhost_20191209_models.ModifyUserGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_group_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: yundun_bastionhost_20191209_models.MoveResourceGroupRequest,
    ) -> yundun_bastionhost_20191209_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def remove_hosts_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse().from_map(
            self.do_rpcrequest('RemoveHostsFromGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_hosts_from_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse().from_map(
            await self.do_rpcrequest_async('RemoveHostsFromGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_hosts_from_group(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_hosts_from_group_with_options(request, runtime)

    async def remove_hosts_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveHostsFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_hosts_from_group_with_options_async(request, runtime)

    def remove_users_from_group_with_options(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse().from_map(
            self.do_rpcrequest('RemoveUsersFromGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_users_from_group_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse().from_map(
            await self.do_rpcrequest_async('RemoveUsersFromGroup', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_users_from_group(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    async def remove_users_from_group_async(
        self,
        request: yundun_bastionhost_20191209_models.RemoveUsersFromGroupRequest,
    ) -> yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_users_from_group_with_options_async(request, runtime)

    def reset_host_account_credential_with_options(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse().from_map(
            self.do_rpcrequest('ResetHostAccountCredential', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_host_account_credential_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse().from_map(
            await self.do_rpcrequest_async('ResetHostAccountCredential', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_host_account_credential(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_host_account_credential_with_options(request, runtime)

    async def reset_host_account_credential_async(
        self,
        request: yundun_bastionhost_20191209_models.ResetHostAccountCredentialRequest,
    ) -> yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_host_account_credential_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.StartInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartInstance', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: yundun_bastionhost_20191209_models.StartInstanceRequest,
    ) -> yundun_bastionhost_20191209_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.TagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unlock_users_with_options(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UnlockUsersResponse().from_map(
            self.do_rpcrequest('UnlockUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unlock_users_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UnlockUsersResponse().from_map(
            await self.do_rpcrequest_async('UnlockUsers', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_users(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    async def unlock_users_async(
        self,
        request: yundun_bastionhost_20191209_models.UnlockUsersRequest,
    ) -> yundun_bastionhost_20191209_models.UnlockUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_users_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return yundun_bastionhost_20191209_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2019-12-09', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: yundun_bastionhost_20191209_models.UntagResourcesRequest,
    ) -> yundun_bastionhost_20191209_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
